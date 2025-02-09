# Реализуйте рекурсивную функцию для подсчета элементов в списке.

def accumulate_count(number_list: list):
  if len(number_list) == 0:
    return 0

  return 1 + accumulate_count(number_list[1:])

print(accumulate_count([1, 6, 3, 2, 10, 11])) # Out: 6
print(accumulate_count([91, 74, 99, 1024])) # Out: 4
print(accumulate_count([])) # Out: 0