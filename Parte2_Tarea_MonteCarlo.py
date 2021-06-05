# -*- coding: utf-8 -*-
"""
Jesús Andrey Salazar Araya, Angello Crawford Clark
"""

#Librerias utilizadas
import numpy as np
import matplotlib.pyplot as plt

####################################   

np.random.seed(4000)

def Espines_aleatorios(numEspines):
    """
    Función que se encarga de crear los espines con orientaciones aleatorias
    """
    #Función que genera números aleatorios enteros entre -1 y 1 
    espines=np.random.randint(-1,1,size=numEspines)
    #El ciclo for se usa para cambiar los valores que asignaron como 0 con una probabilidad de 50%
    for i in range(numEspines):
        if espines[i]==0:
            if np.random.random()>0.5:
                espines[i]=1
            else:
                espines[i]=-1
    return espines
#####################################

def Energia_Ising(arreglo_de_espines, valorJ):
    """
    Función que se encarga de calcular la energia de Ising dado un arreglo de espines y un valor J.
    """
    Energia=0
    for i in range (len(arreglo_de_espines)-1):
        Energia+=arreglo_de_espines[i]*arreglo_de_espines[i+1]
    return -valorJ*Energia

#########################################
def Magnetizacion(arreglo_de_espines):
    """
    Función que se encarga de calcular la magnetizacion de Ising dado un arreglo de espines.
    """
    magnetizacion=0
    for i in arreglo_de_espines:
        magnetizacion+=i
    return magnetizacion


########################################
#Parametros establecidos

kB=1
T=1
nEspines=100
nPasos=4000
valorJ=1

"""
En los siguientes arreglos se determina
la configuracion del arreglo de espines
"""

#Espines con orientacion hacia arriba
Espines_array=np.ones([nEspines],np.int)

#Espines con orientacion hacia abajo
#Espines_array=np.ones([nEspines],np.int)*-1

#Espines con orientaciones aleatorias
#Espines_array=Espines_aleatorios(nEspines)



#Lista que contiene la orientacion de los espines
listaGrafico=[]
listaGrafico.append(np.array(Espines_array))

#Arreglo que almacena la energia de Ising para cada paso cuando el sistema esta en equilibrio
energias_por_paso = []
#Arreglo que almacena la magnetizacion de Ising para cada paso cuando el sistema esta en equilibrio
magnetizacion_por_paso = []


"""
El siguiente ciclo se encarga de calcular 
el delta de energia y en base a este, 
aceptar o rechazar que el espin cambie de direccion
"""
for k in range(nPasos):
    #Energia del estado inicial
    Energia_Estado_I=Energia_Ising(Espines_array,valorJ)
    #Se selecciona el espin que se va a cambiar aleatoriamente
    Espin_seleccionado_random=np.random.randint(nEspines)
    #Se invierte la direccion del espin que fue seleccionado
    Espines_array[Espin_seleccionado_random]*=-1
    #Energia del estado siguiente con el espin cambiado
    Energia_Estado_J=Energia_Ising(Espines_array,valorJ)
    #Cambio de energia del estado inicial al estado siguiente
    deltaE=Energia_Estado_J-Energia_Estado_I
    #Para aceptar o rechazar el cambio se establece la siguiente probabilidad de aceptacion
    valorP=np.exp(-deltaE/(kB*T))
    #Si el cambio de energia es mayor a 0
    #se debe probar si se acepta o se rechaza el cambio
    if deltaE>0:
        #Si la probabilidad es menor a el valor P, se acepta el cambio
        if np.random.random()<valorP:
            pass
        #De lo contrario se rechaza
        else:
            Espines_array[Espin_seleccionado_random]*=-1
    else:
        pass
    #Se agrega el arreglo de espines actualizado al arreglo que luego lo grafica
    listaGrafico.append(np.array(Espines_array))
    
    #A partir de los 2000 pasos, se considera que el sistema se encuentra en equilibrio
    if k >= 2000:
        #Se agrega la energia del arreglo de espines a un arreglo que contiene las energias acumuladas por paso
        energias_por_paso.append(Energia_Ising(Espines_array,valorJ))
        #Se agrega la magnetizacion del arreglo de espines a un arreglo que contiene las magnetizaciones acumuladas por paso
        magnetizacion_por_paso.append(Magnetizacion(Espines_array))

sumatoria_energias = 0
sumatoria_magnetizacion = 0
#Teniendo las energias acumuladas, se procede a calcular la energia interna
#que es el promedio de las energias de configuracion
for i in energias_por_paso:
    sumatoria_energias += i
energia_interna = sumatoria_energias/len(energias_por_paso)
#Teniendo las magnetizaciones acumuladas, se procede a calcular la magnetizacion promedio
for j in magnetizacion_por_paso:
    sumatoria_magnetizacion += j
magnetizacion_promedio = sumatoria_magnetizacion/len(magnetizacion_por_paso)
    
#Convierte la lista de los valores de espines a un arreglo para poderse graficar
arregloGrafico=np.asarray(listaGrafico)
            

#Parte B
print('Magnetizacion en equilibrio al hacer 1 iteración:', magnetizacion_promedio)
print('Energia interna al hacer 1 iteración:', energia_interna)



#Procedimiento para realizar el gráfico
fig,ax=plt.subplots(figsize=(10,10),dpi=120)
ax.imshow(arregloGrafico.T,"plasma")
ax.set_title("Simulación del modelo de Ising I-D")
ax.set_xlabel("Pasos")
ax.set_ylabel("Espines")
ax.set_aspect("5")
plt.show()

######################################################################################
#Parte C
"""
Con el fin de reducir las fluctuaciones, se procede a realizar la simulación anterior
un numero arbitrario de veces para luego promediar entre simulaciones los valores
de energia y magnetizacion.
"""
energia_distintas_replicas = 0
magnetizacion_distintas_replicas = 0

#Cantidad de replicas de la simulacion
M = 5
for replica in range(0,M):
    
    #Parametros establecidos
    kB=1
    T=1
    nEspines=100
    nPasos=4000
    valorJ=1
    
    
    #Espines con orientacion hacia arriba
    Espines_array=np.ones([nEspines],np.int)
    
    #Espines con orientacion hacia abajo
    #Espines_array=np.ones([nEspines],np.int)*-1
    
    #Espines con orientaciones aleatorias
    #Espines_array=Espines_aleatorios(nEspines)
    
    #Arreglo que almacena la energia de Ising para cada paso cuando el sistema esta en equilibrio
    energias_por_paso = []
    #Arreglo que almacena la magnetizacion de Ising para cada paso cuando el sistema esta en equilibrio
    magnetizacion_por_paso = []
    
    """
    El siguiente ciclo se encarga de calcular 
    el delta de energia y en base a este, 
    aceptar o rechazar que el espin cambie de direccion
    """
    
    for k in range(nPasos):
        #Energia del estado inicial
        Energia_Estado_I=Energia_Ising(Espines_array,valorJ)
        
        #Se selecciona el espin que se va a cambiar aleatoriamente
        Espin_seleccionado_random=np.random.randint(nEspines)
        #Se invierte la direccion del espin que fue seleccionado
        Espines_array[Espin_seleccionado_random]*=-1
        #Energia del estado siguiente con el espin cambiado
        Energia_Estado_J=Energia_Ising(Espines_array,valorJ)
        #Cambio de energia del estado inicial al estado siguiente
        deltaE=Energia_Estado_J-Energia_Estado_I
        #Para aceptar o rechazar el cambio se establece la siguiente probabilidad de aceptacion
        valorP=np.exp(-deltaE/(kB*T))
        #Si el cambio de energia es mayor a 0
        #se debe probar si se acepta o se rechaza el cambio
        if deltaE>0:
            #Si la probabilidad es menor a el valor P, se acepta el cambio
            if np.random.random()<valorP:
                pass 
            #De lo contrario se rechaza
            else:
                Espines_array[Espin_seleccionado_random]*=-1 #Se rechaza el cambio
        else:
            pass

       
        
        #A partir de los 2000 pasos, se considera que el sistema se encuentra en equilibrio
        if k >= 2000:
            #Se agrega la energia del arreglo de espines a un arreglo que contiene las energias acumuladas por paso
            energias_por_paso.append(Energia_Ising(Espines_array,valorJ))
            #Se agrega la magnetizacion del arreglo de espines a un arreglo que contiene las magnetizaciones acumuladas por paso
            magnetizacion_por_paso.append(Magnetizacion(Espines_array))
    
   
    
    sumatoria_energias = 0
    sumatoria_magnetizacion = 0
    #Teniendo las energias acumuladas, se procede a calcular la energia interna
    #que es el promedio de las energias de configuracion
    for i in energias_por_paso:
        sumatoria_energias += i
    energia_interna = sumatoria_energias/len(energias_por_paso)
    #Teniendo las magnetizaciones acumuladas, se procede a calcular la magnetizacion promedio
    for j in magnetizacion_por_paso:
        sumatoria_magnetizacion += j
    magnetizacion_promedio = sumatoria_magnetizacion/len(magnetizacion_por_paso)
    
    
    #Se toma la energia interna en equilibrio
    energia_distintas_replicas += energia_interna
    #Se toma la magnetizacion promedio del sistema en equilibrio
    magnetizacion_distintas_replicas += magnetizacion_promedio
    
    
    
"""
Se procede a promediar la energia de Ising, la magnetizacion y la energia interna.
"""
promedio_energia = energia_distintas_replicas/M
promedio_magnetizacion = magnetizacion_distintas_replicas/M


print("El promedio de magnetizacion simulando con", M, "repeticiones es de: ", promedio_magnetizacion)
print("El promedio de las energías internas despues de: ",M,"repeticiones es de: ",promedio_energia)  

"""
Se procede a graficar la energia interna y la magnetizacion para distintos valores de Kb*Temperatura.
"""
Graf_kBT = []
Graf_U = []
Graf_M = []
Graf_U_teorico = []
Graf_M_teorico = []

#El valor de constante de KBoltzmann*Temperatura debe ser cercano a 0 pero no ser igual a 0 dado
#que se indefiniria la funcion que calcula la probabilidad de aceptacion
kB_T = 0.1
nEspines=100
nPasos=4000
valorJ=1



while kB_T <= 5: 
    
    #Determinación del arreglo:
    #Arreglo de espines hacia arriba
    Espines_array=np.ones([nEspines],np.int)
    
    #Arreglo de espines hacia abajo
    #Espines_array=np.ones([nEspines],np.int)*-1
    
    #Arreglo de espines aleatorios
    #Espines_array=Espines_aleatorios(nEspines)
    
   
    #Arreglo que almacena la energia de Ising para cada paso cuando el sistema esta en equilibrio
    energias_por_paso = []
    #Arreglo que almacena la magnetizacion de Ising para cada paso cuando el sistema esta en equilibrio
    magnetizacion_por_paso = []
    
    
    for k in range(nPasos):
        #Energia del estado inicial
        Energia_Estado_I=Energia_Ising(Espines_array,valorJ)
        
        #Se selecciona el espin que se va a cambiar aleatoriamente
        Espin_seleccionado_random=np.random.randint(nEspines)
        #Se invierte la direccion del espin que fue seleccionado
        Espines_array[Espin_seleccionado_random]*=-1
        #Energia del estado siguiente con el espin cambiado
        Energia_Estado_J=Energia_Ising(Espines_array,valorJ)
        #Cambio de energia del estado inicial al estado siguiente
        deltaE=Energia_Estado_J-Energia_Estado_I
        #Para aceptar o rechazar el cambio se establece la siguiente probabilidad de aceptacion
        valorP=np.exp(-deltaE/(kB_T))
        #Si el cambio de energia es mayor a 0
        #se debe probar si se acepta o se rechaza el cambio
        if deltaE>0:
            #Si la probabilidad es menor a el valor P, se acepta el cambio
            if np.random.random()<valorP:
                pass 
            #De lo contrario se rechaza
            else:
                Espines_array[Espin_seleccionado_random]*=-1 #Se rechaza el cambio
        else:
            pass

        #Se agrega el arreglo de espines actualizado al arreglo que luego lo grafica
        listaGrafico.append(np.array(Espines_array))
        #A partir de los 2000 pasos, se considera que el sistema se encuentra en equilibrio
        if k >= 2000:
            #Se agrega la energia del arreglo de espines a un arreglo que contiene las energias acumuladas por paso
            energias_por_paso.append(Energia_Ising(Espines_array,valorJ))
            #Se agrega la magnetizacion del arreglo de espines a un arreglo que contiene las magnetizaciones acumuladas por paso
            magnetizacion_por_paso.append(Magnetizacion(Espines_array))

    sumatoria_energias = 0
    sumatoria_magnetizacion = 0
    #Teniendo las energias acumuladas, se procede a calcular la energia interna
    #que es el promedio de las energias de configuracion
    for i in energias_por_paso:
        sumatoria_energias += i
    energia_interna = sumatoria_energias/len(energias_por_paso)    
    #Teniendo las magnetizaciones acumuladas, se procede a calcular la magnetizacion promedio
    for j in magnetizacion_por_paso:
        sumatoria_magnetizacion += j
    magnetizacion_promedio = sumatoria_magnetizacion/len(magnetizacion_por_paso)
         
    
        
    #Lista que almacena los distintos valores de la constante de Boltzamnn*Temperatura
    Graf_kBT.append(kB_T)
    #Lista que almacena los distintos valores de energia interna
    Graf_U.append(energia_interna)
    #Lista que almacena los distintos valores de magnetizacion
    Graf_M.append(magnetizacion_promedio)
    
    #Valores teoricos de energia y magnetizacion
    U_teorico = -nEspines*np.tanh(valorJ/kB_T)
   
    Graf_U_teorico.append(U_teorico)
    
    #Se aumenta el valor de la kb*temperatura poco a poco
    
    kB_T += 0.1
        
#Parte E
#Grafico U vs kbT
fig,ax=plt.subplots(dpi = 120)
ax.plot(Graf_kBT,Graf_U,'b')
ax.plot(Graf_kBT,Graf_U_teorico,'r')
plt.legend(["Numerica","Analitica"])
ax.set_title("U vs kbT")
ax.set_xlabel("kbT")
ax.set_ylabel("Energia Interna (U)")
plt.show()

#Parte F
#Grafico M vs kbT
fig,ax=plt.subplots(dpi = 120)
ax.plot(Graf_kBT,Graf_M,'b')
plt.legend(["Numerica"])
ax.set_title("M vs kbT")
ax.set_xlabel("kbT")
ax.set_ylabel("Magnetizacion (M)")
plt.show()


################################################################################
#Parte G

Graf_kBT = []
Graf_C = []
Graf_C_teorico = []

nEspines=100
nPasos=4000
valorJ=1
kB_T = 0.1

while kB_T <= 5:

    energia_distintas_replicas = 0
    energia_U_2 = 0
    #Cantidad de replicas de la simulacion
    M = 3
    for replica in range(0,M):
        
        #Espines con orientacion hacia arriba
        Espines_array=np.ones([nEspines],np.int)
        
        #Espines con orientacion hacia abajo
        #Espines_array=np.ones([nEspines],np.int)*-1
        
        #Espines con orientaciones aleatorias
        #Espines_array=Espines_aleatorios(nEspines)
        
        
        #Arreglo que almacena la energia de Ising para cada paso cuando el sistema esta en equilibrio
        energias_por_paso = []
        U_2_por_paso = []
        
        """
        El siguiente ciclo se encarga de calcular 
        el delta de energia y en base a este, 
        aceptar o rechazar que el espin cambie de direccion
        """
        
        for k in range(nPasos):
            #Energia del estado inicial
            Energia_Estado_I=Energia_Ising(Espines_array,valorJ)
            
            #Se selecciona el espin que se va a cambiar aleatoriamente
            Espin_seleccionado_random=np.random.randint(nEspines)
            #Se invierte la direccion del espin que fue seleccionado
            Espines_array[Espin_seleccionado_random]*=-1
            #Energia del estado siguiente con el espin cambiado
            Energia_Estado_J=Energia_Ising(Espines_array,valorJ)
            #Cambio de energia del estado inicial al estado siguiente
            deltaE=Energia_Estado_J-Energia_Estado_I
            #Para aceptar o rechazar el cambio se establece la siguiente probabilidad de aceptacion
            valorP=np.exp(-deltaE/(kB_T))
            #Si el cambio de energia es mayor a 0
            #se debe probar si se acepta o se rechaza el cambio
            if deltaE>0:
                #Si la probabilidad es menor a el valor P, se acepta el cambio
                if np.random.random()<valorP:
                    pass 
                #De lo contrario se rechaza
                else:
                    Espines_array[Espin_seleccionado_random]*=-1 #Se rechaza el cambio
            else:
                pass
            
            
            
            #A partir de los 2000 pasos, se considera que el sistema se encuentra en equilibrio
            if k >= 2000:
                #Se agrega la energia del arreglo de espines a un arreglo que contiene las energias acumuladas por paso
                energias_por_paso.append(Energia_Ising(Espines_array,valorJ))
                U_2_por_paso.append(Energia_Ising(Espines_array,valorJ))
            
        sumatoria_energias = 0
        sumatoria_energias_cuadrado = 0
        
        #Teniendo las energias acumuladas, se procede a calcular la energia interna
        #que es el promedio de las energias de configuracion
        for i in energias_por_paso:
            sumatoria_energias += i
        energia_interna = sumatoria_energias/len(energias_por_paso)
        #Paso para calcular las fluctuaciones de las energias
        for j in U_2_por_paso:
            sumatoria_energias_cuadrado += j**2
        U_2_sin_promediar = sumatoria_energias_cuadrado/len(U_2_por_paso)
       
        
        energia_distintas_replicas += energia_interna
        energia_U_2 += U_2_sin_promediar
      
    #Energia Interna U
    promedio_energia_interna = energia_distintas_replicas/M
   
    #Fluctuaciones de la energia
    U_2 = energia_U_2/M
    
    
    #Calor Especifico
    Calor_especifico = (nEspines)*(1/nEspines**2)*(U_2-promedio_energia_interna**2)/(kB_T**2)
    

    
    #Calor Especifico Teorico
    Calor_especifico_teorico = ((valorJ/kB_T)**2)/(np.cosh(valorJ/kB_T))**2
    
    
    #Lista que almacena los distintos valores de la constante de Boltzamnn
    Graf_kBT.append(kB_T)
    #Lista que almacena los distintos valores de calor especifico
    Graf_C.append(Calor_especifico)
    #Lista que almacena los distintos valores de calor especifico teorico
    Graf_C_teorico.append(Calor_especifico_teorico)
    
   
    kB_T += 0.1


#Grafico Calor especifico vs kbT
fig,ax=plt.subplots(dpi = 120)
ax.plot(Graf_kBT,Graf_C,'b')
ax.plot(Graf_kBT,Graf_C_teorico,'r')
plt.legend(["Numerica","Analitica"])
ax.set_title("C vs kbT")
ax.set_xlabel("kbT")
ax.set_ylabel("Calor especifico (C)")
plt.show()