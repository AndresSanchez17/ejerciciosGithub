# x=1
# while x <=10:
#     print("Python")
#     x= x+1
# Escriba un algoritmo que muestre en pantalla los números del 1 al 10.

# x=1
# while x<=10:
#     print(x)
#     x = x+1
# num=10
# while x>=1:
#     print("Número:",num)
#     num= num-1
# 3. Mostrar números pares del 1 al 20 Escriba un algoritmo que muestre todos los números pares entre 1 y 20.
# 4. Mostrar números impares del 1 al 15 Escriba un algoritmo que muestre todos los números impares entre 1 y 15.
# numeros_par=2
# while numeros_par<=20:
#     print(f"El numero {numeros_par} es par")
#     numeros_par = numeros_par + 2

# numeros_impar=1
# while numeros_impar<=15:
#     print(f"El numero {numeros_impar} es par")
#     numeros_impar = numeros_impar + 1+1

# numero_usuario = int(input("Digite el número:\n")) 

# x=1
# while x< 6:
#     print(numero_usuario)
#     x = x + 1
# Escriba un algoritmo que muestre la tabla de multiplicar del 3 del 1 al 10.

# print("Tabla de multiplicacion :\n")

# numero= int(input("Digite el numero a multiplicar: "))
# m= 1
# while m <= 10:
#     tabla = numero * m
#     print (f" {numero:,.0f} x {m} = {tabla:,.0f}")
#     m= m+1

import random
num_sec= random.randint(1,4)
x=1

while x <=3:
    num_user=int(input("Ingrese su numero ...suerte"))
    if num_sec==num_user :
        print("ganaste")
        break
    else:
        print("Tienes",(3-x),"intentos")
        x+=1

if x==4 :
    print("Mala suerte el numero ganador era",num_sec)    