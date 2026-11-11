nota_1=float(input("Nota 1 "))
#2
nota_2=float(input("Notas 2 "))
#3
nota_3=float(input("Nota 3 "))

x=0

if nota_1 >= 0 and nota_1 <=5:
    if nota_2 >= 0 and nota_2 <=5:
        if nota_3 >=0 and nota_3 <=5:
            x=1
        
        else:
            print("Nota 3 fuera del rango")
    else:
        print("Nota 2 fuera del rango")
else:
    print("Nota 1 fuera del rango")


if x == 1:

    proyecto = input("Digite 1 si presentó proyecto, 0 si no presentó poryecto ")
                #2.6
    promedio =(nota_1 + nota_2 + nota_3)/3

    #    2.6                 1     
    if promedio >=3 and proyecto == "1":
        print("Aprueba")
    elif promedio >= 3 and proyecto == "0":
        print("Condicionado")
    elif promedio >=2.5 and promedio <=2.9 and proyecto == "1":
        print("Habilita")
    else:
        print("Pierde")