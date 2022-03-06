class Alumno:
    nombre = None
    nota = None
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    
        
a = Alumno('Juan', 8)
print(a.nombre)
print(a.nota)

if(a.nota>5):
    print('El alumno ', a.nombre, ' ha aprobado la materia')
else:
    print('El alumno', a.nombre, ' ha suspendido la materia')
