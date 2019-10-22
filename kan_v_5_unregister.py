#NARZEDZIE DO ODREJESTROWANIA(UNREGISTER AS VERSIONED) TABEL W BAZIE SDE DLA GNIEWKOWO_KAN_V_5_0 POTRZEBNE DO UPDATU BAZY

# -*- coding: utf-8 -*-
import sys, arcpy
reload(sys)
sys.setdefaultencoding('utf-8')
it = arcpy.env.workspace = r"Database Connections\s4.asc-polska.pl.gniewkowo_kan_v_5_0.GNIEWKOWO_KAN_V_5_0_OWNER.sde"


ptd = arcpy.ListDatasets()
ptl = arcpy.ListTables()

for i in ptd and ptl:
    unre = arcpy.UnregisterAsVersioned_management(i)



