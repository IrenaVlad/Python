'''1. Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

a = [2, 4, 1, 5, 7]
summa = 0
for i in range(1, len(a)-1, 2):
    summa += a[i]
print(summa)