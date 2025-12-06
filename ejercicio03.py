class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    @staticmethod
    def es_extenso(libro):
        if libro.paginas > 300:
            return True
        else:
            return False


while True:
    print("\nPrograma para verificar la extensión del libro. Para salir coloque 0 en número de páginas.")
    
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    numPag = int(input("Número de páginas: "))

    if numPag == 0:
        print("Programa finalizado.")
        break

    libro = Libro(titulo, autor, numPag)

    print("Es extenso:", Libro.es_extenso(libro))
