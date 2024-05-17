import random

# Define el rango de números para jugar
rango_minimo = 1
rango_maximo = 100

# Genera el número secreto
numero_secreto = random.randint(rango_minimo, rango_maximo)

print(f"¡Bienvenido al juego de adivinanza de números! Elige un número entre {rango_minimo} y {rango_maximo}.")

intentos = 5
while intentos > 0:
    intento = int(input(f"Intento {6 - intentos}: Ingresa tu número: "))
    if intento == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste el número secreto ({numero_secreto}). ¡Ganaste!")
        intentos = 0
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    intentos -= 1

if intentos == 0:
    print(f"¡Perdiste! El número secreto era {numero_secreto}.")
