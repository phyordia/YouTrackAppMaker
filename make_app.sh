#!/bin/bash

PORT=8880
BASEURL="http://localhost"
BASEDIR=$HOME/.youtrack
mkdir -p ${BASEDIR} 

# Install Python dependencies
echo "Installing Python dependencies"
pip install py2app rumps


# Download
echo "Downloading YopuTrack Zip"
if ls youtrack?*.zip 1> /dev/null 2>&1; then
    echo "Zip file exists - not downloading"
else
    echo "Zip file do not exist - downloading"
    wget https://download.jetbrains.com/charisma/youtrack-2020.3.12000.zip
fi


# Unzip
echo "Extacting Zip file"
find . -iname "youtrack*.zip" -exec unzip {}  \;
find . -type d -iname "youtrack*" -maxdepth 1 -exec mv '{}' src \; 
rm -rf ${BASEDIR}/src
mv src ${BASEDIR}/  

# Render python script with template
echo "Rendering python template"
sed "s|{{BASEDIR}}|$BASEDIR|g" YouTrackerLauncher_template.py > YouTrackerLauncher.py

# Create Icon - Requires Inkscape installed. This should be uncommented for recreating icon set (images/youtrack.icns)
#mkdir images
#./svg2icns.sh youtrack/internal/error_pages/logos/youtrack/youtrack.svg images/youtrack


# Build App bundle
echo "Building App bundle"
rm -rf build dist 
python setup.py py2app


# Configuring YouTrack Settings
echo "Configuring YouTrack Settings"
${BASEDIR}/src/bin/youtrack.sh configure \
        --listen-port=${PORT} \
        --data-dir="${BASEDIR}/data" \
        --logs-dir="${BASEDIR}/logs" \
        --backups-dir="${BASEDIR}/backups" \
        --temp-dir="${BASEDIR}/temp" \
        --base-url="${BASEURL}:${PORT}"

#cleanup
echo 'Cleaning Up'
rm -rf youtrack/ build/ YouTrackerLauncher.py

echo 'Done'