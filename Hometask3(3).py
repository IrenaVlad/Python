'''3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

a = [1.1, 1.2, 3.1, 5, 10.01]
b = []
for i in range(len(a)-1):
    a[i] = a.split('.')
    c = int(a[1])
    b.append(c)
maximum = max(b)
minimum = min(b)
summa = maximum - minimum
print(summa)

a = [1.1, 1.2, 3.1, 5, 10.01]
b = []
for symbol in range(a):
    symbol = symbol.split('.')
    c = symbol[1]
    b.append(c)
summa = max(b) - min(b)
print(summa)