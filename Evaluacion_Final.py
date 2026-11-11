# 1. Evaluación definitiva de una asignatura
# En una institución educativa, la nota definitiva de un estudiante se compone de tres notas parciales (cada una entre 0 y 5) y la presentación de un proyecto final.
# El programa debe:
# 1. Leer las tres notas.
# 2. Validar que cada nota esté entre 0 y 5. Si alguna está fuera del rango, mostrar "Error en notas".
# 3. Leer un valor adicional donde:
# o 1 significa que presentó el proyecto.
# o 0 significa que no lo presentó.
# 4. Calcular el promedio de las tres notas.
# 5. Aplicar las siguientes reglas:
#  Si el promedio es mayor o igual a 3.0 y presentó proyecto → Aprueba
#  Si el promedio es mayor o igual a 3.0 y no presentó proyecto → Condicionado
#  Si el promedio está entre 2.5 y 2.9 y presentó proyecto → Habilita
#  En cualquier otro caso → Pierde
nota_1= float(input("Nota 1:\n"))
nota_2=float(input("Nota 2:\n"))
nota_3=float(input("Nota 3:\n"))

if nota_1 >= 0 and nota_2 <=  5:
    if nota_2 and nota_2<=5:
        if nota_3 >=0 and nota_3 <=5:
            proyecto = input("Digite 1 si presentó proyecto, 0 si no presento proyecto")
            promedio = (nota_1 + nota_2 + nota_3)/3
            
            if promedio >= 3 and proyecto =="1":
                print("Aprueba")
            elif promedio >= 3 and proyecto ==0 :
                print("Condicionado")
            elif proyecto >=2.5 and proyecto <=2.9 and proyecto=="1":
                print("Habilita")
            else:
                print("Pierde")
        else:
            print("Nota fuera de rango")
    else:
        print("Nota fuera de rango")
else:
    print("Nota fuera de rango")
    