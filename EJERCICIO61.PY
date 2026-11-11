# En un estacionamiento se cobra 2 USD por cada hora o fracción de hora. Solicite el tiempo de permanencia del vehículo en horas y minutos enteros (por ejemplo: 2 horas y 15 minutos). Calcule e imprima el valor total que debe pagar el cliente. 
print()

tiempo_horas = int(input("Digite el tiempo de horas\n"))
tiempo_minutos = int(input("Digite los minutos"))

usd = 2


if tiempo_minutos > 0:
    horas_a_cobrar =tiempo_horas + 1 
else:
    horas_a_cobrar = tiempo_horas 
total_pagar =horas_a_cobrar * usd
print("Total a  pagar",total_pagar)