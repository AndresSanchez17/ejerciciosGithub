# 30 % oyamel
# 20 % cedro

# 70 % pino
# 20 % oyamel
# 10 % cedro

# • En 10 m² caben 8 pinos.
# • En 15 m² caben 15 oyameles.
# • En 18 m² caben 10 cedros.

#30
tamano_superficie_terreno =float(input("Digite la superficie del bosque en hectáreas "))
#300000                           30
total_metros_cuadrados = tamano_superficie_terreno * 10000
# 50 % pino

#       300000
if total_metros_cuadrados <= 1000000 :
#   150000               300000           
    pino = total_metros_cuadrados * 0.5
#   90000              300000
    oyamel =total_metros_cuadrados * 0.3
#   60000               300000
    cedro = total_metros_cuadrados * 0.2
    x=100
    
else:
   pino = total_metros_cuadrados  * 0.7
   oyamel =total_metros_cuadrados * 0.2
   cedro = total_metros_cuadrados * 0.1
#120000      150000/10=15000*8  
total_pino = pino / 10 * 8  
#90000             90000/15=6000*15 
total_oyamel = oyamel / 15 * 15
#33333            60000/18=3333*10
total_cedro = cedro / 18 * 10

print(f"Total de superficie para pino {pino}m², el total de pinos es de {total_pino:,.2f}")
print(f"Total de superficie oyamel {oyamel}m², el total de oyamel es de {total_oyamel:,.2f}")
print(f"Total de superficie cedros {cedro}m² , el total de cedros es de {total_cedro:,.2f}")