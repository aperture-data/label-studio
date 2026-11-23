"""Prepare the SDK wheel for Poetry or the Docker build context."""
import argparse
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.aperturedb-sdk'
IMAGE = 'registry-1.docker.io/aperturedata/aperturedb-python:latest'


def pull():
    CACHE.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=CACHE) as staging:
        subprocess.run(['oras', 'pull', IMAGE, '--output', staging], check=True)
        wheels = list(Path(staging).glob('aperturedb-*-py3-none-any.whl'))
        if len(wheels) != 1:
            raise SystemExit(f'Expected one ApertureDB wheel in {IMAGE}')
        wheel = wheels[0]
        destination = CACHE / wheel.name
        wheel.replace(destination)
        pointer = Path(staging) / 'selected'
        pointer.write_text(wheel.name + '\n')
        pointer.replace(CACHE / 'selected')
        return destination


def lock():
    pointer = CACHE / 'selected'
    if not pointer.is_file():
        raise SystemExit('Run python scripts/aperturedb_sdk.py pull before the Docker build.')
    wheel = CACHE / pointer.read_text().strip()
    if wheel.parent != CACHE or not wheel.match('aperturedb-*-py3-none-any.whl') or not wheel.is_file():
        raise SystemExit('Run the SDK pull again to refresh the wheel.')
    relative = wheel.relative_to(ROOT).as_posix()
    digest = hashlib.sha256(wheel.read_bytes()).hexdigest()
    # The named runtime requirement stays portable in published packages.
    # Poetry uses the SDK group's local file to resolve the same dependency.
    if (
        f'path = "{relative}"' not in (ROOT / 'pyproject.toml').read_text()
        or f'sha256:{digest}' not in (ROOT / 'poetry.lock').read_text()
    ):
        subprocess.run(['poetry', 'add', '--group', 'sdk', '--lock', './' + relative], cwd=ROOT, check=True)
    subprocess.run(['poetry', 'check', '--lock'], cwd=ROOT, check=True)
    # Poetry can reuse a previously installed wheel with the same version and path.
    subprocess.run(
        [
            'poetry',
            'run',
            'python',
            '-m',
            'pip',
            'install',
            '--no-index',
            '--no-deps',
            '--force-reinstall',
            str(wheel),
        ],
        cwd=ROOT,
        check=True,
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', nargs='?', choices=['prepare', 'pull', 'lock', 'install'], default='prepare')
    action = parser.parse_args().action
    if action in ('pull', 'prepare', 'install'):
        wheel = pull()
    if action == 'install':
        pip = [sys.executable, '-m', 'pip', 'install']
        subprocess.run([*pip, str(wheel), str(ROOT)], check=True)
        # pip can keep an index copy that has the same version.
        subprocess.run([*pip, '--no-index', '--no-deps', '--force-reinstall', str(wheel)], check=True)
    if action in ('lock', 'prepare'):
        lock()
