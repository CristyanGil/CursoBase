# -*- coding: utf-8 -*-
"""
Created on Wed Mar 4 22:51:33 2020

@author: Cristyan Gil
"""
dic = {'nombre' : 'Juan',
       'apellido': 'Perez',
       'edad': 22,
       "aprobo": True,
       'escuela': "IPN",
       'cursos': ['Python','HTML', 'CSS', 'JavaScript'] }

#%%     items
"""
Devuelve una lista de tuplas, cada tupla se compone de dos elementos: 
    el primero será la clave y el segundo, su valor.
"""

tupla = dic.items()
print("\nLa siguiente es la lista de tuplas resultantes: \n{}".format(tupla) )

#%%     keys
"""
Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
"""
llaves = dic.keys()
print("\nLa siguiente es la lista de llaves: \n", llaves )

#%%     values
"""
Retorna una lista de elementos, que serán los valores de nuestro diccionario.
"""

valores = dic.values()
#list(valores)
print(f"\nLa siguiente es la lista de valores: {valores}" )

#%%     pop
"""
Recibe como parámetro una clave, elimina esta y devuelve su valor. 
Si no lo encuentra, devuelve error.
"""
another_dic = {'nombre' : 'Pablo',
               'apellido': 'Martinez',
               'edad': 19,
               'escuela': "IPN",
               'cursos': ['Python','Java', 'C#'] }


another_dic.pop('escuela') 

print("\nEl diccionario resultante es: \n{}".format(another_dic) )

#another_dic['escuela'] = "UNAM"

#escuela = input( "Favor de ingresar el nombre de su escuela: ")
#another_dic['escuela'] = escuela

another_dic['escuela'] = input( "Favor de ingresar el nombre de su escuela: ")

print( another_dic )

#%%     Update
dic_1 = {'a' : 1, 'b' : 2, 'c': 3 , 'd' : 4}
dic_2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}
dic_1.update(dic_2)

print("\nEl diccionario actualizado es: \n{}".format(dic_1) )

#%%     Update
errores = {"error_escuela" : "Le sugiero ingresar el nombre de su escuela"}
try:
    another_dic["escuela"]
except:
    print( errores["error_escuela"] )

