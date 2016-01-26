# -*- coding: utf-8 -*-

firstday = input("Digite o dia: ")
firstmonth = input("Digite o mês: ")
firstyear = input("Digite o ano: ")

secondday = input("Digite o segundo dia: ")
secondmonth = input("Digite o segundo mês: ")
secondyear = input("Digite o segundo ano: ")


differenceyears = secondyear - firstyear
differencemonths = secondmonth - firstmonth
differencedays = secondday - firstday

if(not differenceyears):
    if(not differencemonths):
        print("%d dias" %differencedays)
    else:
        print("%d dias" %(30*differencemonths + differencedays))
else:
    if(not differencemonths):
        print("%d dias" %((differenceyears*360) + differencedays))
    else:
        print("%d dias" %((differenceyears*360) + (differencemonths*30) + differencedays))