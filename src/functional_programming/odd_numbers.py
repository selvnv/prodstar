# Реализуйте рекурсивную функцию, которая выводит только
# нечетные числа из переданного списка на консоль.

def print_odd_numbers(number_list: list):
  if len(number_list) == 0:
    return

  if number_list[0] % 2 != 0:
    print(number_list[0])

  return print_odd_numbers(number_list[1:])

print_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print_odd_numbers([61, 74, 51, 27, 31, 94, 1015])
print_odd_numbers([])