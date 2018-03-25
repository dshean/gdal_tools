# gdal_tools
General command-line utilities based on GDAL/OGR that don't fit in other repos

## Command-line utilities
- `gdal_compress.sh` - In-place LZW compression (with predictor) to reduce filesize
- `gdal_stats.sh` - print out stats, useful for scripting (`stats=$(gdal_stats.sh in.tif)`)
- `gdalinfoglob.sh` - gdalinfo for multiple files, useful to extract single attribute (`gdalinfoglob.sh *.tif | grep 'Pixel Size'`)
- `shp_rename.sh` - rename all files that comprise a shapefile
- `gdaladdo_ro.sh` - parallel external overview generation
- `hs.sh` - parallel shaded relief map generation

## Command-line utilities currently living in other repos (eventually migrate here)
- [`mask_raster.sh`](https://github.com/dshean/pygeotools/blob/master/pygeotools/mask_raster.sh) - mask raster by shp
- [`ogr_merge.sh`](https://github.com/dshean/pygeotools/blob/master/pygeotools/ogr_merge.sh) - merge shp
