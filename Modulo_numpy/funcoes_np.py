import numpy as np

arr2 = np.array([1,2,3,4,5])

print(arr2)

#função arange: cria um array contendo uma PA , recebe os parametros start,stop,step

arr3 = np.arange(0,50,5)
print(arr3)

# os valores passados como parametro formam uma diagonal na matriz

arr6 = np.diag([1,2,3,4])
print(arr6)