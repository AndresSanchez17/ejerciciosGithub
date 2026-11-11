#Luis compra 10 prducto del mismo precio, si el precio total es mayor  a 100 dolares, tendra un descuento del 20% de lo contrario, el descuento será del 10%.

producto_cantidad = 10
precio = float(input("Precio del producto:\n"))
precio_total = producto_cantidad * precio

if precio_total > 100:
    descuento = 20/100
    print("Has obtenido un descuento del 20%")
    
else:
    descuento = 10/100
    print("Su decuento es del 10%")

total_pagar=precio_total -(precio_total* descuento)
print("Su total a pagar es:", total_pagar)


