# Создайте иерархию классов для зоомагазина.

# Иерархия должна включать базовый класс Pet, который имеет следующие атрибуты и методы:

# имя (строка): имя питомца
# вид (строка): вид животного
# возраст (int): возраст питомца
# пол (строка): пол питомца
# get_info() (метод): выводит имя, вид, возраст и пол питомца.
# Далее создайте два подкласса Pet под названием Dog и Cat, каждый со своими специфическими атрибутами и методами:

# Собака: имеет дополнительный атрибут под названием порода (строка) и метод под названием лай(), который печатает "Гав!".
# Кошка: имеет дополнительный атрибут под названием цвет (строка) и метод под названием мяу(), который печатает "Мяу!".
# Убедитесь, что атрибуты каждого класса инкапсулированы, сделав их приватными.

# Наконец, создайте экземпляры классов Dog и Cat и вызовите их соответствующие методы, чтобы продемонстрировать наследование, инкапсуляцию и полиморфизм.

class Pet:
    def __init__(self, name: str, type: str, age: int, gender: str):
        self._protected_name = name
        self._protected_type = type
        self._protected_age = age
        self._protected_gender = gender
    
    def get_info(self):
        print(f'Name: {self._protected_name};\nType: {self._protected_type};\nAge: {self._protected_age};\nGender: {self._protected_gender}\n')

class Dog(Pet):
    def __init__(self, name, type, age, gender, breed):
        super().__init__(name, type, age, gender)
        self.__breed = breed

    def woof(self):
        print('Woof!\n')

class Cat(Pet):
    def __init__(self, name, type, age, gender, color):
        super().__init__(name, type, age, gender)
        self.__color = color
    
    def meow(self):
        print('Meow!\n')

dog = Dog('Willy', 'Dog', 2, 'Male', 'Collie')
cat = Cat("Simon", 'Cat', 3, 'Male', 'White')

dog.get_info()
dog.woof()

cat.get_info()
cat.meow()