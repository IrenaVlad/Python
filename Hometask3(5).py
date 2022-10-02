''' Задайте число. Составьте список чисел Фибоначчи, в том 
числе для отрицательных индексов.'''

n = int(input('Введите число N: '))
def fib(n):
    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)
list1 = []
for e in range(0, n):
    list1.append(fib(e))
a = n*(-1)
def negafib(a):
    if a == -1:
         return 1
    elif a == -2:
        return -1
    else:
        return negafib(a+2) - negafib(a+1)
list2 = []
for e in range(a, 0):
    list2.append(negafib(e))
res = list2 + list1
print (str(res)) 

