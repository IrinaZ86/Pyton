'''
Многомерные списки. Задача 3
3.	Даны две квадратных таблицы чисел.
Требуется построить третью, каждый элемент которой равен сумме элементов,
стоящих на том же месте в 1-й и 2-й таблицах.
'''
import random
import numpy
import numpy as np

n = 3 #порядок квадратной матрицы
matrix1 = np.matrix([[random.randint(0,10) for i in range(n)] for j in range(n)])
matrix2 = np.matrix([[random.randint(0,10) for i in range(n)] for j in range(n)])

print("Матрица 1:")
print(matrix1)
print("Матрица 2:")
print(matrix2)
print("Матрица 3:")
matrix3 = matrix1 + matrix2
print(matrix3)




