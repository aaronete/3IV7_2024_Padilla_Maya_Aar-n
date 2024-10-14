Algoritmo binario
	definir n, res Como Entero
	Definir bin como texto
	
	escribir "ingrese el numero que desea convertir"
	leer n
	
	si n >= 0 entonces 
		Mientras n > 0 Hacer
			res <- n%2
			nuevobin <- ConvertirATexto(res)
			
			bin <- nuevobin + bin
			
			n <- trunc(n/2)
		FinMientras
	FinSi
 escribir bin
FinAlgoritmo
