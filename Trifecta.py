while True:
    # Ingreso de un número
    numero_str = input("Por favor, ingresa un número mayor a 0: ")
    if numero_str.isdigit():
        numero = int(numero_str)
        if numero > 0:
            # Ingreso de una palabra o frase
            palabra_o_frase = input("Ingresa una palabra o frase: ")

            # Contar caracteres
            cantidad_caracteres = 0
            for _ in palabra_o_frase:
                cantidad_caracteres += 1
            print(f"La palabra/frase tiene {cantidad_caracteres} caracteres.")

            # Calcular factorial
            factorial = 1
            for i in range(1, cantidad_caracteres + 1):
                factorial *= i
            print(f"El factorial de {cantidad_caracteres} es {factorial}.")

            # Verificar si el factorial es par o impar
            if factorial % 2 == 0:
                print("El resultado del factorial es par.")
            else:
                print("El resultado del factorial es impar.")
        else:
            print("El número debe ser mayor a 0. Inténtalo nuevamente.")
    else:
        print("Debes ingresar un número válido.")

    # Preguntar si desea continuar
    respuesta = input("¿Deseas ingresar otro número? (s/n): ")
    if respuesta.lower() != "s":
        break
