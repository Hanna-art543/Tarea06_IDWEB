class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def mostrar_info (self):
        return f"Nombre : {self.nombre} | Sueldo: {self.sueldo}"
    
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre} | Sueldo: {self.sueldo} | Departamento: {self.departamento}"
    

empleado1 = Empleado ("Shadeth", 6500)
gerente1 = Gerente ("Matías", 8000, "Ventas")

print(empleado1.mostrar_info())
print(gerente1.mostrar_info())


