# Ejercicio 1. Cálculo de nómina con descuento de seguro social Solicite el nombre de un empleado y la cantidad de horas trabajadas en la semana. El pago bruto se calcula multiplicando las horas trabajadas por una tarifa de 40 USD por hora. A ese pago bruto se le debe descontar el seguro social según la siguiente regla: • Si el pago bruto es mayor a 3.200 USD, el descuento de seguro social es del 8,5 % del pago bruto.   

print("Nomina")

nombre = input("Digite su nombre:\n ")
cantidad_horas = int(input("Digite la cantidad de horas:"))
hora = 40
pago_bruto = hora * cantidad_horas

if pago_bruto > 3200 :
    descuento_seguro = pago_bruto *8.5/100
    print ("Su descuento es:",descuento_seguro)
else:
    print("No tienes descuento")