# crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una
# suma de todos estos elementos obtenidos mediante reduce.

lista_num= []
while(num != 404):
    num = int(input('Agrega un número. Pone 404 para salir'))
    if(num != 404):
        lista_num.add(num)
        
num_impares = lista_num.filter(lambda x: x%2 != 0)
suma_impares = num_impares.reduce()