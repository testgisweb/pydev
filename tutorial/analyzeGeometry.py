# -*- coding: utf-8 -*-
import osgeo.ogr
import math

fic = "/DATA/vector/tl_2009_us_state/tl_2009_us_state.shp"


#Fonction récursive qui parcours une géométrie, extrait chaque points
# et identifie le y le + haut et le y  le + bas, y étant la latitude :)

def findPoints(geometry, results):

    for i in range(geometry.GetPointCount()):
        x,y,z = geometry.GetPoint(i)

    if results['north'] == None or results['north'][1] < y:
        results['north'] = (x,y)

    if results['south'] == None or results['south'][1] > y:
        results['south'] = (x,y)

    for i in range(geometry.GetGeometryCount()):
        findPoints(geometry.GetGeometryRef(i), results)

#shapefile = osgeo.ogr.Open(fic)

#layer = shapefile.GetLayer(0)
#feature = layer.GetFeature(53)
#geometry = feature.GetGeometryRef()
#results = {'north' : None, 'south' : None}
#
#findPoints(geometry, results)
#print "Northernmost point is (%0.4f, %0.4f)" % results['north']
#print "Southernmost point is (%0.4f, %0.4f)" % results['south']


#Fonction d'analyse d'une géométrie
#Retourne le nombre de points composant la géom et son type
def analyzeGeometry(geometry,indent=0):
    s = []
    s.append(" " * indent)
    s.append(geometry.GetGeometryName())

    #
    if geometry.GetPointCount() > 0:
        s.append(" with %d data points " % geometry.GetPointCount())

    #
    if geometry.GetGeometryCount() > 0:
        s.append("containing :")

    print "".join(s)

    for i in range(geometry.GetGeometryCount()):
        analyzeGeometry(geometry.GetGeometryRef(i),indent+1)
#/analyzeGeometry

shapefile = osgeo.ogr.Open(fic)
layer = shapefile.GetLayer(0)
feature = layer.GetFeature(53)
geometry = feature.GetGeometryRef()

analyzeGeometry(geometry)