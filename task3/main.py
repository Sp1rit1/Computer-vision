import  math
import random
from abc import ABC, abstractmethod

class Shape(ABC):
    __area = 0
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    length = 0; width = 0
    def __init__(self, length, width):
        self.length = length; self.width = width
    def get_area(self):
        self.__area = self.length * self.width
        return self.__area

class Circle(Shape):
    radius = 0
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        self.__area = round(math.pi * self.radius ** 2, 1)
        return self.__area

class Rhomb(Shape):
    d1 = 0; d2 = 0
    def __init__(self, d1, d2):
        self.d1 = d1; self.d2 = d2
    def get_area(self):
        self.__area = (self.d2 * self.d1) / 2
        return self.__area


def get_cut(str):
    cut = [-1, -1]; middle = 0
    for i in range(len(str)):
        try:
            num = int(str[i])
            if middle == 0:
                cut[0] = i
            cut[1] = i; middle += 1
        except ValueError:
            if middle > 0:
                cut[1] = i - 1; break
            continue
    return cut


def do_something_with_array(arr, command):
    cut = get_cut(command)
    nomber_instruction = 0
    n = 0; b = 0; v = 0
    if (command[:cut[0]] == "Получить элемент по " and command[cut[1] + 1:] == " индексу"):
        n = int(command[cut[0]:cut[1] + 1])
        nomber_instruction = 1
    elif (command[:cut[0]] == "Получить " and command[cut[1] + 1:] == " элемент с конца массива"):
        n = int(command[cut[0]:cut[1] + 1])
        nomber_instruction = 2
    elif (command[:cut[0]] == "Получить элементы с "):
        n = int(command[cut[0]:cut[1] + 1])
        for i in range(2):
            command = command[cut[1] + 1:]
            cut = get_cut(command)
            if (i == 0 and command[:cut[0]] == " по ") :
                b = int(command[cut[0]:cut[1] + 1])
            elif (i == 1 and command[:cut[0]] == " с шагом "):
                v = int(command[cut[0]:cut[1] + 1])
                nomber_instruction = 3
    if nomber_instruction == 1:
        return  arr[n]
    elif nomber_instruction == 2:
        n *= -1
        return arr[n]
    elif nomber_instruction == 3:
        return arr[n:b:v]
    else:
        return "Введена неверная команда"


a = 5; b = 7
rectangle = Rectangle(a, b)
circle = Circle(a)
rhomb = Rhomb(a, b)
print("\n\nПлощадь прямоугольника со сторонами ", a, " и ", b, " равна ", rectangle.get_area())
print("\nПлощадь круга с радиусом ", a, " равна ", circle.get_area())
print("\nПлощадь ромба с диагоналями ", a, " и ", b, " равна ", rhomb.get_area(), "\n\n")


array1 = [random.randint(1, 100) for _ in range(20)]
print("Исходный массив:\n", array1)
command1 = input("Введите команду: ")
print("\nРезультат: ", do_something_with_array(array1, command1), '\n')
command2 = input("Введите команду: ")
print("\nРезультат: ", do_something_with_array(array1, command2), '\n')
command3 = input("Введите команду: ")
print("\nРезультат: ", do_something_with_array(array1, command3), '\n')