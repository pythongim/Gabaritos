# -*- coding: utf-8 -*-

n = input("Digite o limite inferior: ")
m = input("Digite o limite superior: ")

sum = 0

for x in range(n, m+1):
    sum += (1.0/x)

print(sum)