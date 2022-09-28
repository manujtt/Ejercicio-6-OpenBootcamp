

class Alumno :
        
    def iniciar(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
    def resultado(self):
        if self.nota >= 5:
            print("Ha aprobado")
        else:
            print("No ha aprobado")


alumno1=Alumno()
alumno2=Alumno()

alumno1.iniciar("Juan", 8)
alumno2.iniciar("Antonio", 2)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
