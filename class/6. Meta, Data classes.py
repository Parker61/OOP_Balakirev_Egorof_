##____________33. Вложенные классы ________________________________________________________________
class Women:
    title = 'object with attributes'
    photo = 'object with attributes'
    ordering = 'ordering'

    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        self.meta = self.Meta(user + '@+' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self.access = access


w = Women('root', '1234')
print(w.__dict__)
print(w.Meta.__dict__)
# {'user': 'root', 'psw': '1234', 'meta': <__main__.Women.Meta object at 0x000001E944C68750>}
# {'__module__': '__main__', 'ordering': ['id'], '__init__': <function Women.Meta.__init__ at 0x000001E944C5E020>,
# '__dict__': <attribute '__dict__' of 'Meta' objects>, '__weakref__': <attribute '__weakref__' of 'Meta' objects>,
# '__doc__': None}


# ___Metaclasses________________________________
A = type('Point', (), {'Max': 100, 'Min': 0})


# аналогично как
class Point:
    Max = 100
    Min = 0


################################################################
def method1(self):
    print(self.__dict__)


A = type('Point', (), {'Max': 100, 'method1': method1})
pt.A()


################################################################
# создание метакласса с помощью функции (редко)


def create_class(name, base_class, attributes):
    attributes.update({'Max': 100, 'Min': 0})
    return type(name, base_class, attributes)


class Point(metaclass=create_class):
    def get_coordinates(self):
        return (0, 0)


pt = Point()
print(pt.Max)  # 100
print(pt.get_coordinates())  # (0, 0)


################################################################
# создание метакласса с помощью класса


class Meta(type):
    def __new__(cls, name, base, attributes):  # ч/з __new__ для более тонкой работы
        attributes.update({'Max': 100, 'Min': 0})
        return type.__new__(cls, name, base, attributes)

    # def __init__(cls, name, base, attributes):
    #     super().__init__(name, base, attributes)
    #     cls.Max = 100
    #     cls.Min = 0


class Point(metaclass=Meta):
    def get_coordinates(self):
        return (0, 0)


pt = Point()
print(pt.Max)  # 100
print(pt.get_coordinates())  # (0, 0)


################################################################
# Метаклассы в API ORM Django

class Meta(type):
    def create_local_attributes(self, *args, **kwargs):
        for key, value in self.class_attributes.items():
            self.__dict__[key] = value

    def __init__(cls, name, base, attributes):
        cls.class_attributes = attributes
        cls.__init__ = Meta.create_local_attributes


class Women(metaclass=Meta):
    title = 'title'
    content = 'content'
    photo = 'photo'


w = Women()
print(w.__dict__)


# {'__module__': '__main__', '__qualname__': 'Women', 'title': 'title', 'content': 'content', 'photo': 'photo'}
################################
# Data Classes
@dataclass
class Point:
    x: (int, float)
    y: (int, float)


################################################################
@dataclass
class InventoryItem:
    name: str
    price: float = 9.99  # значения по умолчанию для атрибута прямо в классе.
    quantity: int = 1


# Обязательные атрибуты в классе должны перечисляться вверху, затем должны идти необязательные.

desk = InventoryItem('Computer desk', 1000, 12)
pen = InventoryItem('Pen')
monitor = InventoryItem('Monitor', 300)
clock = InventoryItem('Clock', quantity=10)


################################################################
##если вы не хотите добавлять явный тип в указание атрибута, то используйте typing.Any:
@dataclass
class A:
    name: Any
    value: Any = 42


val1 = A(32, 'hello')
val2 = A([2, 3, 'hello'], {4, 3, 2})


# Но вы должны понимать, что аннотация типов не гарантирует, что будет передаваться именно данный тип в ваш класс
# Аннотации полезны для информирования другого программиста об ожидаемом типе, так аннотации подсказывают вашей IDE о
# типе переменной. Гарантировать определенный тип аннотации могут в паре с использованием пакета mypy
@dataclass
class Customer:
    name: str
    balance: int


cust1 = Customer(32, 'hello')
cust2 = Customer([2, 3, 'hello'], {4, 3, 2})
# никаких ошибок не произошло
################################################################
# вы можете свободно добавлять свои собственные методы в dataclass.
from dataclasses import dataclass


@dataclass
class InventoryItem:
    name: str
    price: float = 9.99
    quantity: int = 1

    def total_cost(self) -> float:
        return self.price * self.quantity


desk = InventoryItem('Desk', 1000, 12)
print(desk.total_cost())
################################################################
from dataclasses import dataclass, field


class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f'Thing: {self.__dict__})'


@dataclass
class ThingsDataClass:
    name: str  # анонсируется какой тип данных будет, если не писать : str , то он пропускается
    weight: float
    price: int
    dims: field(default_factory=list)  # создаётся инициализатор и внутри этого инициализатора создаётся локальное
    # свойство dims и оно присваивается функции list, а list возвращает пустой список, Т.О. для каждого объекта
    # создаётся свой список который будет пустым. Только так можно прописывать изменяемые параметры по умолчанию


t = Thing('name', 'weight', 'price')
t.dims.append(10)
print(t)

t2 = ThingsDataClass('name', 'weight', 'price')
print(t2.dims)


########################################################################
# @dataclass c параметрами по умолчанию
# init: по умолчанию принимает значение True. Это означает, что для вашего dataclass будет генерироваться метод __init__
# . Если передадите False, у вашего класса реализации метода __init__  не будет.
# repr: по умолчанию принимает значение True. Это означает, что для вашего dataclass будет генерироваться метод
# __repr__ . Если передадите False, у вашего класса реализации метода __repr__  не будет.
# eq : по умолчанию принимает значение True. Это означает, что для вашего dataclass будет генерироваться метод
# __eq__ . Если передадите False, у вашего класса реализации метода __eq__  не будет.
# order: по умолчанию принимает значение False . Это означает, что для вашего dataclass не будут генерироваться
# расширенные методы сравнения __gt__ , __ge__, __lt__, __le__ . Если передадите True, у вашего класса реализации всех
# этих методов появиться
# unsafe_hash:  по умолчанию принимает значение False . Это означает, что для вашего dataclass не будет генерироваться
# метод __hash__ . Если передадите True, у вашего класса реализации метода __hash__ появится.
# frozen: по умолчанию принимает значение False . Это означает, что атрибуты экземпляра вашего dataclass являются
# изменяемыми. Если передадите True, то потеряете возможность менять атрибуты

# order=True автоматически генерировать методы сравнения для операций < , =, >, <=, >=.
# Есть особенность использования order=True.Она заключается в том, что при сравнении будут использоваться все атрибуты
# класса, что не всегда полезно. Автоматически сгенерированные методы сравнения будут сравнивать следующие кортежи
# экземпляров между собой:
# Но вы можете повлиять на поля, которые буду участвовать в этих сравнениях при помощи dataclasses.field
@dataclass(order=True)
class User:
    name: str = field(compare=False)
    age: int
    rating: float


# При помощи field(compare=False) мы исключаем атрибут name из кортежа сравнений. Теперь наши пользователи в первую
# очередь сравниваются по возрасту, а уже потом по рейтингу. Вот это уже то, что нам нужно!)

################################
# Enum: работаем с перечислениями
# Иногда в коде возникает необходимость создать объект(тип данных), значения которого находятся в небольшом но
# фиксированном и постоянном списке. Например, день недели может принимать всегда только одно из семи значений.
# Enum позволяет создавать наборы семантически связанных констант, доступ к которым можно получить через само
# перечисление. В Python нет специального синтаксиса для перечислений. Однако в стандартной библиотеке Python есть
# модуль enum, поддерживающий перечисления через класс Enum.

from enum import Enum
from pprint import pprint


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


pprint(list(Weekday))
# pprint позволяет выводить длинные типы данных в удобочитаемом виде.Функция pprint, импортированная из модуля
# pprint (pretty print), используется для красивого и читаемого вывода структур данных в Python. Она форматирует вывод,
# чтобы он был более организованным и легким для восприятия.
################################
# Перед вами перечисление Direction.Распечатайте на первой строке имя атрибута WEST, а на второй строке значение
# атрибута SOUTH
from enum import Enum


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


print(Direction.WEST.name)  # WEST
print(Direction.SOUTH.value)  # S
################################################################
# Создайте перечисление Size, в котором хранятся размеры одежды:#
# S - small
# M - medium
# L - large
# XL - extra large
# XXL - extra extra large
# В списке сперва указаны названия атрибута, затем его строковое значение
#  Ваша задача написать только определения класса Size
from enum import Enum

class Size(Enum):
    S = "small"
    M = "medium"
    L = "large"
    XL = "extra large"
    XXL = "extra extra large"
################################
from dataclasses import dataclass, field, InitVar


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len=True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0  # вычисляемое свойство


# объявление класса ч/з декоратор
@dataclass
class V3D:
    x: int = field(repr=False)  # исключить из __repr__
    y: int
    z: int = field(compare=False)  # исключить из сравнения в методе __eq__
    calc_len: InitVar[bool] = True
    # все атрибуты анонсированные классом InitVar попадаю в __post_init__
    # эквивалентно self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0
    #
    # чтобы можно было вывести вычисляемый атрибут self.length из метода __post_init__ при вызове __repr__:
    length: float = field(init=False, compare=False, default=0)

    # означает что length нельзя добавлять как параметр в инициализатор

    def __post_init__(self, calc_len: bool):  # инициализатор в конце своей работы вызывает этот метод
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v)  # формируется __repr__ автоматически из @dataclass


# V3D(y=2, z=3, length=3.7416573867739413)
################################################################
# @dataclass c изменяемыми параметрами

# @dataclass(init=False)  # не будет формироваться инициализатор для формирование базового класса
# @dataclass(repr=False, eq=False)  # __repr__ не выводить, исключается __eq__
# @dataclass(order=False) # исключается метод сравнения >=/<= __lt__..
@dataclass(frozen=True)  # замораживает значения атрибутов и  нельзя их менять, поэтому  self.length буде default=0
class V3D:
    x: int = field(repr=False)
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)


# с параметром frozen — отличный способ для хранения:констант,настроек
# Но имейте в виду, что если ваш dataclass содержит изменяемые атрибуты, они все равно могут измениться
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class InventoryItem:
    name: str
    price: float = 9.99
    quantity: int = 1


@dataclass(frozen=True)
class ProgramStaff:
    items: List[InventoryItem]


# это не list=список обычный, а импорт из библиотеки typing типа List. Он как раз и является явной аннотацией типа.
# Т.е ожидается что в переменную должен поступить список
# к тому же список, состоящий из экземпляров класса InventoryItem

desk = InventoryItem('Desk', 1000, 12)
monitor = InventoryItem('Monitor', quantity=2)

staff = ProgramStaff([desk, monitor])
print(staff)
print(staff.items[1])
staff.items[1] = InventoryItem('Pen')
print(staff)
################################################################
# Data Classes при наследовании
from dataclasses import dataclass, field
from typing import Any


class GoodMethodFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0  # не анонсирован никаким типом значит декоратор при инициализации его пропустит
    uid: int = field(init=False)  # исключили из инициализации
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Good: post_init")
        Goods.current_uid += 1
        self.uid = Goods.current_uid  # теперь uid автоматически формир-ся при создании нового объекта


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodMethodFactory.get_init_measure)

    def __post_init__(self):
        super().__post_init__()
        print('Book post init')


b = Book(1000, 100, 'Pythons', 'Book')
print(b)
# Good: post_init
# Book post init
# Book(uid=1, price=1000, weight=100, title='Pythons', author='Book', measure=[0, 0, 0])
################################################################
# создание класса ч/з Функцию make_dataclass()
# когда нужно сформировать класс данных в процессе работы программы, поэтому лучше использовать декоратор
from dataclasses import make_dataclass, field


class Car:
    def __init__(self, model, max_speed, prrice):
        self.model = model
        self.max_speed = max_speed
        self.price = prrice

    def get_max_speed(self):
        return self.max_speed


CarData = make_dataclass("CarData", [('model', str),
                                     'max_speed',
                                     ('price', float, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.get_max_speed})

c = CarData('BMV', 256, 4096)
print(c)  # CarData(model='BMV', max_speed=256, price=4096)
print(c.get_max_speed())  # 256
