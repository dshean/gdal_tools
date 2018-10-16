#! /usr/bin/env python

""" 
Return bounding box extent for input raster
xmin ymin xmax ymax

Useful for gdalwarp -te and warptool.py
"""

import sys
from osgeo import gdal
from pygeotools.lib import geolib

fn = sys.argv[1]
ds = gdal.Open(fn)
extent = geolib.ds_extent(ds)
#extent_geom = geolib.ds_geom_extent(ds)
print(' '.join(map(str, extent)))
#print ' '.join(map(str, extent_geom))
