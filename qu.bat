@echo off

call “C:\Program Files\QGIS 3.14\bin\o4w_env.bat

call “C:\Program Files\QGIS 3.14\apps\grass\grass78\etc\env.bat

@echo off

path %PATH%;C:\Program Files\QGIS 3.14\bin

path %PATH%;C:\Program Files\QGIS 3.14\apps\grass\grass78\lib

path %PATH%;C:\Program Files\QGIS 3.14\apps\Qt5\bin

path %PATH%;C:\Program Files\QGIS 3.14\apps\Python37\Scripts

set PYTHONPATH=%PYTHONPATH%;C:\Program Files\QGIS 3.14\apps\qgis\python

set PYTHONHOME=C:\Program Files\QGIS 3.14\apps\Python37

 
start  "" "E:\Program Files\JetBrains\PyCharm Community Edition 2019.1.1\bin\pycharm64.exe"