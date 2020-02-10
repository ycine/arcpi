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
