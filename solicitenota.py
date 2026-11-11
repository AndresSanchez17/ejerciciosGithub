# Solicite la calificación obtenida por un alumno en un examen (en escala de 0 a 10). El programa debe imprimir el mensaje "Aprobado" si la calificación es mayor a 8, y "Reprobado" en caso contrario.
# solicite_calificacion = float(input("Digite su calificación (0 a 10):\n"))

# if solicite_calificacion >8:
#     print("Aprobado")
# else:
#     print("Reprobado")
# En un estacionamiento se cobra 2 USD por cada hora o fracción de hora. Solicite el tiempo de permanencia del vehículo en horas y minutos enteros (por ejemplo: 2 horas y 15 minutos). Calcule e imprima el valor total que debe pagar el cliente. Aclaración: cualquier fracción de hora (es decir, cualquier cantidad de minutos mayor a 0) se cobra como una hora completa adicional. Ejemplo: 2 horas y 15 minutos se cobran como 3 horas → 6 USD. 

# En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas.
# Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
#  ¿Colon descubrió América?
#  ¿La independencia de México fue en el año 1810?
#  ¿The Doors fue un grupo de rock Americano?

print("Bienvenido al juego de preguntas ")

r1="si"
r2="si"
r3="si"

p1=input("Responda si o no a la siguiente pregunta :¿Colon descubrió América? ").lower()

if p1!= r1:
   print("Perdiste vuelve a empezar")
   
elif p1==r1:
     p2=input("¿La independencia de México fue en el año 1810? ").lower()
     if p2!=r2:
         print("Perdiste vuelve a empezar")
     else:      
        #p2==r2
        p3=input("¿The Doors fue un grupo de rock Americano? ").lower() 
        if p3!=r3:
                 print("Perdiste vuelve a empezar")
        else:
            print("Ganaste")