########################################################################
# Подвиг 1. Каково назначение магических методов __str__ и __repr__?
# метод __repr__ возвращает строковую информацию об объекте класса для служебного пользования (например, в командную
# строку), а также может использоваться, если не определен метод __str__

# метод __str__ вызывается (если он определен в классе) для вывода информации об объекте класса в консоль с
# помощью функций print() и str()

# _______________3.1 Магические методы. Методы __str__ и __repr_
#######################################################################
# Создайте класс Person, у которого есть:конструктор __init__, принимающий 3 аргумента: name, surname, gender.
# Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male". Если в атрибут gender
# передается любое другое значение, печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# и проставить атрибут gender значением "male"переопределить метод __str__ следующим образом:
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>"
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя
class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender == 'male' or gender == 'female':
            self.gender = gender
        else:
            self.gender = 'male'
            print(f'Не знаю, что вы имели ввиду? Пусть это будет мальчик!')

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        elif self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'


########################################################################
class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = self.check_gender(gender)

    @classmethod
    def check_gender(cls, gender):
        # @staticmethod
        # def check_gender(gender):
        if gender not in ['male', 'female']:
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            return 'male'
        return gender


###############################################################################################################################################
# Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
# конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо
# оставить только целые числа и сохранить их в атрибут values в виде списка;переопределить метод __str__ так, чтобы
# экземпляр класса Vector выводился следующим образом: «Вектор(<value1>, <value2>, <value3>, ...)», если вектор не
# пустой. При этом значения должны быть упорядочены по возрастанию (будьте аккуратнее с пробелами, они стоят
# только после запятых, см. пример ниже);«Пустой вектор», если наш вектор не хранит в себе значения
class Vector:
    def __init__(self, *args):
        self.values = self.func_args(*args)

    @classmethod
    def func_args(cls, *args):
        return sorted(x for x in args if type(x) == int)

    # return sorted(filter(lambda x: type(x) is int, args))

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        else:
            return f'Пустой вектор'


########################################################################
# Давайте определим магические методы __str__ и __repr__ для класса GroceryItem, представляющего продуктовый товар:
# Создайте класс GroceryItem, который имеет следующие методы:метод __init__, который устанавливает значения
# атрибутов name, price и quantity: название товара, его цену и количествомагический метод __str__, который возвращает
# строковое представление товара в следующем виде:ame: {name}Price: {price}Quantity: {quantity}магический метод
# __repr__, который возвращает однозначное строковое представление объектаGroceryItem({name}, {price}, {quantity})
class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'


########################################################################
class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"""Name: {self.name}
Price: {self.price}
Quantity: {self.quantity}"""

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'


########################################################################
class GroceryItem:
    def __init__(self, *args):
        self.name, self.price, self.quantity = args
        self.attr = ('name', 'price', 'quantity')

    def __str__(self):
        return '\n'.join(f'{attr.title()}: {getattr(self, attr)}' for attr in self.attr)

    def __repr__(self):
        return "GroceryItem" + str(tuple(getattr(self, x) for x in self.attr)).replace("'", "")


#######################################################################
# Создайте класс Hero, который имеет следующие методы:метод __len__, который возвращает количество атрибутов экземпляра
# приватный метод __str__, который возвращает строковое представление героя. Для этого нужно перечислить все атрибуты
# в алфавитном порядке на отдельной строке, напротив каждого атрибута указать его значение. Вот такой формат должен
# получится:атрибут_1: значение_атрибут_1атрибут_2: значение_атрибут_2..атрибут_N: значение_атрибут_N
# Если у экземпляра нету атрибутов, необходимо вернуть пустую строку
class Hero:

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        if not len(self.__dict__):
            return f''
        else:
            string = ''
            for key, value in sorted(self.__dict__.items(), key=lambda x: x[0]):
                string += f'{key}: {str(value)}\n'
            return string.rstrip()

    ########################################################################
    def __str__(self):
        return "\n".join([f"{key}: {value}" for key, value in sorted(self.__dict__.items())])


########################################################################
# Подвиг 2. Объявите класс с именем Book (книга), объекты которого создаются командой:
# book = Book(title, author, pages)где title - название книги (строка); author - автор книги (строка);
# pages - число страниц в книге (целое число).Также при выводе информации об объекте на экран командой:
# print(book)должна отображаться строчка в формате:"Книга: {title}; {author}; {pages}"Например:
# "Книга: Муму; Тургенев; 123"Прочитайте из входного потока строки с информацией
import sys


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Книга: {self.title}; {self.author}; {int(self.pages)}'


lst_in = list(map(str.strip, sys.stdin.readlines()))
book = Book(*lst_in)
# book = Book(lst_in[0], lst_in[1], int(lst_in[2]))

print(book)


#######################################################################
# Подвиг 3. Объявите класс с именем Model, объекты которого создаются командой:
# model = Model()Объявите в этом классе метод query() для формирования записи базы данных. Использоваться этот
# метод должен следующим образом:model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)Например:
# model.query(id=1, fio='Sergey', old=33)Все эти переданные данные должны сохраняться внутри объекта model класса
# Model. Затем, при выполнении команды:print(model)В консоль должна выводиться информация об объекте в формате:
# "Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"Например:"Model: id = 1, fio = Sergey, old = 33"
# Если метод query() не вызывался, то в консоль выводится строка:"Model"
class Model:
    def __init__(self):
        self.model = None

    def query(self, *args, **kwargs):
        # print(kwargs)  # {'id': 1, 'fio': 'Sergey', 'old': 33}
        self.model = kwargs
        # print(self.model)

    def __str__(self):
        if self.model is None:
            return f'Model'
        string = ''
        for k, v in self.model.items():
            string += f'{k} = {v}, '

        return f'Model: {string.rstrip(", ")}'


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)


########################################################################
class Model:
    def __init__(self):
        self.model = 'Model'

    def query(self, **kwargs):
        self.model += ': ' + ', '.join(map(lambda i: f'{i[0]} = {i[1]}', kwargs.items()))

    def __str__(self):
        return self.model


###############################################################################################################################################
def query(self, *args, **kwargs):
    # print(kwargs)  # {'id': 1, 'fio': 'Sergey', 'old': 33}
    self.model = kwargs


# Это решение не учитывает, что у ЭК может быть вызван метод query несколько раз с разным набором параметров.
# При этом    # каждый раз будет происходить не апдейт словаря, а его перенаполнение с утратой всех прежних значений.
# Нужно  использовать self.models|**kwargs


def query(self, *args, **kwargs):
    # self.model |= kwargs
    self.model.update(**kwargs)

    ########################################################################
    def __str__(self):
        if not getattr(self, 'data', False):  # getattr(object, name, default)
            # default - значение по умолчанию, которое будет возвращено, если имя атрибута name отсутствует.
            return 'Model'
        string = ','.join(map(lambda key, value: f' {key} = {value}', self.data.keys(), self.data.values()))
        return f'Model:{string}'


########################################################################
class Model:
    def query(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return 'Model' + (': ' if self.__dict__ else '') + ', '.join(
            [f'{k} = {self.__dict__[k]}' for k in self.__dict__])


########################################################################
class Model:
    def query(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        if self.__dict__:
            return "Model: " + ", ".join(["{} = {}".format(k, v) for k, v in self.__dict__.items()])
        return "Model"


#######################################################################
# Подвиг 4. Объявите класс WordString, объекты которого создаются командами:w1 = WordString()w2 = WordString(string)
# где string - передаваемая строка. Например:words = WordString("Курс по Python ООП")
# Реализовать следующий функционал для объектов этого класса:len(words) - должно возвращаться число слов в переданной
# строке (слова разделяются одним или несколькими пробелами);words(indx) - должно возвращаться слово по его индексу
# (indx - порядковый номер слова в строке, начиная с 0).Также в классе WordString реализовать объект-свойство
# (property):string - для передачи и считывания строки.

class WordString:
    def __init__(self, string=None):
        self.string = string

    def __len__(self):
        return len(self.string.split())

    # str.split() - использование метода без указания разделителя задействует алгоритм благодаря которому разделителем
    # будет являться любая последовательность пробельных символов

    def words(self, indx):
        return self.string.split()[indx]

    def __call__(self, indx):
        return self.words(indx)

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")


########################################################################
class WordString:
    def __setattr__(self, key, value):
        # if key == 'string':
        self.__dict__[key] = value  # чтобы не было зацикливания

    # object.__setattr__(self, key, value)
    # super().__setattr__(key, value)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx):
        if indx < len(self.string):
            return self.string.split()[indx]


########################################################################
# Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:Здесь создается список
# из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:obj = ObjList(data)
# где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие
# локальные атрибуты:__data - ссылка на строку с данными;__prev - ссылка на предыдущий объект связного списка
# (если объекта нет, то __prev = None);__next - ссылка на следующий объект связного списка (если объекта нет,
# то __next = None).В свою очередь, объекты класса LinkedList должны создаваться командой:linked_lst = LinkedList()
# и содержать локальные атрибуты:head - ссылка на первый объект связного списка (если список пуст, то head = None);
# tail - ссылка на последний объект связного списка (если список пуст, то tail = None).
# А сам класс содержать следующие методы:add_obj(obj) - добавление нового объекта obj класса ObjList в конец
# связного списка;remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру
# (индексу); индекс отсчитывается с нуля.Также с объектами класса LinkedList должны поддерживаться следующие операции:
# len(linked_lst) - возвращает число объектов в связном списке;linked_lst(indx) - возвращает строку __data, хранящуюся
# в объекте класса ObjList, расположенного под индексом indx (в связном списке).Пример использования классов
#  Длина обычного списка лимитирована. Связного - нет.
# Все объекты будут храниться в цепочке.Сборщик мусора их не будет трогать так как остаются ссылки на них.
class ObjList:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            # if isinstance(obj,(ObjList,type(None))):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_next(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx):
        obj = self.__get_obj_next(indx)
        if obj is None:
            return
        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        h = self.head
        n = 0
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx):
        obj = self.__get_obj_next(indx)
        return obj.data if obj else None


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1)  # s = Balakirev


#######################################################################
class Description:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'  # Чтоб дескриптор работал, в set_name нужно так прописать чтобы
        # прошли проверки в assert
        # self.name = '__' + name

    # если пишут атрибуты __attr имеется в виду приватный атрибут. если через set_name задавать имя
    # как "__" + name это будет не приватный атрибут а именно, как бы это странно не выгладело, тупо
    # атрибут с двумя подчеркиваниями. попробуйте создать приватный атрибут вообще без десрипторов и
    # проперти и посмотрите как он отображается в __dict__, вот точно с таким же именем и должен
    # создаваться атрибут в вашей программе чтобы прошли тесты, т.к. тесты рассчитаны на приватные
    # атрибуты
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, ObjList) and value is not None:
            raise TypeError("ObjList objects can only be assigned to ObjList objects")
        setattr(instance, self.name, value)


class ObjList:
    data = Description()
    prev = Description()
    next = Description()

    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


########################################################################
class ObjList:

    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

    def __setattr__(self, attr, value):
        if attr == 'data' and isinstance(value, str):
            object.__setattr__(self, '_ObjList__' + attr, value)
        elif attr in ('prev', 'next') and isinstance(value, (ObjList, type(None))):
            object.__setattr__(self, '_ObjList__' + attr, value)

    def __getattribute__(self, attr):
        if attr in ('data', 'prev', 'next'):
            return object.__getattribute__(self, '_ObjList__' + attr)
        return object.__getattribute__(self, attr)


class LinkedList:
    def chek_index(self, index):
        if not isinstance(index, int):
            raise TypeError('list indices must be integers, not str')
        if index >= self.len or index < 0:
            raise IndexError('list index out of range')

    def __init__(self):
        self.head = self.tail = None
        self.len = 0

    def add_obj(self, obj):
        if isinstance(obj, ObjList):
            obj.prev = self.tail
            if self.tail:
                self.tail.next = obj
            else:
                self.head = obj
            self.tail = obj
            self.len += 1

    def remove_obj(self, index):
        obj = self(index, data=False)
        self.len -= 1
        if obj.prev:
            obj.prev.next = obj.next
        else:
            self.head = obj.next
        if obj.next:
            obj.next.prev = obj.prev
        else:
            self.tail = obj.prev

    def __len__(self):
        return self.len

    def __call__(self, index, data=True):
        self.chek_index(index)
        obj = self.head
        index -= 1
        while index != -1:
            obj = obj.next
            index -= 1
        if data:
            return obj.data
        return obj


###############################################################################################################################################
class Desc:
    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        if __name in ('data', 'prev', 'next', 'head', 'tail'):
            __name = f'_{type(self).__name__}__{__name}'
        return super().__setattr__(__name, __value)

    def __getattr__(self, name):
        return self.__getattribute__(f'_{type(self).__name__}__{name}')


class ObjList(Desc):
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None


class LinkedList(Desc):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_obj(self, obj):
        if self.__head:
            self.__tail.next = obj
            obj.prev = self.__tail
        else:
            self.__head = obj
        self.__tail = obj

    def remove_obj(self, indx):
        n = self.iteration_over_all_elements('cnt < indx', 'n', indx)
        if n.prev:
            n.prev.next = n.next
        else:
            self.__head = self.__head.next
        if n.next:
            n.next.prev = n.prev
        else:
            self.__tail = self.__tail.prev

    def __len__(self):
        return self.iteration_over_all_elements('n', 'cnt')

    def __call__(self, indx):
        return self.iteration_over_all_elements('cnt < indx', 'n.data', indx)

    def iteration_over_all_elements(self, condition, data_to_return, indx=0):
        n = self.__head
        cnt = 0
        while eval(condition):
            n = n.next
            cnt += 1
        return eval(data_to_return)


########################################################################
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    def __getattr__(self, name):
        return object.__getattribute__(self, self.__fixname(name))

    def __setattr__(self, name, value):
        self.__dict__[self.__fixname(name)] = value

    def __fixname(self, name):
        return f'_{type(self).__name__}__{name}' if name in ('data', 'prev', 'next') else name

    def __str__(self):
        return self.__data

    def glue(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next


class LinkedList:
    def __init__(self):
        self.__list = []
        self.head = None
        self.tail = None

    def __len__(self):
        return len(self.__list)

    def __call__(self, indx, *args, **kwargs):
        if 0 <= indx < len(self):
            return self.__list[indx].data

    def add_obj(self, obj):
        if not len(self):
            self.head = obj
        else:
            prev = self.__list[-1]
            obj.prev, prev.next = prev, obj
        self.tail = obj
        self.__list.append(obj)

    def remove_obj(self, indx):
        if 0 <= indx < len(self):
            removed = self.__list.pop(indx)
            removed.glue()
            if removed == self.head:
                self.head = removed.next
            if removed == self.tail:
                self.tail = removed.prev


########################################################################
# все на обычном List построено ))
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self): return self.__data


class LinkedList:
    def __init__(self):
        self.__lst = []
        self.__upd()

    def __upd(self):
        if self.__lst:
            self.head = self.__lst[0]
            self.tail = self.__lst[-1]
        else:
            self.head = self.tail = None

    def __len__(self):
        return len(self.__lst)

    def __call__(self, idx):
        try:
            return self.__lst[idx].data
        except:
            return None

    def add_obj(self, obj):
        self.__lst.append(obj)
        self.__upd()

    def remove_obj(self, idx):
        try:
            self.__lst.pop(idx)
            self.__upd()
        except:
            pass


########################################################################
# Подвиг 6. Объявите класс с именем Complex для представления и работы с комплексными числами. Объекты этого класса
# должны создаваться командой:cm = Complex(real, img)где real - действительная часть комплексного числа
# (целое или вещественное значение); img - мнимая часть комплексного числа (целое или вещественное значение).
# Объявите в этом классе следующие объекты-свойства (property):real - для записи и считывания действительного значения;
# img - для записи и считывания мнимого значения.При записи новых значений необходимо проверять тип передаваемых данных.
# Если тип не соответствует целому или вещественному числу, то генерировать исключение командой:
# raise ValueError("Неверный тип данных.")Также с объектами класса Complex должна поддерживаться функция:
# res = abs(cm)возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img) -
# корень квадратный от суммы квадратов действительной и мнимой частей комплексного числа).Создайте объект cmp класса
# Complex для комплексного числа с real = 7 и img = 8. Затем, через объекты-свойства real и img измените эти значения
# на real = 3 и img = 4. Вычислите модуль полученного комплексного числа (сохраните результат в переменной c_abs).
from math import sqrt


class Complex:
    def __init__(self, real, img):
        # чтобы гарантировать существовагние атрибутов
        self.__real = self.__imag = 0
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        self.__img = img

    def __setattr__(self, key, value):
        # чтобы в момент создания приватных аттрибутов туда не передали другие типы данных
        if not isinstance(value, (int, float)):
            raise ValueError("Неверный тип данных.")
        object.__setattr__(self, key, value)

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)


#######################################################################
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __setattr__(self, key, value):
        if key in ('real', 'img'):
            if type(value) not in (int, float):
                raise ValueError("Неверный тип данных.")
        object.__setattr__(self, key, value)
        # super().__setattr__(key, value)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)


########################################################################
from typing import TypeVar
from math import sqrt

T = TypeVar('T', float, int)


def validator(type_value):
    def wrapper1(func):
        def wrapper2(self, value):
            if not isinstance(value, type_value):
                raise ValueError("Неверный тип данных.")
            func(self, value)

        return wrapper2

    return wrapper1


class Complex:
    __img: T
    __real: T

    def __init__(self, real: T, img: T):
        self.img = img
        self.real = real

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)

    @property
    def img(self):
        return self.__img

    # Проверка через декоратор.
    @img.setter
    @validator((float, int))
    def img(self, value: T):
        self.__img = value

    @property
    def real(self):
        return self.__real

    @real.setter
    @validator((float, int))
    def real(self, value: T):
        self.__real = value


########################################################################
# Подвиг 7. Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором (у которого n координат).
# Объекты этого класса должны создаваться командами:# создание 5-мерного радиус-вектора с нулевыми значениями
# координат (аргумент - целое число больше 1)vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0
# создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
# vector = RadiusVector(1, -5, 3.4, 10)То есть, при передаче одного значения, оно интерпретируется, как размерность
# нулевого радиус-вектора. Если же передается более одного числового аргумента, то они интерпретируются, как координаты
# радиус-вектора.Класс RadiusVector должен содержать методы:set_coords(coord_1, coord_2, ..., coord_N) -
# для изменения координат радиус-вектора;get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).
# Также с объектами класса RadiusVector должны поддерживаться следующие функции:len(vector) - возвращает число
# координат радиус-вектора (его размерность);abs(vector) - возвращает длину радиус-вектора (вычисляется как:
# sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N) - корень квадратный из суммы квадратов координат).

class RadiusVector:
    def __init__(self, *args):
        # print(args,*args) # (3,) 3
        if len(args) == 1:
            self.__coords = [0] * args[0]
        else:
            self.__coords = list(args)

    def set_coords(self, *args):
        n = min(len(args), len(self.__coords))
        self.__coords[:n] = args[:n]

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sum(map(lambda x: x ** 2, self.__coords)) ** 0.5

    # def __str__(self):
    #     return str(self.__coords)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)


#######################################################################
def set_coords(self, *args):
    if len(args) > len(self.__coords):
        self.__coords = list(args[:len(self.__coords)])
    else:
        self.__coords[:len(args)] = list(args)


########################################################################
class RadiusVector:
    def __init__(self, *args):
        self.coords = [0] * args[0] if len(args) == 1 else [*args]

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sum([i * i for i in self.coords]) ** 0.5

    def set_coords(self, *coord):
        self.coords = list(coord[:len(self.coords)]) + self.coords[len(coord):]
        # vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
        # vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
        # Т.е. если число параметров передаваемых в метод def set_coords(self, *coord): БОЛЬШЕ чем задано при
        # инициализации, то мы выбираем из этих параметров только необходимое число - coord[:len(self.coords),
        # соответственно self.coords[len(coord):]  будет равен  пустому спискуЕсли число параметров передаваемых в
        # метод def set_coords(self, *coord): МЕНЬШЕ чем задано при инициализации, то мы берем все эти параметры и
        # добавляем к ним необходимое число старых значений атрибута (списка) self.coords
        # здесь self.coords[len(coord):]  будет содержать последние элементы старого списка.

    def get_coords(self):
        return tuple(self.coords)

    ###############################################################################################################################################
    def set_coords(self, *args):
        for i, j in zip(range(len(self.coords)), args):
            self.coords[i] = j


########################################################################
# Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:
# dt = DeltaClock(clock1, clock2)где clock1, clock2 - объекты другого класса Clock для хранения текущего времени.
# Эти объекты должны создаваться командой:clock = Clock(hours, minutes, seconds)где hours, minutes, seconds - часы,
# минуты, секунды (целые неотрицательные числа).В классе Clock также должен быть (по крайней мере) один метод
# (возможны и другие):get_time() - возвращает текущее время в секундах
# (то есть, значение hours * 3600 + minutes * 60 + seconds).После создания объекта dt класса DeltaClock,
# с ним должны выполняться команды:str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате:
# часы: минуты: секундыlen_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
# print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# Если разность получается отрицательной, то разницу времен считать нулевой.Пример использования классов
# (эти строчки в программе писать не нужно):Обратите внимание, добавляется незначащий ноль, если число меньше 10.
class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        start = self.clock1.get_time()
        end = self.clock2.get_time()
        diff = (start - end)
        return diff if diff > 0 else 0

    def __str__(self):
        time = self.__len__()
        h = time // 3600
        m = time % 3600 // 60
        s = time % 3600 % 60
        return f'{h:02}: {m:02}: {s:02}'


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400

str_dt = str(dt)  # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)  # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)  # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды


########################################################################
class DeltaClock:
    def __init__(self, *args):
        self.clock = args

    def calc(self, args):
        start = args[0].get_time()
        end = args[1].get_time()
        return start - end

    def __len__(self):
        diff = self.calc(self.clock)
        return diff if diff > 0 else 0

    def __str__(self):
        time = self.calc(self.clock)
        h, ost_h = divmod(time, 3600)
        m, ost_m = divmod(ost_h, 60)
        s = ost_m
        return f'{h:02}: {m:02}: {s:02}'


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = self.chheck_int(hours)
        self.minutes = self.chheck_int(minutes)
        self.seconds = self.chheck_int(seconds)

    @staticmethod
    def chheck_int(args):
        if type(args) == int and args >= 0:
            return args

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


########################################################################
# import time
def __str__(self):
    # time.strftime(format[, t]) Получение форматированной строки с датой и временем
    # t - кортеж или структура времени time.struct_time.
    # time.gmtime([secs]) -  Преобразовать секунды в структуру даты и времени.
    return time.strftime("%H: %M: %S", time.gmtime(self.__len__()))


#######################################################################
# Подвиг 9. Объявите класс Recipe для представления рецептов. Отдельные ингредиенты рецепта должны определяться классом
# Ingredient. Объекты этих классов должны создаваться командами:ing = Ingredient(name, volume, measure)
# recipe = Recipe()recipe = Recipe(ing_1, ing_2,..., ing_N)где ing_1, ing_2,..., ing_N - объекты класса Ingredient.
# В каждом объекте класса Ingredient должны создаваться локальные атрибуты:name - название ингредиента (строка);
# volume - объем ингредиента в рецепте (вещественное число);measure - единица измерения объема ингредиента (строка),
# например, литр, чайная ложка, грамм, штук и т.д.;С объектами класса Ingredient должна работать функция:
# str(ing)  # название: объем, ед. изм.и возвращать строковое представление объекта в формате:"название: объем, ед. изм.
# "Например:ing = Ingredient("Соль", 1, "столовая ложка")s = str(ing) # Соль: 1, столовая ложкаКласс Recipe должен
# иметь следующие методы:add_ingredient(ing) - добавление нового ингредиента ing (объект класса Ingredient) в
# рецепт (в конец);remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса Ingredient)
# из рецепта;get_ingredients() - получение кортежа из объектов класса Ingredient текущего рецепта.
# Также с объектами класса Recipe должна поддерживаться функция:len(recipe) - возвращает число ингредиентов в рецепте.
class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __setattr__(self, key, value):
        if key in ('name', 'measure'):
            if not isinstance(value, str):
                raise ValueError()
        if key == 'volume':
            if not isinstance(value, int):
                raise ValueError()
        return object.__setattr__(self, key, value)

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args):
        self.ing = list(args)

    @property
    def ing(self):
        return self.__ing

    @ing.setter
    def ing(self, args):
        if len(args):
            self.__ing = [i for i in list(args) if isinstance(i, Ingredient)]
        else:
            self.__ing = list()
        # self.__ing = list(args)

    def add_ingredient(self, ing):
        self.ing.append(ing)

    def remove_ingredient(self, ing):
        self.ing.remove(ing)

    def get_ingredients(self):
        return tuple(self.ing)

    def __str__(self):
        string = ''
        for ing in self.ing:
            string += f'{ing.__str__()}; '
        return f'{string.strip()}'  # Соль: 1, столовая ложка; Мука: 1, кг; Масло: 100, гр;

    def __len__(self):
        return len(self.ing)


ing = Ingredient("Соль", 1, "столовая ложка")
s = str(ing)  # Соль: 1, столовая ложка
print(s)
recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe)  # n = 3
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
