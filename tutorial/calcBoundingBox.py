# -*- coding: utf-8 -*-
# calcBoundingBoxes.py
# Prend un fichier en entrée et calcul la bbox de chaque géométrie (test avec couche des pays du monde)
import os, os.path, shutil, osgeo.ogr, osgeo.osr

class MyLayer:
    "class pour instancier un fichier"
    dstLayer = None
    dstFile = None

    def __init__(self,srs,outpath,file):
        print "Constructeur"

        #Si les fichiers existent déjà on suppr...
        if os.path.exists(outpath):
            shutil.rmtree(outpath)

        os.mkdir(outpath)
        dstPath = os.path.join(outpath, file)


        #Définition du système de référence spatial
        spatialReference = osgeo.osr.SpatialReference()
        spatialReference.SetWellKnownGeogCS(srs)

        type = "ESRI Shapefile" #default is shapefile

        #Création du fichier en sortie
        if file.endswith('.shp'):
            type = "ESRI Shapefile"
        elif file.endswith('.tab'):
            type = "Mapinfo File"
        elif file.endswith('.json'):
            type = "GeoJSON"


        driver = osgeo.ogr.GetDriverByName(type)
        MyLayer.dstFile = driver.CreateDataSource(dstPath)
        MyLayer.dstLayer = MyLayer.dstFile.CreateLayer("layer", spatialReference)


    #Définition des valeurs attributaires
    def add_field(self,name,width):
        fieldDef = osgeo.ogr.FieldDefn(name,osgeo.ogr.OFTString)
        fieldDef.SetWidth(width)
        MyLayer.dstLayer.CreateField(fieldDef)

    def add_feature(self,minLong,maxLong,minLat,maxLat,value1,value2):
         #Création des géométries
        linearRing = osgeo.ogr.Geometry(osgeo.ogr.wkbLinearRing)
        linearRing.AddPoint(minLong, minLat)
        linearRing.AddPoint(maxLong, minLat)
        linearRing.AddPoint(maxLong, maxLat)
        linearRing.AddPoint(minLong, maxLat)
        linearRing.AddPoint(minLong, minLat)

        polygon = osgeo.ogr.Geometry(osgeo.ogr.wkbPolygon)
        polygon.AddGeometry(linearRing)

        #Création d'une feature
        feature = osgeo.ogr.Feature(self.dstLayer.GetLayerDefn())
        feature.SetGeometry(polygon)
        feature.SetField("NAME", value1)
        feature.SetField("ISO3", value2)

        MyLayer.dstLayer.CreateFeature(feature)

        feature.Destroy()

    #Close properly the shapefile
    def close(self):
        MyLayer.dstFile.Destroy()


################################################################################
### MAIN CODE ##################################################################
################################################################################
DATA_PATH = "/Users/macbookair/PycharmProjects/helloworld/DATA/vector/"
BBOX = "bbox.shp"
OUTPATH =  DATA_PATH + "bbox"
SRS = 'WGS84'

FIC = DATA_PATH + "world_borders_tm/world.shp"

#Creation d'un nouveau layer
layer_inst = MyLayer(SRS,OUTPATH,BBOX)
layer_inst.add_field("ISO3",50)
layer_inst.add_field("NAME",50)
#layer_inst.add_feature(0,10,0,10,"FRANCE","1")
#layer_inst.close()


#Ouverture du shapefile
shp = osgeo.ogr.Open(FIC)
layer = shp.GetLayer(0)
#
#countries = []

#Lecture du fichier
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    countryCode = feature.GetField("ISO3")
    countryName = feature.GetField("NAME")
    geometry = feature.GetGeometryRef()
    minLong,maxLong,minLat,maxLat = geometry.GetEnvelope()
    layer_inst.add_feature(minLong,maxLong,minLat,maxLat,countryName,countryCode)

    #lstCountry = (countryName, countryCode, minLat, maxLat, minLong, maxLong)
    #countries.append(lstCountry)

layer_inst.close()
#countries.sort()

#for name,code,minLat,maxLat,minLong,maxLong in countries:
#   print "%s (%s) lat=%0.4f..%0.4f, long=%0.4f..%0.4f" \
#  % (name, code,minLat, maxLat,minLong, maxLong)