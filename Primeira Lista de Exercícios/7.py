# -*- coding: utf-8 -*-

day = input("Digite um dia em 2013: ")

if day > 365 or day <= 0:
    print("O ano de 2013 tem apenas 365 dias.")

if day % 7 == 1:
    print("Terça-feira")
elif day % 7 == 2:
    print("Quarta-feira")
elif day % 7 == 3:
    print("Quinta-feira")
elif day % 7 == 4:
    print("Sexta-feira")
elif day % 7 == 5:
    print("Sábado")
elif day % 7 == 6:
    print("Domingo")
elif day % 7 == 0:
    print("Segunda-feira")