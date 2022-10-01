# 1. Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр

number = input('Введите число: ')
number = number.replace(',', '.')
sum = 0
for symbol in number:
  if symbol !='.':
    sum +=int(symbol)
print(sum)

