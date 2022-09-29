# 1. Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр

#number = input('Введите число: ')
#N = number.split(".")
#a = int(N[0]) # целая часть
#b = int(N[1]) # дробная часть
#sum = 0
#while (a != 0): # складываем числа целой части
 #   sum = sum + (a % 10)
 #   a = a // 10
#hile (b != 0): # складываем числа дробной части
 #   sum = sum + (b % 10)
  #  b = b // 10
#print("Сумма цифр числа равна ")

number = str(input('Введите число: '))
for i in number:
    i = i + number(i+1)
print(i)
exit()
sum = 0
index = 0
while index <= len(list(number)):
   sum = sum + number[index]
   index+=1
print(sum)