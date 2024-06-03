
# Сюди пишіть рішення задачі (функція з вашим прізвищем)
def has_three_same(number_value):
    number_str = str(number_value)
    for digit in set(number_str):
        if number_str.count(digit) == 3:
            return True
    return False

def find_numbers_range(start_value, end_value):
    result_list = []
    for number_value in range(start_value, end_value + 1):
        if has_three_same(number_value):
            result_list.append(number_value)
    return result_list

start_value = 1400
end_value = 1600


result_numbers = find_numbers_range(start_value, end_value)
for number_value in result_numbers:
    print(number_value)