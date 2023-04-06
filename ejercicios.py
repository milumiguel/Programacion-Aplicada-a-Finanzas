#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:58:42 2023

@author: milu
"""

def suma(x):
    # toma lista como unico arg
    s = 0
    for i in range(len(x)): # itera sobre la lista y le suma cada elemento i a s
        s+=x[i]
    return s

lista = [1,2,3,4]

print(suma(lista))



#%%

def suma2(x):
    if len(x)==1:
        s = x[0]
    else:
        s = x[len(x)-1] + suma2(x[:-1])
    return s

# funcion recursiva con condicion! se llama a si misma (linea 28)

#%%

# EJ 174
#Euclides

def div_comun_mayor(a,b):
    """Esta función (recursiva) calcula el divisor comun mayor entre dos numeros
    a y b que toma como argumentos mediante el algoritmo de Euclides."""
    
    if b == 0:
        return a
    else:
        c = a % b
        return div_comun_mayor(b, c)
        
print(div_comun_mayor(7, 49))
        
#%%

# dcm por factores primos
#  factores primos comunes con su menor exponente, dada la descomposicion en factores primos

def descompuesto_en_primos(num):
    """Esta función descompone un número en una lista de factores primos."""
    lista_de_factores = []
    
    k = 2
    while num >= 2:
        if num % k == 0:
            lista_de_factores.append(k)
            num /= k
        else:
            k += 1
             
    return lista_de_factores


def div_comun_mayor_2(a, b):
    """esta función toma 2 numeros como argumentos y calcula y retorna el
    divisor comun mayor entre ambos, usando la funcion descompuesto_en_primos()
    previamente definida."""
    # descompongo a y b en sus factores primos
    lista_de_factores_a = descompuesto_en_primos(a)
    lista_de_factores_b = descompuesto_en_primos(b)
    
    # tengo que buscar los factores comunes y agarrar de cada uno en común el de menor exponente
    # recorro ambas listas de factores (uso while pq pueden tener != len)
    
    indice_a = 0
    indice_b = 0
    
    factores_comunes = []
    
    while indice_a < len(lista_de_factores_a) and indice_b < len(lista_de_factores_b):
        if lista_de_factores_a[indice_a] == lista_de_factores_b[indice_b]:
            factores_comunes.append(lista_de_factores_a[indice_a])
            indice_a += 1
            indice_b += 1
        elif lista_de_factores_a[indice_a] < lista_de_factores_b[indice_b]:
            indice_a += 1
        
        elif lista_de_factores_a[indice_a] > lista_de_factores_b[indice_b]:
            indice_b += 1 

    dcm = 1
    for i in factores_comunes:
        dcm *= i
        
    return dcm
        

#print(div_comun_mayor(,))
        
# HACER MAS EFICIENTE SIN LOOPS --> incorporar variable set (OOP)
        
#%%

# EJ 175
# pasar de notacion decimal a notacion binaria

# función

def convert_to_binary(num):
    """Esta función (recursiva) convierte un decimal no-negativo en binario."""
    # primero siento los casos base donde num es 0 o 1
    
    if num < 2:
        binary_num = str(num)
       
    # funcion recursiva
    else:
        binary_num = convert_to_binary(num // 2) + str(num % 2)
                                    
    return binary_num

# programa

numero_usuario = int(input("Ingrese un número no negativo: "))

while numero_usuario < 0:
    print("Error.")
    numero_usuario = int(input("Ingrese un número no negativo: "))
    
else:
    print(convert_to_binary(numero_usuario))
    

#%%

# EJ 177
# Roman numerals
# constructed from the letters M, D, C, L, X, V and I which
# represent 1000, 500, 100, 50, 10, 5 and 1 respectively.
        
        
def convert_from_roman(rom):
    """Esta función toma un número romano (str) como argumento y lo 
    transforma a número decimal."""
    rom = rom.upper()
    valores = []
    
    # datos
    roman_numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1  
        }    
    
    # establezco el caso base donde mi string rom es vacío
    if rom == "":
        num = 0
    
    else:
        for k in rom:
            valores.append(roman_numerals[k])
          

        for i in valores[0:-1]:
            indice_i = valores.index(i)
            if i < valores[indice_i+1]:               
                valores[indice_i] = -i
      
        num = sum(valores)          
                
    return num
                
        
num_usuario = input("Escribí un número romano: ")
print(convert_from_roman(num_usuario))        

        
        
        
        
        
        
        
        