'''
Многомерные списки. Задача 2
2.	Симметричная матрица.
Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.
'''
import random

n = 3 #порядок квадратной матрицы
#matrix = [[random.randint(0,10) for y in range(n)] for x in range(n)]
matrix = [[1,0,2],[0,0,0],[2,0,1]]
symmetrical = True
print(matrix)
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetrical = False
            break
    if not(symmetrical):
        break #уже понятно что матрица не симметрична, выходим из цикла

if symmetrical:
    print("матрица симметрична")
else:
    print("матрица не симметрична")



