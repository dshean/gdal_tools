#! /bin/bash

#Script for heatmap generation from a vector dataset

in_fn=$1

#proj=true
proj=false
res=0.016666666666667
unit=arcsec

out_fn=${in_fn%.*}_heatmap_${res}m.tif

if $proj ; then
    ogr2ogr -t_srs EPSG:3857 $in_fn_proj $in_fn
    in_fn=${in_fn%.*}_proj.gpkg
    res=1000
    unit=m
fi

gdal_rasterize -co TILED=YES -co COMPRESS=LZW -co BIGTIFF=IF_SAFER -burn 1 -tr $res $res -ot UInt32 -a_nodata 0 -add $in_fn $out_fn
