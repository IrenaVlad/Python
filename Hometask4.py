'''Задана натуральная степень k. Сформировать случайным образом список 
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
степени k.'''

from random import randint

k = int(input('Введите натуральную степень к: '))
a = int(randint(0, 100))
b = int(randint(0, 100))
c = int(randint(0, 100))
with open('file.txt', 'w') as data:
    data.write('a * x**k + b * x + c = 0')
data.close()