# Pida un número. Si el número es mayor a cero, verifique si es par o impar. Si el número es igual a cero, diga que es neutro.


numero = int(input("Digite un número: "))

if numero  > 0:
        if numero % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
elif numero == 0:
    print("El número es neutro")
else:
    print("Elnúmero es negativo") 



