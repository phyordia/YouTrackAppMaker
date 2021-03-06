#!/usr/bin/env bash

inkscape="$HOME/Applications/Inkscape.app/Contents/MacOS/inkscape"
svg_file=$1
output_name=$2

set -e
test -d "$output_name.iconset" && rm -R "$output_name.iconset"
mkdir "$output_name.iconset"
$inkscape -z -o "$PWD/$output_name.iconset/icon_16x16.png" -w 16 -h 16 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_16x16@2x.png" -w 32 -h 32 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_32x32.png" -w 32 -h 32 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_32x32@2x.png" -w 64 -h 64 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_128x128.png" -w 128 -h 128 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_128x128@2x.png" -w 256 -h 256 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_256x256.png" -w 256 -h 256 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_256x256@2x.png" -w 512 -h 512 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_512x512.png" -w 512 -h 512 "$svg_file"
$inkscape -z -o "$PWD/$output_name.iconset/icon_512x512@2x.png" -w 1024 -h 1024 "$svg_file"
iconutil -c icns "$output_name.iconset"
rm -R "$output_name.iconset"
