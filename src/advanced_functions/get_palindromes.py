# Напишите функцию, которая принимает список строк в качестве аргументов
# и возвращает новый список, содержащий только строки, являющиеся палиндромами.
# Палиндром — это слово, которое одинаково читается как вперед так и назад
# (например, «racecar», «level», «deified»).
# Используйте лямбда-функцию, чтобы проверить, является ли строка палиндромом.


def get_palindromes(string_list: list) -> list:
  return list(filter(lambda x: x == x[::-1], string_list))

print(get_palindromes(["racecar", "bober", "peppa", "pop", "siuuuuu", "level", "deified"]))