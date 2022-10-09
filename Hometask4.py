'''Задана натуральная степень k. Сформировать случайным образом список 
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
степени k.'''

from random import randint

k = int(input('Введите натуральную степень k: '))
a = int(randint(1, 100))
b = int(randint(1, 100))
c = int(randint(1, 100))
print(a, b, c)
with open('file.txt', 'w') as data:
    data.write(str(a))
    data.write('*x^ ')
    data.write(str(k))
    data.write(' + ')
    data.write(str(b))
    data.write('*x + ')
    data.write(str(c))
    data.write(' = 0')
data.close()