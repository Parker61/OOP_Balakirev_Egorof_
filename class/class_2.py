# ________Egorof___2.5 Публичные, приватные, защищенные атрибуты и методы______________
#
#
# В коде из предыдущего урока возникала ошибка AttributeError:
# 'AverageCalculator' object has no attribute '__calculate_average'
# Мы не можем напрямую обращаться к приватному методу. Но есть способ, как осуществить такой доступ, мы разобрали его
# на лекции к этому уроку В последней строчке кода используйте эти знания, чтобы вызвать приватный метод вне класса
class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def __calculate_average(self):
        total = sum(self.numbers)
        return total / len(self.numbers)


average_calculator = AverageCalculator([1, 2, 3])
print(average_calculator._AverageCalculator__calculate_average())


########################################################################
class BankDeposit:
    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance / 100 * self.rate

    def get_balance_with_profit(self):
        return self.__calculate_profit() + self.balance


################################################################
class Student:
    def __init__(self, __name, __age, __branch):
        self.__name = __name
        self.__age = __age
        self.__branch = __branch

    def __display_details(self):
        print(f'Имя: {self.__name}')
        print(f'Возраст: {self.__age}')
        print(f'Направление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()


obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()
print(dir(obj))  # ['_Student__age', '_Student__branch', '_Student__display_details', '_Student__name'
print(obj._Student__age)  # не прямой доступ к приватному атрибуту


################################################################
class PizzaMaker:
    def __make_pepperoni(self):
        pass

    def _make_barbecue(self):
        pass


maker = PizzaMaker()
print(PizzaMaker.__dict__.keys())  # dict_keys(['__module__', '_PizzaMaker__make_pepperoni', '_make_barbecue',
maker._make_barbecue()  # protected
maker._PizzaMaker__make_pepperoni()  # private


########################################################################
class Library:
    def __init__(self, __books):
        self.__books = __books

    def __check_availability(self, title):
        return True if title in self.__books else False

    def search_book(self, title):
        return self.__check_availability(title)

    def return_book(self, title):
        self.__books.append(title)

    def _checkout_book(self, title):
        if self.__check_availability(title):
            self.__books.remove(title)
            return True
        return False


########################################################################
class Employee:
    def __init__(self, name, __position, __hours_worked, __hourly_rate):
        self.name = name
        self.__position = __position
        self.__hours_worked = __hours_worked
        self.__hourly_rate = __hourly_rate

    def __calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate

    def _set_position(self, __position):
        self.__position = __position

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return f'Name: {self.name}, Position: {self.get_position()}, Salary: {self.get_salary()}'


################################################################
class RobotVacuumCleaner:
    name = 'Henry'
    charge = 25

    @classmethod
    def update_charge(cls, new_value):
        cls.charge = new_value

    @staticmethod
    def hello(name):
        return f'Привет, {name}'

    @property
    def data(self):
        return {'name': self.name, 'charge': self.charge}

    @classmethod
    def make_clean(self):
        if self.charge < 30:
            return 'Кожаный, заряди меня! Я слаб'
        return 'Я вычищу твою берлогу!!!'


print(RobotVacuumCleaner.hello('Господин'))
RobotVacuumCleaner.update_charge(50)

robot = RobotVacuumCleaner()
print(robot.make_clean())
print(robot.data)

RobotVacuumCleaner.update_charge(False)
print(robot.make_clean())


# #Привет, Господин
# Я вычищу твою берлогу!!!
# {'name': 'Henry', 'charge': 50}
# Кожаный, заряди меня! Я слаб
########################################################################
# Метод @classmethod также можно использовать в качестве метода для создания нового экземпляра класса.
# В нашем примере метод занимается только созданием новых объектов или порождением объектов, поэтому  его можно назвать
# фабричным методом.Фабричный метод (Factory method) - пораждающий шаблон проектирования, определяющий общий
# интерфейс создания объектов в родительском классе и позволяющий изменять создаваемые объекты в дочерних классах.
class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    @classmethod
    def get_red_car(cls, model):
        return cls(model, 'red')


car1 = Car.get_red_car('Audi')
print(car1, car1.model, car1.color)

car2 = Car.get_red_car('BMW')
print(car2, car2.model, car2.color)


########################################################################################################
# Перед вами имеется реализация класса Circle. Ваша задача добавить в него следующее:класс-метод from_diameter,
# принимающий диаметр круга. Метод from_diameter должен возвращать новый экземпляр класса Circle(учитывайте,
# что экземпляры круга создаются по радиусу);статик-метод is_positive, принимающий одно число. Метод is_positive
# должен возвращать ответ является ли переданное число положительным статик-метод area, который принимает радиус и
# возвращает площадь круга. Для этого воспользуйтесь формулой
class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def is_positive(value):
        return True if value > 0 else False

    @staticmethod
    def area(radius):
        return 2 * 3.14 * radius ** 2


circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 6.28


#########################################################################################
# 2.10 Пространство имен класса________________________________

# Создайте класс Robot, у которого есть:атрибут класса population. В этом атрибуте будет храниться общее
# количество роботов, изначально принимает значение 0;конструктор __init__, принимающий 1 аргумент name.
# Данный метод должен сохранять атрибут name и печатать сообщение вида "Робот <name> был создан".
# Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;
# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"
# метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"
# метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"
class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} был создан')
        Robot.population += 1

    def destroy(self):
        print(f'Робот {self.name} был уничтожен')
        Robot.population -= 1

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')


r2 = Robot("R2-D2")  # печатает "Робот R2-D2 был создан"
r2.say_hello()  # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many()  # печатает "1, вот сколько нас еще осталось"
r2.destroy()  # печатает "Робот R2-D2 был уничтожен"


################################################################
# 2.10 Пространство имен класса Создайте базовый класс User, у которого есть:метод __init__, принимающий имя
# пользователя и его роль. Их необходимо сохранить в атрибуты экземпляра name и role соответственно
# Затем создайте класс Access , у которого есть:приватный атрибут класса __access_list , в котором хранится
# список ['admin', 'developer']приватный статик-метод __check_access , который принимает название роли и
# возвращает True, если роль находится в списке __access_list , иначе - Falseпубличный статик-метод get_access ,
# который должен принимать экземпляр класса User и проверять есть ли доступ у данного пользователя к ресурсу при
# помощи метода __check_access  . Если у пользователя достаточно прав, выведите на экран сообщение«User <name>:
# success», если прав недостаточно - «AccessDenied»Если передается тип данных, отличный от экземпляр класса User,
# необходимо вывести сообщение:«AccessTypeError»

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        return role in Access.__access_list

    @staticmethod
    def get_access(self_user):
        if isinstance(self_user, User):
            if Access.__check_access(self_user.role):
                print(f'User {self_user.name}: success')
            else:
                print(f'AccessDenied')
        else:
            print(f'AccessTypeError')


user1 = User('batya99', 'admin')
Access.get_access(user1)  # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya)  # печатает AccessDenied

Access.get_access(5)  # печатает AccessTypeError


#####################################################################

class BankAccount:
    bank_name = "Tinkoff Bank"
    address = 'Москва, ул. 2-я Хуторская, д. 38А'

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, balance):
        return cls(name, balance)

    @classmethod
    def bank_info(cls):
        return f'{cls.bank_name} is located in {cls.address}'


################################################################################################
# _________Balakirev________________________
################################################################
########################################################################
# Создайте объект clock класса Clock и установите время, равным 4530.
class Clock:
    def __init__(self, tm):
        self.__time = 0
        if self.check_time(tm):
            self.__time = tm

    def set_time(self, tm):
        if self.check_time(tm):
            self.__time = tm

    @staticmethod
    def check_time(tm):
        if 0 <= tm < 100000 and type(tm) == int:
            return True
        else:
            return False

    def get_time(self):
        return self.__time


clock = Clock(4530)
clock.set_time(45)
print(clock.get_time())


###############################################################
class Clock:
    def __init__(self, tm):
        self.__time = None
        if self.__check_time(tm):
            self.__time = tm

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    @classmethod
    def __check_time(cls, tm):
        return True if 0 <= tm < 100000 and type(tm) == int else False

    def get_time(self):
        return self.__time


clock = Clock(4530)
clock.set_time(45)
print(clock.get_time())  # 45


################################################################
# Подвиг 4. Объявите класс с именем Money и определите в нем следующие переменные и методы:
# - приватная локальная переменная money (целочисленная) для хранения количества денег (своя для каждого объекта класса
# Money);- публичный метод set_money(money) для передачи нового значения приватной локальной переменной money
# (изменениевыполняется только если метод check_money(money) возвращает значение True);
# - публичный метод get_money() для получения текущего объема средств (денег);
# - публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
# - приватный метод класса check_money(money) для проверки корректности объема средств в параметре money (возвращает True
# если значение корректно и False - в противном случае).
class Money:
    def __init__(self, money):
        self.money = None
        if self.check_money(money):
            self.__money = money
        # self.set_money(money)

    def set_money(self, money):
        if self.check_money(money):
            self.__money = money

    @classmethod  # задумался, зачем  метод, который каждый раз получает новые значения делать методом класса ?
    def check_money(cls, money):
        return True if money >= 0 and type(money) is int else False

    # Проблема isinstance в том, что в основе bool лежит int , поэтому тут сработает код:
    # mn = Money(True)
    # mn.get_money()  # True То есть можно присвоить логическую переменную вместо целочисленной.

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()  # 100
m2 = mn_2.get_money()  # 120


###############################################################
class Money:

    def __init__(self, money):  # Инициал. лок. св-ва экз. класса
        self.set_money(money)  # через сеттер set_money устанавливаем лок. св-ва экз. класса

    def set_money(self, money):  # сеттер set_money. устанавливает лок. св-ва экз. класса
        if self.__check_money(money):  # обращение к приватному методу для проверки корректности ввода данных
            self.__money = money  # Если метод вернет True то устанавливаем приватное лок. св-ва экз. класса

    def get_money(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__money

    def add_money(self, mn):  # метод добавляет к текущему лок. св-ву экз. класса средства от объекта mn.__money
        self.__money += mn.get_money()

    @staticmethod
    def __check_money(money):  # метод проверяет корректность ввода данных
        return type(money) == int and money >= 0  # Если целое число и money больше либо равно 0 то вернет True


################################################################
# Подвиг 6. Объявите класс Book со следующим набором сеттеров и геттеров:
# При этом, в каждом объекте должны создаваться приватные локальные свойства: book = Book(автор, название, цена)
class Book:
    def __init__(self, author, title, price):
        self.__title = None
        self.__author = None
        self.__price = None
        self.set_title(title)
        self.set_author(author)
        self.set_price(price)

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


###############################################################
from typing import Union


class Book:

    def __init__(self, author: str, title: str, price: Union[int, float]):
        self.__author: str = author
        self.__title: str = title
        self.__price: Union[int, float] = price

    def set_title(self, title: str) -> None:
        # запись в локальное приватное свойство __title объектов класса Book значения title
        if type(title) == str:
            self.__title = title

    def set_author(self, author: str) -> None:
        # запись в локальное приватное свойство __author объектов класса Book значения author
        if type(author) == str:
            self.__author = author

    def set_price(self, price: Union[int, float]) -> None:
        # запись в локальное приватное свойство __price объектов класса Book значения price
        if type(price) in (int, float):
            self.__price = price

    def get_title(self) -> str:
        # получение значения локального приватного свойства __title объектов класса Book
        return self.__title

    def get_author(self) -> str:
        # получение значения локального приватного свойства __author объектов класса Book
        return self.__author

    def get_price(self) -> Union[int, float]:
        # получение значения локального приватного свойства __price объектов класса Book;
        return self.__price


################################################################
# Подвиг 7. Объявите класс Line для описания линии на плоскости, объекты которого предполагается создавать командой:
# line = Line(x1, y1, x2, y2)
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)

    def draw(self):
        # print(f'{self.__x1} {self.__y1} {self.__x2} {self.__y2}')
        print(*self.get_coords())


###############################################################
class Line:
    def __init__(self, *args):
        self.set_coords(*args)

    def set_coords(self, *args):
        self.__x1, self.__y1, self.__x2, self.__y2 = args

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())


############################################################
class Line:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, *args):
        self.__dict__ = dict(zip(self.__dict__.keys(), args))

    def get_coords(self):
        return tuple(self.__dict__.values())

    def draw(self):
        print(*self.__dict__.values())


################################################################
from typing import Union, Tuple


class Line:
    __x1: float
    __y1: float
    __x2: float
    __y2: float

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.set_coords(x1, y1, x2, y2)

    def set_coords(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

    def get_coords(self) -> Tuple[Union[int, float], ...]:
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self) -> None:
        print(*self.get_coords())


###############################################################


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2=None, y2=None):
        self.__ep = self.__sp = None
        if isinstance(x1, Point) and isinstance(y1, Point):
            self.set_coords(x1, y1)
        elif all(map(lambda x: type(x) in (int, float), (x1, y1, x2, y2))):
            self.set_coords((x1, y1), (x2, y2))

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: Прямоугольник с координатами: {self.get_coords()} {self.get_coords()}')


rect = Rectangle(0, 0, 20, 34)


################################################################
# Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:
# pt = Point(x, y)где x, y - координаты точки на плоскости (целые или вещественные числа). При этом в объектах класса
# Point должны формироваться следующие локальные свойства:__x, __y - координаты точки на плоскости.и один геттер:
# get_coords() - возвращение кортежа текущих координат __x, __y Объекты второго класса Rectangle (прямоугольник)
# должны создаваться командами:r1 = Rectangle(Point(x1, y1), Point(x2, y2))или
# r2 = Rectangle(x1, y1, x2, y2) Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2)
# - правый нижний. При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться
# следующие локальные свойства:__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
# __ep - объект класса Point с координатами x2, y2 (нижний правый угол).
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2=None, y2=None):
        self.__ep = self.__sp = None
        if isinstance(x1, Point) and isinstance(y1, Point):
            self.set_coords(x1, y1)
            # self.__sp = x1
            # self.__ep = y1
        elif all(map(lambda x: type(x) in (int, float), (x1, y1, x2, y2))):
            self.set_coords(Point(x1, y1), Point(x2, y2))

    def set_coords(self, sp, ep):
        self.__sp = sp  # __sp и __ep  экземпляры класса Point
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: Прямоугольник с координатами: '
              f'{self.__sp.get_coords()}'
              f' {Point.get_coords(self.__ep)} ')


rect = Rectangle(Point(0, 0), Point(20, 30))
rect.draw()
rect2 = Rectangle(1, 2.6, 3.3, 4)
rect2.draw()


###############################################################
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2=None, y2=None):
        self.__ep = self.__sp = None
        if isinstance(x1, Point) and isinstance(y1, Point):
            self.__sp = x1.get_coords()
            self.__ep = Point.get_coords(y1)

        elif all(map(lambda x: type(x) in (int, float), (x1, y1, x2, y2))):
            self.set_coords((x1, y1), (x2, y2))

    def set_coords(self, sp, ep):
        self.__sp = sp  # не как экземпляр Point
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: Прямоугольник с координатами: '
              f'{self.get_coords()}')


rect = Rectangle(Point(0, 0), Point(20, 30))
rect.draw()
rect2 = Rectangle(1, 2.6, 3.3, 4)
rect2.draw()
###############################################################
from typing import Union, Tuple


# Тип аннотации Union[] модуля typing представляет собой тип объединения typing.Union[X, Y]
# эквивалентно X | Y, который означает либо X, либо Y.

class Point:
    __x: float
    __y: float

    def __init__(self, x: float, y: float):
        self.set_coords(x, y)

    def __repr__(self):
        return self.__x, self.__y

    def set_coords(self, x: float, y: float):
        self._check_coords(x, y)
        self.__x = x
        self.__y = y

    def get_coords(self) -> Tuple[Union[int, float], Union[int, float]]:
        return self.__x, self.__y

    @staticmethod
    def _check_coords(x: float, y: float):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Coordinates must be of int of float type")


class Rectangle:
    __sp: Point
    __ep: Point

    def __init__(self, arg1: Union[Point, float], arg2: Union[Point, float], arg3: float = None, arg4: float = None):
        if arg3 is None and arg4 is None:
            self.set_coords(arg1, arg2)
        elif arg3 is not None and arg4 is not None:
            # self.__sp = Point(arg1, arg2)
            # self.__ep = Point(arg3, arg4)
            self.set_coords(Point(arg1, arg2), Point(arg3, arg4))
        else:
            raise TypeError("Pass either 2 points or 4 coordinates when creating a rectangle")

    def set_coords(self, sp: Point, ep: Point) -> None:
        self.__sp = sp
        self.__ep = ep

    def get_coords(self) -> Tuple[Point, Point]:
        return self.__sp, self.__ep

    def draw(self) -> None:
        print(f"Прямоугольник с координатами: ({self.__sp.get_coords()}) ({self.__ep.get_coords()})")


rect = Rectangle(Point(0, 0), Point(20, 30))
rect.draw()
rect2 = Rectangle(1, 2.6, 3.3, 4)
rect2.draw()


################################################################
class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            x, y = args
            self.__sp = x
            self.__ep = y
        elif len(args) == 4:
            x1, y1, x2, y2 = args
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)


###############################################################
# Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке
# Python), когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:
# Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:

class LinkedList:
    """объявите класс LinkedList, который будет представлять связный список в целом
    и иметь набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;        """
        if self.tail:
            self.tail.set_next(obj)  # связывание старого объекта self.tail с новым объектом obj (self.__next = obj)
            obj.set_prev(self.tail)  # связка нового объекта obj,здесь  self.__prev = self.tail
        self.tail = obj  # переместить указатель self.tail на новый объект obj,
        # self.tail будет равен всегда послед добаленому объекту
        if not self.head:  # если добавляем только самый первый объект
            self.head = obj

    def remove_obj(self):
        """удаление последнего объекта из связного списка;        """
        if self.tail is None:
            return  # ничего не делать
        prev = self.tail.get_prev()  # -> self.__prev
        if prev:  # если предыдущий существует
            prev.set_next(None)  # последний объект self.next указывает на None
        self.tail = prev  # переместить tail на предпоследний prev объект
        if self.tail is None:  # если мы удаляем единственный объект то tail будет указывать на None
            self.head = None

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка.        """
        lst = []
        h = self.head
        while h:
            lst.append(h.get_data())  # ->self.__data
            h = h.get_next()  # переход на след объект связного списка,
        return lst


class ObjList:
    """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:    """

    def __init__(self, data):
        self.__data = data
        self.__next = self.__prev = None

    def set_next(self, obj):  # связывание с новым объетом класса ObjList
        """изменение приватного свойства __next на значение obj;        """
        self.__next = obj

    def set_prev(self, obj):  # obj -> self.tail, к новому объекту привязка предыдущего значения self.tail
        """изменение приватного свойства __prev на значение obj;        """
        self.__prev = obj

    def get_next(self):
        """получение значения приватного свойства __next;        """
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev;        """
        return self.__prev

    def set_data(self, data):
        """изменение приватного свойства __data на значение data;        """
        self.__data = data

    def get_data(self):
        """получение значения приватного свойства __data.        """
        return self.__data


# ob = ObjList("данные 1")
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
print(res)


################################################################
class LinkedList:
    '''в каждом объекте этого класса должны создаваться локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None)
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None)'''

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj) -> None:
        '''добавление нового объекта obj класса ObjList в конец связного списка'''
        if self.head is None:  # Если объект первый и указателя начала head не существует..
            self.head = obj  # head будет указывать на передаваемый объект, все, уходим...
            return
        last_obj = self.head  # Если это не так, пусть последним будет head
        while (last_obj.get_next()):  # Пока укатель next не станет указывать на None
            last_obj = last_obj.get_next()  # У предпоследнего объекта проходим по ссылке get_next() получаем последний
        last_obj.set_next(obj)  # У последнего объекта ставим указатель _nex на передаваемый объект
        obj.set_prev(last_obj)  # У передаваемого объекта ставим указатель _prev на бывший последним объект
        self.tail = obj

    def remove_obj(self) -> None:
        '''удаление последнего объекта из связного списка'''
        if self.head is not None:
            if self.head.get_next() is None:
                self.head = None
                return
            self.head = self.head.get_next()
            self.head.set_prev(None)

    def get_data(self):
        '''получение списка из строк локального свойства __data всех объектов связного списка'''
        if self.head is None:
            return []
        if self.head.get_next() is None:
            return [self.head.get_data()]
        data = []
        last_obj = self.head
        while (last_obj != self.tail):  # До предпоследнего объекта переходим по ссылке _next, аппендим
            data.append(last_obj.get_data())
            last_obj = last_obj.get_next()  # Последний объект все равно получен, тк мы перешли у предпоследнего по ссылке :)
        data.append(last_obj.get_data())
        return data


class ObjList:
    '''__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None)
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None)
    __data - строка с данными'''

    def __init__(self, data=None) -> None:
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj) -> None:
        '''изменение приватного свойства __next на значение obj'''
        self.__next = obj

    def set_prev(self, obj) -> None:
        '''изменение приватного свойства __prev на значение obj'''
        self.__prev = obj

    def get_next(self):
        '''получение значения приватного свойства __next'''
        return self.__next

    def get_prev(self):
        '''получение значения приватного свойства __prev'''
        return self.__prev

    def set_data(self, data: str) -> None:
        '''изменение приватного свойства __data на значение data'''
        self.__data = data

    def get_data(self) -> str:
        '''получение значения приватного свойства __data'''
        return self.__data


###############################################################
class LinkedList:

    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
        else:
            self.head = self.tail = obj

    def remove_obj(self):
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self):
        data_list = []
        obj = self.head
        while obj:
            data_list.append(obj.get_data())
            obj = obj.get_next()
        return data_list


################################################################
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if self.head:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
        else:
            self.head = self.tail = obj

    def remove_obj(self):
        if self.head:
            if self.head != self.tail:
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)
            else:
                self.head = self.tail = None

    def get_data(self) -> list:
        result = []
        obj = self.head
        while obj:
            result.append(obj.get_data())
            obj = obj.get_next()
        return result


###############################################################
# Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо
# запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:
# em = EmailValidator() # None В самом классе реализовать следующие методы класса (@classmethod): get_random_email(cls)
# - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email
# (латинский буквы, цифры, символ подчеркивания и точка);
# check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.
# Корректность строки email определяется по следующим критериям:
# - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
# - длина email до символа @ не должна превышать 100 (сто включительно);
# - длина email после символа @ не должна быть больше 50 (включительно);
# - после символа @ обязательно должна идти хотя бы одна точка;
# - не должно быть двух точек подряд. # Также в классе нужно реализовать приватный статический метод класса:
# is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.
#  Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр
#  email не является строкой, то check_email() возвращает False.

from string import ascii_letters, digits
import random


class EmailValidator:
    string_email = ascii_letters + digits + '_' + '.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        email = ''
        n_befor = random.randint(1, 100)
        n_after = random.randint(1, 50)

        for i in range(n_befor):
            email += random.choice(cls.string_email)
        email += '@'

        s2 = ''
        while not s2.count('.') >= 1:
            s2 = ''
            s2 += ''.join(random.choice(cls.string_email) for i in range(n_after))
        return email + s2

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if email.count('@') == 1:
                before, after = email.split('@')
                return all(
                    [len(before) <= 100, len(after) <= 50, set(before + after).issubset(cls.string_email), '.' in after,
                     '..' not in email])
            return False

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


res = EmailValidator.check_email(EmailValidator.get_random_email())
print(res)
################################################################
import random
import string

symbols = string.ascii_letters + string.digits + '_.'


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None  # super().__new__(cls, *args, **kwargs)

    @classmethod
    def check_email(cls, email):
        return cls.__is_email_str(email) and cls.__is_email_correct(email)

    @classmethod
    def get_random_email(cls):
        return f'{"".join([random.choice(symbols) for _ in range(random.randint(1, 100))])}@gmail.com'

    @staticmethod
    def __is_email_correct(email):
        if email.count('@') == 1:
            before, after = email.split('@')
            return all([len(before) <= 100, len(after) <= 50, set(before + after).issubset(symbols), '.' in after,
                        '..' not in email])
        return False

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


###############################################################
from string import ascii_letters, digits
import random


class EmailValidator:
    string = ascii_letters + digits + '_.@'
    string_email = ascii_letters + digits + '_' + '.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        n_befor = random.randint(1, 100)
        n_after = random.randint(1, 50)
        lenghth = len(cls.string_email) - 1
        s1 = ''.join(cls.string_email[random.randint(0, lenghth)] for i in range(n_befor)) + '@'
        s2 = ''
        while not s2.count('.') >= 1:
            s2 = ''
            s2 += ''.join(cls.string_email[random.randint(0, lenghth)] for i in range(n_after))
        return s1 + s2

    @classmethod
    def check_email(cls, email):
        return cls.__is_email_str(email) and cls.__is_email_correct(email)

    @staticmethod
    def __is_email_correct(email):
        string_email = ascii_letters + digits + '_' + '.'
        if email.count('@') == 1:
            before, after = email.split('@')
            return all(
                [len(before) <= 100, len(after) <= 50, set(before + after).issubset(string_email), '.' in after,
                 '..' not in email])
        return False

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


################################################################
###############################################################
# ____________Egorof___2.6 Геттеры и сеттеры, property атрибуты________________________
# создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email

class UserMail:
    def __init__(self, login, __email):
        self.login = login
        self.__email = __email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if email.count('@') == 1 and email.split('@')[1].find('.') >= 1 and isinstance(email, str):
            # if '.' in email[email.find('@'):]
            self.__email = email
        else:
            print(f'ErrorMail:{email}')

    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3]  # ErrorMail:[1, 2, 3]
k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait


################################################################################################
# Создайте класс Employee, который имеет следующие методы:метод __init__, который устанавливает значения приватных
# атрибутов __name  и __salary: имя работника и его зарплату.приватный геттер метод для атрибута __name
# приватный геттер метод для атрибута __salary приватный сеттер метод для атрибута __salary: он должен позволять
# сохранять в атрибут __salary только положительные числа. В остальных случаях не сохраняем переданное значение в
# сеттер и печатаем на экран сообщение "ErrorValue:<value>".свойство title, у которого есть только геттер
# из пункта 2.свойство reward, у которого геттером будет метод из пункта 3, а сеттером — метод из пункта 4.

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__salary = value
        else:
            print(f'ErrorValue:{value}')

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)


################################################################
# ___________Egorof ____________2.7 Декоратор Property________
# Пожалуй самый элементарный вариант использования property — предоставить атрибуты только для чтения в ваших классах.
# Для достижения этой цели вы можете создать Person , как в следующем примере:
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
person = Person('Jack', 33)
# >>> # Считываем значения
person.name
# Jack
person.age
# 33
# >>> # Пытаемся записать новое значение
person.age = 42


# Traceback (most recent call last):
#     ...
# AttributeError: can't set attribute
###############################################################
# а. можно, но это будут просто методы которые вызываются от ЭК как ЭК.method() (по сути это обычная функция)
# например, если  убрать  тут property, то установить баланс можно будет вручную, чего делать не желательно

class User:

    def __init__(self, login):
        self.login = login
        self.__balance = 0

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.__balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        raise ValueError('Баланс нельзя устанавливать вручную, положите депозит')


def deposit(self, value):
    self.balance += value


def payment(self, value):
    if value > self.balance:
        print('Не хватает средств на балансе. Пополните счет')
        return False
    else:
        self.balance -= value
        return True


billy = User('billy@rambler.ru')


########################################################
# свойство notes_list, которое распечатает содержимое атрибута ._notes в виде упорядоченного списка
class Notebook:
    def __init__(self, _notes):
        self._notes = _notes

    @property
    def notes_list(self):
        for i, v in enumerate(self._notes, start=1):
            print(f'{i}.{v}')


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list


################################################################
class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = float(value)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5


sq = Square(42)
# Считываем значения
sq.side  # 42.0
sq.area  # 1764.0
# записаем новое значение
sq.area = 100
sq.side  # 10.0

###############################################################
# Вы также можете создать атрибуты только для записи, изменив способ реализации метода получения ваших свойств.
# Например, вы можете заставить свой метод получения вызывать исключение каждый раз, когда пользователь
# получает доступ к базовому значению атрибута.
import hashlib
import os


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Пароль можно только менять, нельзя смотреть")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000)


jack = User("Jack", "secret_key")

jack._hashed_password
# b'7\x1f+\x02\xc4q\x93\xb6\x98\xb3\r\x9f\x9e\xa4v\nI\xde\x10\x11\x98\xb7\xcf\xff\x9c\x83f\xe4\x07\x8c\xce\xc8'

jack.password
# Traceback (most recent call last):
# ...
#   raise AttributeError("Пароль можно только менять, нельзя смотреть")

jack.password = "new_secret"

print(jack._hashed_password)


# b'H\xd3f\xe5\x92,\xc4\xe6\xf29g\xe0\x96I\xd1\xf3^\xd6D\xb4\xbd\x89\xc8\x85s\x13\xa6YA\x08\x89\x89'

################################################################
# Создайте класс Money, у которого есть:конструктор __init__, принимающий 2 аргумента: dollars, cents. По входным
# аргументам вам необходимо создать атрибут экземпляра total_cents. свойство геттер dollars, которое возвращает
# количество имеющихся долларов;свойство сеттер dollars, которое принимает целое неотрицательное число - количество
# долларов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, при этом значение центов
# должно сохранятся. В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран
# сообщение "Error dollars";
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @property
    def cents(self):
        return self.total_cents % 100

    @dollars.setter
    def dollars(self, dollars):
        if isinstance(dollars, int) and dollars >= 0:
            self.total_cents = dollars * 100 + self.cents
        else:
            print('Error dollars')

    @cents.setter
    def cents(self, cents):
        # if isinstance(cents, int) and 0 <= cents < 100:
        if type(cents) is int and 0 <= cents < 100:
            self.total_cents = self.dollars * 100 + cents
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
        # return f'Ваше состояние составляет {self.total_cents // 100} долларов {self.cents % 100} центов'


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents)  # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
print(Bill.total_cents)  # 66612


################################################################################################
# 2.8 Вычисляемые свойства
class Square:
    def __init__(self, side):
        self.side = side  # идет обращение к @side.setter а он устанавливает self.__area

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if not self.__area:
            self.__area = self.side ** 2
        return self.__area

    @area.setter
    def area(self, value):
        self.side = value ** 0.5
        self.__area = value


################################################################################################
# Создайте класс Password, который имеет:метод __init__, который устанавливает значение атрибута password
# вычисляемое свойство strength, которое определяет стойкость пароля. Если длина пароля меньше 8 символов, то такой
# пароль считается слабым, свойство должно вернуть строку  "Weak". Сильным паролем считается тот, в котором длина
# символов 12 и более, в таком случае свойство возвращает строку "Strong". Во всех остальных случаях необходимо
# вернуть "Medium"
class Password:
    def __init__(self, password):
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def strength(self):
        if len(self.password) < 8:
            return 'Weak'
        elif len(self.password) >= 12:
            return 'Strong'
        else:
            return 'Medium'


pass_1 = Password("Alligator34")
assert pass_1.password == "Alligator34"
assert pass_1.strength == "Medium"

pass_2 = Password("Alligator345678")
assert pass_2.password == "Alligator345678"
assert pass_2.strength == "Strong"

pass_3 = Password("345678")
assert pass_3.strength == "Weak"
print('Good')

pass_1 = Password("Alligator34")
assert pass_1.password == "Alligator34"
assert pass_1.strength == "Medium"

pass_2 = Password("Alligator345678")
assert pass_2.password == "Alligator345678"
assert pass_2.strength == "Strong"

pass_3 = Password("345678")
assert pass_3.strength == "Weak"
print('Good')


###############################################################
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @property
    def date(self):
        return f'{self.d:02}/{self.m:02}/{self.y:04}'

    @property
    def usa_date(self):
        return f'{self.m:02}-{self.d:02}-{self.y:04}'


d1 = Date(5, 10, 1)
d2 = Date(15, 3, 999)

print(d1.date)  # 05/10/2001
print(d1.usa_date)  # 10-05-2001
print(d2.date)  # 15/03/0999
print(d2.usa_date)  # 03-15-0999

# ###############################################################################################
# 2.11 Практика по методам и свойствам (property)
with open("pass.txt") as q:
    q = q.read().strip().split()


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.__secret = "secret"

    @property
    def secret(self):
        r = input("Ввудите ваш пароль: ")
        if r == self.__password:
            print(self.__secret)
        else:
            print("Пароль неверный")

    @property
    def password(self):
        return self.__password

    @staticmethod
    def prov(passw):
        return passw in q

    @password.setter
    def password(self, val):
        if self.prov(val):
            raise TypeError("такой есть уже")
        else:
            self.__password = val


u = User('pad', 'ss')  # ss
print(u.secret)  # secret


###############################################################
# В классе Registration необходимо реализовать:метод __init__ принимающий один аргумент логин пользователя.
# Метод __init__ должен сохранить переданный логин через сеттер (см пункт 3). То есть когда отработает данный код
# def __init__(self, логин):   self.login = логин # передаем в сеттер login значение логин
# должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения
# Cвойство геттер login, которое возвращает значение self.__login;Свойство сеттер login, принимает значение нового
# логина. Новое значение мы должны проверить на следующее:логин, так как является почтой, должен содержать один символ
# собаки «@». В случае, если в логине отсутствует символ «@», вызываем исключение при помощи строки raise ValueError
# ("Логин должен содержать один символ '@'")логин должен содержать символ точки «.» после символа «@».В случае, если
# после @ нету точки, вызываем исключение при помощи строки raise ValueError("Логин должен содержать символ '.'")

class Registration:
    def __init__(self, логин):
        self.login = логин  # передаем в сеттер login значение логин

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if not login.count('@') == 1:
            raise ValueError("Логин должен содержать один символ '@'")
        if not '.' in login.split('@')[1]:
            # if login.split('@')[1].count('.') == 1:
            raise ValueError("Логин должен содержать символ '.'")
        else:
            self.__login = login


####################################################################################

###############################################################

###############################################################################################

###################################################################################################################################################

###############################################################

###############################################################################################
# ______________Balakiref________________________________
###############################################################
# Подвиг 1. Пусть в программе объявлен следующий класс:

class Money:
    def __init__(self):
        self.__money = 0

    def set_money(self, value):
        self.__money = value

    def get_money(self):
        return self.__money

    money = property(get_money, set_money)


m = Money()
m.money = 10


# для считывания информации из локальной переменной __money достаточно записать res = m.money
# в строчке money = property(get_money, set_money) создается объект-свойство с геттером get_money и сеттером set_money
# в строчке m.money = 10 происходит вызов метода set_money и локальной переменной __money присваивается значение 10
################################################################

###############################################################
# Подвиг 4. Объявите в программе класс Car, в котором реализуйте объект-свойство с именем model для записи и считывания
# информации о модели автомобиля из локальной приватной переменной __model.# Объект-свойство объявите с помощью
# декоратора @property. Также в объекте-свойстве model должны быть реализованы проверки:
# - модель автомобиля - это строка;- длина строки модели должна быть в диапазоне [2; 100].
class Car:

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and 2 <= len(model) <= 100:
            # if type(model) == str and len(model) in range(1,101):
            self.__model = model


car = Car()
car.model = "Toyota"


################################################################
# Подвиг 5. Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:
# wnd = WindowDlg(заголовок окна, ширина, высота)В каждом объекте класса WindowDlg должны создаваться приватные
# локальные атрибуты:__title - заголовок окна (строка);__width, __height - ширина и высота окна (числа).
# В классе WindowDlg необходимо реализовать метод:show() - для отображения окна на экране (выводит в консоль строку в
# формате: "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").Также в классе WindowDlg необходимо
# реализовать два объекта-свойства:width - для изменения и считывания ширины окна;height - для изменения и считывания
# высоты окна.При изменении размеров окна необходимо выполнять проверку:- переданное значение является целым числом
# в диапазоне [0; 10000].Если хотя бы один размер изменился (высота или ширина), то следует выполнить
# автоматическую перерисовку окна (вызвать метод show()). При начальной инициализации размеров width, height
# вызывать метод show() не нужно.
class WindowDlg:
    def __init__(self, __title, __width, __height):
        self.__title = __title
        self.__width = __width
        self.__height = __height

    def show(self):
        # print(f'{self.__title}: {self.__width}, {self.__height}", например "Диалог 1: 100, 50')
        print(f'{self.__title}: {self.width}, {self.height}", например "Диалог 1: 100, 50')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if all((self.check(width), self.check_value(self.width, width))):  # итерируемый объект список, кортеж, словарь
            self.__width = width
            self.show()

    @staticmethod
    def check(value):
        return True if type(value) == int and value in range(0, 10001) else False

    # isinstance(num, int) при bool выдает True =)))) лучше type использовать

    @staticmethod
    def check_value(self_value, value):
        return True if self_value != value else False

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check(height) and self.height != height:
            self.__height = height
            self.show()


###############################################################
# Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов),
# когда один объект ссылается на следующий и так по цепочке до последнего:Для этого объявите в программе два класса:
# StackObj - для описания объектов односвязного списка;Stack - для управления односвязным списком.
# Объекты класса StackObj предполагается создавать командой:obj = StackObj(данные)Здесь данные - это строка с
# некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:
# __data - ссылка на строку с данными, указанными при создании объекта;__next - ссылка на следующий объект класса
# StackObj (при создании объекта принимает значение None).Также в классе StackObj должны быть объявлены
# объекты-свойства:next - для записи и считывания информации из локального приватного свойства __next;
# data - для записи и считывания информации из локального приватного свойства __data.При записи необходимо реализовать
# проверку, что __next будет ссылаться на объект класса StackObj или значение None. Если проверка не проходит,
# то __next остается без изменений.Класс Stack предполагается использовать следующим образом:
# st = Stack() # создание объекта односвязного спискаВ объектах класса Stack должен быть локальный публичный атрибут:
# top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).
# А в самом классе Stack следующие методы:
# push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
# get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data
# каждого объекта в порядке их добавления, или пустой список, если объектов нет).

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            # if isinstance(next, (StackObj, type(None))):
            self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if self.tail:
            self.tail.next = obj
        self.tail = obj
        if not self.top:
            self.top = obj

    def pop(self):
        data = self.top
        if data is None:
            return
        while data and data.next != self.tail:
            data = data.next
        if data:
            data.next = None
        last = self.tail  # извлечение последнего объекта перед удалением
        self.tail = data

        if self.tail is None:
            self.top = None
        return last

    def get_data(self):
        lst = []
        h = self.top
        while h:
            lst.append(h.data)
            h = h.next
        return lst


###############################################################
class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
            self.top.next = None
        else:
            self.tail.next = obj
        self.tail = obj
        self.tail.next = None

    def pop(self):
        d = self.tail
        if self.top == self.tail:
            self.top = None
        else:
            n = self.top
            while n.next.next != None:
                n = n.next
            n.next = None
            self.tail = n
        return d


################################################################
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if any((isinstance(obj, StackObj), obj is None)):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):  # при добавлении нового элемента
        if not self.top:  # если отсутствует головной элемент
            self.top = obj  # присваиваем объект в переменную головного элемента
        else:  # иначе (если имеется головной элемент)
            mark = self.top  # вспомогательной переменной присваиваем значение топ
            while mark.next:  # пока у текущего значения вспомогательной переменной есть ссылка на след. элемент
                mark = mark.next  # присваиваем вспомогательной переменной след. элемент (доходим до крайнего эл)
            mark.next = obj  # если больше нет ссылок на следующий элемент, присваиваем этому атрибуту объект

    def pop(self):  # при изъятии элемента
        if not self.top:  # если отсутствует головной элемент (значит ни один элемент не был добавлен)
            return  # выход из метода
        if not self.top.next:  # если у головного элемента нет следующего(в списке только один элемент)
            poper = self.top  # вспомогательной переменной присваиваем значение топ
            self.top = None  # само значение топ меняем на None (удаляем из списка)
            return poper  # возвращаем изъятое значение
        else:  # иначе (если есть следующий элемент)
            mark = self.top  # вспомогательной переменной присваиваем значение топ
            while mark.next.next:  # пока у следующего значения есть следующее значение
                mark = mark.next  # вспомогательная переменная становвится следующим значением (нашли предпоследний эл)
            poper = mark.next  # определяем переменную для возврата последнего элемента
            mark.next = None  # удаляем последний элемент
            return poper  # возвращаем последний элемент

    def get_data(self):
        data = []  # заводим пустой список
        mark = self.top  # отмечаем начало списка
        while mark:  # пока существует текущий элемент
            data.append(mark.data)  # добавляем его данные в список
            mark = mark.next  # переходим к следующему элементу у текущего
        return data  # как только текущий элемент == None - выход из цикла, возвращаем список данных


###############################################################
class StackObj:
    """ для описания объектов стека """

    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        if type(next_) is StackObj or not next_:
            self.__next = next_

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @classmethod
    def check_data(cls, data):
        pass


class Stack:
    """ для управления стек-подобной структурой """

    def __init__(self):
        self.top = None

    def push(self, obj):
        """ Если стэк пустой - просто добавляем элемент.
        Если не пустой - проходимся по стэку, ищем последний элемент и вставляем после него новый"""
        if not self.top:
            self.top = obj
            return
        tmp = self.top
        while tmp.next:
            tmp = tmp.next
        tmp.next = obj

    def pop(self):
        """ Если стэк пуст - ничего не делаем с ним
         Если в стэке 1 элемент, удалвяем его
         Если больше одного - ищем предпоследний и у него свойство __next устанавливаем в None"""
        if not self.top:
            return
        if not self.top.next:
            self.top = None
            return
        tmp1 = self.top
        tmp2 = self.top.next
        while tmp2.next:
            tmp1, tmp2 = tmp2, tmp2.next
        tmp1.next = None
        return tmp2

    def get_data(self):
        """ проходим по всему стэку и добавляем в список res значение data каждого объекта стэка """
        res = []
        tmp = self.top
        if self.top:
            while tmp.next:
                res.append(tmp.data)
                tmp = tmp.next
            else:
                res.append(tmp.data)
        return res


###############################################################
# Подвиг 7. Объявите класс RadiusVector2D, объекты которого должны создаваться командами:
# В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:
# __x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).
# В классе RadiusVector2D необходимо объявить два объекта-свойства:
# x - для изменения и считывания локального атрибута __x;y - для изменения и считывания локального атрибута __y.
# При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
# - значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
# Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0).
# Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.
# Также в классе RadiusVector2D необходимо объявить статический метод:norm2(vector) -  для вычисления квадратической
# нормы vector - переданного объекта класса RadiusVector2D (квадратическая норма вектора: x*x + y*y).

class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @classmethod
    def __is_verify(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    # лучше вместо isinstance(x, (int, float)) проверять через type(x) in (int, float). Иначе у Вас пройдёт проверку
    #  булевая переменная, т.к. её тип наследуется от int.

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__is_verify(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__is_verify(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return (vector.x * vector.x) + (vector.y * vector.y)


################################################################################################
# Большой подвиг 8. Требуется реализовать программу по работе с решающими деревьями:Здесь в каждом узле дерева делается
# проверка (задается вопрос). Если проверка проходит, то осуществляется переход к следующему объекту по левой стрелке
# (с единицей), а иначе - по правой стрелке (с нулем). И так до тех пор, пока не дойдем до одного из листа дерева
# (вершины без потомков).В качестве входных данных используется вектор (список) с бинарными значениями:
# 1 - да, 0 - нет. Каждый элемент этого списка соответствует своему вопросу (своей вершине дерева), например:
# Далее, этот вектор применяется к решающему дереву, следующим образом. Корневая вершина "Любит Python" с ней связан
# первый элемент вектора x и содержит значение 1, следовательно, мы переходим по левой ветви. Попадаем в вершину
# "Понимает ООП". С ней связан второй элемент вектора x со значением 0, следовательно, мы переходим по правой ветви и
# попадаем в вершину "будет кодером". Так как эта вершина конечная (листовая), то получаем результат в виде строки
# "будет кодером". По аналогии выполняется обработка вектора x с другими наборами значений 0 и 1.Для реализации
# решающих деревьев в программе следует объявить два класса:
# TreeObj - для описания вершин и листьев решающего дерева;
# DecisionTree - для работы с решающим деревом в целом.В классе DecisionTree должны быть реализованы (по крайне мере)
# два метода уровня класса (@classmethod):def predict(cls, root, x) - для построения прогноза
# (прохода по решающему дереву) для вектора x из корневого узла дерева root.
# def add_obj(cls, obj, node=None, left=True) - для добавления вершин в решающее дерево (метод должен возвращать
# добавленную вершину - объект класса TreeObj);В методе add_obj параметры имеют, следующие значения:
# obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
# node - ссылка на объект дерева, к которому присоединяется вершина obj;left - флаг, определяющий ветвь дерева
# (объекта node), к которой присоединяется объект obj (True - к левой ветви; False - к правой).В классе TreeObj
# следует объявить инициализатор:def __init__(self, indx, value=None): ...где indx - проверяемый в вершине дерева
# индекс вектора x; value - значение, хранящееся в вершине (принимает значение None для вершин, у которых есть потомки
# - промежуточных вершин).При этом, в каждом создаваемом объекте класса TreeObj должны автоматически появляться
# следующие локальные атрибуты:indx - проверяемый индекс (целое число);value - значение с данными (строка);
# __left - ссылка на следующий объект дерева по левой ветви (изначально None);__right - ссылка на следующий объект
# дерева по правой ветви (изначально None).Для работы с локальными приватными атрибутами __left и __right необходимо
# объявить объекты-свойства с именами left и right.

class TreeObj:
    """для описания вершин и листьев решающего дерева;"""

    def __init__(self, indx, value=None):
        """ indx - проверяемый в вершине дерева индекс вектора x;
        value - значение, хранящееся в вершине
        (принимает значение None для вершин, у которых есть потомки - промежуточных вершин)."""
        self.indx = indx
        self.value = value
        self.left = None
        self.right = None

    @property
    def left(self):
        """__left - ссылка на следующий объект дерева по левой ветви (изначально None);"""
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class DecisionTree:
    """для работы с решающим деревом в целом."""

    @classmethod
    def predict(cls, root, x):
        """для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root"""
        # DecisionTree.predict(root, [1, 1, 0])
        if x[0] == 1:
            c = root.left
            if x[1] == 1:
                return c.left.value  # [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
            else:
                return c.right.value
        else:
            c = root.right
            if x[2] == 1:
                return c.left.value
            else:
                return c.right.value
        # var_2
        current = root
        while current.value == None:
            if x[current.indx]:
                current = current.left
            else:
                current = current.right
        return current.value

        # var_3
        current = root
        while not current.value:
            current = current.left if x[current.indx] == 1 else current.right
        return current.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """для добавления вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj)
            obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
            node - ссылка на объект дерева, к которому присоединяется вершина obj; предыдущий объект
            left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj
            (True - к левой ветви; False - к правой)."""

        # DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
        if node:
            if left:  # left=True
                node.left = obj  # v_11         ###- value : "будет программистом" / "будет кодером"
            else:
                node.right = obj  # v_12        ###- value : "не все потеряно" / "безнадежен"
        return obj


root = DecisionTree.add_obj(TreeObj(0))  # root
v_11 = DecisionTree.add_obj(TreeObj(1), root)  # v_11
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)  # v_12
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)  # будет программистом
print(res)

assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree,
                                                    'predict'), "в классе DecisionTree должны быть методы add_obj и predict"

assert type(TreeObj.left) == property and type(
    TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"


################################################################################################
class DecisionTree:  # var_3

    @classmethod
    def predict(cls, root, x):
        current = root
        while not current.value:
            current = cls.get_next(current, x)
        return current.value

    @classmethod
    def get_next(cls, current, x):
        if x[current.indx] == 1:
            return current.left
        return current.right

    ################################################################################################
    class DecisionTree:
        @classmethod
        def predict(cls, root, x):
            current = root
            while current is not None:
                left, right = current.left, current.right

                # if not (left and right):
                if left is None or right is None:
                    break
                current = current.left if x[current.indx] else current.right
            return current.value

        @classmethod
        def add_obj(cls, obj, node=None, left=True):
            if node:
                setattr(node, 'left' if left else 'right', obj)  # settatr(obj,name,value)
            return obj


################################################################################################
class DecisionTree:
    STEP = {1: 'left', 0: 'right'}

    @classmethod
    def predict(cls, root, x):
        node = root
        while node.indx != -1:
            node = getattr(node, cls.STEP[x[node.indx]])
        return node.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            setattr(node, cls.STEP[left], obj)
        return obj
################################################################################################
#Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных
# сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса
# будут формироваться командой:line = LineTo(x, y)где x, y - следующая координата линейного участка (начало маршрута
# из точки 0, 0).В каждом объекте класса LineTo должны формироваться локальные атрибуты:
# x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).
# Объекты класса PathLines должны создаваться командами:p = PathLines()  начало маршрута из точки 0, 0
# p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
# где line1, line2, ... - объекты класса LineTo.Сам же класс PathLines должен иметь следующие методы:
# get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
# get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
# add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
# Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента
# определяется как евклидовое расстояние по формуле:L = sqrt((x1-x0)^2 + (y1-y0)^2)где x0, y0 - предыдущая точка
# маршрута; x1, y1 - текущая точка маршрута.

import math


class PathLines:
    def __init__(self, *args):
        self.lines = [LineTo(0, 0)] + [*args]

    def get_path(self):
        return self.lines

    def get_length(self):
        L = 0
        for i in range(len(self.lines) - 1):
            L += math.sqrt(
                pow((self.lines[i + 1].x - self.lines[i].x), 2) + pow((self.lines[i + 1].y - self.lines[i].y), 2))
        return L

    def add_line(self, line):
        self.lines.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
###############################################################
class PathLines:
    def __init__(self, *args):
        self.lines = list((LineTo(0, 0),) + args)

    def get_path(self):
        return self.lines

    def get_length(self):
        gen_turple = ((self.lines[i], self.lines[i + 1]) for i in range(len(self.lines) - 1))
        return sum(map(lambda g: ((g[1].x - g[0].x) ** 2 + (g[1].y - g[0].y) ** 2) ** 0.5, gen_turple))

    def add_line(self, line):
        self.lines.append(line)


###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
