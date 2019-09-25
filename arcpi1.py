# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')

mxd = arcpy.mapping.MapDocument("C:\Users\Marcin Wiaderkowicz\Desktop\proba1.mxd")
mxd1 = arcpy.mapping.ListLayers(mxd)

t = 0
mxd1.pop(4)
gni = arcpy.SelectLayerByAttribute_management("gniew","NEW_SELECTION")
we = arcpy.MakeFeatureLayer_management("gniew",'gniew_iter')

set = []
with arcpy.da.SearchCursor("gniew",'jpt_nazwa_') as se:
    for i in se:
        set.append(i)

for dx in set:
    lupa = "\"jpt_nazwa_\" = '%s'" %(dx)
    ui = arcpy.SelectLayerByAttribute_management("gniew_iter","NEW_SELECTION", lupa)
    gni = arcpy.SelectLayerByAttribute_management("gniew", "CLEAR_SELECTION")
    feczu_list = []
    for i in mxd1:
        ficz = arcpy.MakeFeatureLayer_management(i, str(t) + i.name)
        feczu_list.append(ficz)
        t += 1
    for i in feczu_list:
        selectl = arcpy.SelectLayerByLocation_management(i, "WITHIN", "gniew_iter")
    for i in feczu_list:
        with arcpy.da.UpdateCursor(i, 'trzask') as cur:
            for i in cur:
                i[0] = '%s' %(dx)
                cur.updateRow(i)
    for i in feczu_list:
        arcpy.Delete_management(i)
arcpy.Delete_management(we)
print 'Zakończono pomyślnie.'
