#!/usr/bin/python

import os
import sys
import re
import time
from os import walk
from datetime import datetime
import calendar

ROOT = "/data/SDO/sdo.gsfc.nasa.gov/assets/img/browse/2021/10/"
f = []
for (dirpath, dirnames, filenames) in walk(ROOT):
    f.extend(filenames)
    #break

def parse_date(fn):
	dt = fn[0:8]
	year = int(dt[0:4])
	month = int(dt[4:6])
	day = int(dt[6:8])
	return year, month, day


def parse_time(fn):
	tm = fn[9:15]
	hour = int(tm[0:2])
	minute = int(tm[2:4])
	second = int(tm[4:6])
	return hour, minute, second

def parse_datetime(fn):
	year, month, day = parse_date(fn)
	hour, minute, second = parse_time(fn)

	dt = datetime(year, month, day, hour, minute, second)
	timestamp=calendar.timegm(dt.utctimetuple())
	return timestamp


def find_files(pattern):
	lst = []
	prog = re.compile(pattern)
	for fn in f:
		if prog.match(fn) != None:
			mtime = parse_datetime(fn)
			lst.append({
				"file" : fn,
				"mtime" : mtime
			})
	lst.sort(key=lambda x: x["mtime"])
	return lst


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        sys.exit(1)

    year = sys.argv[1]
    month = sys.argv[2]

    ROOT = "/data/SDO/sdo.gsfc.nasa.gov/assets/img/browse/%s/%02d/"%(year, int(month))

    print("Processing for month %s, year %s in root %s"%(month, year, ROOT))

    left_lst = find_files(".*_2048_0304\.jpg")
    r0_lst = find_files(".*_512_HMIIC\.jpg")
    r1_lst = find_files(".*_512_0131\.jpg")
    r2_lst = find_files(".*_512_0211\.jpg")
    r3_lst = find_files(".*_512_0094\.jpg")
    r4_lst = find_files(".*_512_0335\.jpg")
    r5_lst = find_files(".*_512_0193\.jpg")

    print("Left:", len(left_lst))

    print("r0:", len(r0_lst))
    print("r1:", len(r1_lst))
    print("r2:", len(r2_lst))
    print("r3:", len(r3_lst))
    print("r4:", len(r4_lst))
    print("r5:", len(r5_lst))

    master = left_lst

    if len(r0_lst) < len(master):
        master = r0_lst
    if len(r1_lst) < len(master):
        master = r1_lst
    if len(r2_lst) < len(master):
        master = r2_lst
    if len(r3_lst) < len(master):
        master = r3_lst
    if len(r4_lst) < len(master):
        master = r4_lst
    if len(r5_lst) < len(master):
        master = r5_lst

    print("Master:", len(master))


    manifest = []

    def find_nearest_in_list(millis, lst):

        nearest = None
        for entry in lst:
            if nearest == None:
                nearest = entry
            elif abs(entry["mtime"] - millis) < abs(nearest["mtime"] - millis):
                nearest = entry
            #print abs(entry["mtime"] - millis),  abs(nearest["mtime"] - millis)
        return nearest

    outFile = open("manifest.lst", "w")

    frame_num = 1
    for entry in master:
        print("Making selections for frame #", frame_num)
        frame_num = frame_num + 1
        left = find_nearest_in_list(entry["mtime"], left_lst)

        r0 = find_nearest_in_list(entry["mtime"], r0_lst)
        r1 = find_nearest_in_list(entry["mtime"], r1_lst)
        r2 = find_nearest_in_list(entry["mtime"], r2_lst)
        r3 = find_nearest_in_list(entry["mtime"], r3_lst)
        r4 = find_nearest_in_list(entry["mtime"], r4_lst)
        r5 = find_nearest_in_list(entry["mtime"], r5_lst)
        outFile.write("%s:%s:%s:%s:%s:%s:%s\n"%(left["file"], r0["file"], r1["file"], r2["file"], r3["file"], r4["file"], r5["file"]))

    outFile.close()
