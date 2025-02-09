# Напишите генератор-функцию, которая генерирует последовательность
# Коллатца для заданного начального числа. Последовательность генерируется
# путем многократного применения правила к каждому числу в последовательности:
# если число четное, разделите его на 2, иначе умножьте его на 3 и добавьте 1.
# Последовательность завершается, когда достигает числа 1.
# Используйте замыкания для хранения текущего номера в последовательности.

from math import trunc

# Реализация с хранением индекса...
# def coltz_sequence(number: int):
#   current_number = number
#   current_index = 0
#   def get_next():
#     nonlocal current_number
#     nonlocal current_index

#     yield current_number

#     while True:
#       print(f'Current index is {current_index}')
#       if current_number == 1:
#         break
#       elif current_number % 2 == 0:
#         yield trunc(current_number / 2)
#         current_number /= 2
#       else:
#         yield trunc(3 * current_number + 1)
#         current_number = 3 * current_number + 1

#       current_index += 1
#   return get_next

def coltz_sequence(number: int):
  current_number = number

  yield current_number

  while True:
    if current_number == 1:
      break
    elif current_number % 2 == 0:
      yield trunc(current_number / 2)
      current_number /= 2
    else:
      yield trunc(3 * current_number + 1)
      current_number = 3 * current_number + 1

for i in coltz_sequence(19):
  print(i)
