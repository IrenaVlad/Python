'''Задайте последовательность чисел. Напишите программу, которая выведет 
список четных элементов исходной последовательности.'''

from random import randint
n = int(input('Введите число: '))
lst = [randint(0, 10) for i in range(n)]
print(f'Исходный список {lst}')
def f(spisok):
    if spisok%2 == 0:
        return True
    else:
        return False
lst2 = filter(f, lst)
print(f'Конечный список: {list(lst2)}')