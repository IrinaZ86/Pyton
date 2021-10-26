'''Одномерные списки. Вариант 03, первое задание
Найдите сумму отрицательных элементов списка.
'''
import random
lst = [random.randint(-100, 100) for i in range(10) ]
print(lst)
sum = 0

for i in range(len(lst)):
    if lst[i] < 0:
        sum += lst[i]

print("Сумма отрицательных чисел:",sum)