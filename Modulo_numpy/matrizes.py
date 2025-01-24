import numpy as np

# criando com np.array
mat = np.array([ [1,2,3], [4,5,6] ])
print(type(mat))
print(mat)
#print(mat.shape)

# criando com matrix

lista = ([ [1,2,3], [4,5,6], [7,8,9] ])
matrix = np.matrix(lista)
print(matrix)
print(type(matrix))

print(matrix.size)

print(matrix.diagonal())

print(matrix[0,1])