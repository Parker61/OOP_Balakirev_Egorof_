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


########################################################################
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


# >>> person = Person('Jack', 33)
# >>> # Считываем значения
# >>> person.name
# Jack
# >>> person.age
# 33
# >>> # Пытаемся записать новое значение
# >>> person.age = 42
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
        self.side = side

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


###############################################################################################

###############################################################
####################################################################################

###############################################################

###############################################################################################

###################################################################################################################################################

###############################################################

###############################################################################################

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
###############################################################

################################################################

###############################################################
###############################################################

################################################################

###############################################################
