def has_three_identical_digits_OlgaKornieva(num):
    num_str = str(num)
    digit_count = [0] * 10
    for digit in num_str:
        digit_count[int(digit)] ^= 1

    for digit in set(num_str):
        if num_str.count(digit) == 3:
            return True
    return False


a = int(input("Введите начало диапазона чисел: "))
b = int(input("Введите конец диапазона чисел: "))

selectori = [11, 22, 33, 44, 55, 66, 77, 88, 99]

for i in range(a, b + 1):
    if has_three_identical_digits_OlgaKornieva(i):
        print(i)