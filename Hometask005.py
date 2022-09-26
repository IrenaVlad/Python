from math import*
x1 = float(input('Введите значение x для точки А: '))
y1 = float(input('Введите значение y для точки А: '))
x2 = float(input('Введите значение x для точки В: '))
y2 = float(input('Введите значение y для точки В: '))
def distance(x1, y1, x2, y2):
 c = sqrt((x2-x1)**2 + (y2-y1)**2)
 return
c = distance(x1, y1, x2, y2)
print(c)