# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:10:10 2019

@author: Cristyan Gil
"""

# %%
###   Bucle While   ###

numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")

# %%
###   While Infinito   ###
numero = int(input("Escriba un número: "))
while True:
    numero += 1
    print("el numero siguiente es {}".format(numero) )
    if numero >= 1000:
        break
# %%