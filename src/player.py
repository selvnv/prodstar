# Напиши класс, который описывает игрока в компьютерной игре а-ля Mario - игрока характеризует его
# здоровье (от 0 до 4)
# и положение на уровне - по оси x - от 0 до 1000 - 0 начало уровня,
# а 1000 - конец уровня, по оси y - от 0 до 100 - 0 земля, 100 самая верхняя точка экрана.

# Реализуй 2 метода - игрок может ходить в 2 направлениях и прыгать (достаточно выставить позицию по оси y, физику прыжка можно не реализовывать!)

class ModelLevelException(Exception):
    pass

MIN_HEALTH = 0
MAX_HEALTH = 4

MIN_X = 0
MAX_X = 1000

MIN_Y = 0
MAX_Y = 100

class Player:
    def __init__(self):
        self.__health = 4
        self.__x = 0
        self.__y = 0

    def change_health(self, value: int):
        if self.__health + value < MIN_HEALTH:
            print('WARNING: Health is low')
        elif self.__health + value > MAX_HEALTH:
            print('WARNING: Health is max')
        else:
            self.__health += value

    def change_x(self, x):
        if self.__x + x < MIN_X:
            print(f'WARNING: {self.__x + x} out of min border ({MIN_X})')
        elif self.__x + x > MAX_X:
            print(f'WARNING: {self.__x + x} out of max border ({MAX_X})')
        else:
            self.__x += x

    def change_y(self, y):
        if self.__y + y < MIN_Y:
            print(f'WARNING: {self.__y + y} out of min border ({MIN_Y})')
        elif self.__y + y > MAX_Y:
            print(f'WARNING: {self.__y + y} out of max border ({MAX_Y})')
        else:
            self.__y += y

    def __str__(self):
        return f'health: {self.__health}\nx: {self.__x}\ny: {self.__y}\n'


player = Player()

player.change_health(10)
player.change_health(-1)
print(player)
player.change_health(1)
print(player)

player.change_x(-10)
player.change_x(100)
player.change_x(-10)
player.change_x(1000)
print(player)

player.change_y(-10)
player.change_y(90)
player.change_y(-10)
player.change_y(100)
print(player)