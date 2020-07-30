# #zliczanie liczby warstw w qgis:
#
#
#
# layers = iface.mapCanvas().layers()
# t = 0
# for i in layers:
#     t+=1
#
#
#
#
# import os, sys
# from qgis.core import *
#
# layers = iface.mapCanvas().layers()
# #groups = qgis.subLayerCount.layers()
# u = QgsMapLayerRegistry
# c = 0
# for i in layers:
#     b = i.featureCount()
#     print(i.name)
#     print (b)
#     c += 1
#
# print("warstw:"+ str(c))
#
# #for o in QgsMapLayerActionRegistry.instance().mapLayers().values():
# #    print (o.name())
# #zliczanie warstw arcma
#
# import arcpy
#
# t = arcpy.mapping.MapDocument("CURRENT")
# tr = arcpy.mapping.ListLayers(t)
#
# tb = 0
# for i in tr:
#     tb += 1
#
# #jezeli sa podgrupy to
#
# for i in tr:
#     if i.isGroup
#     tb += 1

#DODANIE WARSTWY DO AKUTALNEGO PROJEKTU
# sc = r"D:\studia\Geoinformacja II stopień\Ćwiczenia odatkowe ArcGiS\cw 1\_shapefile\_shapefile\cieki_arc.shp"
# we = iface.addVectorLayer(sc,'dodana','ogr')

#ITERACJA PO POLACH
lej = iface.mapLayer()
for i in lej:
    print(i.getFeatures())