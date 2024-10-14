Algoritmo sin_titulo
	final<-0
	Escribir "ingrese temperatura en fahrenheit"
	leer cantidad
	Escribir "a que desea convertir? 1. celsius | 2. kelvine | 3. rankine"
	leer q
	Segun q Hacer
		1:
			final<-(cantidad - 32) * 5/9 
			escribir "la conversion de fahrenheit a celsius es: ", final
		2:
			final<-(cantidad - 32) * 5/9 + 273.15 
			escribir "la conversion de fahrenheit a kelvine es: ", final
		3:
			final<-cantidad+460.67
			escribir "la conversion de fahrenheit a rankine es: ", final
		De Otro Modo:
			Escribir "ingrese un numero entero"
	Fin Segun
FinAlgoritmo

