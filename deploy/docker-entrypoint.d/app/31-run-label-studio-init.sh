#!/bin/sh
set -e ${DEBUG:+-x}
exec 3>&1

echo >&3 "=> Run label-studio init..."
if [ "${LABEL_STUDIO_CREATE_PROJ_TITLE}" != "" ]; then
    echo >&3 "=> Creating Project \"${LABEL_STUDIO_CREATE_PROJ_TITLE}\""
    label-studio init -q "${LABEL_STUDIO_CREATE_PROJ_TITLE}" >&3
else
    label-studio init -q >&3
fi
echo >&3 "=> label-studio init completed."
