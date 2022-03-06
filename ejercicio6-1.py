class Vehiculo:
    color = 'rojo'
    ruedas = 4
    puertas = 2
    
class Coche (Vehiculo):
    def velocidad(self):
        print('Voy rápido')
    def cilindrada(self):
        pass
    
    
c = Coche()
print(c.puertas)
c.velocidad()
