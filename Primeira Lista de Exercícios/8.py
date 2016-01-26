# -*- coding: utf-8 -*-

number = input("Digite um número: ")

flag = False
counter = 2

while counter*counter <= number:
    if number % counter == 0:
        flag = True
    counter += 1

if flag or number <= 1:
    print("O número não é primo")
else:
    print("O número é primo")