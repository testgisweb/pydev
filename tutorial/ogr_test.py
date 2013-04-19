# -*- coding: utf-8 -*-
import osgeo.ogr
fic = osgeo.ogr.Open("/Users/macbookair/PycharmProjects/helloworld/DATA/vector/world_borders/world_borders.shp")
layer = fic.GetLayer(0)

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    countryCode = feature.GetField("ISO3")
    countryName = feature.GetField("NAME")
    geometry = feature.GetGeometryRef()
    minLong,maxLong,minLat,maxLat = geometry.GetEnvelope()