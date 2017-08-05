#! /bin/bash

#In place compression for gtif (or any GDAL-supported format)

#Want to exit upon error
set -e

in=$1

echo
ls -lh $in

opt="-co TILED=YES -co COMPRESS=LZW -co BIGTIFF=IF_SAFER -co COPY_SRC_OVERVIEWS=YES -co COMPRESS_OVERVIEW=YES"

if gdalinfo $in | grep -q Float ; then 
    opt="$opt -co PREDICTOR=3"
fi

echo gdal_translate $opt $in /tmp/$$.tif
gdal_translate $opt $in /tmp/$$.tif
 
if [ $? -eq 0 ] ; then
    mv -f /tmp/$$.tif $in
else
    echo "Error with $in"
    rm -f /tmp/$$.tif
fi

ls -lh $in
