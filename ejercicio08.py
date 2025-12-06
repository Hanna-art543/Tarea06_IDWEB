def leer_datos():
    try: 
        with open("datos.txt", "r") as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                print(linea.strip())

                print(f"Total de usuarios registrados: {len(lineas)}")

    
    except FileNotFoundError:
        print("Error: El archivo datos.txt no existe.")

leer_datos()


