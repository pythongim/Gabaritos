# -*- coding: utf-8 -*-

minutes = input("Digite o intervalo em minutos: ")

interval = minutes

days = minutes/1440 #1 dia em minutos (24h * 60minutos/1h
minutes -= 1440*days

hours = minutes/60
minutes -= 60*hours

print("%d minutos" %interval + " = %d dias" %days + ", %d horas" %hours + ", %d minutos" %minutes)