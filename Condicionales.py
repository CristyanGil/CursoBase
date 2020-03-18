# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:07:24 2019

@author: Cristyan Gil
"""

# %%
###   Condicional if   ###
numero = int(input("Cuanto es 2+2 ?: "))
if numero == 4:
    print("\nCorrecto señor usuario!")

# %%
###   Condicional if, else  ###
numero = int(input("Escriba un multiplo de 2: "))
if numero%2 != 0:
    print("El número ingresado no es multiplo de 2" )
else:
    print("\nCorrecto señor usuario!")

# %%
###   Condicional if, elif, else  ###
edad = int(input("Cuantos años tiene?: "))
if edad >= 60:
    print("\nÚsted ya pertenece a la tercera edad" )
elif edad <60 and edad >=18:
    print("\nÚsted es mayor de edad" )
elif edad <13 and edad >=2:
    print("\nÚsted es un niño" )
elif edad <2 and edad >=0:
    print("\nÚsted es un bebe" )
else:
    print("\nEdad invalida")
# %%