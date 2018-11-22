#! /usr/bin/env python

""" 
Return bounding box extent for input raster
xmin ymin xmax ymax

Useful for gdalwarp -te and warptool.py
"""

import sys
import argparse
from osgeo import gdal
from pygeotools.lib import geolib, warplib

def getparser():
    desc_str = "Get dataset extent"
    parser = argparse.ArgumentParser(description=desc_str, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t_srs', type=str, default=None, help='Proj4 string for desired output coordinates')
    parser.add_argument('-pad', type=float, default=None, \
            help='Width of padding to be applied to extent (meters, or units of specified t_srs')
    parser.add_argument('fn', type=str, help='Raster filename')
    return parser

parser = getparser()
args = parser.parse_args()

ds = gdal.Open(args.fn)

t_srs = None
if args.t_srs is not None:
    t_srs = warplib.parse_srs(args.t_srs)

extent = geolib.ds_extent(ds, t_srs=t_srs)
#extent = geolib.ds_geom_extent(ds)

#Pad by desired amount
if args.pad is not None:
    extent = geolib.pad_extent(extent, width=args.pad)

#Print to stdout
print(' '.join(map(str, extent)))
