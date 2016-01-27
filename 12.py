# -*- coding: utf-8 -*-

maior = input("Digite o primeiro numero: ")

for x in range(7):
    numero = input("Digite um numero: ")
    if numero > maior:
        maior = numero

print(maior)