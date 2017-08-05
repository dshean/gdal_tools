#! /bin/bash

#Run gdalinfo for multiple input files
#Useful for grep on field: gdalinfoglob.sh *tif | grep 'Pixel Size'

echo
for i in $@
do
    gdalinfo $i
    echo
    echo "---------------------------------------------------------------------------"
    echo
done
