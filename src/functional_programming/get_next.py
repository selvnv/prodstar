# Напишите функцию, которая при каждом следующем своем вызове выводит на консоль
# следующий элемент заданного списка.

def list_iterator(element_list: list):
  index = -1
  def get_next():
    nonlocal index
    if len(element_list) == index + 1:
      return None
    else:
      index += 1
      return element_list[index]

  return get_next


test = [1, 6, 23, 125, 71, 98]
nxt = list_iterator(test)

for i in range(8):
  print(nxt())

test2 = [25, 39, 1, 7, 115, 1745, 100]
nxt = list_iterator(test2)

for i in range(8):
  print(nxt())