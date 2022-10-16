# print('Hello world')

# Ввод и вывод данных
# print('Введите a')
#a = input();
#print('Введите b')
#b = input();
#print(a, b)
#print('{} -- {}'.format(a,b))

#print('Введите a')
#a = input();
#print('Введите b')
#b = input();
#c = 30
#print(a, '+', b, '=', c)

#print('Введите a')
#a = int(input());
#print('Введите b')
#b = int(input());
#c = 30
#print(a, '+', b, '=', c)
#print('{} + {} = {}'.format(a, b, c))

#a = int(input('Введите a'))
#b = int(input('Введите b'))
#c = 33
#print('{} + {} = {}'.format(a, b, c))

#a = int(input('Введите \na: '))
#b = int(input('Введите \nb: '))
#c = 33
#print('{} + {} = {}'.format(a, b, c))

#Арифметические операции
# + (сложение),- (вычитание),* (умножение),/ (деление),
# % (остаток от деления),// (деление нацело),** (возведение в степень).

# += увеличивает значение левого операнда на значение правого операнда 
# и присваивает измененное значение обратно левому операнду. 
# Например,если a = 10, b = 20 => a+ = b будет равно 30.

# Логические операции
# and	Если оба выражения истинны, то условие будет истинным. 
# or	Если одно из выражений истинно, то условие будет истинным. 
# not	Если выражение a истинно, то not (a) будет ложным, и наоборот.

# Побитовые операторы
# &	 Если оба бита в одном и том же месте двух операндов равны 1, 
#    то в результат копируется 1. Иначе копируется 0.
# \| Результирующий бит будет равен 0, если оба бита равны нулю; иначе равен 1.
# ^	 Результирующий бит будет равен 1, если оба бита различны; иначе будет 0.
# ~	 Он вычисляет отрицание каждого бита операнда, т.е. если бит равен 0, 
#    то будет 1 и наоборот.
# << Значение левого операнда сдвигается влево на количество битов, 
#    присутствующих в правом операнде.
# >> Левый операнд сдвигается вправо на количество битов, 
#    присутствующих в правом операнде.

# Управляющие конструкции 
# username = input('Введите имя: ')
# if username == 'Маша':
  #  print('Ура, это же МАША!')
# elif username == 'Марина':
  #  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
  #  print('Ильнар - топ)')
#else:
 #   print('Привет, ', username)

# Управляющие конструкции: while
  # original = 23
 # inverted = 0
 # while original != 0:
     # inverted = inverted * 10 + (original % 10)
     # original //= 10
 # print(inverted)

# While-else
# original = 23
 # inverted = 0
 # while original != 0:
   #  inverted = inverted * 10 + (original % 10)
    # original //= 10
 # else:
   #  print('Пожалуй')
    # print('хватит )')
 # print(inverted)  #32
  
    # Управляющие конструкции: for
 # for i in 1, -2, 3, 14, 5:
   #  print(i)
#1 # -2 #3 # 14 #5
 
# Range 
# r = range(5) # range(0, 5)
# r = range(2, 5)
# r = range(100, 0, -20)

#r = range(100, 0, -20) 
 #for i in r:
  #   print(i)  # 100 80  60 40 20

 #for i in range(5):
  #   print(i)  #0123 4

# Вложенные циклы
# line = ""
 # for i in range(5):
   #  line = ""
    # for j in range(5):
     #    line += "*"
     # print(line)

# Строки
 # text = 'съешь ещё этих мягких французских булок'
  # print(len(text))
# print('ещё' in text) print(text.isdigit()) print(text.islower()) print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
  #  print(c)

# Немного о строках
 # text = 'съешь ещё этих мягких французских булок'
 #print(text[0])   # c
# print(text[1])   # ъ
 #print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])   # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...


# Списки 
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
 #for i in numbers:
     # i *= 2
     # print(i)    # [20, 4, 6, 8, 10]
 #print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
 # for e in colors:
# print(e) # red green blue 
# for e in colors:
# print(e*2) # redred greengreen blueblue
 # colors.append('gray') # добавить в конец
 # print(colors == ['red', 'green', 'blue', 'gray']) # True
 # colors.remove('red') #del colors[0] # удалить элемент

# Функции: 
# def function_name(x)
  # bode line 1
  # ...
  # body line n
# optional return

# def f(x):
     # return x**2
   # def f(x):
    # if x == 1:
       # return 'Целое'
    # elif x == 2.3:
       # return 23
    # else:
    # return

# print(f(1))           # Целое
# print(f(2.3))         # 23
# print(f(28))          # None
# print(type(f(1)))     # str
# print(type(f(2.3)))   # int
# print(type(f(28)))    # Nonetype