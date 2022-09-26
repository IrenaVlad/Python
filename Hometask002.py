x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
z = int(input('Введите значение z: '))
a = x * y * z
b = x + y + z
if(a>0):
    a = 0
elif(a<1):
    a = 1
if(b>0):
    b = 1
elif(b<1):
    b = 1
if(a == b):
    print("Утверждение истинно")
elif(a !=b):
    print('Утверждение ложно')

leftSide = not ( x or y or z)
rigthSide = not x and not y and not z
result = leftSide == rigthSide
if(result == True):
    print('Утверждение истинно')
else:
    print('Утверждение ложно')