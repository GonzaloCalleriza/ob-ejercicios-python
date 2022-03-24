# crear un archivo py y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:
    puertas: 0
    motor: "diesel"
    
    def __init__(self, puertas, motor):
        self.puertas: puertas
        self.motor: motor
        
auto = Vehiculo(5, "diesel")
        

ar = open('ejercicio8vehiculo.bin', 'wb+')
pickle.dump(auto, ar)
ar.close()