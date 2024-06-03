
# Сюди пишіть рішення задачі (функція з вашим прізвищем)

a = input("Введите начало диапозона чисел: ")
b = input("Введите конец диапозона чисел: ")

selectori = [11, 22, 33, 44, 55, 66, 77, 88, 99]

for i in range(a, b+1):
  if i - a in selectori:
    print(i)


def find_special_numbers(a, b):
  results = []
  for number in range(a, b + 1):
    s = str(number)
    if len(s) == 4:
      for digit in s:
        if s.count(digit) == 3 and len(set(s)) == 2:
          results.append(number)
          break
  return results

a = 1400
b = 1600
print(find_special_numbers(a, b))