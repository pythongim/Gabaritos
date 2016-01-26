# -*- coding: utf-8 -*-

payment = input("Digite o valor da conta: ")
commission = payment * 0.10

print("Subtotal: R$ %d \t" %payment)
print("Comissão: R$ %d \t" %commission)
print("Total: R$ %d \t" %(payment+commission))
