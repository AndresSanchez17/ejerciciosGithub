# Ejercicio 10. Cuota de una compañía de seguros Una compañía de seguros está abriendo un departamento de crédito para captar clientes. La cuota que un cliente debe pagar por un crédito se calcula así: • Si el monto de la fianza es menor a 50.000 USD: la cuota equivale al 3 % del monto. • Si el monto de la fianza es mayor o igual a 50.000 USD: la cuota equivale al 2 % del monto. Solicite el monto de la fianza y calcule la cuota que debe pagar el cliente.

monto_fianza = float(input("Digite el monto de la fianza:\n"))

if monto_fianza < 50000 : 
    cuota = monto_fianza * 3/100

else:
    cuota = monto_fianza * 2/100

print(f"La cuota que debe pagar el cliente es de:{cuota:,.0f} USD")