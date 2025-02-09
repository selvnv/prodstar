# Реализуйте рекурсивную функцию для подсчета суммы элементов в списке.

def accumulate_sum(number_list: list):
  if len(number_list) == 0:
    return 0

  return number_list[0] + accumulate_sum(number_list[1:])

print(accumulate_sum([1, 6, 3, 2, 10, 11])) # Out: 33
print(accumulate_sum([91, 74, 99, 1024])) # Out: 1288
print(accumulate_sum([])) # Out: 0