def valor_lista ():
    lista = [89, 45, 67, 23, 34]

    while True:
        try:
            indice = int(input("Ingrese un índice (0-4): "))
            valor = lista[indice]     
            print(f"Elemento en posición {indice}: {valor}")
            break                      

        except ValueError:
            print("Error: Debes ingresar un número entero.\n")

        except IndexError:
            print("Error: El índice está fuera del rango de la lista (0-4).\n")


valor_lista()

