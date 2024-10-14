Algoritmo sin_titulo
	final<-0
	Escribir "ingrese catidad en pies"
	leer cantidad
	Escribir "a que desea convertir? 1.pulgadas | 2. yardas | 3.metros | 4. centimetros"
	leer q
	Segun q Hacer
		1:
		final<-cantidad*12
		escribir "la conversion de pies a pulgadas es: ", final
		2:
			final<-cantidad/3
		escribir "la conversion de pies a yardas es: ", final
		3:
			final<-cantidad/3.281
		escribir "la conversion de pies a metros es: ", final
		4:
			final<-cantidad*30.48
		escribir "la conversion de pies a centimetros es: ", final
		De Otro Modo:
			Escribir "ingrese un numero entero"
	Fin Segun
FinAlgoritmo
