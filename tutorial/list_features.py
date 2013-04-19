# -*- coding: utf-8 -*-
import osgeo.ogr

shapefile = osgeo.ogr.Open("/DATA/vector/tl_2009_us_state/tl_2009_us_state.shp")
#Compte le nombre de couches
numLayers = shapefile.GetLayerCount()
print "Shapefile contains %d layers" %numLayers
print

#Parcours les layers
for layerNum in range(numLayers):
    #récupère la couche
    layer = shapefile.GetLayer(layerNum)
    #récupère son sys réf spatial
    spatialRef = layer.GetSpatialRef().ExportToProj4()
    #récupère le nombre de feature
    numFeatures = layer.GetFeatureCount()
    print "Layer %d has spatial reference %s" %(layerNum,spatialRef)
    print "Layer %d has %d features: " %(layerNum,numFeatures)
    print

#Parcours les features
for featureNum in range(numFeatures):
    feature = layer.GetFeature(featureNum)
    featureName = feature.GetField("NAME")
    print "Feature %d has name %s" %(featureNum, featureName)
    print

print "Feature %d has name %s" % (featureNum,featureName)

