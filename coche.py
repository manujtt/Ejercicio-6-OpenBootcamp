class vehiculo:
    def color(self):
        self.color = "blanco"
        
    def ruedas(self):
        self.ruedas = 4
        
    def puertas(self):
        self.puertas = 5
        


class coche(vehiculo):

    def __init__(self):
        
        self.color = "blanco"
        self.ruedas= 4
        self.puertas = 5
        self.Velocidad = "220 km/h"
        self.Cilindrada= "2000 cc"

    
    def Velocidad(self):
        self.Velocidad = 250
        

    def Cilindrada(self):
        self.Cilindrada = 2000

c = coche()

print(c.color)
print(c.ruedas)
print(c.puertas)
print(c.Velocidad)
print(c.Cilindrada)
