# -*- coding: utf-8 -*-
"""
Jesús Andrey Salazar Araya, Angello Crawford Clark
"""

import numpy as np
import matplotlib.pyplot as plt


#Punto A

def CaminoAleatorio(lista_Pos, nIter,l):
    """
    Genera un par ordenado aleatorio respecto al punto anterior
    """
    
    #Se toma un valor aleatorio entre -1 y 1 para x, y, z
    xPos = (np.random.random()-0.5)*2
    yPos = (np.random.random()-0.5)*2
    zPos = (np.random.random()-0.5)*2
    #L va a ser la distancia para normalizar
    L=np.sqrt((xPos)**2+(yPos)**2+(zPos)**2)
    #Se determina la longitud del cambio en el eje x,y,z
    DeltaX=(1/L)*xPos*l
    DeltaY=(1/L)*yPos*l
    DeltaZ=(1/L)*zPos*l
    

    #Las nuevas posiciones seran las posiciones anteriores 
    #sumado con el cambio de posicion por eje
    nuevaxPos = lista_Pos[0][nIter-1] + DeltaX
    nuevayPos = lista_Pos[1][nIter-1] + DeltaY
    nuevazPos = lista_Pos[2][nIter-1] + DeltaZ

    lista_Pos[0].append(nuevaxPos)
    lista_Pos[1].append(nuevayPos)
    lista_Pos[2].append(nuevazPos)
    

    return lista_Pos, l


#Punto B

#Parametros del problema
#R = 5*(10)**8
R = 5*(10)**(-2)
l=5*(10**(-5))

N = round((R/l)**2) #Estimacion original de cantidad de pasos necesarios para alcanzar R

#Punto C

def Estimacion_pasos(k,R,c,l):
    """
    Esta funcion es la encargada de obtener el camino aleatorio del foton
    asi como determinar la totalidad de pasos que da el foton,
    el tiempo que tarda en alcanzar el radio R,
    el promedio de pasos para un numero arbitrario de simulaciones
    """
    #Contadores de totalidad de pasos y tiempo total
    Total_pasos = 0
    Tiempo_total = 0
   
    #Ciclo for que se usa para hacer la simulacion un numero arbitrario de veces
    for j in range(0,k):
        Distancia_total = 0
        # Inicialización del camino
        camino = [[0.], [0.], [0.]] #Camino del fotón en 3D
        nPasos = 1
        i = 1
        #Ciclo while que verifica si se ha alcanzado la distancia R
        while i != 0:
            camino, Distancia = CaminoAleatorio(camino, nPasos,l)
            Distancia_total += Distancia
            #Condicional que especifica si alguno de los valores en x, y o z sobrepasa la distancia R se detiene el ciclo
            if np.abs(camino[0][nPasos]) < R and np.abs(camino[1][nPasos]) < R and np.abs(camino[2][nPasos]) < R:
                i += 1
                nPasos += 1
                
            else:
                i = 0
        Total_pasos += nPasos #Totalidad de pasos en k simulaciones
        Tiempo_total += Distancia_total/c #Totalidad de tiempo en segundos en k simulaciones
    Pasos_promedio = Total_pasos/k #Pasos promedio que recorre el foton
    
    return camino, Total_pasos, Tiempo_total, Pasos_promedio



def principal(R,l,N):
    """
    Funcion principal que se encarga de llamar a las otras funciones
    y de graficar la trayectoria del foton para la ultima simulacion.
    
    """
    
    #Número de veces que se itera un camino que es lo mismo que numero de trials (k)
    k = 5
    #Velocidad de la luz
    c=3*(10**8)
   
    #Se llama a la funcion que realiza los trials
    camino, Total_pasos,Tiempo_total,Pasos_promedio = Estimacion_pasos(k,R,c,l)
    Tiempo_promedio_años = (Tiempo_total/k)*(1/60)*(1/60)*(1/24)*(1/365.25)
    
    
    print("La cantidad de pasos que deberían darse teóricamente es: ", N)    
    print("El promedio de pasos es ", Pasos_promedio, "con ",k, " réplicas")
    print("El foton va a durar: ",Tiempo_promedio_años," años")
    
    
    #Se procede a graficar en 3D el camino aleatorio de un foton
    fig,ax=plt.subplots(dpi = 120)
    ax = plt.axes(projection="3d")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.plot(camino[0], camino[1], camino[2])
    ax.set_title("Trayectoria aleatoria del foton")
    plt.show()
    
#Se llama a la funcion principal para que se ejecute el codigo
principal(R,l,N)
