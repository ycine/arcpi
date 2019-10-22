
# tu proba zamienienia pustych pol na wartosci <Null> w tabeli

# ref = [1,2,None,4,5,None,8]
#
#
#
# def update(value):
#       if value == None:
#           return NULL
#       else:
#             return value
#
# print update(ref)
#
#
#
#
# #  to w nowym polu zapisuje wartosci cyfrowe jako int z pola stringowego z literami i liczbami
#
# def makestr(TEXTSTRING):
#
#     lis = []
#     for i in TEXTSTRING:
#
#
#         if i.isdigit():
#             lis.append(i)
#
#
#     return ''.join(lis)
#
#
#
#
#
# #to jest ulepszenie tego kodu powyzej ma omijac pola bez liczb bo powyzszy skrypt sie na nich zatrzymuje
#
#
# TEXTSTRING = ("fd23g" ,"kjh567f", "fg44")
#
# def makestr(TEXTSTRING):
#     lis = []
#
#     for i in TEXTSTRING:
#
#         if i.isdigit():
#             lis.append(i)
#         #elif i.isalpha():
#             #continue
#
#
#
#     print lis
#     return ''.join(lis)
#
#
#
#
#
# print makestr(TEXTSTRING)
#
# #kolejne pytanie jak usunac duplikaty po zlaczeniu wartosci stringowych z 2 pol
# #  tak jak tu - "wo32c wo32c"
#
# def duplika(powtarzane):
#
#       pusta = []
#
#       for i in powtarzane:
#
#             if i.REMARK != i.TEXTSTRING:
#                   pole.append(i)
#
#             elif i.REMARK == i.TEXTSTRING:
#                   continue
#       return ''.join(pusta)
#
#
#
# #rozwiazanie z gis stack exchange ktore dziala :)
# def ex(text):
#       if (text is not None and any(char.isdigit() for char in text)):
#             return int(''.join([str(i) for i in text if i.isdigit()]))
#       else:
#             return None
#
#      ex(!TEXTSTRING!)
#
#
#
#
#
# #do powtorzen w kolumnie, dziala, ale zostawia te wartosci ktore sa takie same
# def ul(words):
#       if len(words) < 18:
#
#       wor = words.split()
#       return " ".join(sorted(set(wor), key=wor.index))
#
# ul(!REMARK!)
#
# # nie dziala ten kod nie usuwa powtorzonych slow
# from collections import OrderedDict
#
# def funk(remark_andt_extstring):
#
#     b =''.join(OrderedDict.fromkeys(remark_andt_extstring))
#     return b
#
# # moze cos takiego do kopiowania opisow zeby nie bylo powtorzen
# if TEXTSTRING == REMARK:
#     continue
#
# # to mialo kopiowac te dlugie opisy z uwag kopiuje ale nie wszystkie..
#
# def hi(uu):
#     if len(uu) > 15:
#         return uu
#     else:
#         None
#
# #przypisywanie rzednej nie dziala oczywiscie
# def hi(uu):
#     if [COVERING] == None:
#         if [Text] != None:
#             return uu
#
# #dalej to samo -,-
# def hi(uu):
#       if !COVERING! == None:
#       if uu is not None:
#             return uu
# def hi(uu):
#       if i in uu != None:
#
#             return uu
#       else:
#             None
#
#
# def ui(hh):
#       if !Text! =='':
#             return <Null>
#
#
# def ui(hh):
#     if hh =='':
#         return NULL
#     else:
#         return hh
#
# #to dziala ale nie wiem czemu to wyzej nie.. te 3 ponizej byly stosowane do przypisywania rzednej dla armatury, taki sam proces mozna wykorzystac dla innych punktowych z opisem
#
# def ui(hh):
#     if hh =='':
#         return NULL
#
# #to dziala ale po selekcji inaczej usunie wszystko czyli pewnie mozna to uproscic
# def hi(uu):
#       if uu != None:
#
#             return uu
#       else:
#             None
# #to dziala robilem z selekcja pol null
# def hi(uu):
#       if uu is not None:
#             return uu
#
#
# #do zrobienie skrypt ktory robi export na wszystkich warstwach z dxf i zapisuje je do geobazy jako shp
#
# # przenoszenie rzednej i poczatkowej z warstwy punkotwej na rurociagu i przypisanie ich do odpowiednich kolumn w  masce dla rur
# # skrypt arcpy ktory przypisze wszystkim warstwom uklad wspolrzednych
#
# # potrzebujemy przekopiowac z pola tekstowego wartosc druga liczbowa po "/"  np. "27,34/34,12" jak to zrobic ?
# def ex(text):
#      if text is not None:
#            return float(text[6:])
#      ex(!TEXTSTRING!)
#
#


print("alright")

#skrypt ktory  do roznych warstw poligonow linii itd. znajdujacych sie na danym obszarze przypisze im  wartość z tego obszaru

import arcpy
