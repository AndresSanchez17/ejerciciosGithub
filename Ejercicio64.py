# Lea la temperatura. Si es menor a 10 grados diga "Frío". Si está entre 10 y 25 diga "Templado". Si es mayor a 25 diga "Calor"

temperatura = int(input("Digite la temperatura en  grados :"))

if temperatura < 10:
    print("Frio")
elif temperatura <= 25:  
        print("Templado")
else: 
    print("Calor")