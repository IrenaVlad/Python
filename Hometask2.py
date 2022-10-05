'''Задайте натуральное число N. Напишите программу, которая составит
 список простых множителей числа N.'''

import math

number=int(input('Введите число: '))
list = []
for i in range(2, int(math.sqrt(number)) + 1):
    while (number % i == 0): 
        list.append(i)
        number //= i
print(list)