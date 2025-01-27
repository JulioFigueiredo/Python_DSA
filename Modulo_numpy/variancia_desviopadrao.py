import numpy as np

arr = [30,10,30,90]

media = np.mean(arr)
print(f'Média: {media}')

# desvio

# subtrair cada nota pela media

desvio1 = media - arr[0]
desvio2 = media - arr[1]
desvio3 = media - arr[2]
desvio4 = arr[3] - media

# variancia
# eleva os desvios ao quadrado e divide pela quantidade de desvios

variancia = ((desvio1**2)+(desvio2**2)+(desvio3**2)+(desvio4**2))/4

print(f'Variância: {variancia}')

desvio_padrao = np.sqrt(variancia)

print(f'Desvio padrão: {desvio_padrao}')

