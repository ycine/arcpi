
"""SKRYPT PRZEBIEGA PRZE WARSTWE LINIOWA I ZAPISUJE ID LINI(RUROCIAGOW) NA KTORYCH LEZA DWA
PUNKTY(STUDZIENKI)"""

"""TAK SIE UZYWA KURSORA ZEBY ZAPISAC WARTOSCI Z POLA DO LISTY:
>>> se = arcpy.da.SearchCursor("KANAL_ODCINKI","FID")
>>> for i in se:
...     f = i[0]
...     wolna.append(f)"""


# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')


mxd = arcpy.mapping.MapDocument("E:\ASC\JAROCIN\Jarocin_rzedne1.mxd")
mxd1 = arcpy.mapping.ListLayers(mxd)

t = 0
feczu_list = []

for i in mxd1:
    ficz = arcpy.MakeFeatureLayer_management(i, str(t) + i.name)
    feczu_list.append(ficz)
    t += 1


lista_fid = []
objects = range(0, 27456)
for z in objects:
    lupa = '"FID" = %i' %(z)
    ui = arcpy.SelectLayerByAttribute_management("1KANAL_ODCINKIwyc","NEW_SELECTION", lupa)
    select2 = arcpy.SelectLayerByLocation_management("0KAN_STUDZIENKIb0","INTERSECT","1KANAL_ODCINKIwyc","0.5 Meters","NEW_SELECTION")
    count1 = arcpy.GetCount_management("0KAN_STUDZIENKIb0")
    if count1[0] == '2':
        se = arcpy.da.SearchCursor("1KANAL_ODCINKIwyc", "FID")
        for i in se:
            f = i[0]
            lista_fid.append(f)