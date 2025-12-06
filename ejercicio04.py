def ingresar_numero():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            cuadrado = num ** 2
            print(f"Número: {num} | Cuadrado: {cuadrado}")
            break  

        except ValueError:
            print("Error: debes ingresar un número válido. Intenta otra vez.\n")


def main():
    print("Bienvenidos al programa para ingresar un número entero.")
    ingresar_numero()


main()


