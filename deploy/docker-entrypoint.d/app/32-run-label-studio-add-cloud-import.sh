#!/bin/sh
set -e ${DEBUG:+-x}

echo >&3 "=> Run label-studio init..."
label-studio storage aperturedb "Cloud ApertureDB"
echo >&3 "=> label-studio init completed."
