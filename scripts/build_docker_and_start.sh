SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python3 "${SCRIPT_DIR}/aperturedb_sdk.py" pull || exit $?

if bash ${SCRIPT_DIR}/../deploy/prebuild.sh; then
  docker build -t heartexlabs/label-studio ${SCRIPT_DIR}/..
fi

if [ $? -eq 0 ]; then
    docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
else
    echo "Docker build failed."
fi
