# -*- coding: utf-8 -*-

passo = input("Digite o passo em que vai variar a tabela em Celsius: ")

celsius = 0
farenheit = 32

while celsius < 100:
    print(str(celsius) + "ºC = " + str(farenheit) + " ºF")
    celsius += passo
    farenheit = (9*celsius/5.0)+32

