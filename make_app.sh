#!/bin/bash

PORT=8880
BASEURL="http://localhost"
BASEDIR=$HOME/.youtrack


# Download
wget https://download.jetbrains.com/charisma/youtrack-2020.3.12000.zip

# Unzip
find . -iname "youtrack*.zip" -exec unzip {}  \;
find . -type d -iname "youtrack*" -maxdepth 1 -exec mv '{}' youtrack \;

# Create Icon
mkdir images
./svg2icns.sh youtrack/internal/error_pages/logos/youtrack/youtrack.svg images/youtrack


# Build App bundle
rm -rf build dist 
python setup.py py2app --resources youtrack
mv dist/youtrack_launcher.app .


./youtrack_launcher.app/Contents/Resources/youtrack/bin/youtrack.sh configure \
        --listen-port=${PORT} \
        --data-dir="${BASEDIR}/data" \
        --logs-dir="${BASEDIR}/logs" \
        --backups-dir="${BASEDIR}/backups" \
        --base-url="${BASEURL}:${PORT}"

#cleanup
rm -rf youtrack/ build/ dist/