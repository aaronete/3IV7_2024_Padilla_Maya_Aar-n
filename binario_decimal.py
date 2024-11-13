# Función para convertir de binario a decimal
def binario_a_decimal(binario):
    # El binario se convierte a decimal utilizando la función int() con base 2
    try:
        decimal = int(binario, 2)
        return decimal
    except ValueError:
        return "Error: El valor ingresado no es un número binario válido."

# Función para convertir de decimal a binario
def decimal_a_binario(decimal):
    try:
        # El decimal se convierte a binario utilizando bin()
        if decimal < 0:
            return "Error: El valor decimal debe ser positivo."
        binario = bin(decimal)[2:]  # Eliminamos el prefijo '0b'
        return binario
    except ValueError:
        return "Error: Ingrese un número decimal válido."

# Función principal para interactuar con el usuario
def menu():
    print("Selecciona una opción:")
    print("1. Convertir de binario a decimal")
    print("2. Convertir de decimal a binario")
    print("3. Salir")
    
    opcion = input("Ingresa el número de la opción: ")
    
    if opcion == "1":
        binario = input("Ingresa el número binario: ")
        resultado = binario_a_decimal(binario)
        print(f"El número decimal es: {resultado}")
    
    elif opcion == "2":
        decimal = int(input("Ingresa el número decimal: "))
        resultado = decimal_a_binario(decimal)
        print(f"El número binario es: {resultado}")
    
    elif opcion == "3":
        print("Saliendo del programa.")
        exit()
    
    else:
        print("Opción no válida. Por favor selecciona 1, 2 o 3.")

# Llamamos al menú para ejecutar el programa
while True:
    menu()
