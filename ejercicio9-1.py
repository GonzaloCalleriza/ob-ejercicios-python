# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por 
# consola la lista de países ordenados alfabéticamente y separados por comas.

paises = {}

pais = ''
while(pais != 'q'):
    pais = input("Por favor agregar un país o presiona 'q' para terminar ")
    if(pais != 'q'):
        paises.add(pais)
        
pais_ordenados = paises.sort().join(', ')
print(pais_ordenados)