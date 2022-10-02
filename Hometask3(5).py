''' Задайте число. Составьте список чисел Фибоначчи, в том 
числе для отрицательных индексов.'''

n = int(input('Введите число N: '))
def fib(n):
     if n in [1, 2]:
         return 1
     else:
         return fib(n-1) + fib(n-2)
list1 = []
for e in range(1, 8):
    list1.append(fib(e))

def negafib(n):
    if n in [-1]:
         return 1
    elif n in [-2]:
        return -1
    else:
        return negafib(n+2) - negafib(n+1)
list2 = []
for e in range(1, 8):
    list2.append(negafib(e))
print(list2) 
res = list1 + list2
print ("Concatenated list:\n" + str(res)) 
