#!/bin/sh
set -e ${DEBUG:+-x}
exec 3>&1

if [ "${LABEL_STUDIO_DEFAULT_CLOUD_STORAGE}" != "" ]; then
    JSON_ARG=""
    JSON_CMD=""
    if [ "${LABEL_STUDIO_CLOUD_STORAGE_JSON_PATH}" != "" ]; then
        JSON_CMD="--config-json"
        JSON_ARG="${LABEL_STUDIO_CLOUD_STORAGE_JSON_PATH}"
    fi
    echo >&3 "=> Run manage.py storage_mgr --action add"
    cd label_studio && python3 manage.py storage_mgr --project 1 --action add --storage ${LABEL_STUDIO_DEFAULT_CLOUD_STORAGE} $JSON_CMD "$JSON_ARG"
    echo >&3 "=> manage.py storage_mgr --action add completed."
fi
