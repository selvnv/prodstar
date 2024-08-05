import math

# Ввод коэффициентов
a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

# Вычисление дискриминанта
D = b ** 2 - 4 * a * c

# Вычисление корней
if D > 0:
    x1 = round((-b + math.sqrt(D)) / (2 * a), 2)
    x2 = round((-b - math.sqrt(D)) / (2 * a), 2)
    print(f'Уравнение имеет 2 корня: {x1} и {x2}')
elif D == 0:
    x1 = -b / (2 * a)
    print(f'Уравнение имеет один корень: {x1}')
else:
    print('Корней нет')
