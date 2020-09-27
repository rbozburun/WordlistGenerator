from termcolor import cprint
#!/usr/bin/env python
# -*- coding: utf-8 -*-
cprint("""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#      ~ PyWordlistGen 1.0 beta ~    #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                    #
#       Coded by Resul Bozburun      #
#       Date: 27.09.2020             #
#       Dev: Python3                 #
#                                    #
#~~~~~~~~~~~ INFO ~~~~~~~~~~~~~~~~~~~#
#                                    #
#    Simple wordlist generator       #
#                                    #
#************************************#
""","red")
def get_info():
    name = input("Adı: ")
    surname = input("Soyadı: ")
    bornDay = input("Kendisinin doğum günü (1-31 aralığında -02 yerine '2'-): ")
    bornMonth = input("Kendisinin doğum ayı (1-12 aralığında -02 yerine '2'-): ")
    bornYear = input("Kendisinin doğum yılı (xxxx formatında): ")

    father_name = input("Baba adı: ")
    father_bDay = input("Babasının doğum günü (1-31 aralığında -02 yerine '2'-): ")
    father_bMonth = input("Babasının doğum ayı (1-12 aralığında -02 yerine '2'-): ")
    father_bYear = input("Babasının doğum yılı (xxxx formatında): ")

    mother_name = input("Anne adı: ")
    mother_surname = input("Anne kızlık soyadı: ")
    mother_bDay = input("Annesinin doğum günü (1-31 aralığında -02 yerine '2'-): ")
    mother_bMonth = input("Annesinin doğum ayı (1-12 aralığında -02 yerine '2'-): ")
    mother_bYear = input("Annesinin doğum yılı (xxxx formatında): ")

    license_plate = input("Araba plakası (xx.xx.xx şeklinde giriniz ör: 38.TK.653): ")
    hometown_code = (input("Memleket plakası: "))
    city_code = (input("Yaşadığı ilin plakası: "))

    if license_plate != "":
        license_plateSplitted = license_plate.split(".")
        license_plate_first = license_plateSplitted[0]
        license_plate_second = license_plateSplitted[1]
        license_plate_third = license_plateSplitted[2]
    else:
        license_plate_first = ""
        license_plate_second = ""
        license_plate_third = ""


    infoList = [name,surname,mother_surname,bornDay,bornMonth,bornYear,father_name,father_bDay,father_bMonth,father_bYear,mother_name,mother_bDay,mother_bMonth,mother_bYear,license_plate_first,license_plate_second,license_plate_third,hometown_code,city_code]
    createWordlist(infoList)

def createWordlist(infoList):
    f = open('passwords.txt', 'w')

    bornYear = infoList[5]
    bornYearpre2 = bornYear[:2]
    bornYearlast2 = bornYear[2:]

    father_bornYear = infoList[9]
    father_bornYearpre2 = father_bornYear[:2]
    father_bornYearlast2 = father_bornYear[2:]

    mother_bornYear = infoList[13]
    mother_bornYearpre2 = mother_bornYear[:2]
    mother_bornYearlast2 = mother_bornYear[2:]

    for i in infoList:
        f.write(i + "\n")
        if i != "":
            f.write(i+bornYearpre2+"\n")
            f.write(i+father_bornYearpre2+"\n")
            f.write(i+mother_bornYearlast2+"\n")
            f.write(i+bornYearlast2+"\n")
            f.write(i+father_bornYearlast2+"\n")
            f.write(i+mother_bornYearlast2+"\n")
            for c in range(16):
                f.write(i+infoList[c]+"\n")

    f.close()


cprint("Cevabını bildiğiniz alanları doldurun, bilmediğiniz soruları 'ENTER' ile geçin...","yellow")
print()
get_info()