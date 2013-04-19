# -*- coding: utf-8 -*-
import osgeo.ogr
fic = "/DATA/vector/tl_2009_us_state/tl_2009_us_state.shp"
shapefile = osgeo.ogr.Open(fic)


layer = shapefile.GetLayer(0)
feature = layer.GetFeature(2)

print "Feature 2 has the following attributes:"
print

#Lit les attributs de l'objet
attributes = feature.items()

for key,value in attributes.items():
    print " %s = %s" % (key,value)
    print

geometry = feature.GetGeometryRef()
geometryName = geometry.GetGeometryName()

print "Feature's geometry data consists of " + geometryName
