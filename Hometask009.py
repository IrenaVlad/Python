'''4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных 
позициях. Позиции хранятся в файле file.txt в одной строке одно число.'''

from random import randint

N = int(input('Введите число: '))
a = []
mult = 1
for i in range(N):
  a.append(randint(-N, N))
print(a)

file = open('file.txt', 'r')

for line in file:
  mult *= a[int(line)]
file.close()
print(mult) 