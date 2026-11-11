# Una tienda vende un producto que cuesta 35000 pesos. Primero el programadebe preguntar si el producto está disponible (
# si
# o
# no
# ). Si no está disponible, debemostrar
# Producto agotado
# y no pedir nada más. Si está disponible, debe pedir el saldo dela persona (número entero): si el saldo es 35000 o más, debe mostrar
# Compra exitosa
# ; sies menor, debe mostrar
# Saldo insuficiente

producto = input("El producto esta dispinible (si/no): ")

if producto == "no":
    print("El producto no esta disponible")
elif producto == "si":
    saldo_persona = float(input("Ingrese su saldo: "))
    if saldo_persona == 10:
        print("Compra exitosa")
    else:
        print("Saldo insuficiente")