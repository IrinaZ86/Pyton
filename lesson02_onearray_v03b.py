'''Одномерные списки. Вариант 03, второе задание
Найдите сумму элементов списка между двумя первыми нулями.
Если двух нулей нет в списке, то выведите ноль.
'''
import random
lst = [random.randint(-5, 5) for i in range(20) ]
print(lst)
i_null = 0
i_2null = 0

if lst.count(0) > 1:
    i_null = lst.index(0)
    i_2null = lst.index(0, i_null+1, len(lst))
    lst_sum = lst[i_null: i_2null+1]
    print("Позиции нулей:",i_null, i_2null)
    print("Список суммируемых элементов",lst_sum)
    print("Сумма:",sum(lst_sum))
elif lst.count(0) == 1:
    print("В списке только один элемент со значением <0>, позиция элемента:", lst.index(0))
    print(0)
else:
    print("В списке нет элементов  со значением <0>")
    print(0)
