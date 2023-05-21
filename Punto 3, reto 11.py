
matriz= [[1,2,3],[4,5,6]]
def Transponer(M): # Definimos función y sus variables

    t = [] # Lista vacia 
    for i in range(len(M[0])): # Recorrer la longitud de la primera lista
        t.append([])
        for j in range (len(M)): 
            t[i].append(M[j][i])          # Cambiar orde de posicion 
    return t 
traspuesta= Transponer(matriz)




for linea in matriz:
    for elemento in linea:
        print(elemento,end=" ")
    print()

for linea in traspuesta:
    for elemento in linea: 
        print(elemento,end="")
    print()
