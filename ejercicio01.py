class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def presentarse (self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} y mi DNI es {self.dni}."
    

persona1 = Persona ("Ana", 18, 61048080)
persona2 = Persona ("Eduardo", 16, 43430890)

print(persona1.presentarse())
print(persona2.presentarse())

    
