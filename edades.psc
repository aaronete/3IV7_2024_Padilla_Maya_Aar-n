Algoritmo vivos_y_muertos
    Definir personas, años, i, j, año Como Entero
    Definir vivas, joven, vieja Como Entero
	
    Escribir "¿Cuántas personas vas a considerar?"
    Leer personas
	
    Dimension nacimientos[personas]
    Dimension muertes[personas]
	
    Para i <- 1 Hasta personas Con Paso 1 Hacer
        Escribir "¿En qué año nació la persona ", i, "?"
        Leer nacimientos[i]
        Escribir "¿En qué año falleció la persona ", i, "?"
        Leer muertes[i]
    FinPara
	
    Escribir "¿Cuántos años deseas consultar?"
    Leer años
	
    Dimension consulta[años]
	
    Para i <- 1 Hasta años Con Paso 1 Hacer
        Escribir "¿Qué año deseas consultar ", i, "?"
        Leer consulta[i]
    FinPara
	
    Para i <- 1 Hasta años Con Paso 1 Hacer
        año <- consulta[i]
        vivas <- 0
        joven <- 91681681
        vieja <- -9849
		
        Para j <- 1 Hasta personas Con Paso 1 Hacer
            Si nacimientos[j] <= año Y muertes[j] >= año Entonces
                vivas <- vivas + 1
                edad <- año - nacimientos[j]
				
                Si edad < joven Entonces
                    joven <- edad
                FinSi
				
                Si edad > vieja Entonces
                    vieja <- edad
                FinSi
            FinSi
        FinPara
		
        Escribir "En el año ", año, " había ", vivas, " personas vivas."
        Si vivas > 0 Entonces
            Escribir "La persona más joven tenía ", joven, " años."
            Escribir "La persona más anciana tenía ", vieja, " años."
        SiNo
		Escribir "No había personas vivas en ese año."
        FinSi
    FinPara
FinAlgoritmo