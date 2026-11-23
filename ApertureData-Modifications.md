# Modifications to Label Studio

This is a document which outlines the modifications and how we use label studio
( in case there are multiple ways - which we test! )
## Building
The backend requires Python 3.10+ and the SDK wheel from
`registry-1.docker.io/aperturedata/aperturedb-python:latest`. Install ORAS on the
host to fetch the public SDK wheel.

For a Docker build, run `python3 scripts/aperturedb_sdk.py pull` before
`docker build .`. The Makefile and Docker build scripts prepare the wheel
automatically. For local development, run `python3 scripts/aperturedb_sdk.py`
and then `poetry install`. Preparation records the promoted wheel checksum in
`poetry.lock`. A new SDK version also updates the versioned filename in the
`sdk` Poetry group. Repeated preparation with the same bytes leaves both files
unchanged.
The built Label Studio distribution declares the SDK by package name. Users
install this checkout and its PyPI dependencies with `python -m pip install .`.
For pip-based development against the same wheel used in CI, use
`python3 scripts/aperturedb_sdk.py install`.

## ApertureDB storage

Image and prediction filters accept Athena expression arrays and previously
saved property filters. Import reads across image and bounding-box classes.
Export writes new annotation regions to the `BoundingBoxes` class and updates
existing regions on their source image.

## Changes

- Added token login method to /user/login/ with token? param.

- Added aperturedb as a cloud import/export mechanism.

- Added the ability to filter and organize import/export plugins for when
  running for hosting

