'''Одномерные списки. Вариант 1, первое задание
Удалить в списке все числа, которые повторяются более двух раз.
'''
import random
lst = [random.randint(0,10) for i in range(20)]   #заполненение массива
print(lst)                                #вывод первоначального массива

lst_output = lst.copy()
for item in lst:
    if lst.count(item ) > 1:
        lst_output.remove(item)

print(lst_output)                           #вывод массива без элементов, повторяющихся более двух раз


