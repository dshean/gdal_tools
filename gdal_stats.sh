#! /bin/bash

#Little utility to return the min, max, mean, std as computed by gdal

in_fn=$1

#Delete existing stats file (can cause problems if original image changed)
if [ -e ${in_fn}.aux.xml ] ; then
    rm ${in_fn}.aux.xml
fi

stats=$(gdalinfo -stats $in_fn | grep 'Minimum=' | sed -e 's/=/ /g' -e 's/,//g' | awk '{print $2, $4, $6, $8}') 

#min max mean std
echo $stats
