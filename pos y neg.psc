Algoritmo sin_titulo
	Escribir "cuantos numeros va a ingresar?"
	leer cn
	Para i<-1 Hasta cn Con Paso 1 Hacer
		Escribir "ingrese numero"
		leer n
		si n>0 Entonces
			positivos<-positivos + 1 
		SiNo
			negativos <- negativos + 1
		FinSi
	Fin Para
	escribir "la cantidad total de positivos es: ", positivos 
	Escribir "la cantidad total de negativos es: ", negativos
FinAlgoritmo
