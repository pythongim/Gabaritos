# -*- coding: utf-8 -*-

first = input("Digite a primeira nota: ")

if first < 0 or first > 10:
    print("Nota inválida")
    first = input("Digite um valor válido: ")

second = input("Digite a segunda nota: ")

if second < 0 or second > 10:
    print("Nota inválida")
    second = input("Digite um valor válido: ")

media = (first+second)/2.0

print("A média é igual a: " + str(media))