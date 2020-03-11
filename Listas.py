# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:27:53 2019

@author: Cristyan Gil
"""
###   Definicion de listas   ###

lista1 = [1, 2.0, 4+3j, 'hey!', 100, 1000]

print("longitud de la lista: ", len(lista1))

print ( lista1[0] )
print ( lista1[2:4] )
print ( lista1[-1] )


lista2 = ["inicio", lista1, "fin" ]
print(lista2)


###   Metodos de listas   ###
lista3 = [] #Lista vacia
print(lista3)

lista3.append(100)
lista3.append(5800)
lista3.append([2,5])

lista3.extend([2,5])

print(lista3)

lista3.remove(2)
print(lista3)

lista3.index(5)


lista3.reverse()
print(lista3)
