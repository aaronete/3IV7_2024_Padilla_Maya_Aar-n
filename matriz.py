
def ingresar_matriz(filas, columnas):
    matriz = []
    print(f"Introduce los valores de la matriz de tamaño {filas}x{columnas}:")
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento en la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz


def imprimir_matriz(matriz):
    for fila in matriz:
        print("\t".join(map(str, fila)))


def transponer_matriz(matriz):

    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]


def main():
    print("Seleccione el tamaño de la matriz:")
    print("1. Matriz 3x3")
    print("2. Matriz 5x5")
    opcion = int(input("Ingresa 1 o 2: "))
    
    if opcion == 1:
        filas = 3
        columnas = 3
    elif opcion == 2:
        filas = 5
        columnas = 5
    else:
        print("Opción no válida. Saliendo.")
        return
    
   
    matriz_original = ingresar_matriz(filas, columnas)
    
    
    print("\nMatriz Original:")
    imprimir_matriz(matriz_original)
    

    matriz_transpuesta = transponer_matriz(matriz_original)
    print("\nMatriz Transpuesta:")
    imprimir_matriz(matriz_transpuesta)


main()
