# 2. Напишите программу, которая 
# принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input('Введите число: '))
a = 1
for i in range (1,(N+1)):
    a *= i
print(a)