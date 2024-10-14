Algoritmo sin_titulo
	Escribir "ingrese termino cuadratico"
	leer sq
	Escribir "ingrese termino lineal"
	leer li
	Escribir "inrese termino independiente"
	leer in
	
	arriba1<- -li+(raiz(li*li-4*sq*in))
	arriba2<- -li-(raiz(li*li-4*sq*in))
	
	abajo<-2*sq
	
	sol1<-arriba1/abajo
	sol2<-arriba2/abajo
	
	Escribir "las soluciones son: "
	Escribir sol1
	Escribir sol2
FinAlgoritmo
