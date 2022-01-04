"""
I think what I'm going to try is to create a shapefile will points on
the centroid of known vehicle locations. In the shapefile I will also 
include a column with the image name. Once I have this information I should
be able to load an image, read the image metadata to find the extents of the image, 
pull the points that fall within that image, extract +- 6 meters in each direction
to get the extents of the extract, and then extract the image, and then save it into a 
new directory for use in the cnn.
"""


import tensorflow as tf
import geopandas as gpd

import shapely
import geopandas as gpd
from shapely.geometry import box


shp2 = gpd.read_file('vehicle_points2.shp')

#create a geometry column consisting of the bounding box of +- 6 meters from each vehicle centroid.
#this boxes will be used to clip each of the rasters into smaller images to be used to train the cnn.
shp2['minx'] = shp2['xcoord'] - 6
shp2['maxx'] = shp2['xcoord'] + 6
shp2['miny'] = shp2['ycoord'] -6
shp2['maxy'] = shp2['ycoord'] + 6

shp2['box'] = shp2.apply(lambda x: box(x['minx'], x['miny'], x['maxx'], x['maxy']), axis = 1)
print(shp2.head())

import gdal

ds = gdal.Open('G:/top_images/top15-50cm_48023_nc-cir/top15-nc-cir-50cm-baylor_48023.jp2')
