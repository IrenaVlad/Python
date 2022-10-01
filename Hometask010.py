'''5. Реализуйте алгоритм перемешивания списка.'''

from random import randint

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(len(a)):
    index = randint(0, len(a) -1)
    b.append(a[index])
    a.remove(a[index])
print(b)