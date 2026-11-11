# Pida un usuario y una clave. Si el usuario es "estudiante", verifique la clave. Si la clave es "123", diga "Acceso", si no, "Error de clave".

print("Bienvenido")
print()
usuario = input("Digite su usuario:\n")
clave = 123

estudiante = "estudiante"

if usuario == estudiante:
    clave = int(input("Digite la clave:")) 
    if clave == 123:
        print("Acceso")
    else:
        print("Error de clave")
else:
    print("Usuario no reconocido")

    
