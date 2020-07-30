#TO KOPIUJE WSZYSTKIE TABELE Z BAZY SDE TO BAZY PLIKOWEJ

# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')


it = arcpy.env.workspace = r"Database Connections\s4.asc-polska.pl.swiecie_kan_v_1_2.SWIECIE_KAN_V_1_2_OWNER.sde"
output = r"C:\Users\Marcin Wiaderkowicz\Desktop\kan_1_2filedb.gdb"

list_tables = arcpy.ListTables()
list_datasets = arcpy.ListDatasets()

for i in list_tables and list_datasets:
    arcpy.Copy_management(i, output + str('\\') + str(i))
