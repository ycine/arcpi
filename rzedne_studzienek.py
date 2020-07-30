<<<<<<< HEAD
# -*- coding: utf-8 -*-
import sys, arcpy
from arcpy.sa import *
#DZIEKI TEMU MOZNA KOPIOWAC CALY SKRYPT I WKLEJAC DO ARCMAP
reload(sys)
sys.setdefaultencoding('utf-8')


mxd = arcpy.mapping.MapDocument("C:\Users\Marcin Wiaderkowicz\Desktop\jarocin spatialPY.mxd")
mxd1 = arcpy.mapping.ListLayers(mxd)

for i in mxd1:
    print(i)

t = 0
feczu_list = []

for i in mxd1:
    ficz = arcpy.MakeFeatureLayer_management(i, str(t) + i.name)
    feczu_list.append(ficz)
    t += 1

objects = range(1, 40504)
select_list = []


for z in objects:
    lupa = '"OBJECTID" = %i' %(z)
    ui = arcpy.SelectLayerByAttribute_management("1Linie1_Buffer5","NEW_SELECTION", lupa)
    for t in feczu_list[0]:
        select2 = arcpy.SelectLayerByLocation_management(t, "INTERSECT", "1Linie1_Buffer5")
        count1 = arcpy.GetCount_management(feczu_list[0])
        if count1[0] == '2':
            ee = arcpy.SelectLayerByAttribute_management(t,"SWITCH_SELECTION",)



        else:
            break



        for i in select_list:
            sercz = arcpy.da.SearchCursor(feczu_list[0], "numberstring")
            maks = max(sercz)
        print maks








for z in objects:
    lupa = '"OBJECTID" = %i' %(z)
    ui = arcpy.SelectLayerByAttribute_management("1Linie1_Buffer5","NEW_SELECTION", lupa)
    for t in feczu_list[0]:
        select2 = arcpy.SelectLayerByLocation_management(t, "INTERSECT", "1Linie1_Buffer5")
        count1 = arcpy.GetCount_management(feczu_list[0])
        if count1[0] == '2':
            select_list.append(select2)
        else:
            break
        for i in select_list:
            #sercz = arcpy.da.SearchCursor(feczu_list[0], "numberstring", sql_clause=(None, 'ORDER BY numberstring'))
            sercz = arcpy.da.SearchCursor(feczu_list[0], "numberstring")
            maks = max(sercz)
            makz = round(float('.'.join(str(ele) for ele in maks)), 2)



#DODAC PETLE SPRADZAJACA CZY SA ZNALEZNIONE 2 PUNKTY CZY 1 ALBO WCALE..
#TUTAJ ALBO DODAĆ NOWE POLE I NIECH PRZYPISUJE DO POLA JAKIS ZAPIS


# for i in
# for dx in set:
#     lupa = "\"jpt_nazwa_\" = '%s'" %(dx)
#     ui = arcpy.SelectLayerByAttribute_management("gniew_iter","NEW_SELECTION", lupa)
#     gni = arcpy.SelectLayerByAttribute_management("gniew", "CLEAR_SELECTION")
#
#     for i in mxd1:
#         ficz = arcpy.MakeFeatureLayer_management(i, str(t) + i.name)
#         feczu_list.append(ficz)
#         t += 1
#     for i in feczu_list:
#         selectl = arcpy.SelectLayerByLocation_management(i, "WITHIN", "gniew_iter")
#     for i in feczu_list:
#         with arcpy.da.UpdateCursor(i, 'trzask') as cur:
#             for i in cur:
#                 i[0] = '%s' % (dx)
#                 cur.updateRow(i)


# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')

mxd = arcpy.mapping.MapDocument("C:\Users\dom\Desktop\demo.mxd")
mxd1 = arcpy.mapping.ListLayers(mxd)

t = 0
feczu_list = []

for i in mxd1:
    ficz = arcpy.MakeFeatureLayer_management(i, str(t) + i.name)
    feczu_list.append(ficz)
    t += 1

# objects = arcpy.GetCount_management("1linie_Buffer1")
objects = range(1,5)
objectidlist = []

for z in objects:
    lupa = '"OBJECTID" = %i' %(z)
    ui = arcpy.SelectLayerByAttribute_management("1linie_Buffer1","NEW_SELECTION", lupa)
    for n in feczu_list[0]:
        select2 = arcpy.SelectLayerByLocation_management(n, "INTERSECT", "1linie_Buffer1")
        count1 = arcpy.GetCount_management(feczu_list[0])
        if count1[0] == '2':
            fields = ['liczba', 'OBJECTID']
            sercz = arcpy.da.SearchCursor(feczu_list[0], fields)
            maks = max(sercz)
            objectidlist.append(maks[1])
            print maks

clen = arcpy.SelectLayerByAttribute_management("0punkty","CLEAR_SELECTION")
for o in objectidlist:
    lupa2 = '"OBJECTID" = %i' % (o)
    select3 = arcpy.SelectLayerByAttribute_management("0punkty","ADD_TO_SELECTION",lupa2)
print ('Wykonano.')
=======
# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')

mxd = arcpy.mapping.MapDocument("C:\Users\Marcin Wiaderkowicz\Desktop\jarocin spatialPY.mxd")
mxd1 = arcpy.mapping.ListLayers(mxd)

t = 0
feczu_list = []

for i in mxd1:
    ficz = arcpy.MakeFeatureLayer_management(i, str(t) + i.name)
    feczu_list.append(ficz)
    t += 1

# objects = arcpy.GetCount_management("1linie_Buffer1")
objects = range(1, 10000)
#NIE DAJE RADY PAMIĘĆ ZA DUZO REKORDOW TO 450500
objectidlist = []

for z in objects:
    lupa = '"OBJECTID" = %i' %(z)
    ui = arcpy.SelectLayerByAttribute_management("1Linie1_Buffer5","NEW_SELECTION", lupa)
    for n in feczu_list[0]:
        select2 = arcpy.SelectLayerByLocation_management(n, "WITHIN_A_DISTANCE", "1Linie1_Buffer5")
        count1 = arcpy.GetCount_management(feczu_list[0])
        if count1[0] == '2':
            fields = ['numberstring', 'OBJECTID']
            sercz = arcpy.da.SearchCursor(feczu_list[0], fields)
            maks = max(sercz)
            objectidlist.append(maks[1])
            print maks



clen = arcpy.SelectLayerByAttribute_management("0punkty","CLEAR_SELECTION")
for o in objectidlist:
    lupa2 = '"OBJECTID" = %i' % (o)
    select3 = arcpy.SelectLayerByAttribute_management("0punkty", "ADD_TO_SELECTION", lupa2)
print ('Wykonano.')


#PRZED TYM SELEKCJA PO ANGLE >0

fields = ['OBJECTID', 'IN_FID']
lis1 = []
for i, y in sercz:
    print i, y
    lis1.append(y)

#ODZNACZ SELEKCJE

for o in lis1:
   lupa2 = '"OBJECTID" = %i' % (o)
   select3 = arcpy.SelectLayerByAttribute_management("adnotacje_feature_topoint", "ADD_TO_SELECTION", lupa2)
>>>>>>> ecc87628aead311364f7331d95d234e454b3e894
