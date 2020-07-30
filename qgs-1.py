""" ****************************************************
    **                                                **
    ** Tutaj mozna pisac skrypty bez odpalania qgis-a **
    **                                                **
    ****************************************************"""


from qgis.core import *

QgsApplication.setPrefixPath("C:\Program Files\QGIS 3.14", True)
qgs = QgsApplication([], True)

qgs.initQgis()

mez = r"D:\arc\QGIS_PyQt\cbdg_srodowisko_mezoregiony_2009_06_07\mezoregiony.shp"
vlayer = QgsVectorLayer(mez, "mezoregiony", "ogr")

print(vlayer)
#tutaj wpisujesz processing
qgs.exitQgis()



from pathlib import Path

mez = r"D:\arc\QGIS_PyQt\cbdg_srodowisko_mezoregiony_2009_06_07\mezoregiony.shp"
mez1 = QgsVectorLayer(mez, "mezoregiony", "ogr")

QgsProject.instance().addMapLayer(mez1)
gniew_rury = r"D:\arc\QGIS_PyQt\Gniewkowo_wod_v_3_0\WOD_RURA.shp"
gniew_hydranty= r"D:\arc\QGIS_PyQt\Gniewkowo_wod_v_3_0\WOD_HYDRANT.shp"
gniew_armatury = r"D:\arc\QGIS_PyQt\Gniewkowo_wod_v_3_0\WOD_ARMATURA.shp"

gniewkowo_warstwy = []
gniewkowo_warstwy.append(gniew_rury)
gniewkowo_warstwy.append(gniew_hydranty)
gniewkowo_warstwy.append(gniew_armatury)

t= 0
for i in gniewkowo_warstwy:
    pa = Path(i)
    pa1 = pa.name
    att = QgsVectorLayer(i, pa1 + str(t), "ogr")
    t += 1
    QgsProject.instance().addMapLayer(att)


