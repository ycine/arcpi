#TO KOPIUJE WSZYSTKIE TABELE Z BAZY SDE TO BAZY PLIKOWEJ

# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')


it = arcpy.env.workspace = r"Database Connections\s4.asc-polska.pl.swiecie_kan_v_1_2.SWIECIE_KAN_V_1_2_OWNER.sde"

list_tables = arcpy.ListTables()
list_dataset = arcpy.ListDatasets()

for i in list_tables and list_tables:
    arcpy.Copy_management(i, output + str('\\') + str(i))