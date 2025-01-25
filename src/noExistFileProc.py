# Обработка исключения - случая, когда введенный пользователем файл не существует
# Дополнительно - вывод количества строк в файле

filename = ''

while True:
    filename = input('Введите имя файла: ')
    if filename != '':
        break
    else:
        print('Введите корректное значение.')

lines = []

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError as ex:
    print(f'Файл \'{filename}\' не существует. Попробуйте еще раз, укажите путь к файлу. {ex}')
else:
    print(f'Количество строк в файле \'{filename}\': {len(lines)}')