# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:16:31 2019
@author: Ctoro
"""
#!/usr/bin/env python3
import os
os.system('cls')
print("Bienvendos al programa de CRISTIAN TORO GARCÍA   ")
print("=================================================")
print("=========================================================")
print("El programa imprime números en estilo de una pantalla LCD")
print("El programa te guarda los datos, mientras deseas imprimir")
print("se imprimen ingrensando 0,0 .                            ")
print("El programa controla que los datos ingresados sean del   ")
print("formato correcto.                                        ")
print("Por favor ingresa primero el Tamaño y luego el  numero   ")
print("deben de estar separados por una coma ','                ")
print("=========================================================")
continuar = True
while (continuar == True):    
    A_Sizes = [] #Lista de Tamaños
    A_Numeros = [] #Lista de numeros
    #Funcion que Permite agregar datos y verifica su formato
    def add():
        flag = "ctrl"
        datos = str(input("Ingresa valores, si desas imprimir escribe 0,0 \n"))
        while (flag == "ctrl" ):
            if ("," in datos) :
                split = datos.split(",")
                lon_split = (len(split))
                if(lon_split == 2):
                    flag = " "
                else:
                    datos = str(input("Datos erroneos! Ingresa los datos correctamente, deben de estar separados por una coma','\n"))
                    flag = "ctrl"  
            else : 
                    datos = str(input("Datos erroneos! Ingresa los datos correctamente, deben de estar separados por una coma','\n"))
                    flag = "ctrl"
        return datos        
    #Funcion que revisa que los datos ingresados sean enteros
    def comprobar(split):
        flag = "ctrl"#bandera para controlar ciclo 
        while (flag == "ctrl"):
                try:
                    valor = int(split)
                    return valor 
                except ValueError:
                    if (split == 0):
                        return 0
                    else:
                        return flag
    
    # Funcion para imprimir los datos en forma digiital.
                        
    def imprimir(size,n):
        x = ((size*2)+3)
        y = (size+2)
        a=""
        
        if (n==0):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += ' '
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas Superior
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquina Inferior
                        a += ' '
                    elif ((i==0 and j!=0) or(i==(x-1) and j!=0)  ):#superior-Inferior
                        a += '-'
                    elif ((j==(y-1) and i!=int((x/2)-0.5)) or (j==0 and i!=int((x/2)-0.5))):#lateral
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""               
        if (n==1):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += ' '
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas Superior
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquina Inferior
                        a += ' '
                    elif ((i==0 and j!=0) or(i==(x-1) and j!=0)  ):#superior-Inferior
                        a += ' '
                    elif ((j==(y-1) and i!=int((x/2)-0.5))):#lateral
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""          
        if (n==2):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += '-'
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas Superior
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquinas Inferior
                        a += ' '
                    elif ((i==0 and j!=0) or(i==(x-1) and j!=0)  ):#superior-Inferior
                        a += '-'
                    elif ((j==(y-1) and i<int((x/2)-0.5)) or (j==0 and i>int((x/2)-0.5))):#laterales
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""
        if (n==3):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += '-'
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas Superior
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquina Inferior
                        a += ' '
                    elif ((i==0 and j!=0) or(i==(x-1) and j!=0)  ):#superior-Inferior
                        a += '-'
                    elif ((j==(y-1) and i!= int((x/2)-0.5))):#lateral
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""
        if (n==4):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += '-'
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas Suerior
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquinas Inferior
                        a += ' '
                    elif ((i==0 and j!=0) or(i==(x-1) and j!=0)  ):#superior-Inferior
                        a += ' '
                    elif ((j==(y-1) and i<int((x/2)-0.5)) or (j==0 and i<int((x/2)-0.5)) or (j==(y-1) and i>int((x/2)-0.5))):#laterales
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""
        if (n==5):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += '-'
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas Superior
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquinas Inferior
                        a += ' '
                    elif ((i==0 and j!=0) or(i==(x-1) and j!=0)  ):#superior-Inferior
                        a += '-'
                    elif ((j==(y-1) and i>int((x/2)-0.5)) or (j==0 and i<int((x/2)-0.5))):#lateral
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""
        if (n==6):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += '-'
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas superiores
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquinas inferiores
                        a += ' '
                    elif ((i==0 and j!=0) or(i==(x-1) and j!=0)  ):#superior-Inferior
                        a += '-'
                    elif ((j==(y-1) and i>int((x/2)-0.5)) or (j==0 and i != int((x/2)-0.5))):#lateral
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""
        if (n==7):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += ' '
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas superiores
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquinas inferiores
                        a += ' '
                    elif ((i==0 and j!=0)):#superior-Inferior
                        a += '-'
                    elif (j==(y-1) and i!=int((x/2)-0.5)):#lateral
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""
        if (n==8):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += '-'
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas superiores
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquinas inferiores
                        a += ' '
                    elif ((i==0 and j!=0) or(i==(x-1) and j!=0)  ):#superior-Inferior
                        a += '-'
                    elif ((j==(y-1) and i!=int((x/2)-0.5)) or (j==0 and i != int((x/2)-0.5))):#lateral
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""
        if (n==9):
            for i in range (x) : #filas
                for j in range (y) : #columna
                    if ((j == 0 and i==int((x/2)-0.5)) or (j==(y-2) and i==int((x/2)-0.5))):#Espacios medio
                        a += ' '
                    if ( j>=0 and j<(y-2) and i==int((x/2)-0.5)):#RayasMedio
                        a += '-'
                    elif ((j==0 and i==0) or (i==0 and j==(y-1))): #Espacio Esquinas superiores
                         a += ' '
                    elif ((i==(x-1) and j==0) or (i==(x-1) and j==(y-1)) ): #Espacio Esquinas inferiores
                        a += ' '
                    elif ((i==0 and j!=0)):#superior-Inferior
                        a += '-'
                    elif ((j==(y-1) and i!=int((x/2)-0.5)) or (j==0 and i<int((x/2)-0.5))):#lateral
                        a += '|'
                    else:
                        a+= ' '
                print (a)
                a=""   
    #Inicialización
    datos = add()
    while (datos != "0,0"): 
        split = datos.split(",") #Separa los datos ingresados
        size = comprobar(split[0]) #lleva el tamaño a la vaiable size
        numero = comprobar(split[1]) #Lleva el numero a imprimir a la variable numero
        if (size == "ctrl" or numero == "ctrl"): 
            print ("===============================================")
            print ("ATENCIÓN: solo debe de ingresar Numeros enteros")
            print ("===============================================")
            datos = add()
        elif (size == 0 and numero == 0): 
            datos = "0,0"
        elif (size > 10):
            print ("============================================================")
            print ("ATENCIÓN: Tamaño muy grande el Tamaño debe de ser menor a 10")
            print ("============================================================")
            datos = add()
        elif (size < 0 or numero < 0):
            print ("============================================================")
            print ("ATENCIÓN: tienes uno de los dos Numeros negativos")
            print ("============================================================")
            datos = add()
        elif (size == 0 and numero!=0):
            print ("============================================================")
            print ("ATENCIÓN: El tamaño, debe de ser mayor a cero")
            print ("============================================================")
            datos = add()
        else:
            #si se cumple el formato deseado agregaria datos
            A_Sizes.append(size) #Se añade el tamaño a la lista de Tamaños
            A_Numeros.append(split[1]) #Se añade numero a la lista numeros
            print ("!los datos se agregaron correctamente¡\n ")
            datos = add()
    os.system('cls')  #limpia la consola       
    longitud = (len(A_Sizes))
    if (longitud > 0):
        print ("!ESTOS SON SUS DATOS¡")
    elif (longitud==0):
        print (":( No ingresaste datos :(")
      
    #loop para imprimir los datos
    cont = 0
    while (cont < longitud) :
        size = int(A_Sizes[cont])
        num = (A_Numeros[cont])
        print (str(size) + " => Es el Tamaño con el que se imprime el numero " + num +"\n" )       
        if((len(num)) > 1):
            print ("Debido a que el numero "+ num +" tiene " + str(len(num)) + " digitos se van a imprimir en lista ")
            print ("por tiempo no me fue posible investigar como diseñar el código para imprimir en una sola fila :/")
            for n in num:
                n = int(n)
                imprimir(size,n)
        else : 
            n = int (num)
            imprimir(size,n)       
        cont += 1   
    os.system("pause")
    os.system('cls')
    #loop para controlar que continuidad en el programa
    opc = 1
    while opc == 1 :
        opc = str(input("Deseas seguir en el programa? presiona 1 para continuar ó 2 para salir\n"))
        flag = "ctrl"
        while (flag == "ctrl" ):
            try:
                    opc = int(opc)
                    flag = ""
            except ValueError:
                    opc = str(input("Opcion Invalida escribe un numero 1 ó 2\n"))
                    flag = "ctrl"
        if (opc == 1): 
            os.system('cls')
            continuar = True
            opc = 0
        elif(opc == 2): 
            continuar = False
            opc = 0
        else : opc = 1; print("Opcion Invalida escribe 1 ó 2\n");
    
print ("**************************************")
print ("**EL PROGRAMA TERMINÓn VUELVA PRONTO**")
print ("**************************************")
os.system("pause")       