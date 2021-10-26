"""Одномерные списки.
Вариант 1, второе задание
Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу
"""

import random
lst = [random.randint(0,20) for i in range(10)]   #заполненение массива
sum = random.randint(0,20)
sum_cur = 0

lst_temp = lst.copy()
lst_temp.sort(reverse=True) #сортировка по убыванию
lst_find = []
print(lst)
print(lst_temp)
i_start = 0
fnd = False

print("Заданное число: ", str(sum))
while (sum != sum_cur) and (i_start < len(lst_temp)):
    sum_cur = 0
    lst_find.clear()
    for i in range(i_start, len(lst_temp)):
        if ((sum_cur + lst_temp[i])) < sum:
            sum_cur += lst_temp[i]
            lst_find.append(lst_temp[i])
        elif sum == sum_cur + lst_temp[i]:
            sum_cur += lst_temp[i]
            lst_find.append(lst_temp[i])
            fnd = True
            print(lst_find)
            break
    i_start += 1
if not (fnd):
    print("не удалось найти подмножество")




