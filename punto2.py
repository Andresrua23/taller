import random

# Crear un diccionario vacío llamado Departamentos
Departamentos = {}

# Ingresar el nombre del Departamento y su Capital
Departamentos["Amazonas"] = "Leticia"
Departamentos["Antioquia"] = "Medellin"
Departamentos["Arauca"] = "Arauca"
# Agrega más departamentos y capitales según sea necesario

# Función para adivinar la capital
def adivinar_capital(departamento, capital):
    intentos = 3
    while intentos > 0:
        respuesta = input(f"¿Cuál es la capital de {departamento}? (Escribe 'salir' para terminar): ").strip()
        
        if respuesta.lower() == "salir":
            return "salir"
        
        if respuesta.lower() == capital.lower():
            print("¡Correcto!")
            return "correcto"
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Respuesta incorrecta. Te quedan {intentos} intentos.")
            else:
                print("Hasta luego.")
                return "incorrecto"

# Variable para contar las respuestas incorrectas
respuestas_incorrectas = 0

# Ciclo para imprimir el Departamento y la Capital
while respuestas_incorrectas < 3:
    departamento, capital = random.choice(list(Departamentos.items()))
    resultado = adivinar_capital(departamento, capital)
    
    if resultado == "salir":
        break
    elif resultado == "correcto":
        del Departamentos[departamento]
    elif resultado == "incorrecto":
        respuestas_incorrectas += 1

if respuestas_incorrectas == 3:
    print("Has cometido 3 respuestas incorrectas. Hasta luego.")
else:
    print("Gracias por jugar.")
