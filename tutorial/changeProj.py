# -*- coding: utf-8 -*-
# changeProj.py - chapter 5

import os, os.path, shutil
from osgeo import ogr
from osgeo import osr
from osgeo import gdal

DATA_PATH = "/Users/macbookair/PycharmProjects/helloworld/DATA/vector/"
fic = DATA_PATH + "miami/miami.shp"

# Définition de la projection source
srcProjection = osr.SpatialReference()
srcProjection.SetUTM(17)

# Définition de la projection de destination
dstProjection = osr.SpatialReference()
dstProjection.SetWellKnownGeogCS('WGS84') # Lat/long.

# Définition de la fonction de transformtion
transform = osr.CoordinateTransformation(srcProjection, dstProjection)

# Open the source shapefile.
srcFile = ogr.Open(fic)
srcLayer = srcFile.GetLayer(0)

# Creation du shapefile avec son systeme de projection
if os.path.exists("miami-reprojected"):
    shutil.rmtree("miami-reprojected")

os.mkdir("miami-reprojected")

driver = ogr.GetDriverByName("ESRI Shapefile")
dstPath = os.path.join("miami-reprojected", "miami.shp")
dstFile = driver.CreateDataSource(dstPath)
dstLayer = dstFile.CreateLayer("layer", dstProjection)


for i in range(srcLayer.GetFeatureCount()):
    feature = srcLayer.GetFeature(i)
    geometry = feature.GetGeometryRef()
    geometry.Transform(transform)
    newGeometry = geometry.Clone()
    newGeometry.Transform(transform)
    feature = ogr.Feature(dstLayer.GetLayerDefn())
    feature.SetGeometry(newGeometry)
    dstLayer.CreateFeature(feature)
    feature.Destroy()

# All done.
srcFile.Destroy()
dstFile.Destroy()