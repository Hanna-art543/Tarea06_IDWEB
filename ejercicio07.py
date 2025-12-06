while True:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingresa tu edad: "))

    with open ("datos.txt", "a") as archivo:
        archivo.write(f'Nombre: "{nombre}", Edad: "{edad}"\n')

    print("Datos guardados correctamente en datos.txt")

    opcion = input("¿Continuamos con el siguiente número?(s, n): ")
    
    if opcion != "s":
        print("Programa terminado.")
        break
