"""
I think what I'm going to try is to create a shapefile will points on
the centroid of known vehicle locations. In the shapefile I will also 
include a column with the image name. Once I have this information I should
be able to load an image, read the image metadata to find the extents of the image, 
pull the points that fall within that image, extract +- 6 meters in each direction
to get the extents of the extract, and then extract the image, and then save it into a 
new directory for use in the cnn.
"""


#from osgeo import gdal, osr

'''

ds = gdal.Open('G:/top_images/top15-50cm_48397_nc-cir/top15-nc-cir-50cm-rockwall_48397.jp2')
print(ds.GetProjection())
gt = ds.GetGeoTransform()
print('incorrect')
minx = gt[0]
maxy = gt[3]
maxx = minx + gt[1] * ds.RasterXSize
miny = maxy + gt[5] * ds.RasterYSize
print(minx, maxx, miny, maxy)
print('incorrect')
cols = ds.RasterXSize
rows = ds.RasterYSize
bands = ds.RasterCount
"""Print the information to the screen. Converting the numbers returned to strings using str()"""
print("Number of columns: " + str(cols))
print("Number of rows: " + str(rows))
print("Number of bands: " + str(bands))
geoinformation = ds.GetGeoTransform()
"""The top left X and Y coordinates are at list positions 0 and 3 respectively"""
topLeftX = geoinformation[0]
topLeftY = geoinformation[3]
"""Print this information to screen"""
print("Top left X: " + str(topLeftX))
print("Top left Y: " + str(topLeftY))
"""first we access the projection information within our datafile using the GetProjection() method. This returns a string in WKT format"""
projInfo = ds.GetProjection()
"""Then we use the osr module that comes with GDAL to create a spatial reference object"""
spatialRef = osr.SpatialReference()
"""We import our WKT string into spatialRef"""
spatialRef.ImportFromWkt(projInfo)
"""We use the ExportToProj4() method to return a proj4 style spatial reference string."""
spatialRefProj = spatialRef.ExportToProj4()
"""We can then print them out"""
print("WKT format: " + str(spatialRef))
print("Proj4 format: " + str(spatialRefProj))


'''

import geopandas as gpd
shp = gpd.read_file('vehicle_points2.shp')
print(shp)
