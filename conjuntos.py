# -*- coding: utf-8 -*-
"""
Created on Wed Mar 4 23:16:04 2020

@author: Cristyan Gil
"""
s = {'a', 'b', 'c', 'd', 
     1, 2, 3, 4,
     1, 2, 3, 4}

#s=set(['a', 'b', 'c', 'd', 
#     1, 2, 3, 4,
#     1, 2, 3, 4])

#%%     add y discard
"""
Los conjuntos son objetos mutables. 
Usando los métodos add() y discard() 
podemos añadir y remover un elemento 
indicándolo como argumento.
"""
s.add('e')

s.discard(4)

print("\nEl conjunto actualizado es: \n{}".format(s) )

#%%     in
"""
Para determinar si un elemento pertenece a un conjunto
"""
elem = 4
cond = elem in s
print("El conjunto contiene el elemento {}? \n{}".format(elem, cond) )


elem = 'a'
cond = elem in s
print("\nEl conjunto contiene el elemento {}? \n{}".format(elem, cond) )

#%%     len
"""
Para obtener el número de elementos
"""
l = len(s)
print("El tamaño del conjunto es: ", l)


#%%     union <|> 
"""
retorna un conjunto que contiene los elementos 
que se encuentran en al menos uno de los dos 
conjuntos involucrados en la operación.
"""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a|b
print( union )
#%%     interseccion <&> 

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

inter = a&b
print( inter )

#%%     diferencia <-> 

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

diff = a-b
print( diff )

diff2 = b-a
print( diff2 )

diff3 = b-b
print( diff3 )

#%%     igualdad <==> 

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {4, 2, 1, 3}

eq = a == b
print( eq )

eq = a == c
print( eq )

#%%     issubset e issuperset 
"""
issubset ayuda a probar si el primer conjunto es un subconjunto del segundo 
(o sea, que todos sus elementos estén en el otro) 
mientras que issuperset prueba lo contrario.
"""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {4, 2}

print("\nel conjunto {} es subset del conjunto {}?".format(b, a))
print(b.issubset(a) )

print("el conjunto {} es subset del conjunto {}?".format(c, a))
print(c.issubset(a) )


print("\nel conjunto {} es superset del conjunto {}?".format(a, b))
print(a.issuperset(b) )

print("el conjunto {} es superset del conjunto {}?".format(a, c))
print(a.issuperset(c) )
