'''
Многомерные списки. Задача 1
В матрице найти номер строки, сумма чисел в которой максимальна.
'''
import random
n_row = 5
n_column = 3
matrix = [[random.randint(0,10) for y in range(n_column)] for x in range(n_row)]
print(matrix)
sum_max = 0
for i in range(n_row):
    sum_cur = sum(matrix[i])
    print("строка:",i,"; сумма: ", sum_cur)
    if sum_cur > sum_max:
        sum_max = sum_cur
print("максимальная сумма:",sum_max)



