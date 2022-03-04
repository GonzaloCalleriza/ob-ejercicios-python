print('Cual es tu peso (en kg)?')
peso = int(input())
print('Cuanto mides (en mts)?')
altura = int(input())

indiceDeMasa = peso / (altura**2)

print('Tu indice de masa corporal es: ', indiceDeMasa)