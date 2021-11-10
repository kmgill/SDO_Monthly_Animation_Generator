# SDO Monthly Animation Generator

## Overview:
A set of old scripts which will generate a composite animation of the Sun using imagery from NASA's Solar Dynamics Observatory.

Requires:
 * Python
 * ImageMagick
 * ffmpeg (including libx264)
 * wget

The scripts are not very fancy and will likely break as soon as you look at them funny...

From the SDO Project Scientist: http://sdoisgo.blogspot.com/2014/03/sdo-on-astronomy-picture-of-day.html


**Left Image:** AIA 304, Upper chromosphere and lower transition region (He II)


**On the Right:**
- Top Left: HMI Intensitygram - colored
- Top Middle: AIA 131, Flaring regions of the corona (Fe VIII, Fe XXI)
- Top Right: AIA 211, Active regions of the corona (Fe XIV)
- Bottom Left: AIA 094, Flaring regions of the corona (Fe XVIII)
- Bottom Middle: AIA 335, Active regions of the corona (Fe XVI)
- Bottom Right: AIA 193, Corona and hot flare plasma (Fe XII)

**Images courtesy of NASA/SDO and the AIA, EVE, and HMI science teams.**

Recommended simplified credit when posting: NASA/GSFC/SDO/AIA/EVE/HMI/Your Name
## Running:
To run for a specific month:

`./create_monthly.sh 2021 11`

## Output:

[![Video Screenshot](https://img.youtube.com/vi/Zt5xZSIoPJE/0.jpg)](https://www.youtube.com/watch?v=Zt5xZSIoPJE)
