# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')

#JEZELI CHODZI O ZMIANY NA BAZIE SDE PRZEZ ARCPY TO BAZA NIE MOZE BYC GDZIEKOLWIEK WLACZONA NAWET W ARCMAP WPISUJEMY W OKNIE PYTHONA NA PUSTYM MXD PODCZAS WYKONYWANIA BEDZIE WIDAC TE POWSTAJACE FEATURE LAYER
it = arcpy.env.workspace = r"Database Connections\s4.asc-polska.pl.swiecie_wod_0_0.SWIECIE_WOD_0_0_OWNER.sde\swiecie_wod_0_0.SWIECIE_WOD_0_0_OWNER.WAT"
pt = arcpy.ListFeatureClasses()


t = 0
#tutaj zrobić listę warstw i niech z tego filtruje
# pti ='WAT'
# MOŻLIWE NAZWY PÓL :
# nazwy_kolumn = ['U_LOCATION', 'LOCATION', 'MIEJSCOWOSC']
# pty = [i for i in pt if pti in i]
feczu_list = []
for i in pt:
    kk = arcpy.MakeFeatureLayer_management(i, i + str(t))
    feczu_list.append(kk)
    t += 1

for i in feczu_list:
    arcpy.AddField_management(i, 'LOKALIZACJA', 'TEXT', 25)

# WŁĄCZENIE EDYCJI ŻEBY ZROBIC UPDATE POL
e = "Database Connections\s4.asc-polska.pl.swiecie_wod_0_0.SWIECIE_WOD_0_0_OWNER.sde"
edit = arcpy.da.Editor(e)
edit.startEditing(False, True)
edit.startOperation()

# list_pty.pop(4)
#TO NIE DZIALA NA DOLE ... JEZELI NIE BEDZIE POP TO TEN FEATURE ZROBI SIE WYZEJ
# gni = arcpy.SelectLayerByAttribute_management("Obręby_Świecie","NEW_SELECTION")
# we = arcpy.MakeFeatureLayer_management("Obręby_Świecie",'Obręby_Świecie_iter')

#UZYC DO WYBRANIA WARSTWY POLIGONOWEJ LIST COMPREHENSION
set = []
with arcpy.da.SearchCursor("swiecie_wod_0_0.SWIECIE_WOD_0_0_OWNER.Obreby_Swiecie35",'jpt_nazwa_') as se:
    for i in se:
        set.append(i)

for dx in set:
    lupa = "\"jpt_nazwa_\" = '%s'" %(dx)
    ui = arcpy.SelectLayerByAttribute_management("swiecie_wod_0_0.SWIECIE_WOD_0_0_OWNER.Obreby_Swiecie35","NEW_SELECTION", lupa)
    #DO TEGO MOMENTU JEST OK

    for i in feczu_list:
        selectl = arcpy.SelectLayerByLocation_management(i, "WITHIN", "swiecie_wod_0_0.SWIECIE_WOD_0_0_OWNER.Obreby_Swiecie35")
    for i in feczu_list:
        with arcpy.da.UpdateCursor(i, 'LOKALIZACJA') as cur:
            for i in cur:
                i[0] = '%s' %(dx)
                cur.updateRow(i)
    #POSZLO BEZ TEGO DELETE NIE WIEM CZY TU JEST PRZYCZYNA
    arcpy.Delete_management(i)
edit.stopOperation()
edit.stopEditing(True)
#arcpy.Delete_management(we)
print 'Zakończono pomyślnie.'

