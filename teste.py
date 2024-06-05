import numpy as np

lista1 = [600, 600, 600, 600, 600, 600]
lista2 = [150, 150, 150, 150, 150, 150]

resultado = [x - y for x, y in zip(lista1, lista2)]
print(resultado)