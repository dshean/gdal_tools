#! /usr/bin/env python

#David Shean
#dshean@gmail.com

#Utility to convert csv to a vrt that can be processed with OGR or GIS 

import sys, os
import subprocess

out_csv = sys.argv[1]
#proj = sys.argv[2]
out_vrt = os.path.splitext(out_csv)[0]+'.vrt'

#This is ECEF, the coord sys of ASP PC
#srs='EPSG:4978'
#This is WGS84
srs='EPSG:4326'
#S Polar stereographic
#srs='EPSG:3031'

print("Writing out vrt")

#Header w/ field names
#x = 'x'
#y = 'y'
#z = 'z'

#y = 'lat'
#x = 'lon'
#z = 'z'

y = 'lat'
x = '# lon'
z = 'height_above_datum'

#y = 'Lat'
#x = 'Lon'
#z = 'Elev'

#No header
#lat, lon, z --> x, y, z
#x = 'field_2'
#y = 'field_1'
#z = 'field_3'

#No header
#lon, lat, z --> x, y, z
#x = 'field_4'
#y = 'field_5'
#z = 'field_6'

f = open(out_vrt, 'w')
f.write('<OGRVRTDataSource>\n')
f.write('   <OGRVRTLayer name="%s">\n' % os.path.splitext(out_csv)[0])
f.write('        <SrcDataSource>%s</SrcDataSource>\n' % out_csv)
#f.write('        <GeometryType>wkbPoint25D</GeometryType>\n')
f.write('        <GeometryType>wkbPoint</GeometryType>\n')
f.write('        <LayerSRS>%s</LayerSRS>\n' % srs)
#f.write('        <GeometryField encoding="PointFromColumns" x="%s" y="%s" z="%s"/>\n' % (x, y, z))
f.write('        <GeometryField encoding="PointFromColumns" x="%s" y="%s"/>\n' % (x, y))
f.write('    </OGRVRTLayer>\n')
f.write('</OGRVRTDataSource>\n')
f.close()

#Make sure lon is -180 to 180
#awk -F',' '{OFS=", "};{$2=$2-360; print}' $out_csv > temp
#mv temp $out_csv

#Reproject
#This doesn't work 
#ogr2ogr -f CSV -t_srs EPSG:3031 pig_icesat_all_EPSG3031.csv pig_icesat_all.vrt -lco GEOMETRY=AS_XYZ pig_icesat_all
#This does w/ shp in the middle
#ogr2ogr -t_srs EPSG:3031 pig_icesat_all_EPSG3031.shp pig_icesat_all.vrt
#ogr2ogr -f CSV pig_icesat_all_EPSG3031.csv pig_icesat_all_EPSG3031.shp -lco GEOMETRY=AS_XYZ
#Need to specify the layer name 
#ogr2ogr -f CSV -nln out out.csv in.shp

#cmd = ['ogr2ogr', '-f', 'CSV', '-nln', os.path.splitext(out_csv)[0], os.path.splitext(out_csv)[0]+'.shp', out_csv]
cmd = ['ogr2ogr', '-f', 'GPKG', '-mapFieldType', 'All=Real', '-nln', os.path.splitext(out_csv)[0], os.path.splitext(out_csv)[0]+'.gpkg', out_vrt]
subprocess.call(cmd)
