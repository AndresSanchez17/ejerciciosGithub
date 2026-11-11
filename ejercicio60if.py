# Escribe un programa que pida la edad (entero). Si la persona es menor de 18 años, debe mostrar Eres menor de edad y no pedir nada más. Si tiene 18 años o más, debe pedir el dinero que tiene (entero) para pagar una compra de 20000 pesos: si tiene 20000 o más, debe mostrar Compra realizada; si tiene menos, debe mostrar Dinero insuficiente.

edad= int(input("Digite su edad"))

if edad < 18 :
    print("Eres menor de edad")
elif edad >18 :
    cantidad_dinero = int(input("Ingrese su saldo: "))
    if cantidad_dinero > 20000:
        print("Compra exitosa")