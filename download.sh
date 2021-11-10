#!/bin/bash

year=$1
month=$2

wget -nc -r -l inf -p --no-parent --accept "*_512_0193.jpg" --accept "*_512_0131.jpg" --accept "*_512_0211.jpg" \
--accept "*_512_0094.jpg" --accept "*_512_0335.jpg" --accept "*_512_HMIIC.jpg" \
--accept "*_2048_0304.jpg"  --accept "*.html" \
http://sdo.gsfc.nasa.gov/assets/img/browse/${year}/${month}/
