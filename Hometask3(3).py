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
max = max(b)
min = min(b)
sum = max - min
print(sum)