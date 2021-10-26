'''Одномерные списки. Варианте 2, второе задание
Найдите минимальный по модулю элемент списка.
'''
import random
import math
lst = [random.randint(-100,100) for i in range(10)]
el_min = lst[0]
for it in lst:
    if abs(it) < abs(el_min):
        el_min = it

print(lst)
print ("Минимальный по модулю элемент:", el_min)