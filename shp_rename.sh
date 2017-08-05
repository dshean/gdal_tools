#! /bin/bash

#Utility to rename all shapefile sidecar files 

inshp=$1
outshp=$2

if [ "$#" -ne 2 ] ; then
    echo "Usage is $(basename $0) in.shp out.shp"
fi

#See https://en.wikipedia.org/wiki/Shapefile for full list of sidecar file extensions
extlist="shp shx dbf prj"
extlist+=" sbn sbx cpg qix shp.xml"

for ext in $extlist
do
    if [ -e ${inshp%%.*}.$ext ] ; then 
        mv -iv ${inshp%%.*}.$ext ${outshp%%.*}.$ext
    fi
done
