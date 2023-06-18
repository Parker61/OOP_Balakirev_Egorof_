# _______________bool________________Egorof______

# магический метод __bool__ так, чтобы он возвращал False ,если название города заканчивается на любую гласную букву
# латинского алфавита (a, e, i, o, u), в противном случае True
class City:
    def __init__(self, name):
        self.name = ' '.join(list(map(str.capitalize, name.split())))

    def __str__(self):
        return f'{self.name}'

    def __bool__(self):
        return self.name[-1] not in 'aeiou'
        # return not any(self.name.endswith(i) for i in 'aeiou')


################################################################
# Сейчас вам нужно создать класс Quadrilateral(четырехугольник), в котором есть:метод __init__. Он должен сохранять в
# экземпляр класса два атрибута: width и height. При этом в сам метод __init__ может передаваться один аргумент(тогда
# в width и height присваивать это одно одинаковое значение, тем самым делать квадрат), либо два аргумента( первый идет
# в атрибут width, второй - в height)метод __str__ , который работает следующим образом: если width и height одинаковые
# , возвращать строку «Квадрат размером <width>х<height>»в противном случае, возвращать строку «Прямоугольник
# размером <width>х<height>»переопределить метод __bool__ так, чтобы он возвращал True, если объект является
# квадратом, и False в противном случае
class Quadrilateral:
    def __init__(self, *args):

        if len(args) == 2:
            self.width = args[0]
            self.height = args[1]
        else:
            self.width = self.height = args[0]

    def __str__(self):
        if self.__bool__():
            return f'Квадрат размером {self.width}х{self.height}'
        return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height


################################################################
class Quadrilateral:
    def __init__(self, width, height=None):
        self.width, self.height = width, height if height else width

    def __str__(self):
        return f"{['Прямоугольник', 'Куб'][bool(self)]} размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height


########################################################################
class Quadrilateral:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height or width

    # логика такая:для or:
    # Выбирается первое значение, которое при преобразовании к bool даст True
    # Если таких значений нет, то вернётся первое не None значение
    # Если оба None, то вернёт None
    # для and:
    # Если в одном из двух значений есть None, то вернёт None
    # Если None нет, то выбирается первое значение, которое при преобразовании к bool даст False
    # Если таких нет, то выбирается второе значение
    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.height}'
        return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height


################################################################
class Quadrilateral:

    def __init__(self, width, height=None):
        if height is None:
            height = width
        self.width = width
        self.height = height

    def __str__(self):
        return f'Квадрат размером {self.width}х{self.height}' if self.width == self.height \
            else f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return str(self).startswith('К')


# _____________________Balakirev________________________________________________________________
# Подвиг 4. Объявите в программе класс Player (игрок), объекты которого создаются командой:
# player = Player(name, old, score)где name - имя игрока (строка); old - возраст игрока (целое число);
# score - набранные очки в игре (целое число). В каждом объекте класса Player должны создаваться аналогичные локальные
# атрибуты: name, old, score.С объектами класса Player должна работать функция:bool(player)которая возвращает True,
# если число очков больше нуля, и False - в противном случае.С помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))считываются строки из входного потока в список строк lst_in.
# Каждая строка записана в формате:"имя; возраст; очки"Например:Балакирев; 34; 2048Mediel; 27; 0Влад; 18; 9012
# Nina P; 33; 0Каждую строку списка lst_in необходимо представить в виде объекта класса Player с соответствующими
# данными. И из этих объектов сформировать список players.Отфильтруйте этот список (создайте новый: players_filtered),
# оставив всех игроков с числом очков больше нуля. Используйте для этого стандартную функцию filter() совместно
# с функцией bool() языка Python.
class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.score = int(score)
        self.old = old

    def __bool__(self):
        return self.score > 0


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Балакирев; 34; 2048', 'Mediel; 27; 0', 'Влад; 18; 9012', 'Nina P; 33; 0']

players = [Player(*item.split(';')) for item in lst_in]
players_filtered = list(filter(lambda x: bool(x), players))  # 2 objects
players_filtered = list(filter(bool, players))  # 2 objects
###############################################################################################################################################
players_filtered = list(filter(None, players))


# 'Если функция None, то все элементы iterablу, которые являются ложными - удаляются'
########################################################################

class RestrictedTypeValue:
    def __init__(self, *args, condition=lambda x: True, message="Неверный тип данных."):
        self.__types = args
        self.condition = condition
        self.message = message

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        if instance == None:
            return property()
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        check_1, check_2 = (type(value) in self.__types), (self.condition(value))
        if not (check_1 and check_2):
            raise ValueError(self.message)
        instance.__dict__[self.name] = value


class Player:
    name = RestrictedTypeValue(str)
    old = RestrictedTypeValue(int)
    score = RestrictedTypeValue(int)

    def __init__(self, name, old, score) -> None:
        self.name = name
        self.old = old
        self.score = score

    def __str__(self):
        return f'{self.name}; {self.old}; {self.score}'

    def __bool__(self):
        return self.score > 0


players = []
for w in lst_in:
    name, old, score = w.split(';')
    players.append(Player(name, int(old), int(score)))
players_filtered = list(filter(bool, players))
########################################################################
# Подвиг 5. Объявите в программе класс MailBox (почтовый ящик), объекты которого создаются командой:
# mail = MailBox()Каждый объект этого класса должен содержать локальный публичный атрибут:
# inbox_list - список из принятых писем.Также в классе MailBox должен присутствовать метод:
# receive(self) - прием новых писемЭтот метод должен читать данные из входного потока командой:
# lst_in = list(map(str.strip, sys.stdin.readlines())) результате формируется список lst_in из строк.
# Каждая строка записана в формате:"от кого; заголовок; текст письма"Например:sc_lib@list.ru; От Балакирева;
# Успехов в IT!mail@list.ru; Выгодное предложение; Вам одобрен кредит.mail123@list.ru; Розыгрыш; Вы выиграли 1 млн.
# руб. Переведите 30 тыс. руб., чтобы его получить.Каждая строчка списка lst_in должна быть представлена объектом
# класса MailItem, объекты которого создаются командой:item = MailItem(mail_from, title, content)
# где mail_from - email отправителя (строка); title - заголовок письма (строка), content - содержимое письма (строка).
# В каждом объекте класса MailItem должны формироваться соответствующие локальные атрибуты (с именами: mail_from, title,
# content). И дополнительно атрибут is_read (прочитано ли) с начальным значением False.В классе MailItem должен быть
# реализован метод:set_read(self, fl_read) - для отметки, что письмо прочитано (метод должен устанавливать атрибут
# is_read = fl_read, если True, то письмо прочитано, если False, то не прочитано).С каждым объектом класса MailItem
# должна работать функция:bool(item)которая возвращает True для прочитанного письма и False для непрочитанного.
# Вызовите метод:mail.receive()Отметьте первое и последнее письмо в списке mail.inbox_list, как прочитанное
# (используйте для этого метод set_read). Затем, сформируйте в программе список (глобальный) с именем
# inbox_list_filtered из прочитанных писем, используя стандартную функцию filter() совместно с функцией bool()

import sys


class MailBox:
    def __init__(self):
        self.inbox_list = []
        self.lst_in = None

    def receive(self):
        # self.lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
                       'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
                       'Python ООП; Балакирев С.М.; 2022',
                       'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
        self.inbox_list = [MailItem(*item.split(';')) for item in self.lst_in]


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        if isinstance(fl_read, bool):
            self.is_read = fl_read

    def __bool__(self):
        return self.is_read


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))

########################################################################
for i in (0, -1):
    mail.inbox_list[i].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
#######################################################################
# Подвиг 6 (релакс). Объявите класс Line, объекты которого создаются командой:line = Line(x1, y1, x2, y2)
# где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2).
# Могут быть произвольными числами. В объектах класса Line должны создаваться соответствующие локальные атрибуты с
# именами x1, y1, x2, y2. классе Line определить магический метод __len__() так, чтобы функция:
# bool(line)# возвращала False, если длина линии меньше 1.
from math import hypot


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return int(hypot(self.x1 - self.x2, self.y1 - self.y2))
        # return int(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5)
        # return False if (pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2)) ** 0.5 < 1 else True


########################################################################
# Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:
# el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2el2 = Ellipse(x1, y1, x2, y2)
# где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла.
# Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2.
# Вторая команда создает объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.
# В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все локальные атрибуты
# x1, y1, x2, y2 существуют и False - в противном случае.Также в классе Ellipse нужно реализовать метод:
# get_coords() - для получения кортежа текущих координат объекта.Если координаты отсутствуют
# (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() должен генерировать исключение командой:
# raise AttributeError('нет координат для извлечения')Сформируйте в программе список с именем lst_geom, содержащий
# четыре объекта класса Ellipse. Два объекта должны быть созданы командой Ellipse()и еще два - командой:
# Ellipse(x1, y1, x2, y2)Переберите список в цикле и вызовите метод get_coords() только для объектов,
# имеющих координаты x1, y1, x2, y2. (Помните, что для этого был определен магический метод __bool__()).
from random import randint


class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def __setattr__(self, key, value):
        if value is not None:  # if value != None:
            object.__setattr__(self, key, value)

    def __bool__(self):
        return hasattr(self, 'x1')
        # return all(hasattr(self, a) for a in ('x1', 'x2', 'y1', 'y2'))

    def get_coords(self):
        # if self.__bool__():
        if self:
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse() for i in range(2)] + [Ellipse(*[randint(0, 20) for _ in range(4)]) for i in range(2)]

for i in lst_geom:
    if bool(i):
        # if i:
        i.get_coords()  # (1, 1, 1, 1) (2, 2, 2, 2)


########################################################################
class Ellipse:
    __slots__ = ('x1', 'y1', 'x2', 'y2')

    def __init__(self, *args):
        [setattr(self, name, args[id]) for id, name in enumerate(self.__slots__) if len(args) == len(self.__slots__)]

    def __bool__(self): return all(
        map(lambda v: isinstance(v, int), (getattr(self, name, None) for name in self.__slots__)))

    def get_coords(self):
        if self: return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(*params) for params in ((), (), (1, 2, 3, 4), (9, 8, 7, 6))]
[geom.get_coords() for geom in lst_geom if geom]


#######################################################################
class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return bool(self.__dict__)

    def get_coords(self):
        if not self:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]

for obj in lst_geom:
    if obj:
        obj.get_coords()


########################################################################
class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return len(self.__dict__) == 4

    def get_coords(self):
        if self:
            return tuple((item for item in self.__dict__.values()))
        raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 1, 1), Ellipse(1, 1, 1, 1)]
for geom in lst_geom:
    if geom:
        geom.get_coords()


###############################################################################################################################################
class Ellipse:
    NAME_COORDS = ('x1', 'y1', 'x2', 'y2')

    def __init__(self, *args):
        [setattr(self, key, val) for key, val in zip(self.NAME_COORDS, args)]

    def __bool__(self):
        return sum(map(lambda x: hasattr(self, x), self.NAME_COORDS)) == 4

    def get_coords(self):
        if bool(self):
            return tuple(getattr(self, key) for key in self.NAME_COORDS)
        raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(i, i, i + 2, i + 2) if i % 2 else Ellipse() for i in range(4)]

lst_geom_coords = [item.get_coords() for item in lst_geom if bool(item)]
lst_geom_coords = [item.get_coords() for item in filter(bool, lst_geom)]
lst_geom_coords = [*map(lambda x: x.get_coords(), filter(bool, lst_geom))]


########################################################################
# Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, x3,..., xN)где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).
# С каждым объектом класса Vector должны выполняться операторы:v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторовv1 * v2 # умножение соответствующих координат векторов
# v1 += 10 # прибавление ко всем координатам вектора числа 10v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1
# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
# При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными)
# координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться
# исключение командой:raise ArithmeticError('размерности векторов не совпадают')
class Vector:
    def __init__(self, *args):
        self.v = list(args)

    def __is_check(self, other):
        if len(other.v) != len(self.v) and isinstance(other, Vector):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        if self.__is_check(other):
            return Vector(*[val + other.v[i] for i, val in enumerate(self.v)])
            # return Vector(sum(*zip(self.v, other.v)))

    def __sub__(self, other):
        if self.__is_check(other):
            return self.__class__(*(val - other.v[i] for i, val in enumerate(self.v)))

    def __mul__(self, other):
        if self.__is_check(other):
            return self.__class__(*[val * other.v[i] for i, val in enumerate(self.v)])

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.v = list(i + other for i in self.v)
        elif self.__is_check(other):
            self.v = list(val + other.v[i] for i, val in enumerate(self.v))
        return self

    def __isub__(self, other):
        if type(other) in (int, float):
            self.v = list(i - other for i in self.v)
        elif self.__is_check(other):
            self.v = list(val - other.v[i] for i, val in enumerate(self.v))
        return self

    def __radd__(self, other):
        if self.__is_check(other):
            return self + other

    def __rsub__(self, other):
        if self.__is_check(other):
            return self - other

    def __eq__(self, other):
        if self.__is_check(other):
            return self.v == other.v


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).v)  # [5, 7, 9]
print((v1 - v2).v)  # [-3, -3, -3]
print((v1 * v2).v)  # [4, 10, 18]
v1 += 10
print(v1.v)  # [11, 12, 13]
v1 -= 10
print(v1.v)  # [1, 2, 3]
v1 += v2
print(v1.v)  # [5, 7, 9]
v2 -= v1
print(v2.v)  # [-1, -2, -3]
print(v1 == v2)  # False
print(v1 != v2)  # True

########################################################################
import operator as op


class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __do(self, other, f_name, new_object=True):
        if isinstance(other, self.__class__) and len(other) == len(self):
            new_coords = (f_name(a, b) for a, b in zip(self.coords, other.coords))
        elif isinstance(other, (int, float)):
            new_coords = (f_name(b, other) for b in self.coords)
        else:
            raise ArithmeticError('размерности векторов не совпадают')
        if new_object:
            return self.__class__(*new_coords, )
        else:
            self.coords = (*new_coords,)
            return self

    def __add__(self, other):
        return self.__do(other, op.add)

    def __sub__(self, other):
        return self.__do(other, op.sub)

    def __mul__(self, other):
        return self.__do(other, op.mul)

    def __iadd__(self, other):
        return self.__do(other, op.add, False)

    def __isub__(self, other):
        return self.__do(other, op.sub, False)

    def __imul__(self, other):
        return self.__do(other, op.mul, False)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.coords == other.coords
        raise TypeError('Сравнение векторов не возможно!')


########################################################################
from operator import sub, add, mul


class Vector:

    def __init__(self, *args):
        self.args = args

    @staticmethod
    def check_len(self, other):
        if not type(other) == int and len(self.args) != len(other.args):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __sub__(self, other):
        self.check_len(self, other)
        other = other.args if isinstance(other, Vector) else [other for i in range(other)]
        return Vector(*map(lambda x: sub(*x), zip(self.args, other)))

    def __add__(self, other):
        self.check_len(self, other)
        other = other.args if isinstance(other, Vector) else [other for i in range(other)]
        return Vector(*map(lambda x: add(*x), zip(self.args, other)))

    def __mul__(self, other):
        self.check_len(self, other)
        other = other.args if isinstance(other, Vector) else [other for i in range(other)]
        return Vector(*map(lambda x: mul(*x), zip(self.args, other)))

    def __eq__(self, other):
        return self.args == other.args


#######################################################################
class Vector:
    def __init__(self, *vector):
        self.vector = [*vector]

    def __math(self, other, sign):
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ArithmeticError('размерности векторов не совпадают')
            vector = f"[i{sign}j for i,j in zip({getattr(self, 'vector')},{getattr(other, 'vector')})]"
            # Функция getattr() в Python, значение атрибута по имени
        else:
            vector = f"[i{sign}{other} for i in {getattr(self, 'vector')}]"
        return eval(vector)

    def __add__(self, other):
        return Vector(*self.__math(other, '+'))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.vector = self.__math(other, '+')
        return self

    def __sub__(self, other):
        return Vector(*self.__math(other, '-'))

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        self.vector = self.__math(other, '-')
        return self

    def __mul__(self, other):
        return Vector(*self.__math(other, '*'))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.vector = self.__math(other, '*')
        return self

    def __eq__(self, other):
        return self.vector == other.vector


########################################################################
class Vector:
    def __init__(self, *args):
        self.v = args

    def __is_check(self, other, sign):
        if isinstance(other, Vector):
            if len(self.v) != len(other.v):
                raise ArithmeticError('размерности векторов не совпадают')
            # vector = f'[i{sign}j for i, j in zip(self.v, other.v)]'
            vector = f"[i{sign}j for i,j in zip({getattr(self, 'v')},{getattr(other, 'v')})]"
            # Функция getattr() в Python, значение атрибута по имени
        else:
            # vector = f'[i{sign}{other} for i in self.v]'
            vector = f"[i{sign}{other} for i in {getattr(self, 'v')}]"
        return eval(vector)

    def __add__(self, other):
        return Vector(*self.__is_check(other, '+'))

    def __sub__(self, other):
        return Vector(*self.__is_check(other, '+'))

    def __mul__(self, other):
        return Vector(*self.__is_check(other, '+'))

    def __iadd__(self, other):
        self.v = self.__is_check(other, '+')
        return self

    def __isub__(self, other):
        self.v = self.__is_check(other, '+')
        return self

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return self - other

    def __eq__(self, other):
        return self.v == other.v

    def __str__(self):
        return f'{self.v}'


########################################################################
import numpy


class Vector:
    def __init__(self, *args, **kwargs):
        self.points = args

    def check_vector(func):
        def wrapper(self, vector, *args, **kwargs):
            if not (type(vector) in (int, float)):
                if len(vector.points) != len(self.points):
                    raise ArithmeticError('размерности векторов не совпадают')
            return func(self, vector)

        return wrapper

    @check_vector
    def __add__(self, other):
        return Vector(*[i + y for i, y in zip(self.points, other.points)])
        # return Vector(*[sum(i) for i in zip(self.points, other.points)])

    @check_vector
    def __sub__(self, other):
        return Vector(*[i - y for i, y in zip(self.points, other.points)])

    @check_vector
    def __mul__(self, other):
        return Vector(*[i * y for i, y in zip(self.points, other.points)])

    @check_vector
    def __iadd__(self, other):
        if type(other) in (int, float):
            self.points = tuple(numpy.array(self.points) + other)
        else:
            self.points = tuple(numpy.array(self.points) + numpy.array(other.points))
        return self

    @check_vector
    def __isub__(self, other):
        if type(other) in (int, float):
            self.points = tuple(numpy.array(self.points) - other)
        else:
            self.points = tuple(numpy.array(self.points) - numpy.array(other.points))
        return self

    def __eq__(self, other):
        return self and other and self.points == other.points

    def __ne__(self, other):
        return self and other and self.points != other.points

    def __len__(self):
        return len(self.points)


#######################################################################
# Большой подвиг 8. Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым
# полем. Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса Cell и
# содержать либо число мин вокруг этой клетки, либо саму мину.Для начала в программе объявите класс GamePole,
# который будет создавать и управлять игровым полем. Объект этого класса должен формироваться командой:
# pole = GamePole(N, M, total_mines)И, так как поле в игре одно, то нужно контролировать создание только одного объекта
# класса GamePole (используйте паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический
# метод __new__()).Объект pole должен иметь локальный приватный атрибут:__pole_cells - двумерный (вложенный) кортеж,
# размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.Для доступа к этой коллекции
# объявите в классе GamePole объект-свойство (property):pole - только для чтения (получения) ссылки на коллекцию
# __pole_cells.Далее, в самом классе GamePole объявите следующие методы:init_pole() - для инициализации начального
# состояния игрового поля (расставляет мины и делает все клетки закрытыми);open_cell(i, j) - открывает ячейку с
# индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение атрибута __is_open объекта Cell в
# ячейке (i, j) на True;show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение,
# этот метод - домашнее задание).Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно
# воспользоваться функцией randint модуля random). После расстановки всех total_mines мин, вычислите их количество
# вокруг остальных клеток (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).В методе open_cell()
# необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то генерируется исключение
# командой:raise IndexError('некорректные индексы i, j клетки игрового поля')Следующий класс Cell описывает состояние
# одной ячейки игрового поля. Объекты этого класса создаются командой:cell = Cell()При этом в самом объекте создаются
# следующие локальные приватные свойства:__is_mine - булево значение True/False; True - в клетке находится мина,
# False - мина отсутствует;__number - число мин вокруг клетки (целое число от 0 до 8);__is_open - флаг того, открыта
# клетка или закрыта: True - открыта; False - закрыта.Для работы с этими приватными атрибутами объявите в классе Cell
# следующие объекты-свойства с именами:is_mine - для записи и чтения информации из атрибута __is_mine;
# number - для записи и чтения информации из атрибута __number;is_open - для записи и чтения информации из атрибута
# __is_open.В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение
# True/False, либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:
# raise ValueError("недопустимое значение атрибута")С объектами класса Cell должна работать функция:
# bool(cell)которая возвращает True, если клетка закрыта и False - если открыта.

from random import randint


class GamePole:
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = super().__new__(cls)
        return cls.__isinstance

    def __del__(self):
        GamePole.__isinstance = None  # если instance будет уделён

    def __init__(self, N, M, total_mines):  # создается поле размерами 10x20 с общим числом мин 10
        self.N = N
        self.M = M
        self.total_mines = total_mines
        # self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.__pole_cells = [[Cell() for _ in range(M)] for _ in range(N)]
        self.init_pole()  # чтобы проинициилизировать (создать новый объект) ещё раз когда потребуется
        # не создовая новый объект класса GamePole

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for i in self.__pole_cells:  # сбросить состояние поля
            for j in i:
                j.is_open = False
                j.is_mine = False
        m = 0
        while m < self.total_mines:
            i = randint(0, self.N - 1)  # возвращает случайное целое число i из интервала a <= i <= b.
            j = randint(0, self.M - 1)
            if self.pole[i][j].is_mine:
                continue
            self.__pole_cells[i][j].is_mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.N):
            for y in range(self.M):
                if not self.pole[x][y].is_mine:
                    mines = sum(
                        self.pole[x + i][y + j].is_mine for i, j in indx if 0 <= x + i < self.N and 0 <= y + j < self.M)
                    self.pole[x][y].number = mines

    def open_cell(self, i, j):
        if not 0 <= i < self.N or not 0 <= j <= self.M:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))


class Cell:
    def __init__(self):
        self.__is_mine = False  # True - в клетке находится мина, False - мина отсутствует;
        self.__number = 0  # число мин вокруг клетки (целое число от 0 до 8);
        self.__is_open = False  # True - открыта; False - закрыта.

    def __bool__(self):
        return not self.__is_open  # True клетка закрыта и False -  открыта.

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if value > 8 or value < 0 or type(value) != int:
            # if not (0 < value < 8) or type(value) != int: - так не работает почемуто ???
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value


pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
########################################################################
from random import sample as S


class D:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, obj, owner):
        if obj is None:
            return property()
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        namedct = {'__is_mine': type(value) == bool,
                   '__number': type(value) == int and value in range(0, 9),
                   '__is_open': type(value) == bool}
        if not self.name in namedct:
            setattr(obj, self.name, value)
        elif namedct[self.name]:
            setattr(obj, self.name, value)
        else:
            raise ValueError("недопустимое значение атрибута")


class GamePole:
    pole_cells = D()
    inst = None

    def __new__(cls, *args):
        if not cls.inst:
            cls.inst = super().__new__(cls)
        return cls.inst

    def __init__(self, N, M, total_mines):
        self.rows, self.cols = N, M
        self.total_mines = total_mines
        self.pole = tuple(tuple(Cell((i, j)) for j in range(M)) for i in range(N))
        self.init_pole()

    def init_pole(self):
        unpack = [j for i in self.pole for j in i]
        for i in unpack:
            i.is_mine, i.is_open = False, False
        mined = set(S(unpack, self.total_mines))
        for i in mined:
            i.is_mine = True
        non_mined = set(unpack) - mined
        for i in non_mined:
            x1, x2 = i.pos[0] - 1 if i.pos[0] > 0 else 0, i.pos[0] + 2 if i.pos[0] < self.rows else self.rows - 1
            y1, y2 = i.pos[1] - 1 if i.pos[1] > 0 else 0, i.pos[1] + 2 if i.pos[1] < self.cols else self.cols - 1
            eps = set(j for i in self.pole[x1:x2] for j in i[y1:y2])
            i.number = sum(map(lambda x: x.is_mine, eps))

    def open_cell(self, i, j):
        if all([type(i) == int == type(j), i in range(self.rows), j in range(self.cols)]):
            self.pole[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for i in self.pole:
            for j in i:
                if j.is_open:
                    print(' *' if j.is_mine else f' {j.number}', end='')
                else:
                    print('[]', end='')
            print()


class Cell:
    is_mine, number, is_open, pos = D(), D(), D(), D()

    def __init__(self, pos=None):
        self.is_mine, self.number, self.is_open = False, 0, False
        self.pos = pos

    def __bool__(self):
        return not self.is_open


###############################################################################################################################################


class GamePole:
    _instance = None

    def __new__(cls, *argc, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, N, M, total_mines):
        if '_total_mines' not in self.__dict__:
            self.__N, self.__M, self.__total_mines = N, M, total_mines
            self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
            # - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.
            if '_debug' in globals():
                print(*self.__pole_cells, sep='\n')
                print(len(self.__pole_cells))

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        ''' - для инициализации начального состояния игрового поля расставляет мины и делает все клетки закрытыми);'''
        from random import randrange
        mines = set()
        # Сначала создадим множество точек для минирования
        while len(mines) < self.__total_mines:
            coords = (randrange(0, self.__N), randrange(0, self.__M))
            mines.add(coords)

        # Теперь проведём собственно минирование нужных точек и разминирование остальных
        for i in range(self.__N):
            for j in range(self.__M):
                self.__pole_cells[i][j].is_open = False
                self.__pole_cells[i][j].is_mine = ((i, j) in mines)
                if not self.__pole_cells[i][j].is_mine:
                    self.__pole_cells[i][j].number = len([*filter(
                        lambda x: x in mines,
                        (
                            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                            (i, j - 1), (i, j + 1),
                            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
                        )
                    )])
        self.__mines = mines

    def open_cell(self, i, j):
        ''' - открывает ячейку с индексами (i, j);
        нумерация индексов начинается с нуля; метод меняет значение атрибута __is_open
        объекта Cell в ячейке (i, j) на True;'''
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        '''show_pole() - отображает игровое поле в консоли
        как именно сделать - на ваше усмотрение, этот метод - домашнее задание).
        '''
        for i in range(self.__N):
            for j in range(self.__M):
                cl = self.__pole_cells[i][j]

                if cl:
                    print('?', end='')
                else:
                    print('*' if cl.is_mine else cl.number, end='')

            print()

    def show_pole_all(self):
        for i in range(self.__N):
            for j in range(self.__M):
                cl = self.__pole_cells[i][j]
                print('*' if cl.is_mine else cl.number, end='')
            print()


class Cell:
    def __init__(self):
        self.__is_mine = False
        # - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
        self.__number = 0
        # - число мин вокруг клетки (целое число от 0 до 8);
        self.__is_open = False
        # - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int) or not 0 <= value <= 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open


#########################################################################
# _________3.8 Методы __getitem__, __setitem__ и __delitem________________________________
# __________Egorof________________
# Нам необходимо создать класс Building. Мы должны научиться создавать здание определенной этажности и уметь
# бронировать за компанией определенный этаж в здании. Важно, что в нашем классе за одним этажом может быть закреплена
# только одна компанияДля этого в классе Building должно быть реализованыметод __init__, который принимает количество
# этажей в зданииметод __setitem__, который закрепляет за определенным этажом компанию. Если этаж был занят другой
# компанией, нужно заменить название другой компаниейметод __getitem__, который возвращает название компании с этого
# этажа. В случае, если этаж пустует, следует вернуть Noneметод __delitem__, который высвобождает этаж

class Building:
    def __init__(self, floors):
        # self.floors = [None]*floors
        self.floors = {}

        # self.floors = {floor: None for floor in range(floors)}
        #
        # for floor in range(floors):
        #     self.floors[floor] = None

    def __setitem__(self, key, value):
        # if key < len(self.floors):
        #     self.floors[key] = value

        if key in self.floors:
            # self.__dict__[key] = value
            self.floors[key] = value

    def __getitem__(self, item):
        return self.floors[item]

    def __delitem__(self, key):
        self.floors[key] = None


################################
class Building:
    # С применением декоратора, проверяющего наличие этажа в здании
    def __init__(self, floors):
        self.numb_of_floors = floors
        self.floors = [None] * floors

    def examination(func):
        def wrap(*args):
            if args[0].numb_of_floors >= args[1]:
                return func(*args)
            raise ValueError(f'Этажа №{args[1] + 1} не существует в этом здании')

        return wrap

    @examination
    def __setitem__(self, key, value):
        self.floors[key] = value

    @examination
    def __getitem__(self, key):
        return self.floors[key]

    @examination
    def __delitem__(self, key):
        self.floors[key] = None


################################################################
# ______Balakirev________________________________
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        if item not in self.marks:
            raise KeyError(f"Ключ {item} не существует или был удален")
        return self.marks[item]

    def __setitem__(self, key, value):
        if key in self.marks:
            self.marks[key] = value

    def __delitem__(self, key):
        if key in self.marks:
            del self.marks[key]
            print(f"Ключ {key} удален")


student_1 = Student('Lesha', {'Math': 3, 'History': 5})
print(student_1['Math'])  # 3

student_1['Math'] = 5
print(student_1['Math'])  # 5

del student_1['Math']  # Ключ Math удален

print(student_1['Math'])  # Ключ Math не существует или был удален


################################################################
# метод __init__, который сохраняет в экземпляре два атрибута title и artist: название песни и исполнитель
# Класс Playlist должен содержать:метод __init__. , который создает в экземпляре атрибут songs. Изначально должен
# ыть пустым списком; метод __getitem__ , который возвращает песню из атрибута songs по индексуметод __setitem__ ,
# который добавляет песню в атрибут songs в указанный индекс. При этом нужно сдвинуть уже имеющиеся песни вправо, у
# которых индекс был до момента вставки равен или больше переданного

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:
    def __init__(self):
        self.songs = []

    def __getitem__(self, item):
        return self.songs[item]

    def __setitem__(self, item, value):
        self.songs.insert(item, value)

    def add_song(self, song):
        self.__setitem__(-1, song)


########################################################################
# В этой задаче мы создадим аналог корзины покупок и для этого нам понадобиться реализовать класс ShoppingCart. В нем
# должно содержаться следующее:метод __init__. , который создает в экземпляре атрибут items. Изначально должен быть
# пустым словарем, в нем будут содержаться покупки;метод __getitem__ , который возвращает по названию товара его
# текущее количество или 0, если товар отсутствует в корзине метод __setitem__ , который проставляет по названию
# товара его количество в корзине. Если товар отсутствовал, его необходимо добавить, если присутствовал - нужно
# проставить ему новое количествометод __delitem__ , который удаляет товар из корзиныметод add_item, который добавляет
# товар к текущим. Это значит, что если товар уже присутствовал в корзине, то необходимо увеличить его количество.
# Если товар отсутствовал, нужно его добавить. Данный метод принимает обязательно название товара и необязательно
# его количество (по умолчанию количество равно 1). метод remove_item, который удаляет некоторое количество товара
# из корзины. Если хотят удалить из корзины столько же товара, чем там имеется или больше, необходимо удалить его из
# корзины.  В остальных случаях уменьшаем количество товара на переденное количество. Данный метод принимает
# обязательно название товара и необязательно его количество (по умолчанию количество равно 1). Предусмотрите
# ситуацию, когда удаляемый товар отсутствует в корзине
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, product):
        return self.items.get(product, 0)

    def __setitem__(self, items, value):
        self.items[items] = value

    def add_item(self, product, value=1):
        if product in self.items:
            self.items[product] += value
        else:
            self.__setitem__(product, value)
            # self.items[product] = value

    def __delitem__(self, items):
        del self.items[items]

    def remove_item(self, product, value=1):
        if product in self.items:
            if self.items[product] >= value:
                self.items[product] -= value
            else:
                self.__delitem__(product)
                # del self.items[product]


########################################################################
# Подвиг 2. Объявите класс Record (запись), который описывает одну произвольную запись из БД. Объекты этого класса
# создаются командой:r = Record(field_name1=value1,... , field_nameN=valueN)где field_nameX - наименование поля
# БД; valueX - значение поля из БД.В каждом объекте класса Record должны автоматически создаваться локальные
# публичные атрибуты по именам полей (field_name1,... , field_nameN) с соответствующими значениями. Например:
# r = Record(pk=1, title='Python ООП', author='Балакирев')В объекте r появляются атрибуты:r.pk # 1r.title # Python ООП
# r.author # БалакиревТакже необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:
# r[0] = 2 # доступ к полю pkr[1] = 'Супер курс по ООП' # доступ к полю titler[2] = 'Балакирев С.М.' # доступ к полю
# authorprint(r[1]) # Супер курс по ООПr[3] # генерируется исключение IndexError
# Если указывается неверный индекс (не целое число или некорректное целое число), то должно генерироваться
# исключение командой:raise IndexError('неверный индекс поля')P.S. В программе нужно объявить только класс.
# Выводить на экран ничего не нужно.P.P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта
# класса Record.
class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        # for k, v in kwargs.items():
        #     self.__dict__[k] = v

        # self.__dict__ = kwargs

        # for arg in kwargs:
        #     self.__dict__[arg] = kwargs[arg]

        self.__total_attrs = len(kwargs)
        # self.__total_attrs = len(self.__dict__)

        self.__attrs = tuple(self.__dict__.keys())

    def __check_attrs_(self, indx):
        if type(indx) != int or not (-self.__total_attrs <= indx < self.__total_attrs):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, indx):
        self.__check_attrs_(indx)
        return getattr(self, self.__attrs[indx])

    def __setitem__(self, key, value):
        self.__check_attrs_(key)
        setattr(self, self.__attrs[key], value)


#######################################################################
class Record:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __getitem__(self, item):
        try:
            return self.__dict__[(*self.__dict__.keys(),)[item]]
        except IndexError:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, item, value):
        try:
            self.__dict__[(*self.__dict__.keys(),)[item]] = value
        except IndexError:
            raise IndexError('неверный индекс поля')


########################################################################
# Подвиг 3. Вам необходимо для навигатора реализовать определение маршрутов. Для этого в программе нужно объявить класс
# Track, объекты которого создаются командой:tr = Track(start_x, start_y)где start_x, start_y - координата начала пути.
# В этом классе должен быть реализован следующий метод:add_point(x, y, speed) - добавление новой точки маршрута
# (линейный сегмент), который можно пройти со средней скоростью speed.Также с объектами класса Track должны выполняться
# команды:coord, speed = tr[indx] # получение координаты (кортеж с двумя числами) и скорости (число) для линейного
# сегмента маршрута с индексом indxtr[indx] = speed # изменение средней скорости линейного участка маршрута по
# индексу indxЕсли индекс (indx) указан некорректно (должен быть целым числом от 0 до N-1, где N - число линейных
# сегментов в маршруте), то генерируется исключение командой:raise IndexError('некорректный индекс')
class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.speed = []

    def __setitem__(self, key, value):
        self.speed[key] = value

    def add_point(self, x, y, speed):
        self.speed.append(speed)
        self.start_x = x
        self.start_y = y

    def __getitem__(self, item):
        if item > len(self.speed) - 1:
            raise IndexError('некорректный индекс')
        return tuple([self.start_x, self.start_y]), self.speed[item]


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3]  # IndexError


########################################################################
class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.traffic = {}

    def __setitem__(self, key, value):
        self.traffic[list(self.traffic.keys())[key]] = value

    def add_point(self, x, y, speed):
        self.traffic[(x, y)] = speed

    def __getitem__(self, item):
        if item > len(self.traffic):
            raise IndexError('некорректный индекс')
        return tuple(self.traffic.keys())[item], self.traffic.get(list(self.traffic.keys())[item])


#######################################################################
class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([(x, y), speed])

    def __check(self, idx):
        if type(idx) != int or idx > (len(self.points)):
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        self.__check(key)
        self.points[key][1] = value

    def __getitem__(self, item):
        self.__check(item)
        return self.points[item]


########################################################################
from typing import Union

U = Union[int, float]


class Track:
    def __init__(self, start_x: U, start_y: U):
        self.start_y = start_y
        self.start_x = start_x
        self.points = []

    @staticmethod
    def validator(method):
        def wrapper(self: "Track", key: int, *args, **kwargs):
            if 0 <= key < len(self.points):
                return method(self, key, *args, **kwargs)
            raise IndexError('некорректный индекс')

        return wrapper

    @validator.__get__(0)
    def __getitem__(self, item: int):
        return self.points[item]

    @validator.__get__(0)
    def __setitem__(self, key: int, value):
        point = self.points[key]
        self.points[key] = (point[0][0], point[0][1]), value

    def add_point(self, x: U, y: U, speed: U):
        self.points.append(((x, y), speed))


# Он нужен, чтобы можно было завернуть в декоратор. @staticmethod не вызываемый объект (если убрать __get__(0),
# напишешь "TypeError: 'staticmethod' object is not callable"). Однако с версией Python 3.10 разработчики добавили
# __call__ в staticmethod, так что на новых версия этого не требуется.

###############################################################################################################################################
class Track:
    def __init__(self, *args):
        self.tracks = {}

    def add_point(self, x, y, speed):
        self.tracks[len(self.tracks)] = [(x, y), speed]

    def __getitem__(self, idx):
        try:
            return self.tracks[idx]
        except KeyError:
            raise IndexError('некорректный индекс')

    def __setitem__(self, idx, value):
        self[idx][1] = value


# self[idx][1] в этой композиции self[idx] как раз идет через __getitem__ (tr[2]), возвращает self.tracks[idx] и уже у
# этого # возвращенного значения мы меняем значение по индексу 1(tr[2] = 60). и по той же причине в __setitem__ не
# требуется проверка, она в __getitem__ исполняется красиво
########################################################################
# Подвиг 4. Вам необходимо написать программу по работе с массивом однотипных данных (например, только числа или строки
# и т.п.). Для этого нужно объявить класс с именем Array, объекты которого создаются командой:
# aar = Array(max_length, cell)где max_length - максимальное количество элементов в массиве; cell - ссылка на класс,
# описывающий отдельный элемент этого массива (см. далее, класс Integer). Начальные значения в ячейках массива
# (в объектах класса Integer) должны быть равны 0.Для работы с целыми числами объявите в программе еще один класс с
# именем Integer, объекты которого создаются командой:cell = Integer(start_value)где start_value - начальное значение
# ячейки (в данном случае - целое число).В классе Integer должно быть следующее свойство (property):
# value - для изменения и считывания значения из ячейки (само значение хранится в локальной приватной переменной;
# имя придумайте сами).При попытке присвоить не целое число должно генерироваться исключение командой:
# raise ValueError('должно быть целое число')Для обращения к отдельным элементам массива в классе Array необходимо
# определить набор магических методов для следующих операций:value = ar[0] # получение значения из первого элемента
# (ячейки) массива arar[1] = value # запись нового значения во вторую ячейку массива arr
# Если индекс не целое число или число меньше нуля или больше либо равно max_length, то должно генерироваться
# исключение командой:raise IndexError('неверный индекс для доступа к элементам массива')
class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.__cell = cell
        self.__array = [self.__cell() for _ in range(self.max_length)]  # self.__cell() вызов класса Integer()
        # self.__array = [cell() for _ in range(self.max_length)]

        # self.__array = [self.__cell()] * self.max_length  # не подойдёт такой способ при изм
        # одного эл (ar_int[1] = 10) меняются все в списке 10 10 10 10 10 10 10 10 10 10

    def __check(self, item):
        if type(item) != int or not (-self.max_length <= item < self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check(item)
        return self.__array[item].value

    def __setitem__(self, item, value):
        self.__check(item)
        self.__array[item].value = value

    def __repr__(self):
        return ' '.join(map(str, self.__array))


class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self.__value = value

    def __repr__(self):
        return f'{self.__value}'
    # без repr в классе Array return ' '.join(map(str, self.__array)) будет выдавать
    # <__main__.Integer object at 0x000002022230F190> <__main__.Intege....
    # будут отображаться  просто ссылки на объекты из списка


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)


# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError

########################################################################
class Num:
    NUM_TYPE = None
    INIT_VALUE = None
    NUM_TYPE_STR = {int: 'целое', float: "вещественное"}

    def __init__(self, start_value):
        self.__except_message = f'должно быть {self.NUM_TYPE_STR.get(self.NUM_TYPE)} число'
        self.value = start_value

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) != self.NUM_TYPE:
            raise ValueError(self.__except_message)
        self.__value = value


class Integer(Num):
    NUM_TYPE = int
    INIT_VALUE = 0


class Float(Num):
    NUM_TYPE = float
    INIT_VALUE = 0.0


class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__type = cell
        self.__elements = [self.__type(self.__type.INIT_VALUE) for _ in range(max_length)]

    def __check(self, idx):
        if type(idx) != int or idx not in range(self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check(item)
        return self.__elements[item].value if item < len(self.__elements) else self.__type.INIT_VALUE

    def __setitem__(self, key, value):
        self.__check(key)
        self.__elements[key].value = value

    def __str__(self):
        return ' '.join(map(str, self.__elements))


########################################################################
class Types:
    def __init__(self, start_value=None):
        self.value = start_value or self.value_start

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, self.value_type):
            raise ValueError(self.value_msg)
        self.__value = new_value

    def __str__(self):
        return str(self.__value)


class Integer(Types):
    value_start = 0
    value_type = int
    value_msg = 'должно быть целое число'


class Float(Types):
    value_start = .0
    value_type = float
    value_msg = 'должно быть вещественное число'


class Array:

    def __init__(self, max_length, cell):
        self.max_length, self.cell = max_length, cell
        self.__cells = [cell() for _ in range(self.max_length)]

    def set_raise(self, key):
        if not isinstance(key, int) or key not in range(self.max_length):
            # if not 0 <= indx < len(self):
            raise IndexError('некорректный индекс')

    def __getitem__(self, key):
        self.set_raise(key)
        return self.__cells[key].value

    def __setitem__(self, key, value):
        self.set_raise(key)
        self.__cells[key].value = value

    def __str__(self, *args, **kwargs):
        return ' '.join(map(str, self.__cells))


#######################################################################
# Подвиг 7 (познание срезов). Объявите в программе класс с именем RadiusVector (радиус-вектор), объекты которого
# создаются командой:v = RadiusVector(x1, x2,..., xN)где x1, x2,..., xN - координаты радиус-вектора (числа: целые или
# вещественные).В каждом объекте класса RadiusVector должен быть локальный атрибут:coords - список из координат
# радиус-вектора.P.S. При передаче среза в магических методах __setitem__() и __getitem__() параметр индекса становится
# объектом класса slice. Его можно указывать непосредственно в квадратных скобках упорядоченных коллекций (списков,
# кортежей и т.п.).
class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return tuple(self.coords[key])
        return self.coords[key]

    def __setitem__(self, indx, value):
        self.coords[indx] = value

    def __repr__(self):
        return f'{self.coords}'


v = RadiusVector(1, 1, 1, 1)
print(v)
print(v[1])  # 1
v[:] = 1, 2, 3, 4
print(v[2])  # 3
print(v[1:])  # (2, 3, 4)
v[0] = 10.5
print(v[0])


########################################################################
class RadiusVector(list):
    def __getitem__(self, i):
        res = super().__getitem__(i)
        return tuple(res) if isinstance(res, list) else res

    def __init__(self, *args):
        super().__init__(args)


########################################################################
class RadiusVector:

    def __init__(self, *args):
        self.coords = args

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.coords[slice(key.start, key.stop, key.step)]
        else:
            return self.coords[key]

    def __setitem__(self, key, value):
        tl = list(self.coords)
        if isinstance(key, slice):
            tl[slice(key.start, key.stop, key.step)] = value
        else:
            tl[key] = value
        self.coords = tl


#######################################################################
# Большой подвиг 5. Вам необходимо написать программу для удобного обращения с таблицами однотипных данных (чисел, строк,
# булевых значений и т.п.), то есть, все ячейки таблицы должны представлять какой-то один указанный тип.
# Для этого в программе необходимо объявить три класса:TableValues - для работы с таблицей в целом;CellInteger - для
# операций с целыми числами;IntegerValue - дескриптор данных для работы с целыми числами.Начнем с дескриптора
# IntegerValue. Это должен быть дескриптор данных (то есть, и для записи и считывания значений).
# Если присваиваемое значение не является целым числом, должно генерироваться исключение командой:
# raise ValueError('возможны только целочисленные значения')Следующий класс CellInteger описывает одну ячейку
# таблицы для работы с целыми числами. В этом классе должен быть публичный атрибут (атрибут класса):
# value - объект дескриптора, класса IntegerValue.А объекты класса CellInteger должны создаваться командой:
# cell = CellInteger(start_value)где start_value - начальное значение ячейки (по умолчанию равно 0 и сохраняется в
# ячейке через дескриптор value).Наконец, объекты последнего класса TableValues создаются командой:
# table = TableValues(rows, cols, cell=CellInteger)где rows, cols - число строк и столбцов (целые числа);
# cell - ссылка на класс, описывающий работу с отдельными ячейками таблицы. Если параметр cell не указан, то
# генерировать исключение командой:raise ValueError('параметр cell не указан')Иначе, в объекте table класса
# TableValues создается двумерный (вложенный) кортеж с именем cells размером rows x cols, состоящий из объектов
# указанного класса (в данном примере - класса CellInteger).Также в классе TableValues предусмотреть возможность
# обращения к отдельной ячейке по ее индексам, например:value = table[1, 2] # возвращает значение ячейки с индексом
# (1, 2)table[0, 0] = value # записывает новое значение в ячейку (0, 0)Обратите внимание, по индексам сразу должно
# возвращаться значение ячейки, а не объект класса CellInteger. И то же самое с присваиванием нового значения.
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
# P.P.S. В качестве домашнего задания создайте класс CellString для работы со строками и используйте тот же класс
# TableValues для этого нового типа данных.Последнее: дескрипторы здесь для повторения. В реальной разработке лучше
# использовать в таких задачах объекты-свойства (property).
class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        # self.cells = tuple(tuple(cell() for _ in [self.cols]) for _ in [self.rows])
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    # self.__cells = tuple([tuple([cell()]) * cols for _ in range(rows)])
    # Копируется уже измененный объект по всей строке.
    # Просто приму во внимание. Помнится с матрицами нормально работало. Видимо в классе при работе с объектами другие
    # приоритеты. ААА! Они же одинаковые! ОДИНАКОВЫЕ. По любому хэш же тогда один. Зараза =)
    # cell() * n - вы создаете один объект, а потом размножаете ссылку на него. получается матрица, состоящая из ссылок
    # на один объект

    def __check_index(self, index):
        r, c = index
        if type(r) != int or not (0 <= r < self.rows) or type(c) != int or not (0 <= c < self.cols):
            raise IndexError

    def __getitem__(self, index):
        self.__check_index(index)
        return self.cells[index[0]][index[1]].value

    def __setitem__(self, index, value):
        self.__check_index(index)
        self.cells[index[0]][index[1]].value = value


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
table[0, 0] = 1.45  # генерируется исключение ValueError

for row in table.cells:
    for x in row:
        print(x.value, end=' ')


########################################################################
class ValueDescriptor:
    TYPE = None
    TYPE_STR = {int: "целочисленные", str: "строковые"}

    def __set_name__(self, owner, name):
        self.name = f'__{name}'
        self.__except_message = f'возможны только {self.TYPE_STR.get(self.TYPE, None)} значения'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != self.TYPE:
            raise ValueError(self.__except_message)
        setattr(instance, self.name, value)


class IntegerValue(ValueDescriptor):
    TYPE = int


class StringValue(ValueDescriptor):
    TYPE = str


class Cell:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class CellInteger(Cell):
    INIT_VALUE = 0
    value = IntegerValue()


class CellString(Cell):
    INIT_VALUE = ''
    value = StringValue()


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if not issubclass(cell, Cell):
            raise ValueError('параметр cell не указан')
        self.cells = [[cell(cell.INIT_VALUE) for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, item):
        r, c = item
        return self.cells[r][c].value

    def __setitem__(self, key, value):
        r, c = key
        self.cells[r][c].value = value


#####################################################################################################################
class CellDescriptor:
    TYPES = {int: "целочисленные", str: "строковые"}

    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, new_value):
        if not isinstance(new_value, self.value_type):
            raise ValueError(f'возможны только {self.TYPES.get(self.value_type)} значения')
        setattr(instance, self.name, new_value)


class IntegerValue(CellDescriptor):
    value_type = int


class StringValue(CellDescriptor):
    value_type = str


class CellValue:
    def __init__(self, start_value=None):
        self.value = start_value or self.value_start

    def __str__(self):
        return str(self.value)


class CellInteger(CellValue):
    value_start = 0
    value = IntegerValue()


class CellString(CellValue):
    value_start = ''
    value = StringValue()


class TableValues:

    def __init__(self, *args, **kwargs):
        self.__rows, self.__cols = args
        if kwargs.get('cell') is None:
            raise ValueError('параметр cell не указан')
        self.cells = [[kwargs['cell']() for _ in range(self.__cols)] for _ in range(self.__rows)]

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, item, value):
        self.cells[item[0]][item[1]].value = value

    def __str__(self, *args, **kwargs):
        return '\n'.join(' '.join(map(str, row)) for row in self.cells)


########################################################################
# Подвиг 6. Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по цепочке до
# последнего:Для этого в программе объявлялись два класса: StackObj - для описания объектов стека;
# Stack - для управления стек-подобной структурой.И, далее, объекты класса StackObj следовало создавать командой:
# obj = StackObj(data)где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса
# StackObj должен иметь следующие локальные атрибуты:data - ссылка на строку с данными, указанными при создании объекта;
# next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).
# Класс Stack предполагается использовать следующим образом:st = Stack() # создание объекта стек-подобной структуры
# В каждом объекте класса Stack должен быть локальный публичный атрибут:top - ссылка на первый объект стека
# (если стек пуст, то top = None).А в самом классе Stack следующие методы:push(self, obj) - добавление
# объекта класса StackObj в конец стека;pop(self) - извлечение последнего объекта с его удалением из стека;
# Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:
# obj_top = st[0] # получение первого объектаobj = st[4] # получение 5-го объекта стекаst[2] = StackObj("obj3") #
# замена прежнего (3-го) объекта стека на новыйЕсли индекс не целое число или число меньше нуля или больше числа
# объектов в стеке, то должно генерироваться исключение командой:raise IndexError('неверный индекс')

class StackObj:
    def __init__(self, data):
        self.data = data
        self.__next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__count_obj = 0

    def push(self, obj):
        last = self[self.__count_obj - 1] if self.__count_obj > 0 else None
        if last:
            last.next = obj
        if self.top is None:
            self.top = obj
        self.__count_obj += 1

    def pop(self):
        if self.__count_obj == 0:
            return None

        last = self[self.__count_obj - 1]

        if self.__count_obj == 1:
            self.top = None
        else:
            self[self.__count_obj - 2].next = None
        self.__count_obj -= 1
        return last

    def __check_index(self, item):
        if type(item) != int or not (0 <= item < self.__count_obj):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        count = 0
        h = self.top
        while h and count < item:
            h = h.next
            count += 1
        return h

    def __setitem__(self, key, value):
        self.__check_index(key)
        obj = self[key]  # отрабатывает _getitem_
        prev = self[key - 1] if key > 0 else None
        value.next = obj.next
        if prev:
            prev.next = value


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data)  # obj3
print(st[1].data)  # new obj2
res = st[3]  # исключение IndexError


########################################################################
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)


class Stack:
    def __init__(self):
        self.top = None
        self.__count = 0

    def __check(self, idx):
        if idx not in range(self.items):
            raise IndexError('неверный индекс')

    @property
    def items(self):
        return self.__count

    def push(self, obj):
        self.__count += 1
        if self.top is None:
            self.top = obj
        else:
            el = self.top
            while el.next is not None:
                el = el.next
            el.next = obj

    def pop(self):
        el = self.top
        if el and self.top.next is None:
            self.top = None
            self.__count -= 1
        elif el and el.next:
            self.__count -= 1
            last = el
            el = el.next
            while el.next:
                last = el
                el = el.next
            last.next = None
        return el

    def __get_obj(self, idx):
        cnt = 0
        el = self.top
        while cnt != idx:
            el = el.next
            cnt += 1
        return el

    def __getitem__(self, item):
        self.__check(item)
        return self.__get_obj(item)

    def __setitem__(self, key, value):
        self.__check(key)
        if key == 0:
            value.next = self.top.next
            self.top = value
        else:
            prev = self.__get_obj(key - 1)
            cur = prev.next
            prev.next = value
            value.next = cur.next


########################################################################
# Подвиг 8. Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики". Для этого требуется объявить
# класс TicTacToe (крестики-нолики), объекты которого создаются командой:game = TicTacToe()Каждый объект game должен
# иметь публичный атрибут:pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.
# Каждая клетка игрового поля представляется объектом класса Cell и создается командой:cell = Cell()
# Объекты класса Cell должны иметь следующие публичные локальные атрибуты:is_free - True, если клетка свободна;
# False в противном случае;value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).Также с каждым объектом
# класса Cell должна работать функция:bool(cell)которая возвращает True, если клетка свободна (cell.is_free=True)
# и False в противном случае.Класс TicTacToe должен иметь следующий метод:clear() - очистка игрового поля
# (все клетки заполняются нулями и переводятся в закрытое состояние);А объекты этого класса должны иметь следующую
# функциональность (обращение по индексам):game[0, 0] = 1 # установка нового значения, если поле закрыто
# res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)Если указываются некорректные
# индексы, то должно генерироваться исключение командой:raise IndexError('неверный индекс клетки')Если идет попытка
# присвоить новое значение в открытую клетку поля, то генерировать исключение:raise ValueError('клетка уже занята')
# Также должны быть реализованы следующие полные срезы при обращении к клеткам игрового поля:slice_1 = game[:, indx]
# выбираются все элементы (кортеж) столбца с индексом indxslice_2 = game[indx, :] # выбираются все элементы (кортеж)
# строки с индексом indxP.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
# P.P.S. При передаче среза в магических методах __setitem__() и __getitem__() параметр индекса становится объектом
# класса slice. Его можно указывать непосредственно в квадратных скобках упорядоченных коллекций (списков, кортежей и т

class TicTacToe:
    def __init__(self):
        self.n = 3
        self.pole = tuple(tuple(Cell() for _ in range(self.n)) for _ in range(self.n))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_free = True

    def check_pole(self, item):
        if type(item) != tuple or len(item) != 2:
            raise IndexError('неверный индекс клетки')

        for i in item:
            if type(i) != slice:
                if 0 > i > self.n:
                    raise IndexError('неверный индекс клетки')
        # if any(not (0 <= i < self.n) for i in item if type(i) != slice):
        #     raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        self.check_pole(item)
        r, c = item
        if isinstance(item[0], slice):
            return tuple(self.pole[i][item[1]].value for i in range(self.n))  # срез для столбцов cols
        elif type(c) == slice:
            return tuple(self.pole[r][i].value for i in range(self.n))  # #срез для строк rows
            # return tuple(self.pole[item[1]][i].value for i in range(self.n))  #срез для строк rows

        return self.pole[item[0]][item[1]].value

    def __setitem__(self, item, value):
        self.check_pole(item)
        # if not self.pole[item[0]][item[1]].is_free:
        if not self.pole[item[0]][item[1]]:
            raise ValueError('клетка уже занята')
        self.pole[item[0]][item[1]].value = value
        self.pole[item[0]][item[1]].is_free = False


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0  # значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

    def __bool__(self):
        return self.is_free


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
# game[3, 2] = 2  # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0


#######################################################################
class Cell:
    """Класс описывающий клетку игрового поля в крестики-нолики"""

    # 1 крестик; 2 нолик; 0 пустое место
    # is_free == True (клетка свободна, можно размещать);
    # is_free == False (клетка закрыта, размещать нельзя)
    def __init__(self):
        self.is_free = True
        self.value = 0

    # ниже объект свойство контролирует чтобы значение ячейки игрового поля менялось
    # только в том случае - если эта ячейка свободна, иначе вызываем исключение

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v: int):
        if not self.is_free:
            raise ValueError("клетка уже занята")
        self.__value = v

    def __bool__(self):
        return self.is_free


class TicTacToe:
    """Класс описывающий игровое поле"""

    def __init__(self):
        # игровое поле представленное в виде двумерного кортежа
        self.pole = tuple(tuple(Cell() for col in range(3)) for row in range(3))

    def clear(self):
        """Очищает игровое поле (убирает все крестики и нолики, закрывает клетки)"""

        # Циклом проходимся по каждой клетке
        for row in range(3):
            for col in range(3):
                self.pole[row][col].is_free = True
                self.pole[row][col].value = 0

    @staticmethod
    def __validate_coordinate(coordinate: int):
        """Проверяет чтобы координата не выходила за пределы размеров поля"""
        if coordinate not in range(3):
            raise IndexError("неверный индекс")

    def __getitem__(self, item: tuple):
        """Получение значения по координатам x, y (одна из координат может быть
        представлена срезом (slice). В этом случае выбираются все значения, находящиеся
        на той координате, которая представлена целым числом). Если обе координаты
        представлены целыми числами - просто возвращаем элемент поля находящийся на
        соответствующей координате"""

        row, col = item

        # Возвращается конкретная клетка
        if isinstance(row, int) and isinstance(col, int):
            self.__validate_coordinate(row)  # Проверяем координату (см. выше)
            self.__validate_coordinate(col)  # Проверяем координату (см. выше)
            return self.pole[row][col].value

        # Возвращаются все клетки, находящиеся под столбцом col
        elif isinstance(row, slice) and isinstance(col, int):
            self.__validate_coordinate(col)  # Проверяем координату (см. выше)
            return tuple(self.pole[r][col].value for r in range(3))

        # Возвращаются все клетки, находящиеся под строкой row
        elif isinstance(row, int) and isinstance(col, slice):
            self.__validate_coordinate(row)  # Проверяем координату (см. выше)
            return tuple(self.pole[row][c].value for c in range(3))

    def __setitem__(self, key, value):
        """Устанавливает значение конкретной клетке игрового поля"""

        row, col = key
        self.__validate_coordinate(row)  # Проверяем координату (см. выше)
        self.__validate_coordinate(col)  # Проверяем координату (см. выше)

        self.pole[row][col].value = value  # Срабатывает сеттер из класса Cell
        # (см. выше)
        self.pole[row][col].is_free = False


########################################################################
class TicTacToe:
    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for __ in range(3)]

    def clear(self):
        self.__init__()

    def valid(self, coord):
        if not all([i in range(3) for i in coord if type(i) is int]):
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        self.valid(item)
        pole_ = tuple(zip(*self.pole)) if type(item[0]) is slice else self.pole
        cell_ = pole_[item[0]][item[1]]
        return cell_.value if type(cell_) is Cell else tuple([i.value for i in cell_])

    def __setitem__(self, key, value):
        self.valid(key)
        if not self.pole[key[0]][key[1]].is_free:
            raise ValueError('клетка уже занята')
        self.pole[key[0]][key[1]].value = value
        self.pole[key[0]][key[1]].is_free = False


class Cell:
    def __init__(self):
        self.is_free, self.value = True, 0

    def __bool__(self):
        return self.is_free == True


########################################################################
class Cell:
    def __init__(self):
        self.value = 0
        self.is_free = True

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple([[Cell() for _ in range(3)] for _ in range(3)])

    def clear(self):
        for rows in self.pole:
            for cell in rows:
                cell.value = 0
                cell.is_free = True

    def __setitem__(self, key, value):
        if not 0 <= key[0] < len(self.pole) or not 0 <= key[0] <= len(self.pole[0]) - 1:
            raise IndexError('неверный индекс клетки')
        else:
            if self.pole[key[0]][key[1]]:
                self.pole[key[0]][key[1]].value = value
            else:
                raise ValueError('клетка уже занята')

    def __str__(self):
        return f"{[[cell.value for cell in rows] for rows in self.pole]}"

    def __getitem__(self, item):

        if isinstance(item[0], int) and isinstance(item[1], slice):
            return tuple(x.value for x in self.pole[item[0]][item[1]])
        elif isinstance(item[0], slice) and isinstance(item[1], int):
            return tuple(map(lambda x: x.value, tuple(zip(*self.pole))[item[1]]))
        else:
            return self.pole[item[0]][item[1]].value


#######################################################################
class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for __ in range(3))

    def clear(self):
        for row in self.pole:
            for obj in row:
                obj.is_free = True
                obj.value = 0

    @staticmethod
    def __check_index(ind):
        for i in ind:
            if not (type(i) is slice or type(i) is int and 0 <= i <= 2):
                raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        self.__check_index(item)

        if type(item[0]) is slice:
            return tuple(row[item[1]].value for row in self.pole)

        if type(item[1]) is slice:
            return tuple(map(lambda x: x.value, self.pole[item[0]]))

        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)

        if not self.pole[key[0]][key[1]].is_free:
            raise IndexError('неверный индекс клетки')

        self.pole[key[0]][key[1]].is_free = False
        self.pole[key[0]][key[1]].value = value


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


########################################################################
class Cell:
    def __init__(self):
        self.is_free, self.value = True, 0

    def __bool__(self):
        return self.is_free


class TicTacToe:

    def __init__(self):
        self.pole = [[Cell() for _ in 'XXX'] for _ in 'OOO']

    def clear(self):
        self.__init__()

    @staticmethod
    def set_raise(key):
        if not all(k in range(3) or isinstance(k, slice) for k in key):
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, key):
        self.set_raise(key)
        if isinstance(key[0], slice):
            return tuple(row[key[1]].value for row in self.pole)
        elif isinstance(key[1], slice):
            return tuple(cell.value for cell in self.pole[key[0]])
        return self.pole[key[0]][key[1]].value

    def __setitem__(self, key, value):
        self.set_raise(key)
        if not self.pole[key[0]][key[1]]:
            raise ValueError('клетка уже занята')
        self.pole[key[0]][key[1]].value = value


###############################################################################################################################################
# Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:bag = Bag(max_weight)
# где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.Каждый предмет описывается
# классом Thing и создается командой:t = Thing(name, weight)где name - название предмета (строка); weight - вес
# предмета (вещественное или целочисленное значение). В объектах класса Thing должны автоматически формироваться
# локальные свойства с теми же именами: name и weight.В классе Bag должен быть реализован метод:
# add_thing(thing) - добавление нового объекта thing класса Thing в сумку.Добавление выполняется только если
# суммарный вес вещей не превышает параметра max_weight. Иначе, генерируется исключение:raise ValueError
# ('превышен суммарный вес предметов')Также с объектами класса Bag должны выполняться следующие команды:
# t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
# bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indxdel bag[indx] # удаление вещи из сумки,
# расположенной по индексу indxЕсли индекс в этих командах указывается неверно, то должно генерироваться исключение:
# raise IndexError('неверный индекс')
class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.lst = []

    def add_thing(self, thing):
        if (sum(i.weight for i in self.lst) + thing.weight) > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.lst.append(thing)

    def __check_index(self, item):
        if not (0 <= item < len(self.lst)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.lst[item]

    def __setitem__(self, item, value):
        self.__check_index(item)
        l = self.lst[:]
        l[item] = value
        if sum(i.weight for i in l) > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.lst[item] = value

        self.lst[item] = value

    def __delitem__(self, item):
        del self.lst[item]


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
print(bag[2].name)  # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name)  # платок
del bag[0]
print(bag[0].name)  # платок


# t = bag[4]  # генерируется исключение IndexError
########################################################################
class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.lst = []
        self.things = 0

    def add_thing(self, thing):
        self.__check_weight(thing)
        self.lst.append(thing)
        self.things += thing.weight

    def __check_weight(self, new_thing, old_thing=0):
        if (self.things + new_thing.weight - old_thing) > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def __check_index(self, item):
        if not (0 <= item < len(self.lst)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.lst[item]

    def __setitem__(self, item, value):
        self.__check_index(item)
        w = self.lst[item].weight
        self.__check_weight(value, w)
        self.lst[item] = value
        self.things += (value.weight - w)

    def __delitem__(self, item):
        self.__check_index(item)
        w = self.lst.pop(item)
        self.things -= w.weight


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


########################################################################
class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []

    def check_weight(self, weight):
        if sum([i.weight for i in self.things]) + weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def check_index(self, indx):
        a = len(self.things)
        if indx not in range(-a, a):
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        self.check_weight(thing.weight)
        self.things.append(thing)

    def __getitem__(self, item):
        self.check_index(item)
        return self.things[item]

    def __setitem__(self, key, value):
        self.check_index(key)
        self.check_weight(value.weight - self[key].weight)
        self.things[key] = value

    def __delitem__(self, key):
        self.check_index(key)
        del self.things[key]


########################################################################
# Подвиг 10. Вам необходимо описывать в программе очень большие и разреженные таблицы данных (с большим числом пропусков
# ). Для этого предлагается объявить класс SparseTable, объекты которого создаются командой:st = SparseTable()
# В каждом объекте этого класса должны создаваться локальные публичные атрибуты:rows - общее число строк таблицы
# (начальное значение 0);cols - общее число столбцов таблицы (начальное значение 0).В самом классе SparseTable должны
# быть объявлены методы:add_data(row, col, data) - добавление данных data (объект класса Cell) в таблицу по индексам
# row, col (целые неотрицательные числа);remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами
# (row, col).При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows, cols объекта
# класса SparseTable. Если происходит попытка удалить несуществующую ячейку, то должно генерироваться исключение:
# raise IndexError('ячейка с указанными индексами не существует')Ячейки таблицы представляют собой объекты класса Cell,
# которые создаются командой:data = Cell(value)где value - данные ячейки (любой тип).Хранить ячейки следует в словаре,
# ключами которого являются индексы (кортеж) i, j, а значениями - объекты класса Cell.Также с объектами класса
# SparseTable должны выполняться команды:res = st[i, j] # получение данных из таблицы по индексам (i, j)
# st[i, j] = value # запись новых данных по индексам (i, j)Чтение данных возможно только для существующих ячеек. Если
# ячейки с указанными индексами нет, то генерировать исключение командой:raise ValueError('данные по указанным
# индексам отсутствуют')При записи новых значений их следует менять в существующей ячейке или добавлять новую,
# если ячейка с индексами (i, j) отсутствует в таблице. (Не забывайте при этом пересчитывать атрибуты rows и cols).

class SparseTable:
    def __init__(self):
        self.table = {}
        self.rows = self.cols = 0

    def __check_keys(self, row, col):
        if (row, col) not in self.table:
            raise IndexError('ячейка с указанными индексами не существует')

    def __update_index(self):
        self.rows = max(key[0] for key in self.table) + 1
        self.cols = max(key[1] for key in self.table) + 1
        # self.rows = max(self.table, key=lambda x: x[0])[0] + 1
        # self.cols = max(self.table, key=lambda x: x[1])[1] + 1

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.__update_index()

    def remove_data(self, row, col):
        self.__check_keys(row, col)
        del self.table[(row, col)]
        self.__update_index()

    def __getitem__(self, item):
        try:
            return self.table[(item[0], item[1])].value
        except KeyError:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        item = (key[0], key[1])
        if item not in self.table:
            self.table[item] = Cell(value)
            self.__update_index()
        else:
            self.table[item] = Cell(value)


class Cell:
    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25  # изменение значения существующей ячейки
st[11, 7] = 'cell_117'  # создание новой ячейки
print(st[0, 0])  # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице


# val = st[2, 5]  # ValueError
# st.remove_data(12, 3)  # IndexError

#######################################################################
class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.tbl = {}

    @property
    def rows(self):
        return max(i[0] for i in self.tbl) + 1 if self.tbl else 0

    @property
    def cols(self):
        return max(i[1] for i in self.tbl) + 1 if self.tbl else 0

    def add_data(self, row, col, data):
        self.tbl[row, col] = data

    def remove_data(self, row, col):
        if not (row, col) in self.tbl:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.tbl[row, col]

    def __getitem__(self, key):
        if not key in self.tbl:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.tbl[key].value

    def __setitem__(self, key, v):
        # self.tbl[key] = Cell(v)
        self.tbl.setdefault(key, Cell(None)).value = v


########################################################################
class SparseTable:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.table = {}

    def update_col_row(self):
        self.rows = max(key[0] for key in self.table) + 1
        self.cols = max(key[1] for key in self.table) + 1

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.update_col_row()

    def remove_data(self, row, col):
        try:
            del self.table[(row, col)]
        except:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        try:
            return self.table[(item[0], item[1])].value
        except:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        # if (key[0], key[1]) not in self.table:
        self.table[(key[0], key[1])] = Cell(value)
        self.update_col_row()
        # else:
        #     self.table[(key[0], key[1])] = value


class Cell:
    def __init__(self, value):
        self.value = value


########################################################################
class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.tables = {}

    def update_index(self):
        self.rows = max(row[0] for row in self.tables) + 1
        self.cols = max(self.tables, key=lambda x: x[1])[1] + 1

    def add_data(self, row, col, data):
        self.tables[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        try:
            del self.tables[(row, col)]
            self.update_index()
        except KeyError:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        key = (item[0], item[1])
        try:
            return self.tables[key].value
        except KeyError:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, item, value):
        key = (item[0], item[1])
        self.tables[key] = Cell(value)
        self.update_index()


class Cell:
    def __init__(self, value):
        self.value = value


#######################################################################
# ___________________беседа с чат GPT________________________

# yield - это ключевое слово в Python, которое используется для определения генераторов. Генераторы являются специальным
# типом итераторов, которые позволяют последовательно вычислять значения их элементов по мере необходимости, т.е.
# лениво (lazy) генерировать значения.Когда вызывается функция-генератор с yield, она не выполняется полностью, а
# возвращает результат выполнения только до следующего оператора yield. Таким образом, каждый раз при вызове метода
# next() у объекта генератора будет выполнено только одно следующее выражение после yield.  Это позволяет значительно
# улучшить производительность программы, особенно если требуется обработка больших объемов данных.Вот пример
# функции-генератора, которая возвращает квадраты натуральных чисел:
def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2
        # Эта функция может быть использована для создания объекта-итератора, который можно использовать для
        # последовательного доступа к первым n квадратам натуральных чисел:


squares = square_generator(5)
print(next(squares))  # 1
print(next(squares))  # 4
print(next(squares))  # 9
print(next(squares))  # 16
print(next(squares))  # 25


# Как видите, каждый раз при вызове next() на объекте squares будет выполняться только один шаг функции-генератора,
# что позволяет сэкономить ресурсы и повысить эффективность работы программы.

####################################################################
##################################
################################################################################################
# В Python, для того чтобы создать итератор, необходимо определить два метода: __iter__ и __next__.
# Метод __iter__ возвращает сам объект-итератор, а метод __next__ возвращает следующий элемент последовательности
# или выбрасывает исключение StopIteration, если достигнут конец последовательности.Если вы хотите сделать ваш класс
# итерируемым, то вам нужно реализовать метод __iter__, который будет возвращать итератор. Обычно в таком случае
# __iter__ просто возвращает self, потому что сам объект является своим собственным итератором. Таким образом,
# если ваш класс представляет собой последовательность элементов, вы можете написать iter(self) в методе __iter__
# для создания итератора.

class MyIterator:
    def __init__(self):
        self.items = [1, 2, 3]
        self.current = 0

    def __iter__(self):
        return iter(self.items)


for item in MyIterator():
    print(item)


# Здесь метод __iter__ просто вызывает функцию iter() для списка self.items, чтобы создать итератор.
# аналог analogue
class Iterator:
    def __init__(self):
        self.items = [1, 2, 3]
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count < len(self.items):
            res = self.count
            self.count += 1
            return self.items[res]
        raise StopIteration


###################################################
# В этой версии метод __iter__ возвращает генератор, который последовательно генерирует каждый элемент списка self.items
# при каждом вызове функции next(). Ключевое слово yield используется для возврата элемента и для приостановки
# выполнения функции до следующего вызова.Обратите внимание, что теперь мы используем for i in it:,
# а не for i in Iterator(10):, потому что мы хотим итерироваться по объекту it, который является экземпляром класса
# Iterator.Этот код создает класс Iterator, который является итерируемым объектом.# В конструкторе класса определяется
# список self.items со значениями [1,2,3].# Метод __iter__ возвращает объект-итератор, который может проходить
# по списку self.items. В данном случае метод __iter__ определен в виде генератора, который использует оператор
# yield для последовательного возврата значений списка.

class Iterator:
    def __init__(self):
        self.items = [1, 2, 3]

    def __iter__(self):
        for i in self.items:
            yield i
        # yield from self.items


it = Iterator()
for i in it:
    print(i)


##################################
# Пример итератора
# Метод __iter__ возвращает сам итератор объекта, что позволяет этому объекту быть итерируемым. В приведенном примере
# метод __iter__ возвращает сам объект-итератор, что позволяет его использовать в цикле for.Когда вы используете
# выражение for i in my_object, Python вызывает метод __iter__ вашего объекта-итератора, чтобы получить итератор.
# Затем он использует этот итератор для последовательного извлечения элементов из объекта в цикле.Таким образом, когда
# мы определяем класс итератора, мы должны определить метод __iter__, который возвращает сам итератор объекта, а также
# метод __next__, который возвращает следующий элемент объекта и генерирует исключение StopIteration, когда элементы
# закончились.
class Iterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self  # чтобы экз мог быть итерируемым ч/з for/next

    def __next__(self):
        while self.count < self.limit:
            res = self.count
            self.count += 1
            return res
        raise StopIteration


it = Iterator(10)
for i in it:
    print(i)


##################################
# Аналог class Iterator:
# В Python протокол итерации требует определения методов __iter__ и __next__ в классе, чтобы объекты этого класса могли
# быть использованы в качестве итераторов.Однако, когда мы определяем __iter__ метод с ключевым словом yield, то он
# автоматически делает объект итерируемым и создает итератор для него. Каждый вызов метода __next__ на этом итераторе
# будет продвигать выполнение функции до следующего оператора yield и возвращать соответствующее значение.Таким образом,
# при использовании генераторов в Python, мы можем избежать необходимости явно определять метод __next__ для наших
# итераторов. Вместо этого мы определяем метод __iter__ c использованием ключевого слова yield, который автоматически
# создает итератор и возвращает его для последующего использования.

class Iterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        while self.count < self.limit:
            yield self.count
            self.count += 1


#################
# yield - это ключевое слово в Python, которое используется для определения генераторов. Генераторы являются специальны
# м типом итераторов, которые позволяют последовательно вычислять значения их элементов по мере необходимости, т.е.
# лениво (lazy) генерировать значения.Когда вызывается функция-генератор с yield, она не выполняется полностью,
# а возвращает результат выполнения только до следующего оператора yield. Таким образом, каждый раз при вызове метода
# next() у объекта генератора будет выполнено только одно следующее выражение после yield.  Это позволяет значительно
# улучшить производительность программы, особенно если требуется обработка больших объемов данных.Вот пример
# функции-генератора, которая возвращает квадраты натуральных чисел:

def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2


################################################################
def echo(value=None):
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print('finally echo')


gen = echo(3)
print(next(gen))
print(gen.send(2))
################################################################
string = 'afwgherigg'


def stop_iteration(iteration, stop_items):
    for k, v in enumerate(iteration, 1):
        yield v
        if v == stop_items:
            break


res = stop_iteration(string, 7)
print(next(res))
for i in res:
    print(i, end='')


################################################################
def counter(max):
    i = 0
    while i < max:
        yield i
        # if value is not None:
        #     i = value
        # else:
        i += 1


it = counter(5)
print(next(it))  # 0
print(next(it))  # 1

for i in it:  # 2,3,4
    print(i)


################################################################
# Оператор yield используется внутри генераторных функций для создания объектов-итераторов. Он приостанавливает
# выполнение функции и возвращает значение, которое будет использоваться как следующий элемент последовательности,
# генерируемой генераторной функцией. После этого выполнение функции продолжается с того же самого места, где оно
# было остановлено.
# Выражение yield может использоваться в любом выражении, где ожидается значение, и представляет
# собой генераторное выражение. Оно также создает объект-итератор и возвращает каждый элемент последовательности по
# запросу. Однако, в отличие от оператора yield, выражение yield не останавливает выполнение функции, а просто
# возвращает значение итератора.Таким образом, оператор yield используется для создания генераторных функций, а
# выражение yield - для создания генераторных выражений.

# Пример использования оператора yield для создания генератора:

def countdown(n):
    while n > 0:
        yield n
        n -= 1


for i in countdown(5):
    print(i)

l = [1, 2, 3, 4, 5, 6, 7, 8]
for i in countdown(l):
    print(i)


# В этом примере функция countdown является генераторной функцией, которая производит последовательность чисел
# от n до 1. Каждый вызов оператора yield приостанавливает выполнение функции и возвращает очередное значение из
# последовательности.

# Пример использования выражения yield для создания генераторного выражения:
def countdown(n):
    yield from n


squares = (x ** 2 for x in range(10))
for square in squares:
    print(square)


# В этом примере выражение (x**2 for x in range(10)) является генераторным выражением, которое производит
# последовательность квадратов чисел от 0 до 9. Значение каждого выражения x**2 возвращается по запросу, когда оно
# запрашивается в цикле for.


#################
# _________3.9 Магические методы __iter__ и __next______Egorof_________

class Marks:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        print('call iter Mark')
        return self

    def __next__(self):
        if self.index >= len(self.values):
            self.index = 0
            raise StopIteration
        mark = self.values[self.index]
        self.index += 1
        return f'call next, mark = {mark}'


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        print('call iter Student')
        self.index = 0
        return self.marks

    # def __next__(self):
    #     if self.index >= len(self.marks):
    #         raise StopIteration
    #     res = self.marks[self.index]
    #     self.index += 1
    #     return f'call next Student = {res}'


misha_marks = Marks([3, 4, 5])
misha = Student('Misha', 'Ivanov', misha_marks)
for m in misha:
    print(m)


########################################################################
# Ниже в коде представлена реализация карточной колоды при помощи классов Card и Deck.
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        res = self.cards[self.index]
        self.index += 1
        return res  # вызов Card(rank, suit)
        # return f"{self.cards[self.index].rank} {self.cards[self.index].suit}"


deck = Deck()
for card in deck:
    print(card)
    # 2 Clubs 3 Clubs 4 Clubs5 Clubs6 Clubs7 Clubs8 Clubs9 Clubs10 ClubsJ ClubsQ Clubs
    # K ClubsA Clubs.....


###############################################################################################################################################
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return iter(self.cards)


########################################################################
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __getitem__(self, i):
        return self.cards[i].rank, self.cards[i].suit


deck = Deck()
for card in deck:
    print(*card)


########################################################################
# метод __iter__  возвращает генератор по шаблону ответа
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return (f'{i.rank} {i.suit}' for i in self.cards)


########################################################################
class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.cards):
            raise StopIteration
        return self.cards[self.index].rank, self.cards[self.index].suit


deck = Deck()
for card in deck:
    print(*card)


#######################################################################
class Deck:
    ranks = [*map(str, range(2, 11))] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return map(lambda x: f'{x.rank} {x.suit}', self.cards)


[print(card) for card in Deck()]


########################################################################
# Ниже в коде представлена реализация класса FileReader, который должен при итерирации считывать построчно содержимое
# файлаВаша задача дописать метод __next__, чтобы он возвращал по порядку строки из файла, пока содержимое файла не
# закончится. Строку нужно очистить слева и справа от символов пробелов и переносов на новую строку
# text = 'Lorem ipsum dolor sit amet consectetur adipiscing elit Cras euismod ex a ante sollicitudin' \
#        ' sollicitudin gravida massa bibendum Pellentesque quis mi ultricies gravida purus placerat   aliquam sapien
#        'fringilla velit at lobortis interdum elit augue faucibus nuncet ullamcorper nisl lorem vitae risus Fusce magn

class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.file).strip()


for line in FileReader('lorem.txt'):
    print(line)


    #########################################################################
    def __next__(self):
        line = self.file.readline().strip()
        if line:
            return line
        self.file.close()
        raise StopIteration


    #######################################################################
    def __iter__(self):
        return self.file
        # return (line.strip() for line in self.file.readlines())


    def __next__(self):
        for line in self.file.readlines():
            return line

for line in FileReader('lorem.txt'):
    print(line.strip())


    ########################################################################
    def __next__(self):
        text_str = self.file.readline().strip()
        if not text_str:
            raise StopIteration
        return text_str


###############################################################################################################################################
class FileReader:
    def __init__(self, filename):
        self.file = open(filename)
        self.lines = self.file.readlines()

    def __iter__(self):
        self.value = - 1
        return self

    def __next__(self):
        self.value += 1
        if self.value < len(self.lines):
            return self.lines[self.value].strip()
        else:
            raise StopIteration


########################################################################
# Создайте класс Countdown, который должен принимать начальное значение и вести обратный отсчет до нуля,
# возвращая каждое значение в последовательности каждый раз, когда вызывается __next__. Когда обратный отсчет
# достигает нуля, итератор должен вызвать исключение StopIteration. Для этого вам понадобиться реализовать:
# метод __init__. Он должен принимать одно положительное число - начало отсчета
# методы __iter__ и __next__ для итерирования по значениям класса Countdown.
class Countdown:
    def __init__(self, value):
        self.length = list(range(value + 1))

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        while self.index > -len(self.length) - 1:
            res = self.length[self.index]
            self.index -= 1
            return res
        raise StopIteration


########################################################################
class Countdown:
    def __init__(self, value):
        self.length = sorted(list(range(value + 1)), reverse=True)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.length):
            raise StopIteration
        res = self.length[self.index]
        self.index += 1
        return res


########################################################################
class Countdown:
    def __init__(self, value):
        self.length = sorted(list(range(value + 1)), reverse=True)

    def __iter__(self):
        return iter(self.length)

    def __next__(self):
        while self.length:
            return next(self.length)
        raise StopIteration


#######################################################################
class Countdown:
    def __init__(self, value):
        self.length = sorted(list(range(value + 1)), reverse=True)

    def __iter__(self):
        return iter(self.length)

    def __next__(self):
        return self.length


########################################################################
# Создайте класс PowerTwo, который возвращает следующую степень двойки, начиная с нулевой степени (20=1). Внутри класса
# реализуйте:метод __init__. Он должен принимать одно положительное число - степень двойки, до которой нужно
# итеририроваться включительно (см пример ниже)методы __iter__ и __next__ для итерирования по степеням двойки


class PowerTwo:
    def __init__(self, value):
        self.value = list(range(value + 1))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.value):
            res = pow(2, self.value[self.index])
            self.index += 1
            return res
        raise StopIteration


for i in PowerTwo(4):  # итерируемся до 4й степени двойки
    print(i)

numbers = PowerTwo(2)

iterator = iter(numbers)

print(next(iterator))  # печатает 1
print(next(iterator))  # печатает 2
print(next(iterator))  # печатает 4
print(next(iterator))  # исключение StopIteration


########################################################################
class PowerTwo:
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index <= self.value:
            res = pow(2, self.index)
            self.index += 1
            return res
        raise StopIteration


#######################################################################
# получается, что вычисление всех значений и запись в память идет при инициализации.
class PowerTwo:
    def __init__(self, power):
        self.pow_gen = (2 ** p for p in range(power + 1))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.pow_gen)


########################################################################
# С помощью yield  мы запрашиваем следующий элемент в числовой последовательности. А next просто возвращает iter(self)
class PowerTwo:
    def __init__(self, num=0):
        self.num = num

    def __iter__(self):
        # return self
        for i in range(self.num + 1):
            m = 2 ** i
            yield m

    # def __next__(self):
    #     return iter(self)


#############################################################################################
# Создайте класс InfinityIterator, который реализует бесконечный итератор, который будет при каждой новой итерации или
# вызовы функции next будет возвращать число, увеличенное на 10 от предыдущего значения. Начинать нужно с нуля.

class InfinityIterator:
    def __init__(self, value=0):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        result = self.value
        self.value += 10
        return result


a = iter(InfinityIterator())
next(a)
next(a)
next(a)
next(a)


########################################################################
class InfinityIterator:
    def __iter__(self):
        self.index = -10
        return self

    def __next__(self):
        self.index += 10
        return self.index


########################################################################
class InfinityIterator:
    def __init__(self, value=0):
        self.value = value

    def __iter__(self):
        while True:
            yield self.value
            self.value += 10


########################################################################
# ____________iter____Balakiref___________________________________________
# Подвиг 3. Пусть в программе объявлен класс для реализации геометрической прогрессии:
class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration


g = GeomRange(1, 1.2, 2)
res = next(g)
res = next(g)


#######################################################################
class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration

    def __iter__(self):
        self.__value = self.start
        return self


g = GeomRange(1, 1.2, 2)
res = next(g)

it = iter(g)
res = next(g)
# Если строку с неправильным синтаксисом разбить на две, то она работает при обоих запусках:
for x in g: print(x)
for x in g: print(x)

# Это свидетельствует о том, что объект 'g' не является Итератором в классическом понимании. То есть он не опустошается
# после первого цикла for. Однако его размер 48 байт, как у обычного ('ленивого') итератора. Просто в этой реализации
# оператор 'for' создает итератор с обновленным значением self.value каждый раз, когда мы его запускаем. Для сравнения:
r = iter(range(5))
for x in r: print()
for x in r: print()


# Оператор 'for' сработает только один раз, потому что первый 'for' опустошает итератор.
#
# многоразовый range:

class ReusableRange:
    def __init__(self, start=0, stop=None, step=1):
        if stop is None:
            stop, start = start, 0
        self._range = range(start, stop, step)
        self._iter = iter(self._range)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._iter)
        except StopIteration:
            self._iter = iter(self._range)
            raise


# создание нового итератора (self._iter = iter(self._range)) после опустошения текущего дает возможность опустошать его
# сколь угодно раз:
numbers = ReusableRange(10)
list(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(numbers)


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
########################################################################
# Подвиг 5. Объявите в программе класс Person, объекты которого создаются командой:
# p = Person(fio, job, old, salary, year_job)где fio - ФИО сотрудника (строка); job - наименование должности
# (строка); old - возраст (целое число); salary - зарплата (число: целое или вещественное); year_job - непрерывный стаж
# на указанном месте работы (целое число).В каждом объекте класса Person автоматически должны создаваться локальные
# атрибуты с такими же именами: fio, job, old, salary, year_job и соответствующими значениями.Также с объектами класса
# Person должны поддерживаться следующие команды:data = p[indx] # получение данных по порядковому номеру (indx)
# атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)p[indx] = value # запись в поле с указанным
# индексом (indx) нового значения valuefor v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary,
# year_job    print(v)При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в
# диапазоне [0; 4]. Иначе, генерировать исключение командой:raise IndexError('неверный индекс')
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.lst = [self.fio, self.job, self.old, self.salary, self.year_job]
        self.index = -1

    def __check_index(self, index):
        if index not in range(0, len(self.lst)):
            raise IndexError('неверный индекс')

    def __getitem__(self, index):
        self.__check_index(index)
        return self.lst[index]

    def __setitem__(self, index, value):
        self.__check_index(index)
        self.lst[index] = value

    # def __iter__(self):
    #     return self

    def __next__(self):
        self.index += 1
        while self.index < len(self.lst):
            return self.lst[self.index]
        raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)


########################################################################
# генерацию ошибок через декоратор
def error(func):
    def wrapper(*args):
        try:
            assert args[1] in range(0, 5)
            return func(*args)
        except:
            raise IndexError('неверный индекс')

    return wrapper


class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    @error
    def __getitem__(self, item):
        return self.__dict__[list(self.__dict__.keys())[item]]

    @error
    def __setitem__(self, item, value):
        self.__dict__[list(self.__dict__.keys())[item]] = value

    def __iter__(self):
        return iter(self.__dict__.values())


#######################################################################
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.lst = self.__dict__

    def __getitem__(self, item):
        if item < 0 or item > 4:
            raise IndexError('неверный индекс')
        return self.__dict__[list(self.lst.keys())[item]]

    def __setitem__(self, key, value):
        if key < 0 or key > 4:
            raise IndexError('неверный индекс')
        self.__dict__[list(self.lst.keys())[key]] = value

    def __iter__(self):
        self.value = -1
        return self

    def __next__(self):
        if self.value < 4:
            self.value += 1
            return self.__dict__[list(self.lst.keys())[self.value]]
        else:
            raise StopIteration


########################################################################
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__keys = tuple(self.__dict__.keys())

    def __getitem__(self, key):
        self.__validate_key(key)
        return getattr(self, self.__keys[key])

    def __setitem__(self, key, value):
        self.__validate_key(key)
        setattr(self, self.__keys[key], value)

    def __next__(self):
        if self.value >= 4:
            raise StopIteration
        self.value += 1
        return self[self.value]

    def __iter__(self):
        self.value = -1
        return self

    @staticmethod
    def __validate_key(key):
        if not isinstance(key, int) or key not in range(5):
            raise IndexError('неверный индекс')


###############################################################################################################################################
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.order = list(self.__dict__.keys())

    def __getitem__(self, indx):
        try:
            return getattr(self, self.order[indx])
        except IndexError:
            raise IndexError('неверный индекс')

    def __setitem__(self, indx, value):
        try:
            setattr(self, self.order[indx], value)
        except IndexError:
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.order):
            raise StopIteration
        return self[self.index]


########################################################################

# при отсутствии метода __iter__ итератор формируется из правильно настроенного метода __getitem__.
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __raise(self):
        raise IndexError('неверный индекс')

    def __getitem__(self, idx):
        try:
            return list(self.__dict__.items())[idx][1]
        except IndexError:
            self.__raise()

    def __setitem__(self, idx, value):
        try:
            key = list(self.__dict__.keys())[idx]
            self.__dict__[key] = value
        except IndexError:
            self.__raise()


########################################################################
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.attr = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __getitem__(self, item):
        self.__check_indx(item)
        return self.attr[item]

    def __setitem__(self, item, value):
        self.__check_indx(item)
        self.attr[item] = value

    def __check_indx(self, indx):
        if type(indx) != int or not 0 <= indx <= 4:
            raise IndexError('неверный индекс')


########################################################################
self.card = [self.fio, self.job, self.old, self.salary, self.year_job]


@staticmethod
def check_indx(indx):
    if 0 <= indx <= 4 and type(indx) == int:
        return True
    else:
        raise IndexError('неверный индекс')


def __getitem__(self, item):
    if self.check_indx(item):
        return self.card[item]


def __setitem__(self, key, value):
    if self.check_indx(key):
        self.card[key] = value


def __iter__(self):
    return iter(self.card)


#######################################################################
@staticmethod
def __check_indx(indx):
    if not isinstance(indx, int) or indx not in range(0, 5):
        raise IndexError('неверный индекс')
    return True


def __getitem__(self, item):
    self.__check_indx(item)
    key = tuple(self.__dict__)[item]
    return getattr(self, key)


def __setitem__(self, key, value):
    self.__check_indx(key)
    key = tuple(self.__dict__)[key]
    setattr(self, key, value)


def __iter__(self):
    self.value = -1
    return self


def __next__(self):
    if self.value < 4:
        self.value += 1
        return self[self.value]
    else:
        raise StopIteration


########################################################################
# Подвиг 6. Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных) списков
# следующей структуры:lst = [[x00],       [x10, x11],       [x20, x21, x22],       [x30, x31, x32, x33],       ... ]
# Для этого необходимо в программе объявить класс с именем TriangleListIterator, объекты которого создаются командой:
# it = TriangleListIterator(lst)где lst - ссылка на перебираемый список.Затем, с объектами класса TriangleListIterator
# должны быть доступны следующие операции:for x in it:  # последовательный перебор всех элементов списка:
# x00, x10, x11, x20, ...    print(x)it_iter = iter(it)x = next(it_iter)Итератор должен перебирать элементы
# списка по указанной треугольной форме. Даже если итератору на вход будет передан прямоугольная таблица
# (вложенный список), то ее перебор все равно должен осуществляться по треугольнику. Если же это невозможно
# (из-за структуры списка), то естественным образом должна возникать ошибка IndexError: index out of range (выход
# индекса за допустимый диапазон)

class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i + 1):
                yield self.lst[i][j]  # вернёт генератор, а for ч/з next будет перебирать


######################################################################################
def __iter__(self):
    return iter(self.lst[i][j] for i in range(len(self.lst)) for j in range(i + 1))


#########################################################################################
def __iter__(self):
    return iter(j for i in range(len(self.lst)) for j in self.lst[i][:i + 1])


########################################################################


def __iter__(self):
    self.ind = 1
    for i in range(len(self.lst)):
        for j in self.lst[i][:self.ind]:
            yield j
        self.ind += 1

    ########################################################################


def __iter__(self):
    self.ind = 1
    for i in self.lst:
        for j in i[:self.ind]:
            yield j
        self.ind += 1


#######################################################################
class TriangleListIterator:
    def __init__(self, lst):
        self.__lst = lst

    def __iter__(self):
        self.__col = self.__row = -1
        return self

    def __next__(self):
        if self.__row == self.__col:
            self.__row += 1
            self.__col = 0
        else:
            self.__col += 1

        if self.__row == len(self.__lst):
            raise StopIteration

        return self.__lst[self.__row][self.__col]


#######################################################################
class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.idx = [0, 0]
        return self

    def __next__(self):
        r, c = self.idx
        if r > len(self.lst) - 1:
            raise StopIteration
        self.idx = (r, c + 1) if c < r else (r + 1, 0)
        return self.lst[r][c]


########################################################################
class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst  # ссылка на перебираемый список

    def __iter__(self):
        self.length = len(self.lst)  # длина (количество "строк") двумерного списка
        self.i = 0  # начальное значения для перебора "строк" двумерного списка
        self.j = -1  # начальное значения для перебора элементов в "строке"
        return self

    def __next__(self):
        if self.j + 1 < len(self.lst[self.i]):
            self.j += 1
            return self.lst[self.i][self.j]
        else:
            self.i += 1
            self.j = 0
            if self.i >= self.length:
                raise StopIteration
            return self.lst[self.i][self.j]


###############################################################################################################################################
class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.gener = ((i, j) for i in range(len(self.lst)) for j in range(i + 1))

    def __next__(self):
        i, j = next(self.gener)
        return self.lst[i][j]

    def __iter__(self):
        self.gener = ((i, j) for i in range(len(self.lst)) for j in range(i + 1))
        return self


########################################################################
class TriangleListIterator:
    def __init__(self, lst):
        self._lst = lst
        self.row = self.col = -1

    def __iter__(self):
        self.row = self.col = -1
        return self

    def __next__(self):
        if self.row == self.col:
            self.row += 1
            self.col = -1
        self.col += 1
        if self.row > len(self._lst) - 1:
            raise StopIteration
        if self.col > len(self._lst[self.row]) - 1:
            raise IndexError
        return self._lst[self.row][self.col]


########################################################################
class TriangleListIterator:
    def __init__(self, lst=[]):
        self.lst = lst

    def __iter__(self):
        l = []
        for i in self.lst:
            for j in i:
                l.append(j)
        return iter(l)


########################################################################
# Подвиг 7. Теперь, вам необходимо разработать итератор, который бы перебирал указанные столбцы двумерного списка.
# Список представляет собой двумерную таблицу из данных:lst Для этого в программе необходимо объявить класс с
# именем IterColumn, объекты которого создаются командой:it = IterColumn(lst, column)где lst - ссылка на двумерный
# список; column - индекс перебираемого столбца (отсчитывается от 0).
class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in range(len(self.lst)):
            yield lst[i][self.column]


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)


#######################################################################
class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for row in self.lst:
            yield row[self.column]


########################################################################
class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        g = (row[self.column] for row in self.lst)  # создаём генератор
        return iter(g)  # перебираем генератор

    ########################################################################
    def __iter__(self):
        g = (row[self.column] for row in self.lst)
        yield from g
        # аналог :
        for i in g:
            yield i


#######################################################################
class IterColumn:
    def __init__(self, lst, column):
        self.__lst = lst
        self.__col = column

    def __iter__(self):
        self.rows = -1
        return self

    def __next__(self):
        self.rows += 1
        if self.rows == len(self.__lst):
            raise StopIteration
        return self.__lst[self.rows][self.__col]


########################################################################
class IterColumn:
    def __init__(self, lst, col):
        self.lst = lst
        self.col = col

    def __iter__(self):
        return iter([*zip(*self.lst)][self.col])


###############################################################################################################################################
# Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:
# Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:Stack - для представления стека в целом;
# StackObj - для представления отдельных объектов стека.В классе Stack должны быть методы:
# push_back(obj) - для добавления нового объекта obj в конец стека;push_front(obj) - для добавления нового объекта
# obj в начало стека.В каждом объекте класса Stack должен быть публичный атрибут:top - ссылка на первый объект стека
# (при пустом стеке top = None).Объекты класса StackObj создаются командой:obj = StackObj(data)где data - данные,
# хранящиеся в объекте стека (строка).Также в каждом объекте класса StackObj должны быть публичные атрибуты:
# data - ссылка на данные объекта;next - ссылка на следующий объект стека (если его нет, то next = None).
# Наконец, с объектами класса Stack должны выполняться следующие команды:st = Stack()st[indx] = value # замена прежних
# данных на новые по порядковому индексу (indx); отсчет начинается с нуляdata = st[indx]  # получение данных из
# объекта стека по индексу n = len(st) # получение общего числа объектов стека for obj in st: # перебор объектов стека
# (с начала и до конца)    print(obj.data)  # отображение данных в консольПри работе с индексами (indx),
# нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе,
# генерировать исключение командой:raise IndexError('неверный индекс')
class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj  # для связки
        self.last = obj

    def push_front(self, obj):
        if self.top is None:
            self.last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __len__(self):
        # return sum(1 for _ in self.__dict__.keys())
        return sum(1 for _ in self)

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next

    def __get_obj_index(self, item):  # взятие объекта по индексу
        if type(item) != int or not (0 <= item < len(self.__dict__)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__get_obj_index(item)
        for i, obj in enumerate(self):  # self является итератором
            # for i, obj in enumerate(self.__dict__.values()):
            if i == item:
                return obj.data

    def __setitem__(self, key, value):
        self.__get_obj_index(key)
        for i, obj in enumerate(self):  # self является итератором
            if i == key:
                obj.data = value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


st = Stack()

st[0] = 'value'  # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[0]  # получение данных из объекта стека по индексу
n = len(st)  # получение общего числа объектов стека

for obj in st:  # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль


########################################################################
class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj  # для связки
        self.last = obj

    def push_front(self, obj):
        if self.top is None:
            self.last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __len__(self):
        # return sum(1 for _ in self.__dict__.keys())
        return sum(1 for _ in self)

    def __iter__(self):
        self.h = self.top
        return self
        # метод __iter__ должен возвращать объект-итератор, а не просто устанавливать какое-то состояние. При вызове
        # метода __iter__ он инициализирует начальное состояние объекта-итератора и возвращает его. Затем этот объект
        # используется для последующего перебора элементов в цикле for.В данном коде, при создании объекта-итератора
        # в методе __iter__, переменная self.current устанавливается в self.top, то есть на первый элемент стека,
        # таким образом гарантируя, что итерация начнется с начала стека при использовании for obj in st:. Если бы
        # мы установили self.current = self.top в методе __next__ вместо метода __iter__, то каждый раз при переборе
        # элементов стека циклом for, итератор бы начинался с самого начала, что может привести к непредсказуемому
        # поведению в случае измененhа внутри цикла.

    def __next__(self):
        # Метод __next__ теперь использует цикл for, используя переменную self.h как начальное состояние. Цикл
        # выполняется, пока self.h не станет None, и при каждой итерации он возвращает следующий элемент из стека.
        # if self.h:
        #     next = self.h
        #     self.h = self.h.next
        #     return next
        # else:
        #     raise StopIteration()
        while self.h is not None:
            next = self.h
            self.h = self.h.next
            return next
        raise StopIteration()

    def __get_obj_index(self, item):  # взятие объекта по индексу
        if type(item) != int or not (0 <= item < len(self.__dict__)):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__get_obj_index(item)
        for i, obj in enumerate(self):  # self является итератором
            if i == item:
                return obj.data

    def __setitem__(self, key, value):
        self.__get_obj_index(key)
        for i, obj in enumerate(self):  # self является итератором
            if i == key:
                if i == 0:
                    obj.data = value

    ########################################################################
    def __iter__(self):
        self.h = self.top
        while self.h is not None:
            yield self.h
            self.h = self.h.next


########################################################################
class StackObj:

    def __init__(self, data):
        self.__next = None
        self.data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


class Stack:
    # Метод __getitem__ в данном классе используется для получения значения элемента стека по его индексу. При вызове
    # метода с аргументом get_data=True, он возвращает значение (атрибут data) элемента стека, соответствующего данному
    # индексу. А при передаче аргумента False, метод возвращает сам элемент стека (StackObj), а не его значение.
    # В строке root = self.__getitem__(self.__count - 1, False), метод __getitem__ вызывается с параметрами
    # self.__count - 1 и False. Это означает, что будет получен последний элемент стека (так как индекс последнего
    # элемента равен self.__count - 1), но не его значение. Полученный объект будет присвоен переменной root.
    def __init__(self):
        self.top = None
        self.__count = 0

    @staticmethod
    def check_index(idx, count):
        if not (isinstance(idx, int) and 0 <= idx < count):
            raise IndexError('неверный индекс')

    def __len__(self):
        return self.__count

    def push_back(self, obj):
        if not isinstance(obj, StackObj):
            return
        if self.__count == 0:
            self.top = obj
        else:
            root = self.__getitem__(self.__count - 1, False)
            root.next = obj
        self.__count += 1

    def push_front(self, obj):
        if not isinstance(obj, StackObj):
            return
        if self.__count == 0:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj
        self.__count += 1

    def pop(self):
        if self.__count == 1:
            obj = self.top
            self.top = None
        elif self.__count > 1:
            obj = self.__getitem__(self.__count - 1)
            prev = self.__getitem__(self.__count - 2)
            prev.next = None
        self.__count -= 1
        return obj

    def __getitem__(self, idx, get_data=True):
        self.check_index(idx, self.__count)
        if idx == 0:
            return self.top.data if get_data else self.top
        count, root = 0, self.top
        while count < idx:
            count += 1
            root = root.next
        return root.data if get_data else root

    def __setitem__(self, idx, value):
        self.check_index(idx, self.__count)
        if idx == 0:
            next = self.top.next
            self.top.data = value
            self.next = next
        else:
            root = self.__getitem__(idx, False)
            prev = self.__getitem__(idx - 1, False)
            next = root.next
            root.data = value
            root.next, prev.next = next, root

    def __iter__(self):
        for i in range(len(self)):
            yield self.__getitem__(i, False)


#######################################################################
# Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:Каждая ячейка таблицы должна быть
# представлена классом Cell. Объекты этого класса создаются командой:Cell = Cell(data)где data - данные в ячейке. В
# каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с соответствующим значением.
# Для работы с ним в классе Cell должно быть объект-свойство (property):data - для записи и считывания информации из
# атрибута __data.Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:
# table = TableValues(rows, cols, type_data)где rows, cols - число строк и столбцов таблицы; type_data - тип данных
# ячейки (int - по умолчанию, float, list, str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).
# С объектами класса TableValues должны выполняться следующие команды:table[row, col] = value# запись нового значения
# в ячейку с индексами row, col (индексы отсчитываются с нуля)value = table[row, col] # считывание значения из ячейки
# с индексами row, colfor При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с
# атрибутом type_data объекта класса TableValues), должно генерироваться исключение командой:
# raise TypeError('неверный тип присваиваемых данных')При работе с индексами row, col, необходимо проверять их
# корректность. Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение
# командой:raise IndexError('неверный индекс')
class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))
        # self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __check_index(self, index):
        r, c = index
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, index):
        self.__check_index(index)
        r, c = index
        # return self.cells[index[0]][index[1]].data
        return self.cells[r][c].data

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.cells[key[0]][key[1]].data = value

    def __iter__(self):
        for row in self.cells:
            yield (i.data for i in row)


cell = Cell(0)
table = TableValues(2, 2, int)
table[0, 0] = 12  # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[0, 0]  # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row:  # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()


    ########################################################################
    def __iter__(self):
        # for row in self.cells:
        #     for key in row:
        #         yield [key.data]
        # for row in self.cells:
        #     yield tuple(i.data for i in row)
        #     # yield [i.data for i in row]
        for row in self.cells:
            for key in row:
                yield (key.data,)

# так не работает
# for row in self.cells:
#     for key in row:
#         yield tuple(key.data)
# потому что:
#  Проблема в методе __iter__(self). В текущей реализации он возвращает только  значения ячеек (key.data) из каждой
# строки, а не целые строки. И когда вы выполняете цикл for row in table, каждый элемент row - это число (значение
# одной ячейки), и при попытке перебрать его циклом for value in row возникает ошибка 'int' object is not iterable.
# вы используете tuple() для создания кортежа из единственного элемента key.data. Однако, переменная key не является
# отдельным элементом, а является словарем, содержащим data в качестве ключа. Поэтому использование tuple() для
# создания кортежа из одного элемента не является правильным способом создания кортежа.


# но вот так всё работает и итерируется
# for row in self.cells:
#     for key in row:
#         yield [key.data]
# Во втором коде вы используете [key.data] для создания списка с одним элементом key.data. Это работает, потому что вам
# нужно создать список, а не кортеж, и вы непосредственно добавляете элемент key.data в список.
# Если вы хотите создать кортеж из одного элемента, то можно использовать следующий синтаксис: (key.data,). Обратите
# внимание на запятую после key.data, которая говорит Python, что это кортеж, а не просто выражение в скобках.
#         for row in self.cells:
#             for key in row:
#                 yield (key.data,)


cell = Cell(0)
table = TableValues(2, 2, int)
table[0, 0] = 12  # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[0, 0]  # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row:  # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()


    ############################################################################
    def __iter__(self):
        self.indx = -1
        return self


    def __next__(self):
        if self.indx + 1 < len(self.__cells):
            self.indx += 1
            return (i.data for i in self.__cells[self.indx])
            #
            for i in self.__cells[self.indx]:
                return [i.data]
            #
            return map(lambda x: x.data, self.__cells[self.indx])
            return iter(map(lambda x: x.data, self.__cells[self.indx]))
        else:
            raise StopIteration


    #######################################################################

    ########################################################################
    def __iter__(self):
        return (iter(j.data for j in i) for i in self.cells)


    #######################################################################
    def __iter__(self):
        self.__n_row = -1
        return self


    @staticmethod
    def row_iter(row):
        for el in row:
            yield el.data


    def __next__(self):
        if self.__n_row + 1 < len(self.__cells):
            self.__n_row += 1
            return self.row_iter(self.__cells[self.__n_row])
        else:
            raise StopIteration


########################################################################
# Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны
# создаваться командой:m1 = Matrix(rows, cols, fill_value)где rows, cols - число строк и столбцов матрицы;
# fill_value - заполняемое начальное значение элементов матрицы (должно быть число: целое или вещественное).
# Если в качестве аргументов передаются не числа, то генерировать исключение:raise TypeError('аргументы rows, cols -
# целые числа; fill_value - произвольное число')Также объекты можно создавать командой:m2 = Matrix(list2D)
# де list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не
# прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:
# raise TypeError('список должен быть прямоугольным, состоящим из чисел')Для объектов класса Matrix должны выполняться
# следующие команды:matrix = Matrix(4, 5, 0)res = matrix[0, 0] # возвращается первый элемент матрицы
# matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
# Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:
# raise TypeError('значения матрицы должны быть числами')Если указываются недопустимые индексы матрицы (должны быть
# целыми числами от 0 и до размеров матрицы), то генерировать исключение:raise IndexError('недопустимые значения
# индексов')Также с объектами класса Matrix должны выполняться операторы:
# matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
# matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
# matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
# matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
# Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не
# совпадают (разные хотя бы по одной оси), то генерировать исключение командой:
# raise ValueError('операции возможны только с матрицами равных размеров')


class Matrix:
    def __init__(self, rows, cols=None, fill_value=None):
        if type(rows) == list:  # rows в виде list
            self.rows = len(rows)
            self.cols = len(rows[0])
            if not all(len(r) == self.cols for r in rows) or not all(self.__is_digit(x) for row in rows for x in row):
                # if not self.__check_rows_int(rows) or not self.__check_rows(rows):  # or not self.__check_rows(rows)
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.lst = rows  # ссылается на переданный список
        else:
            if type(rows) != int or type(cols) != int or type(fill_value) not in [int, float]:
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.rows = rows
            self.cols = cols
            self.fill_value = fill_value
            self.lst = [[fill_value for _ in range(cols)] for _ in range(rows)]

    def __is_digit(self, x):
        return type(x) in (int, float)

    @staticmethod
    def __check_index(other):
        if type(other) not in (int, float):
            raise IndexError('недопустимые значения индексов')

    def __check_ind_(self, item):
        r, c = item
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item):
        self.__check_ind_(item)
        r, c = item[0], item[1]  # item
        return self.lst[r][c]

    def __setitem__(self, item, value):
        self.__check_ind_(item)
        # if type(value) not in [int, float]:
        #     raise TypeError('значения матрицы должны быть числами')
        if not self.__is_digit(value):
            raise TypeError('значения матрицы должны быть числами')
        r, c = item[0], item[1]
        self.lst[r][c] = value

    def __check_matrix(self, other):
        rows, cols = other.rows, other.cols
        if self.rows != rows or cols != other.cols:
            # if len(other.lst) != len(self.lst):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        # if isinstance(other, Matrix):
        if type(other) == type(self):
            self.__check_matrix(other)
            # self.lst = [list(zip(self.lst[i], other.lst[i])) for i in range(len(self.lst))]
            return Matrix([[self[i, j] + other[i, j] for j in range(self.cols)] for i in range(self.rows)])
            # Matrix([[self.lst[i][j] + other.lst[i][j] for j in self.cols] for i in range(self.rows)])
            # Matrix([[self.lst[i][j] + other.lst[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst))])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if type(other) == type(self):
            self.__check_matrix(other)
            return Matrix(
                [[self.lst[i][j] - other.lst[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst))])
        else:
            return Matrix(
                [[self.lst[i][j] - other for j in range(len(self.lst[i]))] for i in range(len(self.lst))])


###############################################################################################################################################
class Matrix:
    def __init__(self, rows, cols=None, fill_value=None):
        if type(rows) == list:  # rows в виде list
            self.rows = len(rows)
            self.cols = len(rows[0])
            if not self.__check_rows_int(rows) or not self.__check_rows(rows):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.lst = rows  # ссылается на переданный список
        else:
            if type(rows) != int or type(cols) != int or type(fill_value) not in [int, float]:
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.rows = rows
            self.cols = cols
            self.fill_value = fill_value
            self.lst = [[fill_value for _ in range(cols)] for _ in range(rows)]

    @staticmethod
    def __check_rows(rows):
        for row in rows:
            if len(row) != len(rows[0]):
                return False
        return True  # список должен быть прямоугольным

    def __is_digit(self, x):
        return type(x) in (int, float)

    @staticmethod
    def __check_rows_int(rows):
        for row in rows:
            for i in row:
                if type(i) != int:
                    return False
        return True  # состоящим из чисел
        # return all(type(i) == int for row in rows for i in row)

    @staticmethod
    def __check_index(other):
        if type(other) not in (int, float):
            raise IndexError('недопустимые значения индексов')

    def __check_ind_(self, item):
        r, c = item
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item):
        self.__check_ind_(item)
        r, c = item[0], item[1]  # item
        return self.lst[r][c]

    def __setitem__(self, item, value):
        self.__check_ind_(item)
        if not self.__is_digit(value):
            raise TypeError('значения матрицы должны быть числами')
        r, c = item[0], item[1]
        self.lst[r][c] = value

    def __check_matrix(self, other):
        rows, cols = other.rows, other.cols
        if self.rows != rows or cols != other.cols:
            # if len(other.lst) != len(self.lst):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        if isinstance(other, Matrix):
            self.__check_matrix(other)
            return Matrix(
                [[self.lst[i][j] + other.lst[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst))])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if type(other) == type(self):
            self.__check_matrix(other)
            return Matrix(
                [[self.lst[i][j] - other.lst[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst))])
        else:
            return Matrix(
                [[self.lst[i][j] - other for j in range(len(self.lst[i]))] for i in range(len(self.lst))])


########################################################################
from operator import add, sub


class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            if not all(map(isinstance, args, [int, int, (int, float)])):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.rows, self.cols, fill_value = args
            self.table = [[fill_value] * self.cols for _ in range(self.rows)]
        elif len(args) == 1:
            lst, = args
            self.rows = len(lst)
            self.cols = len(lst[0])
            check_length = lambda x: len(x) == self.cols
            if all(map(check_length, lst)) and all(isinstance(x, (int, float)) for row in lst for x in row):
                self.table = lst
            else:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def check_indx(self, i, j):
        if not (0 <= i < self.rows and 0 <= j < self.cols):
            raise IndexError('недопустимые значения индексов')

    def check_equal(self, other):
        if not (self.rows == other.rows and self.cols == other.cols):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __getitem__(self, item):
        i, j = item
        self.check_indx(i, j)
        return self.table[i][j]

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        i, j = key
        self.check_indx(i, j)
        self.table[i][j] = value

    def __iter__(self):
        return (col for row in self.table for col in row)

    def calculate(self, op, it2):
        temp = Matrix(self.rows, self.cols, 0)
        it1 = iter(self)
        for i in range(self.rows):
            for j in range(self.cols):
                temp.table[i][j] = op(next(it1), next(it2))
        return temp

    def operation(self, op, other):
        if isinstance(other, Matrix):
            self.check_equal(other)
            return self.calculate(op, iter(other))
        elif isinstance(other, (float, int)):
            return self.calculate(op, iter([other] * self.rows * self.cols))

    def __add__(self, other):
        return self.operation(add, other)

    def __sub__(self, other):
        return self.operation(sub, other)


#######################################################################################################
class Matrix:
    def __init__(self, rows_or_list2D, cols=None, fill_value=None):
        if cols is not None and fill_value is not None:
            self.rows = rows_or_list2D
            self.cols = cols
            self.matrix = [[fill_value for j in range(cols)] for i in range(rows_or_list2D)]
        else:
            list2D = rows_or_list2D
            rows = len(list2D)
            if rows == 0:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            cols = len(list2D[0])
            for row in list2D:
                if len(row) != cols:
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
                for elem in row:
                    if not isinstance(elem, (int, float)):
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.rows = rows
            self.cols = cols
            self.matrix = list2D

    def __getitem__(self, indexes):
        i, j = indexes
        return self.matrix[i][j]

    def __setitem__(self, indexes, value):
        i, j = indexes
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            raise IndexError('недопустимые значения индексов')
        self.matrix[i][j] = value

    def __add__(self, other):
        if not isinstance(other, Matrix):
            other = Matrix(self.rows, self.cols, other)
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')
        result = Matrix(self.rows, self.cols, 0)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] + other[i, j]
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            other = Matrix(self.rows, self.cols, other)
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')
        result = Matrix(self.rows, self.cols, 0)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] - other[i, j]
        return result

    def __rsub__(self, other):
        return self.__sub__(other)


########################################################################
# Техническое задание Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом.
# Объекты этого класса будут создаваться командой:game = TicTacToe()В каждом объекте этого класса должен быть
# публичный атрибут:pole - двумерный кортеж, размером 3x3.Каждый элемент кортежа pole является объектом класса Cell:
# cell = Cell()В объектах этого класса должно автоматически формироваться локальное свойство:value - текущее значение
# в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.Также с объектами класса Cell должна выполняться
# функция:bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.
# К каждой клетке игрового поля должен быть доступ через операторы:res = game[i, j] # получение значения из клетки с
# индексами i, jgame[i, j] = value # запись нового значения в клетку с индексами i, jЕсли индексы указаны неверно
# (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение командой:
# raise IndexError('некорректно указанные индексы')Чтобы в программе не оперировать величинами: 0 - свободная
# клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны быть три публичных атрибута (атрибуты класса):
# FREE_CELL = 0      # свободная клеткаHUMAN_X = 1        # крестик (игрок - человек)COMPUTER_O = 2     # нолик (игрок
# - компьютер)В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):
# init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
# show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
# human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
# computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).
# Также в классе TicTacToe должны быть следующие объекты-свойства (property):
# is_human_win - возвращает True, если победил человек, иначе - False;
# is_computer_win - возвращает True, если победил компьютер, иначе - False;
# is_draw - возвращает True, если ничья, иначе - False.Наконец, с объектами класса TicTacToe должна выполняться функция:
# bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в
# противном случае.Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе
########################################################################
from random import choice, randint, randrange


class Cell:
    def __init__(self):
        self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return not self.value
        # return self.value == 0  # True, если клетка свободна (value = 0)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.size = 3
        self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))
        self.lst_human = []
        self.lst_computer = []

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL
        self.lst_human = []
        self.lst_computer = []
        self.is_human_win
        self.is_computer_win
        self.is_draw

    def show(self):
        for row in self.pole:
            print()
            for cell in row:
                print(cell.value, end=' ')
        print()

    def human_go(self):
        # key_row = int(input("Enter index: "))
        # key_col = int(input("Enter index: "))
        # key = key_row, key_col,
        key = tuple(map(int, input('Enter index: ').split()))
        while self.__getitem__(key) != self.FREE_CELL:  # while key != 0
            print("Error, Enter index yet")
            key = tuple(map(int, input('Enter index: ').split()))
        self.__setitem__(key, self.HUMAN_X)

    def computer_go(self):
        key_row = randrange(len(self.pole))
        key_col = randrange(len(self.pole))
        key = key = key_row, key_col,
        # key = choice(choice(self.pole)).value
        # while key == self.FREE_CELL:
        while self.__getitem__(key) != self.FREE_CELL:  # FREE_CELL = 0 - свободная клетка
            key_row = randrange(len(self.pole))
            key_col = randrange(len(self.pole))
            key = key = key_row, key_col,
            # key = choice(choice(self.pole)).value
            # if self.FREE_CELL else choice(choice(self.pole)
        self.__setitem__(key, self.COMPUTER_O)

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = index
        if not 0 <= r < self.size or c not in range(self.size):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        self.pole[r][c].value = value
        self.is_human_win
        self.is_computer_win
        self.is_draw

    @property
    def is_human_win(self):
        for i in range(len(self.pole)):  # сумма по строкам
            v = 0
            for j in range(len(self.pole)):
                if self.pole[i][j].value == self.HUMAN_X:
                    v += 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        for i in range(len(self.pole)):  # сумма по столбцам
            x = -1
            v = 0
            for j in range(len(self.pole)):
                if self.pole[i][x + 1].value == self.HUMAN_X:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        for i in range(1):  # сумма по диагонали с (0,0) по (2,2)
            v = 0
            x = 0
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.HUMAN_X:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        for i in range(1):  # сумма по диагонали с (0,2) по (2,0)
            v = 0
            x = 2
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.HUMAN_X:
                    v += 1
                x -= 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        if 3 in self.lst_human:
            # print(self.lst_human)
            return True
        elif len(self.lst_human) == 0:
            return False
        else:
            return False

    @property
    def is_computer_win(self):
        for i in range(len(self.pole)):  # сумма по строкам
            v = 0
            for j in range(len(self.pole)):
                if self.pole[i][j].value == self.COMPUTER_O:
                    v += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        for i in range(len(self.pole)):  # сумма по столбцам
            x = -1
            v = 0
            for j in range(len(self.pole)):
                if self.pole[i][x + 1].value == self.COMPUTER_O:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        for i in range(1):  # сумма по диагонали с (0,0) по (2,2)
            v = 0
            x = 0
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.COMPUTER_O:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        for i in range(1):  # сумма по диагонали с (0,2) по (2,0)
            v = 0
            x = 2
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.COMPUTER_O:
                    v += 1
                x -= 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        if 3 in self.lst_computer:
            # print(self.lst_computer)
            return True  # победа
        elif len(self.lst_computer) == 0:
            return False
        else:
            return False

    @property
    def is_draw(self):  # возвращает True, если ничья,  - иначе - False.
        if not self.__bool__() and not self.is_human_win and not self.is_computer_win:
            return True  # ничья
        else:
            return False

    def __bool__(self):
        # возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.
        if not self.is_human_win and self.is_computer_win == False and any(
                cell.value == self.FREE_CELL for row in self.pole for cell in row):
            return True  # игра не окончена
        else:
            return False


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()
    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
    step_game += 1

print("Stop________________")
game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
elif game.is_draw:
    # else:
    print("Ничья.")

#
#######################################################################
from random import choice, randint, randrange


class Cell:
    def __init__(self):
        self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return self.value == 0  # True, если клетка свободна (value = 0)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.size = 3
        self.win = 0  # 0 - игра , 1 - победа человека, 2 - победа компьютера, 3 - ничья
        self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))

    def init(self):
        for i in range(self.size):
            for j in range(self.size):
                self.pole[i][j].value = 0
        self.win = 0  # 0 - игра

    def show(self):
        for row in self.pole:
            print(*map(lambda x: x.value, row))
        print('________________________________________________________________')

    def human_go(self):
        # if not self.__bool__():
        if not self:
            return
        while True:
            i, j = map(int, input('Enter index: ').split())
            if not (0 <= i < self.size) or not (0 <= j < self.size):
                continue
            # self.pole[y][x].value можно заменить на просто self[y, x], для этого и  __setitem__ создавали)
            if self[i, j] == self.FREE_CELL:  # отправляет в getitem
                self[i, j] = self.HUMAN_X  # отправляет в setitem
                break

    def computer_go(self):
        if not self:
            return
        while True:
            i = randint(0, self.size - 1)
            j = randint(0, self.size - 1)
            if self[i, j] != self.FREE_CELL:
                continue
            self[i, j] = self.COMPUTER_O
            break

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = index
        if not 0 <= r < self.size or c not in range(self.size):
            raise IndexError('некорректно указанные индексы')

    def __update_win_status(self):
        for row in self.pole:
            if all(i.value == self.HUMAN_X for i in row):  # проверка на выигрыш по строкам человека
                self.win = 1
                return
            if all(i.value == self.COMPUTER_O for i in row):
                self.win = 2
                return
        for i in range(self.size):  # проверка на выигрыш по столбцам человека
            if all(col.value == self.HUMAN_X for col in (row[i] for row in self.pole)):
                self.win = 1
                return
            if all(col.value == self.COMPUTER_O for col in (row[i] for row in self.pole)):
                self.win = 2
                return
        # проверка на выигрыш по диагоналям человека
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self.size)) \
                or all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(self.size)):
            self.win = 1
            return
        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self.size)) \
                or all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(self.size)):
            self.win = 2
            return
        # проверка на ничью
        if all(col.value != self.FREE_CELL for row in self.pole for col in row):
            self.win = 3
            return

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        self.pole[r][c].value = value
        self.__update_win_status()  # пересчёт статуса победителя

    @property
    def is_human_win(self):
        return self.win == 1

    @property
    def is_computer_win(self):
        return self.win == 2

    @property
    def is_draw(self):  # возвращает True, если ничья,  - иначе - False.
        return self.win == 3

    def __bool__(self):
        return self.win == 0 and self.win not in (1, 2, 3)


########################################################################
class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        '''Инициализация'''
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.free_cells = 9
        self.winner = None
        self.diagonals = [[self.pole[i][i] for i in range(3)], [self.pole[-i - 1][i] for i in range(-3, 0)]]
        # Список self.diagonals содержит все возможные диагонали на игровом поле, включая главную диагональ и все
        # побочные диагонали. Для каждой диагонали список элементов заполняется по порядку, начиная с верхнего левого
        # угла игрового поля и заканчивая нижним правым углом.
        for diag in self.diagonals:
            for cell in diag:
                cell._priority += 2

    def __getitem__(self, coords):
        '''Геттер значения клетки по координатам'''
        if self._valid_coords(*coords):
            return self.pole[coords[0]][coords[1]].value
        raise IndexError('некорректно указанные индексы')

    def __setitem__(self, coords, value):
        '''Сеттер значения клетки по координатам'''
        if not self._valid_coords(*coords):
            raise IndexError('некорректно указанные индексы')
        if value in (0, 1, 2):
            self.pole[coords[0]][coords[1]].value = value
        self.__bool__()

    def __bool__(self):
        '''Проверка окончена игра или нет'''
        for row in self.pole:  # перебор по строкам
            if not any(row) and len(set(row)) == 1:
                # any(row) xотя бы один элемент в последовательности True,т е. хотя бы один self.value = 0,т.к return
                # not self.value
                # not any(row) вернет False обращаясь к def __bool__(self):/ return not self.value когда self.value = 0,
                # если все элементы row являются ложными. это означает, что если все элементы
                # в ряду пустые (отсутствуют), то возвращается False, а если в ряду есть хотя бы один непустой элемент
                # и все элементы имеют одинаковое значение, то возвращается True. len(set(row)) возвращает количество
                # уникальных значений в строке. Если это значение равно 1, то все элементы в этой строке имеют одно и
                # то же значение, и выражение вернет True. len(set(row)) == 1 проверяет, что длина множества уникальных
                # элементов в списке row равна 1, то есть все элементы списка равны между собой. Если оба условия
                # истинны, то значит в данной строке все ячейки пустые и равны между собой, что соответствует ситуации
                # "ничья" в игре. Таким образом, если все клетки в первом столбце равны нулю, а в других столбцах есть
                # свободные клетки, то игра продолжится, и не будет закончена как ничья до тех пор, пока не будут
                # заполнены все клетки на игровом поле.
                self.winner = row[0].value  # определяется победитель
                return False  # был найден победитель, игра заканчивается и дальнейшие проверки уже не нужны.
        for col in zip(*self.pole):  # транспорнирование матрицы, перебор по столбцам
            # col будет содержать все элементы из одного столбца игрового поля.
            if not any(col) and len(set(col)) == 1:
                self.winner = col[0].value
                return False
        for diag in self.diagonals:
            # Каждый элемент списка diag представляет собой объект Cell
            if not any(diag) and len(set(diag)) == 1:
                self.winner = diag[0].value
                return False
        if self.free_cells == 0:
            self.winner = 0
            return False
        return True  # продолжение игры

    @property
    def is_human_win(self):
        return self.winner == self.HUMAN_X

    @property
    def is_computer_win(self):
        return self.winner == self.COMPUTER_O

    @property
    def is_draw(self):
        return self.winner == 0

    @classmethod
    def _valid_coords(cls, y, x):
        '''Проверка координат'''
        return type(y) == type(x) == int and 0 <= y < 3 and 0 <= x < 3

    def init(self):
        self.__init__()

    def human_go(self):
        '''Ход человека'''
        while True:
            print('Введите координаты свободной клетки через пробел:')
            coords = input()
            if len(coords.split()) != 2:
                print('Было введено неверное количество координат.')
                continue
            try:
                y, x = map(int, coords.split())
                if not self._valid_coords(y, x):
                    print('Введённые координаты вне диапазона поля.')
                    continue
            except ValueError:
                print('Введённые данные не являются координатами.')
                continue
            # if self.pole[y][x].value not in [1, 2]:
            if self.pole[y][x]:  # обращение к клетке а она обращается к __bool__(self): return not self.value  ->
                # self.value = 0 -> not False -> True
                # проверять, существует ли объект Cell для ячейки поля (y, x), но не будет проверять её значение.
                self.pole[y][x].value = self.HUMAN_X
                self.free_cells -= 1
                self._compute_priority(y, x)
                break
            else:
                print('Выбранная клетка занята.')
                continue

    def computer_go(self):
        '''Ход компьютера'''
        # собирает все клетки которые не заняты, if cell проверка не занята ли клетка через __bool__
        free_cells = [(y, x) for y, row in enumerate(self.pole) for x, cell in enumerate(row) if cell]
        y, x = max(free_cells, key=lambda c: self.pole[c[0]][c[1]]._priority)
        # координаты свободной ячейки с максимальным значением приоритета.
        if y == x == 1:  # Реакция на среднюю клетку
            for cell in (self.pole[0][1], self.pole[1][0], self.pole[1][2], self.pole[2][1]):
                cell._priority += 2
        self.free_cells -= 1
        self.pole[y][x].value = self.COMPUTER_O

    def _compute_priority(self, y, x):
        '''Просчёт хода компьютера'''
        # Реакция на ход противника
        # Метод self._compute_priority(y, x) используется для пересчёта приоритетов доступных ходов для игрока. Он
        # вызывается после того, как игрок сделал очередной ход в свободную ячейку поля.Для каждой свободной ячейки
        # поля метод вычисляет её приоритет, основываясь на том, сколько потенциальных выигрышных комбинаций может быть
        # построено, если игрок сделает ход в эту ячейку. Чем больше потенциальных выигрышных комбинаций можно
        # построить, тем выше приоритет у этой ячейки.Пересчёт приоритетов доступных ходов позволяет игроку выбирать
        # более "выгодные" ходы на каждом шаге игры и повышать свои шансы на победу.Кроме того, метод
        # self._compute_priority(y, x) также запускается один раз в начале игры, чтобы вычислить начальные приоритеты
        # для всех ячеек поля.
        for cell in self.pole[y]:
            cell._priority -= 1
        for cell in list(zip(*self.pole))[x]:
            cell._priority -= 1
        if y == x:
            for cell in self.diagonals[0]:
                cell._priority -= 1
        if y + x == 2:
            for cell in self.diagonals[1]:
                cell._priority -= 1
        # Корректировка опасности
        for row in self.pole + [list(lst) for lst in zip(*self.pole)] + self.diagonals:
            counter = [0, 0, 0]
            for cell in row:
                counter[cell.value] += 1
            if counter[1] == 2:
                for cell in row:
                    cell._priority = 5
            if counter[2] == 2:
                for cell in row:
                    cell._priority = 6

    def show(self):
        '''Отрисовка поля'''
        for row in self.pole:
            for cell in row:
                print(cell, end=' ')
            print()
        print('* ' * 10)


class Cell:
    def __init__(self):  # содержит значение клетки и приоритет.
        self.value = 0
        self._priority = 2
        # используется для определения приоритета клетки при выполнении каких-либо операций.

    def __bool__(self):
        return not self.value

    def __str__(self):
        if self.value == 1:
            return 'X'
        if self.value == 2:
            return '0'
        return '-'

    # __eq__ при проверке того, занята ли определенная клетка на игровом поле или нет
    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        # Хеш-код нужен, чтобы быстро и эффективно сравнивать объекты между собой быстро сравнить их между собой и
        # выполнить необходимые действия (например, проверить, занята ли определенная клетка на игровом поле или нет).
        return hash(self.value)


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()
    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
    step_game += 1

print("Stop____________________________________")
game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
    # elif game.is_draw:
else:
    print("Ничья.")


########################################################################

#######################################################################

########################################################################

###############################################################################################################################################

########################################################################

########################################################################

########################################################################

#######################################################################

########################################################################

########################################################################

#######################################################################

########################################################################

###############################################################################################################################################

########################################################################

########################################################################

########################################################################

#######################################################################

########################################################################

########################################################################

#######################################################################

########################################################################

###############################################################################################################################################

########################################################################

########################################################################

########################################################################

#######################################################################

########################################################################

########################################################################

#######################################################################

########################################################################

########################################################################
