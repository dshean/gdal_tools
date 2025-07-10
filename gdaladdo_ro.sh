#! /bin/bash

#Wrapper around gdaladdo

r=gauss
#r=average
#r=nearest

#gdaladdo -ro -r $r --config COMPRESS_OVERVIEW LZW --config BIGTIFF_OVERVIEW YES $1 2 4 8 16 32 64

#Run in parallel for all inputs
parallel --bar "gdaladdo -q -ro -r $r --config COMPRESS_OVERVIEW LZW --config BIGTIFF_OVERVIEW YES {} 2 4 8 16 32 64" ::: "$@" 

#Add option for recursive overview generation
#Build first overview, then loop with that as input, always doing level 2
