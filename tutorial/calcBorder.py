# -*- coding: utf-8 -*-
# calcBorders.py - chapter 5
#Task: Calculate the border between Thailand and Myanmar
import os, os.path, shutil
from osgeo import ogr
from osgeo import osr
from shapely import wkt

DATA_PATH = "/Users/macbookair/PycharmProjects/helloworld/DATA/vector/TM_WORLD_BORDERS-0.3/"

shapefile = ogr.Open(DATA_PATH + "TM_WORLD_BORDERS-0.3.shp")
thailand = None
myanmar = None

for i in range(layer.GetFeatureCount()):

    feature = layer.GetFeature(i)
    if feature.GetField("ISO2") == "TH":
        geometry = feature.GetGeometryRef()
        thailand = wkt.loads(geometry.ExportToWkt())

    elif  feature.GetField("ISO2") == "MM":
        geometry = feature.GetGeometryRef()
        myanmar = wkt.loads(geometry.ExportToWkt())

    commonBorder = thailand.intersection(myanmar)

    if os.path.exists("common-border"):
        spatialReference = ospageo.osr.StialReference()
        spatialReference.SetWellKnownGeogCS('WGS84')
        driver = osgeo.ogr.GetDriverByName("ESRI Shapefile")
        dstPath = os.path.join("common-border", "border.shp")
        dstFile = driver.CreateDataSource(dstPath)
        dstLayer = dstFile.CreateLayer("layer", spatialReference)

        wkt = shapely.wkt.dumps(commonBorder)

        feature = osgeo.ogr.Feature(dstLayer.GetLayerDefn())
        feature.SetGeometry(osgeo.ogr.CreateGeometryFromWkt(wkt))
        dstLayer.CreateFeature(feature) feature.Destroy()
        dstFile.Destroy()