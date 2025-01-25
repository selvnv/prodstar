import numpy as np

# Считывание строки, содержащей числе через пробел и разбиение на элементы по пробелу
string_num_array = input('Enter array of numbers: ').split()

# Получение на основе массива строк числового массива
num_array = [float(num) for num in string_num_array]

# Вычисление среднего
avg = np.mean(num_array)

print(f'Average number in source array: {avg}')