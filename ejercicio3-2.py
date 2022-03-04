print('Cual es tu peso (en kg)?')
peso = input()
print('Cuanto mides (en mts)?')
altura = input()

indiceDeMasa = peso / (altura**2)

print('Tu indice de masa corporal es: ' + indiceDeMasa)