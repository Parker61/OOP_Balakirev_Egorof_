# ________Egorof________________
class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyPoint(2 * self.x + other.x, 2 * self.y + other.y)


p1 = MyPoint(3, 4)
p2 = MyPoint(5, 12)
p3 = p1 + p2
print(p3.x + p3.y)


################################
# Создайте класс Rectangle, который имеет следующие методы:метод __init__, который устанавливает значения атрибутов
# width и height: ширина и высота прямоугольникамагический метод __add__, который описывает сложение двух
# прямоугольников. Результатом такого сложения должен быть новый прямоугольник, в котором ширина и высота получились
# в результате сложения исходных прямоугольников. Новый прямоугольник нужно вернуть в качестве результата вызова метода
# __add__. Сложения с другими типами данных реализовывать не нужно магический метод __str__, который возвращает
# строковое представление  прямоугольника в следующем виде:Rectangle({width}x{height})
# Напишите определение класса Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        # Type-хинты в методе __add__ в данном случае писать в кавычках (на момент парсинга метода класс Rectangle
        # ещё не определён). Вроде как начиная с Python3.11 можно писать typing.Self
        return Rectangle(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


# Ниже код для проверки методов класса Rectangle

r1 = Rectangle(5, 10)
assert r1.width == 5
assert r1.height == 10
print(r1)

r2 = Rectangle(20, 5)
assert r2.width == 20
assert r2.height == 5
print(r2)

r3 = r2 + r1
assert isinstance(r3, Rectangle)
assert r3.width == 25
assert r3.height == 15
print(r3)


################################################################
# Создайте класс  Order, который имеет следующие методы:метод __init__, который устанавливает значения атрибутов
# cart и customer: список покупок и имя покупателямагический метод __add__, который описывает добавления товара в
# список покупок. Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из старого
# заказа и в конец добавляется новый товар. Покупатель в заказе остается прежниммагический метод __radd__, который
# описывает добавления товара в список покупок при правостороннем сложении. Результатом такого сложения должен быть
# новый заказ, в котором все покупки берутся из старого заказа и в начало списка покупок добавляется новый товар.
# Покупатель в заказе остается прежним магический метод __sub__, который описывает исключение товара из списка покупок.
# Результатом вычитания должен быть новый заказмагический метод __rsub__, который описывает исключение товара из
# списка покупок при правостороннем вычитании. Результатом должен быть таким же как и при __sub__
class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        return Order(self.cart + [other], self.customer)

    def __radd__(self, other):
        if isinstance(other, str):
            return Order([other] + self.cart, self.customer)

    def __sub__(self, other):
        if other in self.cart:
            self.cart.remove(other)
        return self
        # return Order(self.cart, self.customer)

    def __rsub__(self, other):
        return self.__sub__(other)
        # return self - product

    def __repr__(self):
        return f"{', '.join(self.cart)} - {self.customer}"


################################################################
# Ваша задача создать класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
# конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо
# оставить только целые числа и сохранить их в атрибут values в виде списка. Причем значения должны хранится в порядке
# неубывания. В случае, если целых чисел не передано, нужно в атрибут values сохранять пустой список;переопределить
# метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:"Вектор(<value1>, <value2>, <value3>, ..
# .)", если вектор не пустой. При этом значения должны быть упорядочены по возрастанию;"Пустой вектор", если наш
# вектор не хранит в себе значенияпереопределить метод __add__ так, чтобы экземпляр класса Vector мог складываться
# с целым числом, в результате должен получиться новый Vector, у которого каждый элемент атрибута values увеличен на
# числос другим вектором такой же длины. В результате должен получиться новый Vector, состоящий из суммы элементов,
# расположенных на одинаковых местах. Если длины векторов различаются, выведите сообщение "Сложение векторов разной
# длины недопустимо";В случае, если вектор складывается с другим типом(не числом и не вектором), нужны вывести
# сообщение "Вектор нельзя сложить с <значением>"переопределить метод __mul__ так, чтобы экземпляр класса Vector
# мог умножатьсяна целое число. В результате должен получиться новый Vector, у которого каждый элемент атрибута
# values умножен на переданное число;на другой вектор такой же длины. В результате должен получиться новый Vector,
# состоящий из произведения элементов, расположенных на одинаковых местах. Если длины векторов различаются,
# выведите сообщение "Умножение векторов разной длины недопустимо";В случае, если вектор умножается с другим
# типом(не числом и не вектором), нужны вывести сообщение "Вектор нельзя умножать с <значением>";
class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if type(i) == int])

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'  # либо можно если список args состоит из строк ['2','12'] (хоть внутри и числа, но они в виде строк) , то
        # можно использовать метод join для вывода значений списка через запятую по условию задачи : ', '.join(['2','12']) out: 2,12
        # если же внутри списка будут  находиться числа [2,12], а не строки, то метод join не сработает.
        # поэтому перед использованием метода join нужно преобразовать каждый элемент списка в строку
        # вот таким образом list = [str(i) for i in self.values] и далее применить метод: ', '.join(list) out: 2, 12
        else:
            return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            res = map(lambda x: x + other, self.values)
            return Vector(*res)  # f'Вектор{tuple(res)}'
        elif isinstance(other, Vector) and len(self.values) == len(other.values):
            res = map(sum, zip(self.values, other.values))
            # с помощью zip склеиваем по -элементно оба вектора в один кортеж
            #  то есть v1 = Vector(1,2,3) и v2 = Vector(3,4,5)  через zip(v1,v2) дадут объект с тремя элементами
            #  (1,3),(2,4),(3,5)  далее с помощью map перебираем каждый элемент внутри кортежа ((1,3),(2,4),(3,5))
            #  полученного из zip выше и применяем функцию sum, чтобы просуммировать внутренние числа и на выходе
            #  получим (1+3,2+4,3+5) или (4,6,8)
            return Vector(*res)
            # возвращаем класс Vector куда в качестве args передали все элементы содержащиеся внутри res.
        # оператор распаковки * позволил вытянуть из res все элементы по -отдельности и передать из в Vector
        elif isinstance(other, Vector) and len(self.values) != len(other.values):
            return f'Сложение векторов разной длины недопустимо'
        else:
            return print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            res = map(lambda x: x * other, self.values)
            return Vector(*res)
        elif isinstance(other, Vector) and len(self.values) == len(other.values):
            res = map(lambda i: i[0] * i[1], zip(self.values, other.values))
            # внутрь map передали каждый элемент из zip(self.values, other.values)
            # каждый элемент из zip(self.values, other.values) - это пара значений из двух векторов , у
            # которых совпадают индексы. далее с помощью map перебираем каждый элемент внутри кортежа и
            # применяем функцию i[0]*i[1] , то есть умножаем 1й элемент на 2й
            return Vector(*res)
        elif isinstance(other, Vector) and len(self.values) != len(other.values):
            return f'Умножение векторов разной длины недопустимо'
        else:
            return print(f'Вектор нельзя умножать с {other}')


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"

v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"
v6 = v1 * v2
print(v6)  # Вектор(3, 8, 15)


########################################################################
class Vector:
    def __init__(self, *args):
        self.values = args

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        lst = []
        for i in value:
            if type(i) == int:
                lst.append(i)
        self.__values = sorted(lst)
        return self.__values

    def __str__(self):
        if self.values:
            # lst = [str(i) for i in self.values]
            # return f"Вектор({', '.join(lst)})"
            # return f"Вектор({', '.join(map(str, self.values))})"
            return f'"Вектор{tuple(self.values)}'
        return f'Пустой вектор'

    def __add__(self, other):
        # print(type(other), other.__values) # <class '__main__.Vector'> [3, 4, 5]
        if type(other) == int:
            lst = [i + other for i in self.values]
            return Vector(*lst)
        if isinstance(other, self.__class__):
            if len(other.values) == len(self.values):
                lst = list(map(sum, zip(self.values, other.values)))
                return Vector(*lst)
            else:
                print(f'Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if type(other) == int:
            lst = [i * other for i in self.values]
            return Vector(*lst)
        if isinstance(other, self.__class__):
            if len(other.values) == len(self.values):
                lst = list(map(lambda x: x[0] * x[1], zip(self.values, other.values)))
                return Vector(*lst)
            else:
                print(f'Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other}')


# ########################################################################
class Vector:

    def __init__(self, *args):
        self.values = sorted([int(arg) for arg in args if isinstance(arg, int)])

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(self.values)}'
        else:
            return f'Пустой вектор'

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*list(map(lambda x: x + other, self.values)))
        elif isinstance(other, Vector) and len(self) == len(other):
            return Vector(*list(map(lambda y, z: y + z, self.values, other.values)))
        elif isinstance(other, Vector) and len(self) != len(other):
            print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*list(map(lambda p: p * other, self.values)))
        elif isinstance(other, Vector) and len(self) == len(other):
            return Vector(*list(map(lambda y, z: y * z, self.values, other.values)))
        elif isinstance(other, Vector) and len(self) != len(other):
            print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other}')


# ########################################################################
from typing import Union, Optional


class Vector:

    def __init__(self, *args: int) -> None:
        self.values = sorted(Vector.is_integer(*args))

    @staticmethod
    def is_integer(*args: int) -> list:
        # не использую isinstance(i, int), потому что пропускает булевые значения (класс bool – это подкласс int)
        return [i for i in args if type(i) == int]

    def __add__(self, other: Union[int, 'Vector']) -> Optional['Vector']:
        if isinstance(other, int):
            new_vector = [i + other for i in self.values]
        elif isinstance(other, Vector):
            if not len(other) == len(self):
                print('Сложение векторов разной длины недопустимо')
                return None
            new_vector = [sum(i) for i in zip(self.values, other.values)]
        else:
            print(f'Вектор нельзя сложить с {other}')
            return None

        return Vector(*new_vector)

    def __mul__(self, other: Union[int, 'Vector']) -> Optional['Vector']:
        if isinstance(other, int):
            new_vector = [i * other for i in self.values]
        elif isinstance(other, Vector):
            if not len(other) == len(self):
                print('Умножение векторов разной длины недопустимо')
                return None
            new_vector = [i * j for i, j in zip(self.values, other.values)]
        else:
            print(f'Вектор нельзя умножать с {other}')
            return None

        return Vector(*new_vector)

    def __len__(self) -> int:
        return len(self.values)

    def __str__(self) -> str:
        return f'Вектор{tuple(self.values)}' if self.values else 'Пустой вектор'


# ########################################################################
class Vector:

    def __init__(self, *args):
        self.values = sorted(([i for i in args if isinstance(i, int)]))

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        else:
            return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*map(lambda x: x + other, self.values))
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*map(lambda x, y: x + y, self.values, other.values))
            else:
                print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*map(lambda x: x * other, self.values))
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*map(lambda x, y: x * y, self.values, other.values))
            else:
                print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other}')


# ########################################################################
# с ф-й len
class Vector:
    def __init__(self, *args):
        self.values = sorted(list(filter(lambda x: type(x) == int, args)))

    def __str__(self):
        return ['Пустой вектор', f'Вектор{tuple(self.values)}'][len(self.values) >= 1]

    def __len__(self):
        return len(self.values)

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*map(lambda x: x + other, self.values))
        if isinstance(other, Vector):
            if len(other) == len(self):
                return Vector(*map(lambda x: x[0] + x[1], (zip(self.values, other.values))))
            else:
                print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*map(lambda x: x * other, self.values))
        if isinstance(other, Vector):
            if len(other) == len(self):
                return Vector(*map(lambda x: x[0] * x[1], (zip(self.values, other.values))))
            else:
                print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other}')


# ########################################################################
# Без дублирования кода в методах __add__ и __mul__
class Vector:
    def __init__(self, *args):
        self.values = sorted(filter(lambda x: type(x) == int, args))

    def __len__(self):
        return len(self.values)

    def calc(self, func, arg):
        """        Вызываем метод func у элемента списка self.values
        :param func: имя метода
        :param arg: аргумент
        :return: объект        """
        if isinstance(arg, Vector):
            if len(self) != len(arg):
                err = {'__add__': 'Сложение', '__mul__': 'Умножение'}
                return print(f'{err.get(func)} векторов разной длины недопустимо')
            other = arg.values
        elif type(arg) == int:
            other = [arg] * len(self)
        else:
            err = {'__add__': 'сложить', '__mul__': 'умножать'}
            return print(f'Вектор нельзя {err.get(func)} с {arg}')
        return Vector(*[getattr(x, func)(y) for x, y in zip(self.values, other)])

    def __add__(self, other):
        return self.calc('__add__', other)

    def __mul__(self, other):
        return self.calc('__mul__', other)

    def __str__(self):
        return f"Вектор{tuple(self.values)}" if self.values else 'Пустой вектор'


# ########################################################################

# _________Песнь 13. Магические методы __add__, __sub__, __mul__, __truediv________________

class Desc:
    def __init__(self):
        self.opdct = {'add': '+', 'sub': '-', 'mul': '*', 'truediv': '/'}

    def __set_name__(self, owner, name):
        name = name.strip('_')
        self.prefix = name[0] if name.startswith(('i', 'r')) else None
        self.name = name[1:] if self.prefix else name

    def __get__(self, obj, owner):
        def wrapp(other):
            if type(other) in (int, float):
                n1, n2 = obj.num, other
            else:
                n1, n2 = obj.num, other.num
            if not self.prefix:
                return owner(self.op(self.opdct[self.name], n1, n2))
            if self.prefix == 'r':
                return owner(self.op(self.opdct[self.name], n2, n1))
            if self.prefix == 'i':
                setattr(obj, 'num', self.op(self.opdct[self.name], n1, n2))
                return obj

        return wrapp

    @staticmethod
    def op(opsign, n1, n2):
        return eval(f'{n1}{opsign}{n2}')


class A:
    __add__ = Desc()
    __sub__ = Desc()
    __mul__ = Desc()
    __truediv__ = Desc()
    __radd__ = Desc()
    __rsub__ = Desc()
    __rmul__ = Desc()
    __rtruediv__ = Desc()
    __iadd__ = Desc()
    __isub__ = Desc()
    __imul__ = Desc()
    __itruediv__ = Desc()

    def __init__(self, num):
        self.num = num


########################################################################
# Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:
# lst = [1, 2, 3] + [4.5, -3.6, 0.78]Но нет реализации оператора -, который бы убирал из списка соответствующие
# значения вычитаемого списка, как это показано в примере:lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4]
# (порядок следования оставшихся элементов списка должен сохраняться)Давайте это поправим и создадим такой функционал.
# Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:lst = NewList() # пустой
# списокlst = NewList([-1, 0, 7.56, True]) # список с начальными значениямиРеализуйте для этого класса работу с
# оператором вычитания, чтобы над объектами класса NewList можно было выполнять следующие действия:
# Также в классе NewList необходимо объявить метод:get_list() - для возвращения результирующего списка объекта
# класса NewListНапример:lst = res_2.get_list() # [1, 2, 3]
class NewList:
    def __init__(self, *args):
        # self.lst = lst[:] if lst and type(lst) == list else []
        self.lst = list(*args)
        # self.lst = args  # ([1, 2, -4, 6, 10, 11, 15, False, True],)

    def get_list(self):
        return self.lst

    def __sub__(self, other):
        if type(other) not in (list, self.__class__):
            raise ArithmeticError('list must be.....')
        other_lst = other if type(other) == list else other.get_list()
        return self.__class__(self.diff_list(self.lst, other_lst))
        # return NewList(self.diff_list(other, self.lst))

    @staticmethod
    def diff_list(lst1, lst2):
        if len(lst2) == 0:
            return lst1
        sub = lst2[:]
        return [i for i in lst1 if not __class__.is_element(i, sub)]

    @staticmethod
    def is_element(i, sub):
        res = any(map(lambda x: type(x) == type(i) and x == i, sub))
        if res:
            sub.remove(i)
        return res

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError
        return self.__class__(self.diff_list(other, self.lst))
        # return NewList(self.diff_list(other, self.lst))


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
# res_1 = lst1 - '2'  # ArithmeticError: list must be.....
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])


#######################################################################
class NewList(list):

    def __sub__(self, other: ('NewList', 'list')) -> 'NewList':
        tmp_lst = [(i, type(i)) for i in self]
        for i in [(i, type(i)) for i in other]:
            if i in tmp_lst:
                tmp_lst.remove(i)
        return NewList(i[0] for i in tmp_lst)

    def __rsub__(self, other):
        return NewList(other) - self

    def get_list(self):
        return self


########################################################################
class NewList:

    def __init__(self, box=None):
        self.box = box if box else []

    def get_list(self):
        return self.box

    def __sub__(self, other):
        other = other if isinstance(other, list) else other.box
        box = self.box[:]
        for item1 in other:
            count = 0
            for item2 in box:
                if type(item1) is type(item2) and item1 == item2:
                    del box[count]
                    break
                count += 1
        return NewList(box)

    def __rsub__(self, other):
        return NewList(other) - self


###############################################################################################################################################
class NewList:
    def __init__(self, *args):
        self.elements = list(*args)

    def __sub__(self, other):
        other = self.valid_operand(other)
        return NewList(self.lists_difference(self.get_list(), other))

    def __rsub__(self, other):
        other = self.valid_operand(other)
        return NewList(self.lists_difference(other, self.get_list()))

    def __isub__(self, other):
        other = self.valid_operand(other)
        self.elements = self.lists_difference(self.get_list(), other)
        return self

    @staticmethod
    def valid_operand(op):
        if type(op) not in (list, NewList):
            raise AttributeError('Неверный тип операнда')
        if type(op) is NewList:
            op = op.get_list()
        return op

    @staticmethod
    def lists_difference(list_1, list_2):
        for elem_2 in list_2:
            for i, elem_1 in enumerate(list_1):
                if elem_2 is elem_1:
                    del list_1[i]
                    break
        return list_1

    def get_list(self):
        return self.elements.copy()
    # геттер использую для получения элементов в сеттере. Если геттер вернёт просто self.elements, то выполнение
    # операций будет влиять на оригинал этого списка. Поэтому мне нужна копия.


########################################################################
class NewList:

    def __init__(self, list_=None) -> None:
        if not list_:
            self.list_ = []
            return
        self.list_ = list_

    def get_list(self) -> list:
        return self.list_

    def __sub__(self, other: (list, object)) -> object:
        if isinstance(other, NewList):
            other = other.list_
        new_list = self.list_[:]
        for i, v in enumerate(other):
            for j, k in enumerate(new_list):
                if v == k and type(v) == type(k):
                    del new_list[j]
                    break
            if not new_list:
                break
        return NewList(new_list)

    def __rsub__(self, other):
        return NewList(other) - self


########################################################################
class NewList:
    def __init__(self, lst=None):
        self.lst = lst or []

    def __sub__(self, other):
        other = other.lst if type(other) is self.__class__ else other
        a, b = [(x, type(x)) for x in self.lst], [(x, type(x)) for x in other]
        n_lst = []
        for i in a:
            b.remove(i) if i in b else n_lst.append(i[0])
        return NewList(n_lst)

    def __rsub__(self, other):
        other = other.lst if type(other) is self.__class__ else other
        return NewList(other) - self

    def get_list(self):
        return self.lst


########################################################################
class NewList:
    def __init__(self, lst=None):
        self.lst = list(lst)

    def get_list(self):
        return self.lst

    @staticmethod
    def __get_diff(lst_0, lst_1):
        lst_0 = [(i, type(i)) for i in getattr(lst_0, 'lst', lst_0)]  # getattr(object, name, default)
        lst_1 = [(i, type(i)) for i in getattr(lst_1, 'lst', lst_1)]
        for i in lst_1:
            if i in lst_0:
                lst_0.remove(i)
        return [i[0] for i in lst_0]

    def __sub__(self, other):
        return self.__class__(self.__get_diff(self, other))

    def __rsub__(self, other):
        return self.__class__(self.__get_diff(other, self))

    def __isub__(self, other):
        self.lst = self.__get_diff(self, other)
        return self


#######################################################################
# Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:
# lst1 = ListMath() # пустой списокlst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
# В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа,
# остальные игнорировать (если указываются в списке). Например:lst = ListMath([1, "abc", -5, 7.68, True]) #
# ListMath: [1, -5, 7.68]В каждом объекте класса ListMath должен быть публичный атрибут:
# lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).
# Также с объектами класса ListMath должны работать следующие операторы:
# При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми
# списками, прежние списки не меняются.При использовании операторов +=, -=, *=, /= значения должны меняться внутри
# списка текущего объекта (новый объект не создается).

class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst if lst and type(lst) == list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    # @property
    # def lst_math(self):
    #     return self.__lst_math
    #
    # @lst_math.setter
    # def lst_math(self, value):
    #     if value is not None:
    #         self.__lst_math = list(i for i in value if type(i) in (int, float))
    #     else:
    #         self.__lst_math = None
    #     return self.__lst_math

    def __verify__(self, value):
        if type(value) not in (int, float):
            raise ArithmeticError('')

    def __add__(self, other):
        self.__verify__(other)
        return ListMath([i + other for i in self.lst_math])  # должны формироваться новые объекты класса ListMath с
        # новыми списками, прежние списки не меняются.т.е. создаются копии библиотек

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.lst_math = ([i + other for i in self.lst_math])
        return self  # При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего
        # объекта (новый объект не создается).

    def __sub__(self, other):
        return self.__class__([i - other for i in self.lst_math])

    def __rsub__(self, other):
        return self.__class__([other - i for i in self.lst_math])

    def __isub__(self, other):
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __mul__(self, other):
        return self.__class__([other * i for i in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.lst_math = [other * i for i in self.lst_math]
        return self

    def __truediv__(self, other):
        return self.__class__([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        return self.__class__([other / i for i in self.lst_math])

    def __itruediv__(self, other):
        self.lst_math = [i / other for i in self.lst_math]
        return self


lst_math = ListMath([1, "abc", -5, 7.68, True])  # ListMath: [1, -5, 7.68]
print(lst_math)  # [1, -5, 7.68]
lst_math = lst_math + 76  # сложение каждого числа списка с определенным числом
print(lst_math)  # [77, 71, 83.68]
lst_math = 6.5 + lst_math  # сложение каждого числа списка с определенным числом
print(lst_math)  # [83.5, 77.5, 90.18]
lst_math += 76.7  # сложение каждого числа списка с определенным числом
print(lst_math)  # [160.2, 154.2, 166.88]
lst_math = lst_math - 76  # вычитание из каждого числа списка определенного числа
print(lst_math)  # [84.19999999999999, 78.19999999999999, 90.88]
lst_math = 7.0 - lst_math  # вычитание из числа каждого числа списка
print(lst_math)  # [77.19999999999999, 71.19999999999999, 83.88]
lst_math -= 76.3
print(lst_math)  # [0.8999999999999915, -5.1000000000000085, 7.579999999999998]
lst_math = lst_math * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst_math)  # [4.499999999999957, -25.500000000000043, 37.89999999999999]
lst_math = 5 * lst_math  # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst_math)  # [22.499999999999787, -127.50000000000021, 189.49999999999994]
lst_math *= 5.54
print(lst_math)  # [124.64999999999883, -706.3500000000012, 1049.8299999999997]
lst_math = lst_math / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
print(lst_math)  # [9.588461538461448, -54.334615384615475, 80.75615384615382]
lst_math = 3 / lst_math  # деление числа на каждый элемент списка
print(lst_math)  # [0.31287605294825804, -0.055213421108515515, 0.03714887172208835]
lst_math /= 13.0
print(lst_math)  # [0.024067388688327543, -0.004247186239116578, 0.002857605517083719]
########################################################################
## V2 - Коротенько, на основе numpy.ndarray :)
import numpy as np


class ListMath(np.ndarray):

    def __new__(cls, in_list=[]):
        self = np.asarray([x for x in in_list if type(x) in (int, float)]).view(cls)
        return self

    @property
    def lst_math(self):
        return self.tolist().copy()

    def __idiv__(self, other):
        return self / other


########################################################################
class ListMath:
    def __init__(self, arg=[]):
        self.lst_math = [i for i in arg if type(i) in (int, float)]

    def do(self, fn_name, other, new=True):
        result = [getattr(i, fn_name)(other) for i in self.lst_math]  # getattr(object, name, default)
        if new:
            return ListMath(result)
        else:
            self.lst_math = result
            return self

    def __add__(self, other):
        return self.do('__add__', other)

    def __sub__(self, other):
        return self.do('__sub__', other)

    def __rsub__(self, other):
        return self.do('__rsub__', other)

    def __mul__(self, other):
        return self.do('__mul__', other)

    def __rmul__(self, other):
        return self.do('__rmul__', other)

    def __truediv__(self, other):
        return self.do('__truediv__', other)

    def __iadd__(self, other):
        return self.do('__add__', other, False)

    def __isub__(self, other):
        return self.do('__sub__', other, False)

    def __imul__(self, other):
        return self.do('__mul__', other, False)

    def __idiv__(self, other):
        return self.do('__truediv__', other, False)


#######################################################################
class ListMath:

    def __init__(self, ls=None):
        if ls is None:
            self.lst_math = []
        else:
            self.lst_math = ls

    @staticmethod
    def check_values(n):
        return isinstance(n, (int, float)) and not isinstance(n, bool)

    @property
    def lst_math(self):
        return self.__ls

    @lst_math.setter
    def lst_math(self, item):
        if isinstance(item, list):
            item = list(filter(self.check_values, item))
        self.__ls = item

    def __add__(self, other):
        return ListMath([i + other for i in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.__ls = [i + other for i in self.lst_math]
        return self

    def __sub__(self, other):
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - i for i in self.lst_math])

    def __isub__(self, other):
        self.__ls = [i - other for i in self.lst_math]
        return self

    def __mul__(self, other):
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.__ls = [i * other for i in self.lst_math]
        return self

    def __truediv__(self, other):
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / i for i in self.lst_math])

    def __itruediv__(self, other):
        self.__ls = [i / other for i in self.lst_math]
        return self


########################################################################
# Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один
# объект ссылается на следующий и так далее):Давайте снова создадим такую структуру данных. Для этого объявим
# два класса:Stack - для управления односвязным списком в целом;StackObj - для представления отдельных объектов
# в односвязным списком.Объекты класса StackObj должны создаваться командой:obj = StackObj(data)
# где data - строка с некоторыми данными.Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
# __data - ссылка на строку с переданными данными;__next - ссылка на следующий объект односвязного списка
# (если следующего нет, то __next = None).Объекты класса Stack создаются командой:st = Stack()
# и каждый из них должен содержать локальный атрибут:top - ссылка на первый объект односвязного списка
# (если объектов нет, то top = None).Также в классе Stack следует объявить следующие методы:
# push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop_back(self) - удаление последнего объекта из односвязного списка.Дополнительно нужно реализовать следующий
# функционал (в этих операциях копии односвязного списка создавать не нужно):# добавление нового объекта класса
# StackObj в конец односвязного списка stst = st + obj st += obj# добавление нескольких объектов в конец
# односвязного спискаst = st * ['data_1', 'data_2', ..., 'data_N']st *= ['data_1', 'data_2', ..., 'data_N']
# В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из
# списка (каждый элемент списка для очередного добавляемого объекта).
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    # @property
    # def data(self):
    #     return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack:
    def __init__(self):
        self.top = self.__last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        if self.__last:
            self.__last.next = obj
        self.__last = obj

    def pop_back(self):
        h = self.top
        if h is None:
            return
        while h.next and h.next != self.__last:
            h = h.next

        if self.__last == self.top:
            self.__last = self.top = None
        else:
            self.__last = h
            # h.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):  # ['data_1', 'data_2', ..., 'data_N']
        for i in other:
            self.__add__(StackObj(i))  # создать объект StackObj для каждого i
        return self

    def __imul__(self, other):
        return self.__mul__(other)


st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"


###############################################################################################################################################
class Desc:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class StackObj:
    data = Desc()
    next = Desc()

    def __init__(self, data):
        self.data = data
        self.next = None


########################################################################
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if type(value) is StackObj or value is None:
            self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        if type(other) is list and other:
            for data in other:
                self.push_back(StackObj(data))
        return self

    def push_back(self, obj):
        if type(obj) is StackObj:
            if self.top:
                self.get_last().next = obj
            else:
                self.top = obj

    def pop_back(self):
        if self.top and self.top.next:
            cur_obj = self.top
            while cur_obj.next.next:
                cur_obj = cur_obj.next
            cur_obj.next = None
        else:
            self.top = None

    def get_last(self):
        cur_node = self.top
        while cur_node.next:
            cur_node = cur_node.next
        return cur_node


########################################################################
# Двухсвязный список, чтобы не искать последний елемент.
class DescObj:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class StackObj:
    data, next, prev = DescObj(), DescObj(), DescObj()

    def __init__(self, data):
        self.__data = data
        self.__prev = self.__next = None


class Stack:
    def __init__(self):
        self.top = self.tail = None

    def push_back(self, obj):
        if self.top:
            self.tail.next = obj
            obj.prev = self.tail
        else:
            self.top = obj
        self.tail = obj

    def pop_back(self):
        last = self.tail
        if self.tail is not None and self.tail.prev:
            last = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.__init__()
        return last

    def __add__(self, obj):
        self.push_back(obj)
        return self

    def __mul__(self, data_items):
        [self.push_back(StackObj(data)) for data in data_items]
        return self


########################################################################
# Подвиг 7. Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два
# класса:Lib - для представления библиотеки в целом;Book - для описания отдельной книги.Объекты класса Book должны
# создаваться командой:book = Book(title, author, year)где title - заголовок книги (строка); author - автор книги
# (строка); year - год издания (целое число).Объекты класса Lib создаются командой:lib = Lib()Каждый объект должен
# содержать локальный публичный атрибут:book_list - ссылка на список из книг (объектов класса Book). Изначально
# список пустой.Также объекты класса Lib должны работать со следующими операторами:lib = lib + book # добавление
# новой книги в библиотекуlib += booklib = lib - book # удаление книги book из библиотеки (удаление происходит
# по ранее созданному объекту book класса Book)lib -= booklib = lib - indx # удаление книги по ее порядковому
# номеру (индексу: отсчет начинается с нуля)lib -= indxПри реализации бинарных операторов + и - создавать копии
# библиотек (объекты класса Lib) не нужно.Также с объектами класса Lib должна работать функция:
# n = len(lib) # n - число книгкоторая возвращает число книг в библиотеке.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)


class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Book) and other in self.book_list:
            self.book_list.remove(other)
        elif isinstance(other, int) and other < len(self.book_list):
            self.book_list.pop(other)
            # del self.book_list[other]
        return self

    def __isub__(self, other):
        return self.__sub__(other)


book = Book('title', 'author', '12')
lib = Lib()
lib = lib + book  # добавление новой книги в библиотеку
print(lib)
lib += book
print(lib)
lib = lib - book  # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
print(lib)
lib -= book
print(lib)  # []
lib = lib - 0  # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
print(lib)
lib -= 0
print(lib)


#######################################################################
# Подвиг 8. Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите два
# класса с именами:Budget - для управления семейным бюджетом;Item - пункт расходов бюджета.
# Объекты класса Item должны создаваться командой:it = Item(name, money)где name - название статьи расхода; money -
# сумма расходов (вещественное или целое число).Соответственно, в каждом объекте класса Item должны формироваться
# локальные атрибуты name и money с переданными значениями. Также с объектами класса Item должны выполняться следующие
# операторы:s = it1 + it2 # сумма для двух статей расходови в общем случае:s = it1 + it2 + ... + itN # сумма N статей
# расходовПри суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих
# объектов класса Item.Объекты класса Budget создаются командой:my_budget = Budget()А сам класс Budget должен иметь
# следующие методы:add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);remove_item(self,
# indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
# get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).
class Budget:
    def __init__(self):
        self.items = list()

    def add_item(self, it):
        if isinstance(it, Item):
            self.items.append(it)

    def remove_item(self, indx):
        if isinstance(indx, int) and 0 <= indx < len(self.items):
            del self.items[indx]

    def get_items(self):
        return self.items


class Item:
    def __init__(self, name, __money):
        self.__name = name
        self.__money = __money

    # @property
    # def __money(self):
    #     return self.__money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.__money + other.__money

        elif isinstance(other, (int, float)):
            return self.__money + other

    def __radd__(self, other):
        return self.__add__(other)


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
# print(my_budget.get_items())
# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)


########################################################################
# Подвиг 9. Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска), объекты которого создаются
# командой:box = Box3D(width, height, depth)где width, height, depth - ширина, высота и глубина соответственно
# (числа: целые или вещественные)В каждом объекте класса Box3D должны создаваться публичные атрибуты:
# width, height, depth - ширина, высота и глубина соответственно.С объектами класса Box3D должны выполняться следующие
# операторы:box1 = Box3D(1, 2, 3)box2 = Box3D(2, 4, 6)box = box1 + box2 # Box3D: width=3, height=6, depth=9
# (соответствующие размерности складываются)ox = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность
# умножается на 2)box = 3 * box2    # Box3D: width=6, height=12, depth=18box = box2 - box1 # Box3D: width=1, height=2,
# depth=3 (соответствующие размерности вычитаются)box = box1 // 2   # Box3D: width=0, height=1, depth=1
# (соответствующие размерности целочисленно делятся на 2)box = box2 % 3    # Box3D: width=2, height=1, depth=0
# При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями
# локальных атрибутов.

class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_atr(self):
        return self.width, self.height, self.depth

    def _check_verify_(self, other):
        if isinstance(other, (int, float)) or isinstance(other, self.__class__):
            return True

    def __add__(self, other):
        if self._check_verify_(other):
            return self.__class__(*map(sum, zip(self.get_atr(), other.get_atr())))

    def __mul__(self, other):
        if self._check_verify_(other):
            return self.__class__(*[i * other for i in self.get_atr()])

    def __rmul__(self, other):
        # return self*other
        return self.__mul__(other)

    def __sub__(self, other):
        if self._check_verify_(other):
            return self + other * (-1)  # все атрибуты other умн на -1 и затем метод переопределяется в __add__
            # return self.__class__(*map(lambda i: i[0] - i[1], zip(self.get_atr(), other.get_atr())))

    def __floordiv__(self, other):
        if self._check_verify_(other):
            return self.__class__(*[i // other for i in self.get_atr()])

    def __mod__(self, other):
        if self._check_verify_(other):
            return self.__class__(*[i % other for i in self.get_atr()])


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2  # Box3D: width=6, height=12, depth=18
box = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2  # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3  # Box3D: width=2, height=1, depth=0
########################################################################
from operator import add, sub, mul, mod, floordiv


class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __make_calc(self, other, op):
        data = self.width, self.height, self.depth
        if isinstance(other, Box3D):
            data2 = other.width, other.height, other.depth
            return (op(s, o) for s, o in zip(data, data2))
        elif type(other) in (int, float):
            return (op(b, other) for b in data)
        return 0, 0, 0

    def __add__(self, other):
        return Box3D(*self.__make_calc(other, add))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Box3D(*self.__make_calc(other, sub))

    def __mul__(self, num):
        return Box3D(*self.__make_calc(num, mul))

    def __rmul__(self, num):
        return self.__mul__(num)

    def __mod__(self, num):
        return Box3D(*self.__make_calc(num, mod))

    def __floordiv__(self, num):
        return Box3D(*self.__make_calc(num, floordiv))


#######################################################################
class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.dimensions = (self.width, self.height, self.depth)

    def __add__(self, other):
        return type(self)(*map(sum, zip(self.dimensions, other.dimensions)))

    def __sub__(self, other):
        return type(self)(*map(lambda x, y: x - y, self.dimensions, other.dimensions))

    def __mul__(self, other):
        return type(self)(*map(lambda x: x * other, self.dimensions))

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        return type(self)(*map(lambda x: x // other, self.dimensions))

    def __mod__(self, other):
        return type(self)(*map(lambda x: x % other, self.dimensions))


########################################################################
class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def do(self, fname, oth):
        return Box3D(*([getattr(self.__dict__[i], fname)(oth.__dict__[i]
                                                         if type(oth) is Box3D else oth)
                        for i in self.__dict__]))

    def __add__(self, other):
        return self.do('__add__', other)

    def __mul__(self, other):
        return self.do('__mul__', other)

    def __rmul__(self, other):
        return self.do('__rmul__', other)

    def __sub__(self, other):
        return self.do('__sub__', other)

    def __floordiv__(self, other):
        return self.do('__floordiv__', other)

    def __mod__(self, other):
        return self.do('__mod__', other)


###################################################################################################################
# Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в
# сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора
# наибольшего значения в пределах этого окна: Или, если окна выходят за пределы матрицы, то они пропускаются
# (игнорируются):Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling,
# объекты которого создаются командой:mp = MaxPooling(step=(2, 2), size=(2,2))где step - шаг смещения окна по
# горизонтали и вертикали; size - размер окна по горизонтали и вертикали.Параметры step и size по умолчанию
# должны принимать кортеж со значениями (2, 2).Для выполнения операции Max Pooling используется команда:
# res = mp(matrix)где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix
# (должна создаваться новая таблица чисел.Прямоугольную таблицу чисел следует описывать вложенными списками. Если
# при сканировании таблицы часть окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).
# Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно
# генерироваться исключение командой:raise ValueError("Неверный формат для первого параметра matrix.")
# Пример использования класса (эти строчки в программе писать не нужно):Результатом будет таблица чисел:
class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.__step = step
        self.__size = size

    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        if rows == 0:
            return [[]]
        if not all(map(lambda x: len(x) == cols, matrix)) or \
                not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
            raise ValueError("Invalid matrix")

        h, w = self.__size[0], self.__size[1]
        sh, sw = self.__step[0], self.__step[1]
        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1
        res = [[0] * cols_range for _ in range(rows_range)]

        for i in range(rows_range):
            for j in range(cols_range):
                s = (x for r in matrix[i * sh:i * sh + h] for x in r[j * sw:j * sw + w])
                res[i][j] = max(s)
        return res


mp = MaxPooling(step=(2, 2), size=(2, 2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])  # [[6, 8], [9, 7]]
print(res)  # [[6, 8], [9, 7]]


# ########################################################################
class MaxPooling:
    def __init__(self, step: tuple = (2, 2), size: tuple = (2, 2)) -> None:
        self.step = step
        self.size = size

    def validateMatrix(self, matrix: list) -> None:
        rowLength = len(matrix[0])
        if all(len(row) == rowLength for row in matrix):
            if all(type(i) in (int, float) for row in matrix for i in row):
                return
        raise ValueError("Неверный формат для первого параметра matrix.")

    def __call__(self, matrix: list) -> list:
        self.validateMatrix(matrix)

        rangeI = range(self.size[1], len(matrix) + 1, self.step[1])
        rangeJ = range(self.size[0], len(matrix[0]) + 1, self.step[0])

        return [[max(matrix[y][x]
                     for y in range(i - self.size[1], i)
                     for x in range(j - self.size[0], j)
                     ) for j in rangeJ]
                for i in rangeI]


########################################################################
class MaxPooling:
    def __init__(self, step: tuple = (2, 2), size: tuple = (2, 2)) -> None:
        self.step = step
        self.size = size

    def validateMatrix(self, matrix: list) -> None:
        rowLength = len(matrix[0])
        if all(len(row) == rowLength for row in matrix):
            if all(type(i) in (int, float) for row in matrix for i in row):
                return
        raise ValueError("Неверный формат для первого параметра matrix.")

    def __call__(self, matrix: list) -> list:
        self.validateMatrix(matrix)

        return [[max(matrix[y][x]
                     for y in range(i - self.size[1], i)
                     for x in range(j - self.size[0], j))

                 for j in range(self.size[0], len(matrix[0]) + 1, self.step[0])]
                for i in range(self.size[1], len(matrix) + 1, self.step[1])]


########################################################################
class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, m):
        items_in_1row = len(m[0])
        for row in m:
            if len(row) != items_in_1row:
                raise ValueError("Неверный формат для первого параметра matrix.")
        for i in range(len(m)):
            for j in range(len(m[0])):
                if type(m[i][j]) not in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")

        # Определяем количество колонок и столбцов в результирующей матрице
        cols = len(m[0]) // self.step[0]
        rows = len(m) // self.step[1]
        # формируем новую матрицу и заполняем её нулями
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        # заполняем новую матрицу максимальными значениями из "окна"
        for i in range(rows):
            for j in range(cols):
                res[i][j] = max([m[i * 2][j * 2], m[i * 2 + 1][j * 2], m[i * 2][j * 2 + 1], m[i * 2 + 1][j * 2 + 1]])
        return res


#######################################################################
# https://docs-python.ru/donate/732618839844207080/
########################################################################
# ___Специальные методы сравнения объектов классов________________________________________________________________
# Создайте класс  Fruit, который имеет:метод __init__, который устанавливает значения атрибутов name и price:
# название и цена фрукта
# при сравнении  с экз других классов или числами как здесь нужно прописывать все методы, а
# если сравнивать экз одного класаа то достатточно прописать на равенство,меньше, меньше равно
# обратное действие интерпритатолр сам перевернёт
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        # if isinstance(other, Fruit):
        #     return self.price == other.price
        return self.price == other

    def __gt__(self, other):
        return self.price > other

    def __ge__(self, other):
        return self.price >= other

    def __lt__(self, other):
        return self.price < other

    def __le__(self, other):
        return self.price <= other


apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')
########################################################################
from functools import total_ordering


# Добавляет в пользовательский класс недостающие методы сравнения.
# Класс должен определять один из методов __lt__(), __le__(), __gt__() или __ge__(). Кроме того, класс должен
# предоставлять метод __eq__().

@total_ordering
class Fruit:

    def __init__(self, *args):
        self.name, self.price = args

    def __eq__(self, other):
        return self.price == (other.price if isinstance(other, Fruit) else other)

    def __lt__(self, other):
        return self.price < (other.price if isinstance(other, Fruit) else other)


########################################################################
# Чтобы не реализовывать все магические методы сравнения, можно использовать декоратор functools.total_ordering,
# который позволяет  сократить код, реализовав только методы __eq__ и __lt__
from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other

    def __lt__(self, other):
        return self.area < other


###############################################################################################################################################
from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, *args):
        self.width, self.height = args

    @property
    def area(self):
        return self.width * self.height

    def compare(self, func, arg):
        return getattr(self.area, func)(arg.area if isinstance(arg, Rectangle) else arg)

    def __eq__(self, other):
        return self.compare('__eq__', other)

    def __gt__(self, other):
        return self.compare('__gt__', other)


########################################################################
# Подвиг 3. Объявите класс Track (маршрут), объекты которого создаются командой:track = Track(start_x, start_y)
# где start_x, start_y - координаты начала маршрута (целые или вещественные числа).Каждый линейный сегмент
# маршрута определяется классом TrackLine, объекты которого создаются командой:
# line = TrackLine(to_x, to_y, max_speed)где to_x, to_y - координаты следующей точки маршрута
# (целые или вещественные числа); max_speed - максимальная скорость на данном участке (целое число).
# Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:
# add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
# get_tracks(self) - получение кортежа из объектов класса TrackLine.Также для объектов класса Track должны быть
# реализованные следующие операции сравнения:
# n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
# Создайте два маршрута track1 и track2 с координатами:
# 1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 1002-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90
# Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.
class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = []

    def add_track(self, tr):
        if isinstance(tr, TrackLine):
            self.tracks.append(tr)

    def get_tracks(self):
        return tuple(self.tracks)

    def __len__(self):
        len_1 = ((self.start_x - self.tracks[0].x) ** 2 + (self.start_y - self.tracks[0].y) ** 2) ** 0.5
        return int(len_1 + sum(self._calc_(i) for i in range(1, len(self.tracks))))

    def _calc_(self, i):
        return ((self.tracks[i - 1].x - self.tracks[i].x) ** 2 + (self.tracks[i - 1].y - self.tracks[i].y) ** 2) ** 0.5

    def __eq__(self, other):
        if isinstance(other, Track):
            return len(self) == len(other)

    def __lt__(self, other):
        if isinstance(other, Track):
            return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

    @property
    def x(self):
        return self.to_x

    @property
    def y(self):
        return self.to_y


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2


########################################################################
class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track_lines = []

    def add_track(self, track):
        self.track_lines.append(track)

    def get_tracks(self):
        return tuple(self.track_lines)

    def __len__(self):
        ans = 0
        x1, y1 = self.start_x, self.start_y
        for obj in self.track_lines:
            x2, y2 = obj.to_x, obj.to_y
            ans += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
            x1, y1 = x2, y2
        return int(ans)


########################################################################
from typing import Tuple, Union


class TrackLine:
    def __init__(self, to_x: Union[int, float], to_y: Union[int, float], max_speed: int) -> None:
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x: Union[int, float], start_y: Union[int, float]) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.__tracks = []

    def add_track(self, tr: TrackLine):
        """добавление линейного сегмента маршрута (следующей точки)"""
        self.__tracks.append(tr)

    def get_tracks(self) -> Tuple[TrackLine]:
        """получение кортежа из объектов класса TrackLine"""
        return tuple(self.__tracks)

    def __len__(self) -> int:
        distance = 0
        if not self.__tracks:
            return distance

        x, y = self.start_x, self.start_y

        for point in self.__tracks:
            distance += ((x - point.to_x) ** 2 + (y - point.to_y) ** 2) ** 0.5
            x, y = point.to_x, point.to_y

        return int(distance)

    def __eq__(self, other) -> bool:
        return self.__len__() == len(other)

    def __lt__(self, other) -> bool:
        return self.__len__() < len(other)


#######################################################################
class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.trackLines = []

    def __setattr__(self, key, value):
        if key in ('start_x', 'start_y') and isinstance(value, (int, float)):
            object.__setattr__(self, key, value)
        elif key == 'trackLines':
            object.__setattr__(self, key, value)
        else:
            raise ValueError("Неверный тип данных.")

    def add_track(self, tr):  # добавление линейного сегмента маршрута (следующей точки)
        if isinstance(tr, TrackLine):
            self.trackLines.append(tr)

    def get_tracks(self):  # получение кортежа из объектов класса TrackLine
        return tuple(self.trackLines)

    def __eq__(self, track):
        return len(self) == len(track)

    def __gt__(self, track):
        return len(self) > len(track)

    def __len__(self):  # возвращает целоч. длину маршрута (привести к типу int) для объекта track
        l = 0
        x, y = self.start_x, self.start_y
        for c in self.get_tracks():
            l += ((c.to_x - x) ** 2 + (c.to_y - y) ** 2) ** 0.5
            x, y = c.to_x, c.to_y
        return int(l)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

    def __setattr__(self, key, value):
        if key in ('to_x', 'to_y') and isinstance(value, (int, float)):
            object.__setattr__(self, key, value)
        elif key == 'max_speed' and isinstance(value, int):
            object.__setattr__(self, key, value)
        else:
            raise ValueError("Неверный тип данных.")


########################################################################
class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x, start_y):
        self.track = [TrackLine(start_x, start_y, 0)]

    def add_track(self, tr):
        self.track.append(tr)

    def get_tracks(self):
        return tuple(self.track)

    @staticmethod
    def __get_dist(start, end):
        x0, y0 = start.to_x, start.to_y
        x1, y1 = end.to_x, end.to_y
        return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

    def __len__(self):
        track = self.track
        return int(sum([self.__get_dist(track[i], track[i + 1]) for i in range(len(track) - 1)]))

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


########################################################################
# Подвиг 4. Объявите класс Dimensions (габариты) с атрибутами:MIN_DIMENSION = 10MAX_DIMENSION = 10000
# Каждый объект класса Dimensions должен создаваться командой:d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
# Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого класса.
# Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены объекты-свойства (property)
# с именами: a, b, c. Причем, в момент присваивания нового значения должна выполняться проверка попадания числа в
# диапазон [MIN_DIMENSION; MAX_DIMENSION]. Если число не попадает, то оно игнорируется и существующее значение не
# меняется.С объектами класса Dimensions должны выполняться следующие операторы сравнения:
# dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2dim1 > dim2    # True, если объем dim1 больше
# объема dim2dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2dim1 < dim2
# True, если объем dim1 меньше объема dim2Объявите в программе еще один класс с именем ShopItem (товар),
# объекты которого создаются командой:item = ShopItem(name, price, dim)где name - название товара (строка);
# price - цена товара (целое или вещественное число); dim - габариты товара (объект класса Dimensions).
# В каждом объекте класса ShopItem должны создаваться локальные атрибуты:
# name - название товара;price - цена товара;dim - габариты товара (объект класса Dimensions).
# Создайте список с именем lst_shop из четырех товаров со следующими данными:
# - кеды; 1024; (40, 30, 120)- зонт;
# 500.24; (10, 20, 50)
# - холодильник; 40000; (2000, 600, 500)
# - табуретка; 2000.99; (500, 200, 200)Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию
# объема (габаритов) товаров списка lst_shop, используя стандартную функцию sorted() языка Python и ее параметр
# key для настройки сортировки. Прежний список lst_shop должен оставаться без изменений.

class Desc:

    def __set_name__(self, owner, name):
        # self.name = f'_{owner.__name__}__{name}'
        # self.name = '_' + owner.__name__ + '__' + name
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__validate(instance, value):
            setattr(instance, self.name, value)

    @staticmethod
    def __validate(instance, value):
        return instance.MIN_DIMENSION <= value <= instance.MAX_DIMENSION


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    a = Desc()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION + 1):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION + 1):
            self.__c = value

    def __volume__(self):
        return int(self.a * self.b * self.c)

    def __le__(self, other):
        if isinstance(other, Dimensions):
            return self.__volume__() <= other.__volume__()

    def __lt__(self, other):
        if isinstance(other, Dimensions):
            return self.__volume__() < other.__volume__()


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = [trainers, umbrella, fridge, chair]
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.__volume__())

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)  # dim - габариты товара (объект класса Dimensions).
# У dim переопределены ge, gt. А sorted с key сам к ним обращается. Похожая ситуация, как key=len, key=get и т.п.
# Этими методами (ge, gt) обладает объект dim, Ты же не обращаешься к каким-то методам, когда просто сортируешь список
# чисел, а sorted их дергает
# Т.О. в key=lambda x: x.dim сравниваются экземпляры класса :
# d2 = Dimensions(40, 30, 120)
# d3 = Dimensions(30, 20, 100)
# assert d2 <= d3, "неверно отработал оператор <="

#######################################################################
from functools import total_ordering


@total_ordering
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10_000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = 0
        self.a = a
        self.b = b
        self.c = c

    @property
    def volume(self):
        return self.a * self.b * self.c

    @classmethod
    def __validate(cls, val):
        return cls.MIN_DIMENSION <= val <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__validate(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__validate(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__validate(value):
            self.__c = value

    def __eq__(self, other):
        return self.volume == other.volume

    def __lt__(self, other):
        return self.volume < other.volume


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

    def __repr__(self):
        return self.name


s = """- кеды; 1024; (40, 30, 120)
- зонт; 500.24; (10, 20, 50)
- холодильник; 40000; (2000, 600, 500)
- табуретка; 2000.99; (500, 200, 200)"""

lst_shop = []

for line in s.splitlines():
    name, price, dim = line.lstrip('- ').split('; ')
    dim = Dimensions(*map(int, dim.strip('()').split(',')))
    item = ShopItem(name, float(price), dim)
    lst_shop.append(item)

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume)


# так как вы научили Python сравнивать объекты, то должно было хватить key=lambda x: x.dim
########################################################################
# Подвиг 5. Имеется стихотворение, представленное следующим списком строк:stich = ["Я к вам пишу – чего же боле?",
# "Что я могу еще сказать?",        "Теперь, я знаю, в вашей воле",        "Меня презреньем наказать.",
# "Но вы, к моей несчастной доле",        "Хоть каплю жалости храня,",        "Вы не оставите меня."]
# Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в конце каждого слова и разбить строку
# по словам (слова разделяются одним или несколькими пробелами). На основе полученного списка слов, создать объект
# класса StringText командой:st = StringText(lst_words)где lst_words - список из слов одной строчки стихотворения.
# С объектами класса StringText должны быть реализованы операторы сравнения:st1 > st2   # True, если число слов
# в st1 больше, чем в st2st1 >= st2  # True, если число слов в st1 больше или равно st2st1 < st2   # True, если число
# слов в st1 меньше, чем в st2st1 <= st2  # True, если число слов в st1 меньше или равно st2
# Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text. Затем,
# сформировать новый список lst_text_sorted из отсортированных объектов класса StringText по убыванию числа слов.
# Для сортировки использовать стандартную функцию sorted() языка Python. После этого преобразовать данный список
# (lst_text_sorted) в список из строк (объекты заменяются на соответствующие строки, между словами ставится пробел).

# from functools import total_ordering
#
#
# @total_ordering
class StringText:
    def __init__(self, lst):
        # print(lst)
        self.lst_word = list(lst)  # список из слов одной строчки стихотворения.

    def __len__(self):
        return len(self.lst_word)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self.lst_word) < len(other.lst_word)

    def __le__(self, other):
        return len(self.lst_word) <= len(other.lst_word)

    def __str__(self):
        return f'{self.lst_word}'


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

lst_text = []
strip_chars = '–?!,.;'
for line in stich:
    lst_text.append(StringText([word.strip(strip_chars) for word in line.split() if word.strip(strip_chars)]))
# lst_text = [StringText([word.strip('–?!,.;') for word in line.split() if word.strip('–?!,.;')]) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
print(lst_text_sorted)  # [<__main__.StringText object at 0x00000216DE138....
lst_text_sorted = [' '.join(x.lst_word) for x in lst_text_sorted]
# lst_text_sorted = list(map(lambda x: ' '.join(x.lst_words), lst_text_sorted))
print(lst_text_sorted)  # ['Я к вам пишу чего же боле', 'Теперь я знаю в вашей воле',....


###############################################################################################################################################
class RemoveChars:
    def __init__(self, words):  # "–?!,.;"
        self.words = words

    def __call__(self, arg):  # 'Я к вам пишу чего же боле'
        if isinstance(arg, str):
            for char in self.words:
                arg = arg.replace(char, '')
            return arg.split()


class StringText:
    def __init__(self, lst):
        self.lst = lst

    def __eq__(self, other):
        if isinstance(other, StringText):
            return len(self) == len(other)
        raise AttributeError

    def __gt__(self, other):
        if isinstance(other, StringText):
            return len(self) > len(other)
        raise AttributeError

    def __ge__(self, other):
        if isinstance(other, StringText):
            return len(self) >= len(other)
        raise AttributeError

    def __len__(self):
        return len(self.lst)


parce = RemoveChars("–?!,.;")
lst_text = [StringText(parce(sentence)) for sentence in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [" ".join(i.lst) for i in lst_text_sorted]
########################################################################
import re
from functools import total_ordering


@total_ordering
class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __str__(self):
        return ' '.join(self.lst_words)


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

pattern = re.compile(r"[–?!,.;]")
# re.compile(pattern, flags=0) Функция compile() модуля re компилирует шаблон
# регулярного выражения pattern в объект регулярного выражения, который может быть использован для поиска
# совпадений с использованием методов Match.match(), Match.search() и других способов.
# re.sub(pattern, repl, string, count=0, flags=0) - Функция sub() модуля re возвращает строку, полученную
# путем замены крайнего левого неперекрывающегося вхождения шаблона регулярного выражения pattern в строке string
# на строку замены repl.
lst_text = [StringText(el.split()) for el in map(lambda s: pattern.sub('', s), stich)]
lst_text_sorted = sorted(lst_text, reverse=True)
print(lst_text_sorted)  # [<__main__.StringText object at 0x00000274DD75FF90>,
lst_text_sorted = [*map(str, lst_text_sorted)]
print(lst_text_sorted)  # ['Я к вам пишу чего же боле', 'Теперь я знаю в вашей воле',....
########################################################################
# Подвиг 6. Ваша задача написать программу поиска слова в строке. Задача усложняется тем, что слово должно определяться
# в разных его формах. Например, слово:программированиеможет иметь следующие формы:программирование, программированию,
# программированием, программировании, программирования, программированиям, программированиями, программированиях
# Для решения этой задачи необходимо объявить класс Morph (морфология), объекты которого создаются командой:
# mw = Morph(word1, word2, ..., wordN)где word1, word2, ..., wordN - возможные формы слова.
# В классе Morph реализовать методы:add_word(self, word) - добавление нового слова (если его нет в списке слов
# объекта класса Morph);get_words(self) - получение кортежа форм слов.Также с объектами класса Morph должны
# выполняться следующие операторы сравнения:mw1 == "word"  # True, если объект mv1 содержит слово "word"
# (без учета регистра)mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)
# И аналогичная пара сравнений:"word" == mw1"word" != mw1После создания класса Morph, формируется список dict_words
# из объектов этого класса, для следующих слов с их словоформами:- связь, связи, связью, связей, связям, связями, связях
# - формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
# - вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
# - эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
# - день, дня, дню, днем, дне, дни, дням, днями, дняхЗатем, прочитайте строку из входного потока командой:
# text = input()Найдите все вхождения слов из списка dict_words (используя операторы сравнения) в строке text
# (без учета регистра, знаков пунктуаций и их словоформы). Выведите на экран полученное число.
s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""


class Morph:
    def __init__(self, *args):
        self.words = args

    def add_word(self, word):
        if word not in self.words:
            self.words += (word,)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        return other.lower() in self.words


text = 'Мы будем устанавливать связь завтра днем.'
text = text.rstrip('.')
print([[j.lstrip('- ') for j in i.split(', ')] for i in s.split('\n')])
print([i.lstrip('- ').split(', ') for i in s.split('\n')])
print([line.lstrip('- ').split(', ') for line in s.splitlines()])
# делит текст по символу '\n' print(dict_words)

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.split('\n')]
# print(dict_words)


count = 0
for word in text.split():
    for obj in dict_words:
        if word == obj:
            count += 1

count = sum(word == obj for word in text.split() for obj in dict_words)
print(count)


########################################################################
# Подвиг 7 (на повторение). Перед вами стоит задача выделения файлов с определенными расширениями из списка файлов,
# например:filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg",
# Для этого необходимо объявить класс FileAcceptor, объекты которого создаются командой:
# acceptor = FileAcceptor(ext1, ..., extN)где ext1, ..., extN - строки с допустимыми расширениями файлов,
# например: 'jpg', 'bmp', 'jpeg'.После этого предполагается использовать объект acceptor в стандартной функции
# filter языка Python следующим образом:filenames = list(filter(acceptor, filenames))То есть, объект acceptor
# должен вызываться как функция:acceptor(filename) и возвращать True, если файл с именем filename содержит
# расширения, указанные при создании acceptor, и False - в противном случае. Кроме того, с объектами класса
# FileAcceptor должен выполняться оператор:acceptor12 = acceptor1 + acceptor2Здесь формируется новый объект
# acceptor12 с уникальными расширениями первого и второго объектов. Например:acceptor1 = FileAcceptor("jpg", "jpeg",
# "png")acceptor2 = FileAcceptor("png", "bmp")acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")

class FileAcceptor:
    def __init__(self, *args):
        self.filename = args

    def __call__(self, args):
        return args.split('.')[-1] in self.filename

    def __add__(self, other):
        if isinstance(other, self.__class__):
            self.filename = self.filename + other.filename
            return self


acceptor = FileAcceptor("jpg", "jpeg")
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")
print('acceptor12 ', acceptor12)  # acceptor12  <__main__.FileAcceptor object at 0x0000....
filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
             "eq_2.xls"]
filenames = list(filter(acceptor, filenames))
print(filenames)  # ['boat.jpg', 'my.ava.jpg', 'forest.jpeg']

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)  # ['boat.jpg', 'my.ava.jpg', 'forest.jpeg']


#######################################################################
def __add__(self, other):
    if isinstance(other, self.__class__):
        return FileAcceptor(*(self.filename + other.filename))
    # return FileAcceptor(*self.args + other.args)


########################################################################
class FileAcceptor:
    def __init__(self, *extensions):
        self.extensions = extensions

    def __call__(self, filename):
        return filename.endswith(self.extensions)

    # x = 'заканчивается указанным суффиксом suffix'>> x.endswith('suffix') True

    def __add__(self, other):
        return FileAcceptor(*self.extensions + other.extensions)


########################################################################
class FileAcceptor:
    def __init__(self, *args):
        self.extensions = set(args)

    def __call__(self, file: str):
        if type(file) is str:
            return file.endswith(tuple('.' + e for e in self.extensions))

    def __add__(self, other):
        if type(other) is FileAcceptor:
            return FileAcceptor(*self.extensions.union(other.extensions))


#######################################################################
class FileAcceptor:
    def __init__(self, *args):
        self.ext_list = set(args)

    def __call__(self, filename: str):
        return filename.endswith(tuple(self.ext_list))

    def __add__(self, other):
        return self.__class__(*(self.ext_list | other.ext_list))


########################################################################
class FileAcceptor:
    def __init__(self, *args):
        self.lst = list(args)

    def __call__(self, item):
        return any(item.endswith(i) for i in self.lst)

    def __add__(self, other):
        return FileAcceptor(*self.lst, *other.lst)


###############################################################################################################################################
# Подвиг 8. В программе необходимо объявить классы для работы с кошельками в разных валютах:
# MoneyR - для рублевых кошельковMoneyD - для долларовых кошельковMoneyE - для евро-кошельков
# Объекты этих классов могут создаваться командами:rub = MoneyR()   # с нулевым балансом
# dl = MoneyD(1501.25) # с балансом в 1501.25 долларовuro = MoneyE(100)  # с балансом в 100 евро
# В каждом объекте этих классов должны формироваться локальные атрибуты:__cb - ссылка на класс CentralBank
# (центральный банк, изначально None);__volume - объем денежных средств в кошельке (если не указано, то 0).
# Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства (property) для работы с локальными атрибутами:
# cb - для изменения и считывания данных из переменной __cb;volume - для изменения и считывания данных из переменной
# __volume.Объекты классов должны поддерживать следующие операторы сравнения:rub < dldl >= eurorub == euro
# значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)
# euro > rubПри реализации операторов сравнения считываются соответствующие значения __volume из сравниваемых
# объектов и приводятся к рублевому эквиваленту в соответствии с курсом валют центрального банка.
# Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки, необходимо в программе объявить
# еще один класс CentralBank. Объекты класса CentralBank создаваться не должны (запретить), при выполнении команды:
# cb = CentralBank()должно просто возвращаться значение None. А в самом классе должен присутствовать атрибут:
# rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}Здесь числа (в значениях словаря) - курс валюты по отношению к
# доллару. Также в CentralBank должен быть метод уровня класса:register(cls, money) - для регистрации объектов
# классов MoneyR, MoneyD и MoneyE.При регистрации значение __cb объекта money должно ссылаться на класс CentralBank.
# Через эту переменную объект имеет возможность обращаться к атрибуту rates класса CentralBank и брать нужные котировки.
# Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:
# raise ValueError("Неизвестен курс валют.")

# @property
# def volume(self):
#     return self.__volume
#
# @volume.setter
# def volume(self, value):
#     self.__volume = value
#
# @property
# def cb(self):
#     return self.__cb
#
# @cb.setter
# def cb(self, cb):
#     self.__cb = cb


# @property
# def volume(self):
#     return self.__volume
#
# @volume.setter
# def volume(self, value):
#     self.__volume = value
#
# @property
# def cb(self):
#     return self.__cb
#
# @cb.setter
# def cb(self, cb):
#     self.__cb = cb


class Desc:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Money:
    type_money = None
    EPS = 0.1
    volume = Desc()
    cb = Desc()

    def __init__(self, volume=0):
        self.volume = volume
        self.cb = None

    def __calc__(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if self.type_money is None:
            raise ValueError("Неизвестный тип кошелька.")
        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.__calc__(other)
        return abs(v1 - v2) < self.EPS
        # return round(v1, 1) == round(v2, 1)

    def __lt__(self, other):
        v1, v2 = self.__calc__(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.__calc__(other)
        return v1 <= v2


class MoneyR(Money):
    type_money = 'rub'


class MoneyD(Money):
    type_money = 'dollar'


class MoneyE(Money):
    type_money = 'euro'


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return

    @classmethod
    def register(cls, money):
        money.cb = cls


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")


########################################################################
class Money:
    def __init__(self, volume=0.):
        self.cb, self.volume = None, volume

    @property
    def cb(self): return self.__cb

    @cb.setter
    def cb(self, value): self.__cb = value

    @property
    def volume(self): return self.__volume

    @volume.setter
    def volume(self, value): self.__volume = value

    def __abs__(self):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self.volume, self.prop, 'rub')

    def __eq__(self, other): return abs(abs(self) - abs(other)) <= 0.1

    def __gt__(self, other): return abs(self) - abs(other) > 0.1

    def __ge__(self, other): return abs(self) - abs(other) >= 0.1


class MoneyR(Money): prop = 'rub'


class MoneyD(Money): prop = 'dollar'


class MoneyE(Money): prop = 'euro'


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return None

    @classmethod
    def register(cls, money):
        if isinstance(money, Money):
            money.cb = cls

    @classmethod
    def convert(cls, _value, _from, _to):
        if _from == _to:  # 'rub'=='rub'
            return _value
        return _value * cls.rates.get(_to) / cls.rates.get(_from)


########################################################################
class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return None

    @classmethod
    def register(cls, money):
        if isinstance(money, Money):
            money.cb = cls


class Money:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.valuate() == other.valuate()

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.valuate() < other.valuate()

    def __le__(self, other):
        if isinstance(other, Money):
            return self.valuate() <= other.valuate()

    def valuate(self):
        if self.cb:
            return round(self.volume / self.cb.rates[self.currency_name], 1)
        raise ValueError("Неизвестен курс валют.")

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        if value is CentralBank:
            self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        if type(value) in (int, float):
            self.__volume = value


class MoneyR(Money):
    currency_name = 'rub'


class MoneyD(Money):
    currency_name = 'dollar'


class MoneyE(Money):
    currency_name = 'euro'


########################################################################
class BaseMoney:
    account = 'base'

    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def valuate(self):
        if self.cb:
            return self.volume / self.cb.rates[self.account] * self.cb.rates['rub']
        raise ValueError("Неизвестен курс валют.")

    def __eq__(self, other):
        return round(self.valuate(), 1) == round(other.valuate(), 1)

    def __ge__(self, other):
        return self.valuate() >= other.valuate()

    def __gt__(self, other):
        return self.valuate() > other.valuate()


class CentralBank:
    def __new__(cls, *args, **kwargs):
        return None

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    @classmethod
    def register(cls, money: BaseMoney):
        money.cb = cls


class MoneyR(BaseMoney):
    account = 'rub'


class MoneyD(BaseMoney):
    account = 'dollar'


class MoneyE(BaseMoney):
    account = 'euro'


#######################################################################
# Может мое решение будет кому интересно. Использовал isclose из библиотеки math. Достаточно удобная вещь
# Функция math.isclose() возвращает True если в пределах указанной точности, числа a и b близки настолько,
# что их можно считать равными.math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0):
from math import isclose


class DescriptorMoney():
    def __set_name__(self, owner, name):
        self.name = f'_{type(self).__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(self, *args, **kwargs):
        return

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    cb = DescriptorMoney()
    volume = DescriptorMoney()

    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    def __eq__(self, other):
        return isclose(self.converter(self), self.converter(other), rel_tol=0.1)

    # Аргумент rel_tol это относительный допуск, определяемый как максимально допустимая разница между числами a и b
    # относительно большего из них по модулю. По умолчанию rel_tol=1e-09, что гарантирует, что числа a и b будут
    # одинаковы, в пределах 9 десятичных цифр. Чтобы числа считались равными, если они, допустим, отличаются меньше
    # чем на 0.1%, то достаточно установить rel_tol=0.001, но в любом случае данный параметр, должен быть больше нуля:
    def __lt__(self, other):
        return self.converter(self) < self.converter(other)

    def __le__(self, other):
        return (self < other) or (self == other)

    def converter(self, obj):
        self.registered(obj)
        return obj.volume * obj.cb.rates['rub'] / obj.cb.rates[obj.val]

    @staticmethod
    def registered(obj):
        if not obj.cb:
            raise ValueError("Неизвестен курс валют.")


class MoneyR(Money): val = 'rub'


class MoneyD(Money): val = 'dollar'


class MoneyE(Money): val = 'euro'


########################################################################
# Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:
# body = Body(name, ro, volume)где name - название тела (строка); ro - плотность тела (число: вещественное или
# целочисленное); volume - объем тела  (число: вещественное или целочисленное).Для объектов класса Body должны
# быть реализованы операторы сравнения:body1 > body2  # True, если масса тела body1 больше массы тела body2
# body1 == body2 # True, если масса тела body1 равна массе тела body2
# body1 < 10     # True, если масса тела body1 меньше 10body2 == 5     # True, если масса тела body2 равна 5
# Масса тела вычисляется по формуле:m = ro * volume
# Задача только на первый взгляд кажется простой (релакс). На самом деле здесь есть очень нетривиальная вещь -
# сравнение вещественных чисел. В python выражение 0.1 + 0.2 == 0.3 возвращает False,  а 0.8 - 0.1 > 0.7 возвращает
# True. Если вы не знаете про метод math.isclose , то вы практически наверняка сделали задачу неверно
# (даже если она проходит тесты). Вот здесь неплохое объяснение проблемы:
# https://www.youtube.com/watch?v=6kPbj5o5aqA
# https://www.youtube.com/watch?v=c7tpUDT1Zmc
# https://davidamos.dev/the-right-way-to-compare-floats-in-python/
# В частности там рассказано почему не работает метод round и сравнение abs(a - b) < epsilon, в чем отличие
# absolute_tolerance и relative_tolerance. З.Ы. насчет своего решения тоже полной уверенности нет, но то
# что оно "ближе к истине" в этом не сомневаюсь.
from math import isclose

from functools import total_ordering


@total_ordering
class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __setattr__(self, key, value):
        if key == 'volume' and type(value) in (int, float):
            object.__setattr__(self, key, value)
        elif key == 'ro' and type(value) in (int, float):
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def __mass__(self):
        return self.volume * self.ro

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return isclose(self.__mass__(), other, rel_tol=1e-09, abs_tol=0.0)
        return isclose(self.__mass__(), other.__mass__())

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return round(self.__mass__(), 25) < round(other, 25)
        return round(self.__mass__(), 25) < round(other.__mass__(), 25)


########################################################################
def mass_arg(func):
    def wrapper(instance, other, *args):
        if isinstance(other, Body):
            return func(instance, other.mass)
        elif isinstance(other, (int, float)):
            return func(instance, other)
        else:
            raise TypeError(f"Not supported type {type(other)} in {func}")

    return wrapper


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    @property
    def mass(self):
        return (self.ro * self.volume)

    @mass_arg
    def __lt__(self, other):
        return (self.mass < other)

    @mass_arg
    def __eq__(self, other):
        return self.mass == other

    @mass_arg
    def __gt__(self, other):
        return self.mass > other


#######################################################################
from functools import total_ordering


@total_ordering
class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    @property
    def mass(self):
        return self.volume * self.ro

    def __eq__(self, other):
        val = other.mass if isinstance(other, Body) else other
        return self.mass == val

    def __lt__(self, other):
        val = other.mass if isinstance(other, Body) else other
        return self.mass < val


########################################################################
# Подвиг 10. Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:
# box = Box()А сам класс иметь следующие методы:
# add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
# get_things(self) - получение списка объектов ящика.Для описания предметов необходимо объявить еще один класс Thing.
# Объекты этого класса должны создаваться командой:obj = Thing(name, mass)где name - название предмета (строка);
# mass - масса предмета (число: целое или вещественное).Объекты класса Thing должны поддерживать операторы сравнения:
# obj1 == obj2obj1 != obj2Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и
# массы mass.Также объекты класса Box должны поддерживать аналогичные операторы сравнения:
# box1 == box2box1 != box2Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса
# Thing одного ящика и можно найти ровно один равный объект из второго ящика).

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __lt__(self, other):
        return self.mass < other.mass


class Box:
    def __init__(self):
        self.lst = list()

    def add_thing(self, obj):
        self.lst.append(obj)

    def get_things(self):
        return self.lst

    def __eq__(self, other):
        return all((value.name == sorted(other.lst, key=lambda x: x.mass)[i].name)
                   for i, value in enumerate(sorted(self.lst, key=lambda x: x.mass))) \
            and len(self.lst) == len(other.lst)


###############################################################################################################################################
class Thing:
    def __init__(self, name, mass):
        self.name = name.lower()
        self.mass = mass

    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass

    def __lt__(self, other):
        return self.mass < other.mass


class Box:
    def __init__(self):
        self.dct = dict()

    def add_thing(self, obj):
        if obj.name in self.dct:
            self.dct[obj.name] = sum([self.dct[obj.name], obj.mass])
        else:
            self.dct[obj.name] = obj.mass

    def get_things(self):
        return [*self.dct.items()]

    def __eq__(self, other):
        return all(value == other.dct[key] if other.dct[key] else None \
                   for key, value in self.dct.items())


########################################################################
class Box:
    def __init__(self):
        self.things = {}

    def add_thing(self, obj):
        self.things.setdefault(obj, 0)
        self.things[obj] += 1

    def get_things(self):
        return self.things

    def __eq__(self, other):
        return self.things == other.things


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name.lower(), self.mass))


########################################################################
class Box:
    def __init__(self):
        self.content = []

    def __eq__(self, other):
        if type(other) is Box:
            return sorted(self.content) == sorted(other.content)

    def add_thing(self, obj):
        if type(obj) is Thing:
            self.content.append(obj)

    def get_things(self):
        return self.content


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if type(other) is Thing:
            return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __lt__(self, other):
        if type(other) is Thing:
            return (self.name, self.mass) < (other.name, other.mass)


########################################################################
from collections import Counter


# Подсчет количества повторений элементов в последовательности.

class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        return Counter(self.things) == Counter(other.things)


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __hash__(self):
        return hash((self.name, self.mass))


#######################################################################
# __________________________________Методы __eq__ и __hash________________________________________

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))  # т.е. hash((1, 2))  <----


p1 = Point(1, 2)
a = (1, 2)
#  hash((1,2)) == hash((1, 2)) --------------------------------|

print(hash(p1) == hash(a))  # True, хэши в переменной "а" и с экземпляре класса вычисляются одинаково, отсюда и равные


# хеши, но не равные объекты
###################################################################
# Объекты равны, хеши не равны:

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y


a = Point(1, 2)
b = Point(1, 2, 3)
print(a == b, hash(a) == hash(b))  # True False


########################################################################
# Подвиг 4. Объявите в программе класс с именем Rect (прямоугольник), объекты которого создаются командой:
# rect = Rect(x, y, width, height)где x, y - координата верхнего левого угла (числа: целые или вещественные);
# width, height - ширина и высота прямоугольника (числа: целые или вещественные).
# В этом классе определите магический метод, чтобы хэши объектов класса Rect с равными width, height были равны.
class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __eq__(self, other):
        return (self.width, self.height) == (other.width, other.height)
        # return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.width, self.height))


# По примеру указанному в задаче, идет проверка хешей записанных в переменную, и потом эти переменные сравниваются.
# Не идет сравнение объектов, а их хешей
r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)  # h1 == h2


########################################################################
class Rect:
    def __init__(self, *args):
        if not all([isinstance(x, (int, float)) for x in args]):
            raise TypeError()
        self.x, self.y, self.width, self.height = args

    def __hash__(self):
        return hash((abs(self.x), self.width, self.height))


#######################################################################
class Index:
    START_INDEX = 0

    def __init__(self):
        self.id = Index.START_INDEX
        Index.START_INDEX += 1

    def __hash__(self):
        return hash(str(self.id))


# И делается попытка создать словарь с ключами из объектов этого класса:

id1 = Index()
id2 = Index()
d = {id1: id1, id2: id2}
# словарь будет успешно создан и к его значениям можно обращаться, например, командой: d[id1].id
# Судя по id, объекты разные (у меня id были 2479904554144 и 2479904553664). Они и должны быть разными,
# так как у первого локальный атрибут = 0, а у второго = 1.
# прикол с тем что сначала index = 0 а потом 1 от того и разные хеши
########################################################################
# Подвиг 6. Объявите класс с именем ShopItem (товар), объекты которого создаются командой:
# item = ShopItem(name, weight, price)где name - название товара (строка); weight - вес товара
# (число: целое или вещественное); price - цена товара (число: целое или вещественное).Определите в этом классе
# магические методы:__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы
# равные хэши;__eq__() - чтобы объекты с одинаковыми хэшами были равны.Затем, из входного потока прочитайте
# строки командой:lst_in = list(map(str.strip, sys.stdin.readlines()))Строки имеют следующий формат:
# название товара 1: вес_1 цена_1...название товара N: вес_N цена_NНапример:
# Системный блок: 1500 75890.56Монитор Samsung: 2000 34000Клавиатура: 200.44 545Монитор Samsung: 2000 34000
# Как видите, товары в этом списке могут совпадать.Необходимо для всех этих строчек сформировать соответствующие
# объекты класса ShopItem и добавить в словарь с именем shop_items. Ключами словаря должны выступать сами объекты,
# а значениями - список в формате:[item, total]где item - объект класса ShopItem; total - общее количество
# одинаковых объектов (с одинаковыми хэшами). Подумайте, как эффективно программно наполнять такой словарь,
# проходя по списку lst_in один раз.
import sys

lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!

shop_items = dict()
# total = 1
for i in lst_in:
    name, v = i.split(':')
    weight, price = map(float, v.split())
    if ShopItem(name, weight, price) in shop_items:
        # total += 1
        # shop_items[ShopItem(name, weight, price)] = [ShopItem(name, weight, price), total]
        shop_items[ShopItem(name, weight, price)][1] += 1
    else:
        # shop_items[ShopItem(name, weight, price)] = [ShopItem(name, weight, price), total]
        shop_items[ShopItem(name, weight, price)] = [ShopItem(name, weight, price), 1]
    # shop_items[ShopItem(name, weight, price)] = [ShopItem(name, weight, price),
    # total + 1 if ShopItem(name, weight,price) in shop_items else total]
###############################################################################################################################################
for item in lst_in:
    name, weight, price = item.rsplit(maxsplit=2)  # Разбивает строку по символу/подстроке начиная справа.
    # maxsplit=-1 - int, сколько раз делить строку. По умолчанию -1 - неограниченно.

    # obj = ShopItem(name[:-1], weight, price)
    obj = ShopItem(name.rstrip(':'), weight, price)
    # v1
    shop_items.setdefault(obj, [obj, 0])[1] += 1
    # Метод dict.setdefault() вернет значение словаря dict, соответствующее ключу key.
    # Если указанный ключ key отсутствует, вставит его в словарь dict со значением default и вернет значение default.
    # v2
    shop_items[obj] = shop_items.get(obj, [obj, 0])  # значение по умолчанию если ключа нет.
    shop_items[obj][1] += 1
########################################################################
from collections import Counter

items = []
for line in lst_in:
    name, data = line.split(':')
    weight, price = map(float, data.split())
    items.append(ShopItem(name, weight, price))

shop_items = {k: [k, v] for k, v in Counter(items).items()}
# Подсчет количества повторений элементов в последовательности.Это коллекция, в которой элементы хранятся в
# виде словарных ключей, а их счетчики хранятся в виде значений словаря.
########################################################################
lst = []
shop_items = {}
for i in lst_in:
    i = i.split(":")
    item = ShopItem(i[0], i[1].split()[0], i[1].split()[1])
    if item not in shop_items.keys():
        shop_items[item] = [item, 1]
    else:
        shop_items[item] = [item, shop_items[item][1] + 1]
########################################################################
shop_items = {}
for s in lst_in:
    s = s.split(':')
    name = s[0].strip()
    weight, price = map(float, s[1].strip().split())
    obj = ShopItem(name, weight, price)
    shop_items[obj] = [obj, shop_items.get(obj)[1] + 1 if obj in shop_items else 1]


#######################################################################
# Реализация с дескриптором, в котором решил попробовать добавить __repr__ для более красивого и наглядного вывода
# ошибок при проверке типов данных. При переборе входящих данных циклом перед добавлением в словарь также реализовал
# проверку price и weight на принадлежность к int или float.
class DataDescriptor:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __repr__(self):
        return self.name.split('__')[-1]

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__check_value(instance, value)
        setattr(instance, self.name, value)

    def __check_value(self, instance, value):
        attr_to_check = str(self)
        if attr_to_check == 'name' and type(value) != str:
            raise ValueError(f'для атрибута "{attr_to_check}" значение должно быть типа str')
        if attr_to_check in ('weight', 'price') and type(value) not in (int, float):
            raise ValueError(f'для атрибута "{attr_to_check}" значение должно быть типа int или float')


class ShopItem:
    name = DataDescriptor()
    weight = DataDescriptor()
    price = DataDescriptor()

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


# lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = {}
for line in lst_in:
    name, other = line.split(': ')
    weight, price = other.split()
    weight = float(weight) if '.' in weight else int(weight)
    price = float(price) if '.' in price else int(price)
    obj = ShopItem(name, weight, price)
    if obj in shop_items.keys():
        shop_items[obj][1] += 1
    else:
        shop_items[obj] = [obj, 1]


########################################################################
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name' and type(value) == str:
            object.__setattr__(self, key, value)
            # super().__setattr__(key, value)
        elif key in ('weight', 'price') and type(value) in (int, float):
            super().__setattr__(key, value)
        else:
            raise TypeError('Неверный формат данных')

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


def get_ShopItem(item_string):
    name = item_string.split(':')[0].strip()
    weight = float(item_string.split(':')[1].split()[0].strip())
    price = float(item_string.split(':')[1].split()[1].strip())
    return ShopItem(name, weight, price)


shop_items = {get_ShopItem(i): [get_ShopItem(i), lst_in.count(i)] for i in lst_in}
# сколько раз указанный элемент i появился в последовательности lst_in.
########################################################################
shop_items = {}
for i in lst_in:
    s = re.split(': |\s+(?=\d)', i)
    # Функция split() модуля re делит строку по появлению шаблона регулярного выражения pattern и возвращает
    # список получившихся подстрок
    k = ShopItem(name=s[0], weight=s[1], price=s[2])
    if k not in shop_items:
        shop_items[k] = [k, 1]
    else:
        shop_items[k][1] += 1


#######################################################################
# Подвиг 7. Объявите класс с именем DataBase (база данных - БД), объекты которого создаются командой:
# db = DataBase(path)где path - путь к файлу с данными БД (строка).Также в классе DataBase нужно объявить следующие
# методы:write(self, record) - для добавления новой записи в БД, представленной объектом record;
# read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk
# (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)
# Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:
# record = Record(fio, descr, old)где fio - ФИО некоторого человека (строка); descr - характеристика человека
# (строка); old - возраст человека (целое число).В каждом объекте класса Record должны формироваться следующие
# локальные атрибуты:pk - уникальный идентификатор записи (число: целое, положительное);
# формируется автоматически при создании каждого нового объекта;fio - ФИО человека (строка);
# descr - характеристика человека (строка);old - возраст человека (целое число).
# Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old (без учета регистра).
# Если они одинаковы для разных записей, то и хэши должны получаться равными. Также для объектов класса Record  с
# одинаковыми хэшами оператор == должен выдавать значение True, а с разными хэшами - False.
# Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase),
# ключами которого являются объекты класса Record, # dict_db[rec1] = [rec1, rec2, ..., recN]где rec1, rec2, ..., recN
# - значениями словаря должен быть список из объектов  класса Rect с набором атрибутов: descr (строка), fio (строка),
# old (целое число) Для наполнения БД прочитайте строки из входного потока с помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))где каждая строка представлена в формате:
# "ФИО; характеристика; возраст"Например:Балакирев С.М.; программист; 33Кузнецов А.В.; разведчик-нелегал; 35
# уворов А.В.; полководец; 42Иванов И.И.; фигурант всех подобных списков; 26Балакирев С.М.; преподаватель; 37
# Каждая строка должна быть представлена объектом класса Record и записана в БД db (в словарь db.dict_db).

class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

        # setdefault вернёт пустой список, если ключа нет, а если есть, то его значение,
        # Метод dict.setdefault() вернет значение словаря dict, соответствующее ключу key.
        # Если указанный ключ key отсутствует, вставит его в словарь dict со значением default и вернет значение
        # default. Если значение по умолчанию default не установлено и ключ отсутствует, метод вставит ключ в словарь
        # со значением None, при этом никакое значение не возвращается.

        # ч/з key == pk :
        # self.dict_db.setdefault(record.pk, []).append(record)
        # print(self.dict_db.items())
        # dict_items([(1, [<__main__.Record object at 0x0000022469570250>]), (2, [<__main__.Re....

        # for item in self.dict_db.items():  # item: [<__main__.Record object at 0x000001C4133B0650>]
        #     for value in item[1]:  # value: <__main__.Record object at 0x000001C4133B0710>

    def read(self, pk):
        for row in self.dict_db.values():
            for i in row:  # row:  [<__main__.Record object at 0x00000156F4C60B10>]
                if i.pk == pk:  # i 7
                    return i  # <__main__.Record object at 0x000001FE18000610>

    # obj = [i for item in self.dict_db.values() for i in item if i.pk == pk]
    # return obj[0]

    # r = (x for row in self.dict_db.values() for x in row)
    # obj = tuple(filter(lambda x: x.pk == pk, r))
    # return obj[0] if len(obj) > 0 else None


class Record:
    record_count = 0

    def __init__(self, fio, descr, old):
        self.descr = descr
        self.old = old
        self.fio = fio
        self.pk = self.__count()

    @classmethod
    def __count(cls):
        cls.record_count += 1
        return cls.record_count

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    # hash(()) -> выч-ся на основе кортежа

    def __eq__(self, other):
        return hash(self) == hash(other)


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33']

db = DataBase('bdDatabase')
for l in lst_in:
    args = list(map(str.strip, l.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"
########################################################################

###############################################################################################################################################
##

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
