'''2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

a = [2, 3, 4, 5, 6]
length = 0
i = 0
if len(a)%2 == 0:
    length = len(a)//2
else:
    length = len(a)//2+1   
b = [a[i]*a[len(a)-1-i] for i in range(length)]
print(b)