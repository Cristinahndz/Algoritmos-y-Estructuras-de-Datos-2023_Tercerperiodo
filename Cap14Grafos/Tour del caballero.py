import time #
import numpy as np #trabajar con matrices
import matplotlib.pyplot as plt #visualiza los datos

tamaño =8
numsol =0 #soluciones encontradas
tablero = np.zeros((tamaño,tamaño), dtype=np.int32) #matriz de ceros y registrar mov del caballo
tiempo=time.time()

def buscarCaballo (cual): #encontrar posic de un #
    for fila in range(tamaño): #itera sobre cada fila
        for col in range(tamaño): #columna
            if tablero[fila, col] == cual: return fila,col #verif si el elem igual al #buscado, devuelve en forma de tupla

def pintarTableroGraf (): 
    for x in range(tamaño+1): #itera desde 0 hasta tamaño
        plt.plot ([0,tamaño],[x,x], color="gray") #dibuja linea horizontal desde 0 hasta tamaño
        plt.plot ([x,x],[0,tamaño], color="gray")#dibuja linea vertical
    X=[]
    Y=[]#almac coordenadas de los punts
    for x in range(1, tamaño*tamaño + 1):#numer que el caballo visitara
        fila,col = buscarCaballo(x)#obtiene coord del num actual
        X.append([col + 0.5])#para centrar pts en las celdas
        Y.append([tamaño - fila - 0.5])
        plt.text(col+0.5, tamaño - fila - 0.5, str(x))
    plt.plot(X,Y)#representan el recorrido del caballo
    plt.suptitle("El tour del caballero",fontsize=16)
    plt.show()#muestra graf final

def Resolver (row, col, counter):
    global tamaño
    global numsol
    for i in [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]: #representan los posib movimientos en las coorde x,y
        new_x = row + i[0]#calcula nuevas coordenadas despues de realizar un mov
        new_y = col + i[1]
        if new_x < tamaño and new_x >= 0 and new_y < tamaño and new_y >= 0 and tablero[new_x,new_y] == 0:#verif si las new coord estan dentro del tablero y si la celda esta vacia 
            tablero[new_x,new_y] = counter #marca new posc del cabllo con el num actual del recorrid
            if counter >= tamaño * tamaño: #verif si el recorrido esta completo
                numsol += 1
                print("··································································")
                print("#", numsol, ", tiempo:", time.time() - tiempo)
                print(tablero)
                pintarTableroGraf()
            else:
                Resolver (new_x, new_y, counter + 1)#llama otra vez a la funcion
            tablero[new_x, new_y] = 0 #permite explo otras posibles sol

tablero[3, 2] = 1
Resolver(3, 2, 2)