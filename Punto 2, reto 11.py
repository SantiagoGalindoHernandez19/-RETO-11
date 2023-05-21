

def CalcularMatrices(A, B): # Definimos las variables a utilizar 
    if len(A) != len(B):  # Decimos que si la longitud de la fila de la matriz A es diferente a la del B, debe registrar 2 iguales
        print("Las dos matrices deben tener la misma cantidad de filas") # Se mostrara este mensaje

    if len(A[0]) != len(B[0]):   # Cantidad de columnas en cualquier posicion es diferente debera registrar que tengas la misma cantidad
        print("Las dos matrices deben tener la misma cantidad de filas") # Se mostrara este mensaje


    SumaMatriz = [] # Creamos variable vacia 
    Fila = [] # Creamos una fila por cada iteracion
    for i in range(len(A)): # Realizamos la iteracion por cualquiera de las dos matrices 
        for j in range(len(A[0])):
            Fila.append(A[i][j]*B[i][j]) # Agregamos nuestra fila anteriormente creada 

        SumaMatriz.append(Fila)
    return SumaMatriz

A = [[1, 2 , 3], [4, 5, 6]]   
B = [[2, 3 , 5], [11, 7, 5]] # 

Resultado = CalcularMatrices(A,B)
print(Resultado)