class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    @staticmethod
    def es_extenso(libro):
        return libro.paginas > 300


libros = []

while True:
    print("\nPrograma para verificar la extensión del libro. Para salir coloque 0 en número de páginas.")
    
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    numPag = int(input("Número de páginas: "))

    if numPag == 0:
        break

    libro = Libro(titulo, autor, numPag)
    libros.append(libro)

    print("Es extenso:", Libro.es_extenso(libro))


print("\nRESUMEN")
for lib in libros:
    print(f"'{lib.titulo}' — Extenso: {Libro.es_extenso(lib)}")
