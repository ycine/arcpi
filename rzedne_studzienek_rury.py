"""Z DWOCH RZEDNYCH STUDZIENEK CZYLI Z POLA 'rzedna_dna'
MAJA BYC UPDATOWANE POLA Z 'KANAL_ODCINKI' DO 'rzedna_kon' i rzedna_poc' MNIEJSZA WARTOSC TO
RZEDNA KONCOWA A WYZSZA RZEDNA POCZATKOWA --SKRYPT WYKONUJE SIE OKOLO 15 MINUT POLECAM MAKSYMALNA
LICZBE OBIEKTOW NIE WIEKSZA NIZ 1000 W TYM MOMENCIE SKRYPT ZABIERA ARCMAP PONAD 2200MB PAMIECI"""

"""zaznacz pierwszy obiekt z rury nastepnie, select by location z opcja radius, if select count = 2 ==True

TAK SIE UZYWA KURSORA ZEBY ZAPISAC WARTOSCI Z POLA DO LISTY:
>>> se = arcpy.da.SearchCursor("KANAL_ODCINKI","FID")
>>> for i in se:
...     f = i[0]
...     wolna.append(f)


zobaczyc czy da sie wybraz vertex poczatkowy z linii jak byla rysowana..
proceed ..
from selected 
"""

# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')

arcpy.env.workspace = r"E:\ASC\JAROCIN"

mxd = arcpy.mapping.MapDocument("E:\ASC\JAROCIN\Jarocin_rzedne1.mxd")
mxd1 = arcpy.mapping.ListLayers(mxd)

t = 0
feczu_list = []
tt = mxd1[1], mxd1[2]
for i in mxd1:
    ficz = arcpy.MakeFeatureLayer_management(i, str(t) + i.name)
    feczu_list.append(ficz)
    t += 1

feczu_list.pop(1)
# objects = arcpy.GetCount_management("1linie_Buffer1")
objects = range(0, 9)
#NIE DAJE RADY PAMIĘĆ ZA DUZO REKORDOW TO 450500
objectidlist = []

# arcpy.env.workspace = workspace
# edit = arcpy.da.Editor(workspace)
# edit.startEditing(True, True)
# edit.startOperation()

for z in objects:
    lupa = '"FID" = %i' %(z)
    ui = arcpy.SelectLayerByAttribute_management("3KANAL_ODCINKIwyc","NEW_SELECTION", lupa)
    for n in feczu_list[0]:
        select2 = arcpy.SelectLayerByLocation_management("0Export_Output","INTERSECT","3KANAL_ODCINKIwyc","0.5 Meters","NEW_SELECTION")
        count1 = arcpy.GetCount_management(feczu_list[0])
        if count1[0] == '2':
            fields = ["rzedna_dna"]
            sercz = arcpy.da.SearchCursor(feczu_list[0], fields)
            maks = max(sercz)
            sercz = arcpy.da.SearchCursor(feczu_list[0], fields)
            mini = min(sercz)
            objectidlist.append(maks[0])
            print mini
            print maks
            with arcpy.da.UpdateCursor("3KANAL_ODCINKIwyc", 'gora') as cur:
                for i in cur:
                    i[0] = '%s' % (maks)
                    cur.updateRow(i)
            with arcpy.da.UpdateCursor("3KANAL_ODCINKIwyc", 'dol') as cur:
                for i in cur:
                    i[0] = '%s' % (mini)
                    cur.updateRow(i)



#ZZERA ZA DUZO PAMIECI PONIZEJ WERSJA TROCHE ODCHUDZONA PETLI POWYZEJ
for z in objects:
    lupa = '"FID" = %i' %(z)
    ui = arcpy.SelectLayerByAttribute_management("1KANAL_ODCINKIwyc","NEW_SELECTION", lupa)
    for n in feczu_list[0]:
        select2 = arcpy.SelectLayerByLocation_management(n,"INTERSECT","1KANAL_ODCINKIwyc","0.5 Meters","NEW_SELECTION")
        count1 = arcpy.GetCount_management(feczu_list[0])
        if count1[0] == '2':
            fields = ["rzedna_dna"]
            sercz = arcpy.da.SearchCursor(feczu_list[0], fields)
            maks = max(sercz)
            sercz = arcpy.da.SearchCursor(feczu_list[0], fields)
            mini = min(sercz)
            with arcpy.da.UpdateCursor("1KANAL_ODCINKIwyc", 'gora') as cur:
                for i in cur:
                    i[0] = '%s' % (maks)
                    cur.updateRow(i)
            with arcpy.da.UpdateCursor("1KANAL_ODCINKIwyc", 'dol') as cur:
                for i in cur:
                    i[0] = '%s' % (mini)
                    cur.updateRow(i)
