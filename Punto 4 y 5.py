def MostrarMatriz(matriz):
    for fila in matriz:
        print(fila)
matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]     # Matriz a utilizar 
]

MostrarMatriz(matriz)

filas= len(matriz)  # Calcular cantidad de filas y columnas 
columnas= len(matriz[0])

print(filas,columnas)

for i in range(filas):
    suma = sum(matriz[i]) # Suma de la variable actual como primera iteracion 
    matriz[i].append(suma) # Fila actual agregandole el nuevo elemento en la matriz

print()

MostrarMatriz(matriz)

NuevaFila = []

for j in range(columnas):  # Sumatoria por columnas
    suma = sum([fila[i] for fila in matriz])             # Iterar por cada fila tomando la j columna
    NuevaFila.append(suma)

print(NuevaFila)
