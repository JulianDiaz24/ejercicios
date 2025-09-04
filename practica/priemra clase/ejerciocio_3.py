# Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
# conjunto de los elementos que se encuentran en A o en B, pero no en ambos

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

diferencia=conjunto1.symmetric_difference(conjunto2)

print("los elemntos que no se encuentran en ambos son:",diferencia)

