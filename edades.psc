Algoritmo vivos_y_muertos
    Definir personas, a�os, i, j, a�o Como Entero
    Definir vivas, joven, vieja Como Entero
	
    Escribir "�Cu�ntas personas vas a considerar?"
    Leer personas
	
    Dimension nacimientos[personas]
    Dimension muertes[personas]
	
    Para i <- 1 Hasta personas Con Paso 1 Hacer
        Escribir "�En qu� a�o naci� la persona ", i, "?"
        Leer nacimientos[i]
        Escribir "�En qu� a�o falleci� la persona ", i, "?"
        Leer muertes[i]
    FinPara
	
    Escribir "�Cu�ntos a�os deseas consultar?"
    Leer a�os
	
    Dimension consulta[a�os]
	
    Para i <- 1 Hasta a�os Con Paso 1 Hacer
        Escribir "�Qu� a�o deseas consultar ", i, "?"
        Leer consulta[i]
    FinPara
	
    Para i <- 1 Hasta a�os Con Paso 1 Hacer
        a�o <- consulta[i]
        vivas <- 0
        joven <- 91681681
        vieja <- -9849
		
        Para j <- 1 Hasta personas Con Paso 1 Hacer
            Si nacimientos[j] <= a�o Y muertes[j] >= a�o Entonces
                vivas <- vivas + 1
                edad <- a�o - nacimientos[j]
				
                Si edad < joven Entonces
                    joven <- edad
                FinSi
				
                Si edad > vieja Entonces
                    vieja <- edad
                FinSi
            FinSi
        FinPara
		
        Escribir "En el a�o ", a�o, " hab�a ", vivas, " personas vivas."
        Si vivas > 0 Entonces
            Escribir "La persona m�s joven ten�a ", joven, " a�os."
            Escribir "La persona m�s anciana ten�a ", vieja, " a�os."
        SiNo
		Escribir "No hab�a personas vivas en ese a�o."
        FinSi
    FinPara
FinAlgoritmo