#!/bin/bash

year=$1
month=$2

month=`printf "%02d" $month`

./download.sh $year $month

python create_manifest.py $year $month

./create_composites.sh

ffmpeg -i "composites/composite_%05d.jpg" -pix_fmt yuv420p -vcodec libx264 -c:v libx264 -crf 18 -b:v 1M  SDO_${year}${month}.mp4