#!/bin/bash



rm composites/*
python create_manifest.py

function comp() {
	geo=$1
	f=$2
	out=$3
	
	if [ "x${geo}" != "x" ]; then
		composite -geometry ${geo} $f $out $out
	fi
}

idx=0
for l in $(cat manifest.lst | awk '{print $0}'); do
	echo Compositing frame \#${idx}
	outfile=`printf "composites/composite_%05d.jpg" $idx`
	
	convert -size 1920x1080 xc:black $outfile
	
	
	left=`echo $l | cut -f 1 -d :`
	r0=`echo $l | cut -f 2 -d :`
	r1=`echo $l | cut -f 3 -d :`
	r2=`echo $l | cut -f 4 -d :`
	r3=`echo $l | cut -f 5 -d :`
	r4=`echo $l | cut -f 6 -d :`
	r5=`echo $l | cut -f 7 -d :`
	
	left=`find . -name $left`
	r0=`find . -name $r0`
	r1=`find . -name $r1`
	r2=`find . -name $r2`
	r3=`find . -name $r3`
	r4=`find . -name $r4`
	r5=`find . -name $r5`
	
	convert -size 1920x1080 xc:black \
		\( $left -resize 960x960 \) -geometry 960x960+0+60 -composite \
		\( $r0 -resize 320x320 \)   -geometry 320x320+960+220 -composite \
		\( $r1 -resize 320x320 \)   -geometry 320x320+1280+220 -composite \
		\( $r2 -resize 320x320 \)   -geometry 320x320+1600+220 -composite \
		\( $r3 -resize 320x320 \)   -geometry 320x320+960+540 -composite \
		\( $r4 -resize 320x320 \)   -geometry 320x320+1280+540 -composite \
		\( $r5 -resize 320x320 \)   -geometry 320x320+1600+540 -composite \
		$outfile

	let idx=$idx+1
done

