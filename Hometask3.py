'''Задайте последовательность чисел. Напишите программу, которая выведет 
список неповторяющихся элементов исходной последовательности.'''

from random import randint
n=int(input('Введите число: '))
list = []
for i in range(n):
    list.append(randint(0, 10))
print(f'Исходный списоk {list}')
list2 = []
for i in list:
	if list.count(i) < 2:
		list2.append(i)
print(f'Конечный список {list2}')