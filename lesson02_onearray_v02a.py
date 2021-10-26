'''Одномерные списки. Вариант 2, задание 1
Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
'''
import random
lst = [random.randint(0,100) for i in range(10)]
print(lst)
max = 0
for it in lst:
    if it%2 != 0: #число отрицательное
        if it > max:
            max = it

if max == 0:
    print('В списке нет отрицательных чисел')
else:
    print(max)

