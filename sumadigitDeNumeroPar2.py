# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 08:25:57 2021

@author: Guillermo Hondermann
"""

def sumaPar(numEntero):
    sumDigit, ultimoDigito = 0, 0
    validacion=False

    while numEntero != 0:
        ultimoDigito = numEntero % 10
        numEntero =numEntero// 10
        sumDigit = sumDigit+ultimoDigito
    print("La suma de los digitos es: {}".format(sumDigit))
    if(sumDigit % 2==0):
        validacion=True
    else: validacion= False
    return validacion


elementosLista=int(input('Ingrese numeros de elementos de la lista  [>4]: '))
while not elementosLista>4:
    elementosLista=int(input('vuelva a ingresar el tamaño  de la lista  [>4]: '))




lista=[]
for i in range(elementosLista):
    nEntero = int(input("ingrese el numero entero [4-6] digitos"+str(i+1)))
    while not 1000 <= nEntero <= 999999:
        nEntero = int(input("ingrese el numero entero [4-6] digitos" +str(i+1)))
    SumadigitosEsPar = sumaPar(nEntero)
    if SumadigitosEsPar:
        lista.append(nEntero)


print(lista)