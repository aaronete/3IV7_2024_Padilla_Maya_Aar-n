import math

#se creara funcion para alcular area y perimetro

def rectangulo(base, altura):
    area = base * altura
    perimetro = 2*(base+altura)
    return area, perimetro


def triangulo(base, altura):
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro

def esfera(radio):
    volumen = (4/3)*math.pi*radio**3

    return volumen
def menu():
    print("hola bienvenido a python con funciones")
    print("elije una opcion:")
    print("A. Area y perimetro de rectangulo")
    print("B. Area y perimetro de triangulo")
    print("C. volumen de esfera")

#programa
menu()
opcion = input("introduce la opcion a desear: ").upper()


if opcion == "A":
    base=float(input("introduce base"))
    altura= float(input("introduce altura"))
    area, perimetro = rectangulo(base, altura)
    print("el area es de: ",area)
    print("el perimetro es de: ",perimetro) 

elif opcion == "B":
    base=float(input("introduce base"))
    altura= float(input("introduce altura"))
    lado1= float(input("introduce lado1"))
    lado2= float(input("introduce lado2"))
    lado3= float(input("introduce lado3"))
    area, perimetro = triangulo(base, altura, lado1, lado2, lado3)
    print("el area es de: ",area)
    print("el perimetro es de: ",perimetro)


if opcion == "C":
    radio=float(input("introduce el radio"))
    volumen= esfera(radio)
    print("el volumen es de: ",volumen)