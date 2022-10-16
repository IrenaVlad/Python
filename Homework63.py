'''Задайте последовательность чисел. Напишите программу, которая выведет 
список неповторяющихся элементов исходной последовательности.'''

from random import randint
n=int(input('Введите число: '))
#list = []
#for i in range(n):
#    list.append(randint(0, 10))
#print(f'Исходный списоk {list}')
#list2 = []
#for i in list:
#	if list.count(i) < 2:
#		list2.append(i)
#print(f'Конечный список {list2}')
lst = [randint(0, 10) for i in range(n)]
print(f'Исходный списоk {lst}')
def f(list):
    count = list.count[i]
    if count[i] < 2:
        return list[i]
lst2 = filter(f, lst)
print(lst2)