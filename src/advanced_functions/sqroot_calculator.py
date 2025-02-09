# Напишите функцию, которая принимает на вход список целых чисел и
# возвращает новый список, в котором каждое целое число
# заменено квадратным корнем, округленным до ближайшего
# целого числа. Используйте аргументы с ключевыми словами,
# чтобы пользователь мог указать направление округления (вверх или вниз).
# Используйте декоратор для определения времени выполнения функции.

from math import sqrt, floor, ceil
import time

def measure_spent_time(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f'Total (sec): {end - start} (function {func.__name__})')
    return result
  return wrapper

@measure_spent_time
def get_sqrt_list(source_list: list, round_down = True, round_up = False):
  if round_down:
    return [floor(sqrt(x)) for x in source_list]
  elif round_up:
    return [ceil(sqrt(x)) for x in source_list]
  else:
    return [sqrt(x) for x in source_list]


sqrt_list = get_sqrt_list(range(1, 1000))
