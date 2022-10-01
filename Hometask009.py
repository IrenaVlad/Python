'''4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных 
позициях. Позиции хранятся в файле file.txt в одной строке одно число.'''
n = int(input("Введите n: "))
 some_list = []
for i in range (1, n+1):
   some_list.append((1 + 1/n)**n)
 print(some_list)

PythonВыделить код
1
2
3
n = int(input())
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')