
# Сюди пишіть рішення задачі (функція з вашим прізвищем)

a = input("Введите начало диапозона чисел: ")
b = input("Введите конец диапозона чисел: ")

selectori = [11, 22, 33, 44, 55, 66, 77, 88, 99]

for i in range(a, b+1):
  if i - a in selectori:
    print(i)

# Olexandr Moiseienko
x1 = [1, 2, 33, 4, 5, 6, 7, 88]
x2 = [12, 22, 33, 44, 54, 64, 74, 88]

for el in range(0, len(x1)):
    if x1[el] != x2[el]:
        x1, x2 = x2, x1
    print(x1, x2)