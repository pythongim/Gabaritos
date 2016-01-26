# -*- coding: utf-8 -*-

number = input("Digite um número real: ")

integerNumber = int(number)

if(number == integerNumber or integerNumber+0.4 >= number):
    number = integerNumber
else:
    number = integerNumber+1

print(number)