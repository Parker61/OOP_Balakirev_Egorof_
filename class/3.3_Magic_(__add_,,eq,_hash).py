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

# ########################################################################

########################################################################

########################################################################

#######################################################################
# https://docs-python.ru/donate/732618839844207080/
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
