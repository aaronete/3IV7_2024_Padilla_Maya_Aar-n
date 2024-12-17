import math

# Función para calcular el área y perímetro de un polígono regular
def poligono_regular(lados, lado):
    # Cálculo del perímetro
    perimetro = lados * lado
    
    # Cálculo del área usando la fórmula para polígonos regulares
    area = (lados * lado ** 2) / (4 * math.tan(math.pi / lados))
    
    return area, perimetro

# Función para mostrar el menú de opciones
def menu():
    print("\n¡Bienvenido al programa de cálculo de áreas y perímetros de polígonos regulares!")
    print("Elige una opción: ")
    print("A. Cuadrado (4 lados)")
    print("B. Pentágono (5 lados)")
    print("C. Hexágono (6 lados)")
    print("D. Heptágono (7 lados)")
    print("E. Octágono (8 lados)")
    print("F. Decágono (10 lados)")

# Función principal para ejecutar el programa
def main():
    menu()  # Muestra el menú de opciones
    opcion = input("Introduce la opción deseada (A, B, C, D, E, F): ").upper()

    if opcion == "A":
        lados = 4
        nombre_figura = "Cuadrado"
    elif opcion == "B":
        lados = 5
        nombre_figura = "Pentágono"
    elif opcion == "C":
        lados = 6
        nombre_figura = "Hexágono"
    elif opcion == "D":
        lados = 7
        nombre_figura = "Heptágono"
    elif opcion == "E":
        lados = 8
        nombre_figura = "Octágono"
    elif opcion == "F":
        lados = 10
        nombre_figura = "Decágono"
    else:
        print("Opción no válida. Por favor elige una opción entre A y F.")
        return
    
    # Solicitar el valor del lado de la figura
    lado = float(input(f"Introduce la longitud del lado del {nombre_figura}: "))
    
    # Calcular área y perímetro
    area, perimetro = poligono_regular(lados, lado)
    
    # Mostrar los resultados
    print(f"\nResultados para el {nombre_figura}:")
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
