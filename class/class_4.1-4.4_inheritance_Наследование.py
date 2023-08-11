# _______Egorof________________________________________________________________
# __________Наследование______________________________________________________
#  Создайте базовый класс  Person, у которого есть:конструктор __init__, который должен принимать на вход имя и номер
#  паспорта и записывать их в атрибуты name, passportметод display, который печатает на экран сообщение «<имя>:
#  <паспорт>»;Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:

class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print(f'{self.name}: {self.passport}')


class Employee(Person):
    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department


a = Employee('Raul', 886012, 200000, "QA")

a.display()  # печатает "Raul: 886012"


################################################################
#   Создайте базовый класс Vehicle, у которого есть:метод __init__, принимающий название транспортного средства,
#   пробег и вместимость. Их необходимо сохранить в атрибуты экземпляра name, mileage и  capacity соответственно
#   метод fare , который возвращает стоимость проезда из расчета  capacity * 100:метод display , который печатает
#   строку следующего вида:Total <name> fare is: <метод fare>Затем создайте подкласс Bus , унаследованный от Vehicle.
#   В нем необходимо:переопределить метод __init__. Он должен принимать два значения: название транспортного средства
#   и пробег. Необходимо делегировать создание атрибутов name, mileage и  capacityбазовому классу, в качестве аргумента
#   передайте capacity  значение 50переопределить метод fare . Он должен получить стоимость проезда у родительского
#   класса и увеличить ее на 10%. После создайте подкласс Taxi , унаследованный от Vehicle. В нем необходимо:
#   переопределить метод __init__. Он должен принимать два значения: название транспортного средства и пробег.
#   Необходимо делегировать создание атрибутов name, mileage и  capacityбазовому классу, в качестве аргумента
#   передайте capacity  значение 4переопределить метод fare . Он должен получить стоимость проезда у родительского
#   класса и увеличить ее на 35%.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')


class Bus(Vehicle):
    def __init__(self, name, mileage, capacity=50):
        super().__init__(name, mileage, capacity)
        # !!! ч/з super().__init__ идёт обращение к базовому классу, здесь к __init__ базового (родителького класса)

    def fare(self):
        return super().fare() * (0.1 + 1)


class Taxi(Vehicle):
    def __init__(self, name, mileage):
        # capacity = 4
        super().__init__(name, mileage, capacity=4)

    def fare(self):
        return Vehicle.fare(self) * (0.35 + 1)


################################################################
# В этой задаче у нас будет один родительский класс Transport и три дочерних класса: Car, Boat, Plane.В классе Transport
# должны быть реализованы:метод __init__, который создает атрибуты brand, max_speed и kind. Значения атрибутов brand,
# max_speed , kind поступают при вызове метода __init__. При этом значение kindне является обязательным и по умолчанию
# имеет значение None;метод __str__, который будет возвращать строку формата: "Тип транспорта <kind> марки <brand>
# может развить скорость <максимальная скорость> км/ч". классе Carдолжны быть реализованы:метод __init__, создающий у
# экземпляра атрибуты brand, max_speed, mileage и приватный атрибут gasoline_residue. Все значения этих атрибутов
# передаются при вызове класса Car. Внутри инициализации делегируйте создание атрибутов brand, max_speed , kind
# родительскому классу Transport , при этом атрибуту kindпередайте значение "Car";свойство-геттер gasoline, который
# будет возвращать строку: "Осталось бензина <gasoline_residue> л";свойство-сеттер gasoline, которое должно принимать
# ТОЛЬКО целое число value, увеличивает уровень топлива gasoline_residue на переданное значение и затем вывести фразу
# 'Объем топлива увеличен на <value> л и составляет <gasoline_residue> л'. Если в значение value подается не целое
# число, вывести 'Ошибка заправки автомобиля'.В классе Boatдолжны быть реализованы:метод __init__, принимающий три
# значения brand, max_speed, owners_name. Их нужно сохранить в соответствующие атрибуты. При этом внутри инициализации
# нужно делегировать создание атрибутов brand, max_speed , kind родительскому классу Transport , в атрибут kind при
# этом передайте значение "Boat";метод __str__, который будет возвращать строку: 'Этой лодкой марки <brand> владеет
# <owners_name>'.
class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Осталось бензина {self.__gasoline_residue} л'

    @gasoline.setter
    def gasoline(self, value):
        if type(value) == int:
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, "Boat")
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, "Plane")
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


################################################################
# проводили опрос и выявили, к какому классу люди себя относят. По результатам опроса все люди разделились на сладкоежек,
# вегетарианцев и любителей мяса. Давайте напишем программу, которая поможет нам подвести итоги опроса. Для создания
# программы нужно:1. Создать родительский класс Initialization, который состоит из: метода инициализации, в который
# поступают аргументы: capacity - целое число, food - список из строковых названий еды. Если в значение capacity
# передается не целое число, вывести надпись ‘Количество людей должно быть целым числом’ и не создавать для таких
# экземпляров атрибуты capacity и food.2. Создать дочерний класс Vegetarian от класса Initialization, который состоит
# из: метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов
# родительского метода __init__.метода __str__, который возвращает строку формата "<capacity> людей предпочитают не
# есть мясо! Они предпочитают <food>"3. Создать дочерний класс MeatEater от класса Initialization, который состоит из:
# метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов
# родительского метода __init__.метода __str__, который возвращает строку формата "<capacity> мясоедов в Москве! Помимо
# мяса они едят еще и <food>". Создать дочерний класс SweetTooth от класса Initialization, который состоит из:
# метода инициализации, принимающего аргументы capacity, food. Нужно создать одноименные атрибуты через вызов
# родительского метода __init__.магического метода __str__, который возвращает строку формата ‘Сладкоежек в Москве
# <capacity>. Их самая любимая еда: <food>’; агического  метода __eq__, который будет позволять сравнивать экземпляры
# класса SweetTooth  с числами и другими нашими классами. Если сравнение происходит с целым числом и атрибут capacity
# с ним совпадает, то необходимо вернуть True, в противном случае - False. Если же сравнение идет с другим нашим
# классом(Vegetarian или MeatEater) и значения атрибутов capacity равны, то возвращается True, в противном случае
# - False. А если же сравнивается с другим типом данных, верните ‘Невозможно сравнить количество сладкоежек с
# <значение>’;магического  метода __lt__. Если сравнение происходит с целым числом и количество сладкоежек
# (атрибут capacity) меньше, необходимо вернуть True, в противном случае - False. Если сравнение происходит с
# экземпляром одного из наших классов Vegetarian или MeatEater и сладкоежек меньше, то верните True, в противном
# случае верните False. В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить
# количество сладкоежек с <значение>’магического  метода __gt__. Если сравнение происходит с целым числом и количество
# сладкоежек больше, необходимо вернуть значение True, в противном же случае - False. Если сравнение происходит с
# другим нашим классом Vegetarian или MeatEater и сладкоежек больше, то верните True, в противном случае - False.
# В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить количество сладкоежек с <значени

from functools import total_ordering


class Initialization:
    def __init__(self, capacity, food):
        if type(capacity) == int:
            self.capacity = capacity
            self.food = food
        else:
            print(f'Количество людей должно быть целым числом')


class Vegetarian(Initialization):
    # def __init__(self, capacity, food):
    #     super().__init__(capacity, food)
    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


@total_ordering
class SweetTooth(Initialization):

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if type(other) == int:
            return self.capacity == other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity == other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}’'

    def __lt__(self, other):
        if type(other) == int:
            return True if self.capacity < other else False
        elif isinstance(other, Initialization):
            return True if self.capacity < other.capacity else False
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}’'

    # def __gt__(self, other):
    #     if type(other) == int:
    #         return True if self.capacity > other else False
    #     elif isinstance(other, (MeatEater, Vegetarian)):
    #         return True if self.capacity > other.capacity else False
    #     else:
    #         return f'Невозможно сравнить количество сладкоежек с {other}’'


################################################################
# _________Balakiref________________________________Наследование________________________
#
# ______________4.3 Наследование. Функция super() и делегирование
#
# Подвиг 4. Создается программа по учету склада. Каждый предмет на складе должен описываться базовым классом Thing.
# Объекты этого класса создаются командой:th1 = Thing(name, weight)где name - наименование предмета (строка);
# weight - вес предмета (вещественное число).Для описания каждого конкретного вида предметов, создаются дочерние
# классы (на основе базового Thing):ArtObject - для представления арт-объектов;Computer - для системных блоков
# компьютеров;uto - для автомобилей.Объекты этих классов создаются командами:obj = ArtObject(name, weight, author,
# date)  # author - автор (строка); date - дата создания (строка)obj = Computer(name, weight, memory, cpu)
# memory - размер памяти (целое число); cpu - тип процессора (строка)obj = Auto(name, weight, dims)
# dims - габариты, кортеж (width, length, height) - вещественные или целые числаНа основе класса Auto создаются
# дочерние классы Mercedes и Toyota
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        # Thing.__init__(self, name, weight)
        # super(ArtObject, self).__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, *args):
        *name_weight, self.memory, self.cpu = args
        super().__init__(*name_weight)


class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


################################################################
# каждый вызванный класс вызывает __init__ у базового класса,  переопределяет аргумент arg на свой arg , и в цикле по
# индексам(arg[i] = имя, args[i] = значение) в setattr создает для класса локальные атрибуты .
class Thing:
    arg = ['name', 'weight']

    def __init__(self, *args):
        for i in range(len(args)):
            setattr(self, self.arg[i], args[i])


class ArtObject(Thing):
    arg = ['name', 'weight', 'author', 'date']


class Computer(Thing):
    arg = ['name', 'weight', 'memory', 'CPU']


class Auto(Thing):
    arg = ['name', 'weight', 'dims']


class Mercedes(Auto):
    arg = ['name', 'weight', 'dims', 'model', 'old']


class Toyota(Auto):
    arg = ['name', 'weight', 'dims', 'model', 'wheel']


################################################################
# Подвиг 5. Вам поручено организовать представление объектов для продажи в риэлтерских агентствах
class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


# Agency можно унаследовать от list'а )
class Agency(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def add_object(self, obj):
        self.append(obj)

    def remove_object(self, obj):
        if obj in self:
            super().remove(obj)
            # self.remove(obj) self.remove(obj) ошибка RecursionError.

    def get_objects(self):
        return self


################################################################
class Constractor:
    _name_core = ("name", "price")
    _name_add = ()

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)
        if args:
            self.__dict__.update(zip((self._name_core + self._name_add), args))


class SellItem(Constractor):
    pass


class House(SellItem):
    _name_add = ("material", "square")


class Flat(SellItem):
    _name_add = ("size", "rooms")


class Land(SellItem):
    _name_add = ("square",)


class Agency(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def add_object(self, obj):
        super().append(obj)

    def remove_object(self, obj):
        super().remove(obj)

    def get_objects(self):
        return self


################################################################
class SellItem:
    names_attr = ('name', 'price')

    def __init__(self, *args, **kwargs):
        self.__dict__.update(zip(self.names_attr, args))
        self.__dict__.update(kwargs)


class House(SellItem):
    names_attr = ('name', 'price', 'material', 'square')


class Flat(SellItem):
    names_attr = ('name', 'price', 'size', 'rooms')


class Land(SellItem):
    names_attr = ('name', 'price', 'square')


class Agency:
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def get_objects(self):
        return self.objects


################################################################
# Подвиг 6 (на повторение). Ваша команда создает небольшой фреймворк для веб-сервера. Для этого был объявлен класс:
# class Router:
# И его предполагается использовать следующим образом:
# @Callback('/', Router)Здесь Callback - это класс-декоратор с параметрами: path = '/' - маршрут; router_cls = Router -
# класс роутера. Декоратор Callback должен обеспечивать добавление функции (в примере index) в словарь app класса Router.
# Ключом словаря выступает маршрут (path), а значением - ссылка на декорируемую функцию. Для этого следует использовать
# метод add_callback класса Router.Затем, из роутера (Router) методом get выбирается ранее добавленная функция
# (в примере index), и если она существует, то вызывается с выводом результата в консоль.Ваша задача реализовать
# класс-декоратор Callback. Небольшая справка.Для реализации декоратора с параметрами на уровне класса в
# инициализаторе __init__(self, methods) прописываем параметр для декоратора, а магический метод __call__()
# объявляем для декорирования функции:
class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, route_cls):
        self.path = path
        self.route_cls = route_cls

    def __call__(self, func):
        self.route_cls.add_callback(self.path, func)
        return func  # чтобы func ссылалась на суму себя


@Callback('/about', Router)
def about():
    return '<h1>About</h1>'


route = Router.get('/about')
ret = route()
assert ret == '<h1>About</h1>', "декорированная функция вернула неверные данные"

route = Router.get('/')
assert route is None, "Класс Router, при вызове метода get, вернул неверные данные"


################################################################
class Callback(Router):
    def __init__(self, path, router_cls):
        self.path = path
        self.router_cls = router_cls

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        self.add_callback(self.path, func)
        return wrapper


################################################################
# C наследованнием можно
class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback(Router):
    def __init__(self, path='/', router_cls=Router):
        self.path = path
        self.router_cls = router_cls

    def __call__(self, func):
        self.add_callback(self.path, func)
    ################################################################


# Подвиг 7. В программе объявлена функция integer_params для класса Vector, которая применяет к каждому методу класса
# декоратор integer_params_decorated:
# Декоратор integer_params_decorated должен проверять, чтобы все передаваемые аргументы в методы класса
# (кроме первого self) были целыми числами (имели тип int). Если это не так, то должно генерироваться исключение
# командой:raise TypeError("аргументы должны быть целыми числами")


def integer_params_decorated(func):
    def wrapper(*args):
        for i in args[1:]:
            if type(i) != int:
                raise TypeError("аргументы должны быть целыми числами")
        return func(*args)

    return wrapper


@integer_params_decorated
def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))
    # callable(), проверяет можно ли вызвать объект, объект вызываемый, если в нем определен метод __call__().
    return cls


# В integer_params декорируются уже сами методы класса, причем только те которые были записаны в словарь methods
# integer_params_decorated(v) стоит воспринимать буквально как декорирование некой функции v. А в setattr происходит
# банальная перезапись соответсвующих методов(функций) на декорированые

@integer_params  # Vector = integer_params(Vector)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
print(vector[1])
vector[1] = 20.4  # TypeError


################################################################
def integer_params_decorated(func):  # функция для декориррования других функций
    def wrapper(self, *args, **kwargs):
        if not all(map(lambda x: type(x) == int, args)):
            raise TypeError("аргументы должны быть целыми числами")
        if not all(map(lambda x: type(x) == int, kwargs.values())):
            raise TypeError("аргументы должны быть целыми числами")
        return func(self, *args, **kwargs)

    return wrapper
    # kwargs.values() В данном случае в декораторе integer_params_decorated используется *kwargs.values() вместо просто
    # *kwargs, потому что мы хотим получить значения переданных именованных аргументов, игнорируя их ключи.
    # Параметр kwargs представляет собой словарь именованных аргументов, где ключами являются имена параметров, а
    # значениями - соответствующие им значения. Используя *kwargs, мы распаковываем словарь и передаем его значения
    # как позиционные аргументы в функцию wrapper. Однако, в данном случае, нам нужны только значения, поэтому мы
    # используем kwargs.values(), чтобы получить их без ключей. Таким образом, выражение (*args, *kwargs.values())
    # объединяет позиционные аргументы (*args) и значения именованных аргументов (*kwargs.values()) в один кортеж,
    # который затем проверяется на типы в декораторе.,нужно для проверки reverse=False


# @integer_params_decorated
def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))
    # callable(), проверяет можно ли вызвать объект, объект вызываемый, если в нем определен метод __call__().
    return cls


# В integer_params декорируются уже сами методы класса, причем только те которые были записаны в словарь methods
# integer_params_decorated(v) стоит воспринимать буквально как декорирование некой функции v. А в setattr происходит
# банальная перезапись соответсвующих методов(функций) на декорированые

@integer_params  # Vector = integer_params(Vector)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


################################################################

################################################################
from itertools import chain


# здесь объявляйте функцию-декоратор
def integer_params_decorated(func):
    def wrapper(self, *args, **kwargs):
        if any(type(arg) != int for arg in chain(args, kwargs.values())):
            raise TypeError("аргументы должны быть целыми числами")
        return func(self, *args, **kwargs)

    return wrapper


################################################################
# Подвиг 8 (на повторение). Объявите класс SoftList, который наследуется от стандартного класса list. В классе
# SoftList следует объявить необходимые магические методы так, чтобы при обращении к несуществующему элементу
# (по индексу) возвращалось значение False (а не исключение Out of Range).
class SoftList(list):
    def __init__(self, value):
        self.list = value

    def __getitem__(self, index):
        if not (-len(self.list) < index < len(self.list) - 1):
            return False
        return self.list[index]


sl = SoftList("python")
sl[0]  # 'p'
sl[-1]  # 'n'
sl[6]  # False
sl[-7]  # False


################################################################
class SoftList(list):

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        # вызов родительского класса  (list) для выполнения операции получения элемента по индек
        except IndexError:
            return False


################################################################
class SoftList(list):

    def __getitem__(self, index):
        if index in range(-self.__len__(), super().__len__()):
            super().__getitem__(index)
        return False


################################################################
# Подвиг 9 (на повторение). Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса
# StringDigit должны создаваться командой:sd = StringDigit(string)где string - строка из цифр (например,
# "12455752345950"). Если в строке string окажется хотя бы один не цифровой символ, то генерировать исключение
# командой:raise ValueError("в строке должны быть только цифры")Также в классе StringDigit нужно переопределить
# оператор + (конкатенации строк) так, чтобы операции:sd = sd + "123"sd = "123" + sdсоздавали новые объекты класса
# StringDigit (а не класса str). Если же при соединении строк появляется не цифровой символ, то генерировать
# исключение:raise ValueError("в строке должны быть только цифры")

class StringDigit(str):

    def __init__(self, string):
        self.check(string)
        self.string = string

    @staticmethod
    def check(string):
        if any(map(lambda x: not x.isdigit(), string)):
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        if isinstance(other, StringDigit):
            other = other.string

        # self.check(other) # можно не вызывать проверку, т.к. она вызывается в инициализаторе
        self.string += other
        return StringDigit(self.string)  # создавали новые объекты класса StringDigit (а не класса str).
        # return StringDigit(super().__add__(other))

    def __radd__(self, other):
        return StringDigit(other) + self


################################################################################################################################
class StringDigit(str):

    def __init__(self, string):
        self.check(string)
        self.string = string

    @staticmethod
    def check(string):
        if not string.isdigit():  # не надо в проверке проверять каждый символ, isdigit проверяет всю строку.
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return self.__class__(self.string + other)

    # return self.__class__(f'{self}{other}')

    def __radd__(self, other):
        return StringDigit(other + self.string)


################################################################
# через декоратор
def check_args(func):
    def wrapper(self, *args, **kwargs):
        for arg in args + tuple(kwargs.values()):
            if isinstance(arg, str) and not all(i.isdigit() for i in arg):
                raise ValueError("в строке должны быть только цифры")
        return func(self, *args, **kwargs)

    return wrapper


def only_digits(cls):
    for k, v in cls.__dict__.items():
        if callable(v):
            setattr(cls, k, check_args(v))
    return cls


@only_digits
class StringDigit(str):
    def __new__(cls, *args, **kwargs):
        if args and all(i.isdigit() for i in args[0]):
            return super().__new__(cls, *args, **kwargs)
        raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        return StringDigit(other + str(self))


################################################################
class StringDigit(str):
    def __init__(self, string):
        self.__check_str(string)

    @staticmethod
    def __check_str(string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return self.__class__(super().__add__(other))

    # В данном случае, строка кода return self.__class__(super().__add__(other)) выполняет сложение двух экземпляров
    # класса StringDigit.При выполнении операции self + other, вызывается __add__ у объекта self. Внутри метода __add__,
    # используется ф. super().__add__(other), которая вызывает метод базового класса (в данном случае, метод __add__
    # класса str). Результат сложения строк получается с помощью базового класса str.Затем, результат сложения строк
    # передается в конструктор self.__class__(...). Здесь self.__class__ обращается к классу текущего объекта self
    # (классу StringDigit), и создается новый объект того же класса, используя полученную строку.Таким обр., выражение
    # return self.__class__(super().__add__(other)) возвращает новый объект класса StringDigit, содержащий результат
    # сложения двух строк.
    def __radd__(self, other):
        return self.__class__(other) + self
    # В данном слу, вместо строки return self.__class__(other) + self вы не можете написать return self.__add__(other)
    # и ожидать того же результата.Разница между этими строками заключается в способе создания нового объекта класса.
    # В строке return self.__class__(other) + self создается новый объект класса StringDigit путем вызова конструктора
    # self.__class__. Это означает, что новый объект будет иметь тот же класс, что и текущий объект self (StringDigit).
    # Затем результат сложения (other + self) присваивается этому новому объекту.Если вы замените эту строку на return
    # self.__add__(other), то будет вызван метод __add__, который также возвращает новый объект. Однако этот новый
    # объект будет иметь класс, который возвращает метод __add__. В данном случае это может быть класс str, поскольку
    # мы используем super().__add__. Следовательно, результатом будет объект класса str, а не StringDigit, как
    # ожидается.Поэтому для соответствия ожидаемому поведению кода следует использовать
    # return self.__class__(other) + self, чтобы создать новый объект класса StringDigit с результатом сложения строк.


################################################################
def check_digits(func):
    def wrapper(*args, **kwargs):
        if not args[0].isdigit():
            raise ValueError("в строке должны быть только цифры")
        return func(*args, **kwargs)

    return wrapper


@check_digits
class StringDigit(str):

    def __add__(self, other):
        # return self.__class__(super().__add__(other))
        return StringDigit(str(self) + other)

    def __radd__(self, other):
        return StringDigit(other + str(self))


################################################################
class StringDigit(str):

    # def __new__(cls, string):
    #     return super().__new__(cls, cls.check(string))
    def __init__(self, string):
        self.check(string)

    def __add__(self, other):
        return self.__class__(super().__add__(other))

    def __radd__(self, other):
        return self.__class__(str.__add__(other, self))

    # В методе __add__ класса StringDigit используется строка кода return self.__class__(str.__add__(other, self)),
    # а не return self.__class__(super().__add__(other)).Разница заключается в следующем: super().__add__(other)
    # вызывает метод __add__ родительского класса (str), который возвращает обычную строку. Однако, поскольку
    # StringDigit является подклассом str, вы хотите вернуть экземпляр StringDigit после выполнения операции сложения.
    # Используя self.__class__(str.__add__(other, self)), вы создаете новый экземпляр StringDigit, явно вызывая его
    # конструктор (self.__class__) и передавая результат операции сложения (str.__add__(other, self)). Это гарантирует,
    # что результат будет экземпляром StringDigit, а не обычной строкой.Использование super().__add__(other) обойдет
    # конструктор StringDigit и просто вернет объект обычной строки.

    @staticmethod
    def check(string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return string


################################################################
# по-моему самый понятный способ
class StringDigit(str):

    def __init__(self, string):
        self.check(string)
        self.string = string

    def __add__(self, other):
        self.check(other)
        return self.__class__(self.string + other)
        # return self.__class__(str(self) + other)

    def __radd__(self, other):
        self.check(other)
        return self.__class__(other + self.string)

    @staticmethod
    def check(string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return string


################################################################
# Подвиг 10 (на повторение). Объявите базовый класс с именем ItemAttrs, который бы позволял обращаться к локальным
# атрибутам объектов дочерних классов по индексу. Для этого в классе ItemAttrs нужно переопределить следующие методы:
# __getitem__() - для получения значения атрибута по индексу;__setitem__() - для изменения значения атрибута по индексу.
# Объявите дочерний класс Point для представления координаты точки на плоскости. Объекты этого класса должны создаваться
# командой:pt = Point(x, y)где x, y - целые или вещественные числа.
class ItemAttrs:
    def __init__(self, *args):
        # *args распаковка tuple
        self.name = [*args]

    def __getitem__(self, item):
        return self.name[item]

    def __setitem__(self, item, value):
        self.name[item] = value


class Point(ItemAttrs):
    def __init__(self, *args):
        super().__init__(*args)


pt = Point(1, 2.5)
x = pt[0]  # 1
y = pt[1]  # 2.5
pt[0] = 10
print(*filter(lambda x: x.startswith(('__geti', '__seti')), dir(ItemAttrs)))  # __getitem__ __setitem__


################################################################
class ItemAttrs(list):
    def __init__(self, *args):
        super().__init__(args)


class Point(ItemAttrs): pass


################################################################
class ItemAttrs:

    def __setitem__(self, item, value):
        self.__dict__[list(self.__dict__.keys())[item]] = value

    def __getitem__(self, item):
        return self.__dict__[list(self.__dict__.keys())[item]]


class Point(ItemAttrs):

    def __init__(self, x, y):
        self.x = x
        self.y = y


################################################################
class ItemAttrs:
    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, value):
        self.list[key] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.list = [x, y]


################################################################
class ItemAttrs:
    def __getitem__(self, k):
        d = list(self.__dict__.values())
        return d[k]

    def __setitem__(self, k, v):
        d = list(self.__dict__.keys())
        d[k] = v
        # setattr(self, d[k], v)


################################################################
# _____4.1 Наследование в объектно-ориентированном программировании________________________
# Подвиг 4. Наследование часто используют, чтобы вынести общий код дочерних классов в базовый класс. Сделаем такой
# пример. Объявите в программе базовый класс Animal (животное), объекты которого можно создать командой:
# an = Animal(name, old)где name - название животного (строка); old - возраст животного (целое число). Такие же
# локальные атрибуты (name и old) должны создаваться в объектах класса.Далее, объявите дочерний класс
# (от базового Animal) с именем Cat (кошки), объекты которого создаются командой:cat = Cat(name, old, color, weight)
# где name, old - те же самые параметры, что и в базовом классе; color - цвет кошки (строка); weight - вес кошки
# (любое положительное число).В объектах класса Cat должны автоматически формироваться локальные атрибуты: name,
# old, color, weight. Формирование атрибутов name, old должен выполнять инициализатор базового класса.
# По аналогии объявите еще один дочерний класс Dog (собака), объекты которого создаются командой:
# dog = Dog(name, old, breed, size)здесь name, old - те же самые параметры, что и в базовом классе;
# breed - порода собаки (строка); size - кортеж в формате (height, length) высота и длина - числа.
# В объектах класса Dog по аналогии должны формироваться локальные атрибуты: name, old, breed, size.
# За формирование атрибутов name, old отвечает инициализатор базового класса. Наконец, в классах Cat и Dog
# объявите метод:get_info() - для получения информации о животном.Этот метод должен возвращать строку в формате:
# "name: old, <остальные параметры через запятую>"
class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def get_info(self):
        print(self.__dict__.values())  # dict_values(['кот', 4, 'black', 2.25])
        # Объявлять в родительском классе методы для работы с дочерними - очень плохая практика !! в родительском
        # классе нельзя объявлять методы, которых в нем нет или которые будут ссылаться на атрибуты которых в нем нет.
        print(*self.__dict__.values())  # кот 4 black 2.25
        return f"{self.name}: {', '.join(map(str, list(self.__dict__.values())[1:]))}"


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    # def get_info(self):
    #     return f'{self.name}: {self.old}, {self.color}, {self.weight}'


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    # def get_info(self):
    #     return f'{self.name}: {self.old}, {self.breed}, {self.size}'


c = Cat('кот', 4, 'black', 2.25)
print(c.get_info())


################################################################
class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old
        self.info = f'{self.name}: {self.old}, '

    def get_info(self):
        return self.info


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight
        self.info += f'{self.color}, {self.weight}'


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
        self.info += f'{self.breed}, {self.size}'


c = Cat('кот', 4, 'black', 2.25)
print(c.get_info())


################################################################
def get_info(self):
    return '{}: {}, {}, {}'.format(*self.__dict__.values())

    ################################################################
    def get_info(self):
        name, old, param_3, param_4 = self.__dict__.values()
        return f"{name}: {old}, {param_3}, {param_4}"


################################################################
from typing import Any


class Animal:

    def __init__(self, name, old):

        self.name = name
        self.old = old

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'name' and self.check_string(__value):
            raise AttributeError('name should be a atring')

        if __name == 'old' and type(__value) is not int:
            raise AttributeError('old should be an int')

        super().__setattr__(__name, __value)

    @classmethod
    def check_string(self, value):
        if type(value) is not str:
            raise ValueError('value should be a string')

    @classmethod
    def check_positive_value(self, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError('value should be positive int or float')

    @classmethod
    def check_tuple(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise ValueError('value should be a tuple with two items')
        h, l = value
        if type(h) not in (int, float) or type(l) not in (int, float):
            raise ValueError('values in tuple should be in (int, float)')

    @staticmethod
    def dec(func):
        def wrapper(self):
            res = f'{self.name}: {self.old}, '
            cur = func(self)
            return res + cur

        return wrapper


class Cat(Animal):

    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.check_string(color)
        self.color = color
        self.check_positive_value(weight)
        self.weight = weight

    @Animal.dec
    def get_info(self):
        return f'{self.color}, {self.weight}'


class Dog(Animal):

    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.check_string(breed)
        self.breed = breed
        self.check_tuple(size)
        self.size = size

    @Animal.dec
    def get_info(self):
        return f'{self.breed}, {self.size}'


c = Cat('кот', 4, 'black', 2.25)
print(c.get_info())


################################################################
# Подвиг 5. Иногда наследование используют, чтобы наделить объекты дочерних классов определенным набором атрибутов.
# Сделаем такой пример.Предположим, вы разрабатываете программу для интернет-магазина. В этом магазине могут быть как
# реальные (физические) товары, так и электронные. Для этих двух групп, очевидно, нужен разный набор атрибутов:
# - для реальных физических товаров: id, name, price, weight, dimsгде id - идентификатор товара (целое число);
# name - наименование товара (строка); price - цена товара (вещественное число); weight - вес товара (вещественное
# число); dims = (lenght, width, depth) - длина, ширина, глубина - габариты товара (вещественные числа);
# - для электронных товаров: id, name, price, memory, frmгде id - идентификатор товара (целое число); name -
# наименование товара (строка); price - цена товара (вещественное число); memory - занимаемый размер
# (в байтах - целое число); frm - формат данных (строка: pdf, docx и т.п.)Так как все товары могут идти вперемешку,
# то мы хотим, чтобы в каждом объекте (для товара) присутствовали все атрибуты:id, name, price, weight, dims, memory,
# frmс начальными значениями None. А уже, затем, нужным из них будут присвоены конкретные данные.Для реализации этой
# логики объявите в программе базовый класс с именем Thing (вещь, предмет), объекты которого могут создаваться командой
# th = Thing(name, price)А атрибут id должен формироваться автоматически и быть уникальным для каждого товара
# (например, можно для каждого нового объекта увеличивать на единицу).В объектах класса Thing должен формироваться
# полный набор локальных атрибутов (id, name, price, weight, dims, memory, frm) со значением None, кроме атрибутов:
# id, name, price.Далее, нужно объявить два дочерних класса:Table - для столов;ElBook - для электронных книг.
# Объекты этих классов должны создаваться командами:table = Table(name, price, weight, dims)book = ElBook(name, price,
# memory, frm)Причем, атрибуты name, price (а также id) следует инициализировать в базовом классе, т.к. они общие для
# всех товаров. Остальные атрибуты должны либо принимать значение None, если не используются, либо инициализироваться
# конкретными значениями уже в дочерних классах.Наконец, в базовом классе Thing объявите метод:get_data() -
# для получения кортежа в формате (id, name, price, weight, dims, memory, frm)
class Thing:
    id = 0

    def __new__(cls, *args, **kwargs):
        cls.id += 1
        return super().__new__(cls)

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None
        Thing.id += 1
        # self.id = id(self)

    def get_data(self):
        return tuple(
            [i for i in [self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm] if i])


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())


################################################################
class Thing:
    id = 0

    def __init__(self, name, price):
        __class__.id += 1
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    def get_data(self):
        return tuple(
            [i for i in [self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm] if i])


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims
        self.id = super().id


################################################################
class Thing:
    id = 0
    __attribute = ('id', 'name', 'price', 'weight', 'dims', 'memory', 'frm')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None
        # self.id = id(self)
        self.id = self.get_id()

    @classmethod
    def get_id(cls):
        Thing.id += 1
        return Thing.id

    # Когда self находится в пространстве имен базового класса (метод get_data внутри Thing), то он
    # имеет доступ ко всем приватным атрибутам этого класса (так сделали Python и это разумно). А вот если метод
    # get_data скопировать в дочерний класс, то уже будет ошибка, т.к. меняется пространство имен и доступ к приватному
    # атрибуту напрямую будет закрыт.
    def get_data(self):
        return tuple(getattr(self, name) for name in self.__attribute)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


################################################################
# так уже нет доступа к __attribute из Table.get_data
# AttributeError: 'Table' object has no attribute '_Table__attribute'. Did you mean: '_Thing__attribute'?
class Thing:
    id = 0
    __attribute = ('id', 'name', 'price', 'weight', 'dims', 'memory', 'frm')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None
        # self.id = id(self)
        self.id = self.get_id()
        self.__attribute = ('id', 'name', 'price', 'weight', 'dims', 'memory', 'frm')

    @classmethod
    def get_id(cls):
        Thing.id += 1
        return Thing.id


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims

    def get_data(self):
        return tuple(getattr(self, name) for name in self.__attribute)


################################################################
# или так тоже нет доступа private attribute
class Thing:
    id = 0
    __attribute = ('id', 'name', 'price', 'weight', 'dims', 'memory', 'frm')


################################################################
import sys


class Thing:
    SEQ_ID = (i for i in range(1, sys.maxsize))

    def __init__(self, name, price):
        self.id = self.get_id()
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    @classmethod
    def get_id(cls):
        return next(cls.SEQ_ID)


################################################################
class Thing:
    id = 1

    def __init__(self, *args):
        self.id = Thing.id
        self.name, self.price, self.weight, self.dims, self.memory, self.frm = args
        Thing.id += 1

    def get_data(self):
        return tuple(self.__dict__.values())


class Table(Thing):

    def __init__(self, name, price, weight, dims, memory=None, frm=None):
        super().__init__(name, price, weight, dims, memory, frm)


class ElBook(Thing):

    def __init__(self, name, price, memory, frm, weight=None, dims=None):
        super().__init__(name, price, weight, dims, memory, frm)


################################################################
class Thing:
    def __init__(self, name, price):
        self.id = hash(self)
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None
        # на самом деле у разных объектов хэш может совпадать. У разных объектов теоретически возможен одинаковый хэш,
        # но у одинаковых объектов разного хэша не может быть.


################################################################
class Thing:
    __ids = iter(range(1_000_000))

    def __init__(self, name, price, *, weight=None, dims=None, memory=None, frm=None):
        self.name = name
        self.price = price
        self.id = next(self.__ids)


################################################################
import itertools


class Thing:
    goods_id = itertools.count(1)

    def __init__(self, name, price):
        self.id = next(self.goods_id)


################################################################
class Thing:
    id = 0

    def __init__(self, name, price):
        __class__.id += 1
        # if self.id+=1 -> 0
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    def get_data(self):
        return tuple(
            [i for i in [self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm] if i])


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims
        self.id = super().id


################################################################
class Thing:
    ID = 0

    def __init__(self, name: str, price: float):
        Thing.ID += 1
        self.id = Thing.ID


################################################################
class Thing:
    id = 0

    def __init__(self, name: str, price: float):
        __class__.id += 1
        self.id = __class__.id


################################################################
# Подвиг 6. Еще один пример, когда в базовом классе прописывается необходимый начальный функционал для дочерних классов.
# Известно, что браузер (и не только) может отправлять на сервер различные типы запросов: GET, POST, PUT, DELETE и др.
# Каждый из этих типов запросов обрабатывается в программе на сервере своим отдельным методом. Чтобы каждый раз не
# прописывать все необходимые методы в классах при обработке входящих запросов, они выносятся в базовый класс и
# вызываются из дочерних. Выполним такой пример.Пусть в программе объявлен следующий базовый класс с именем GenericView:
# Здесь каждый метод отвечает за обработку своего типа запроса. Параметр methods - это кортеж или список, состоящий
# из набора разрешенных запросов: строк с именами соответствующих методов (как правило, пишут заглавными буквами).
# Вам необходимо объявить дочерний класс с именем DetailView, объекты которого можно создавать командами:
# dv = DetailView()  # по умолчанию methods=('GET',)dv = DetailView(methods=('PUT', 'POST'))Для инициализации атрибута
# methods следует вызывать инициализатор базового класса GenericView.Далее, в классе DetailView нужно определить метод:
# def render_request(self, request, method): ...который бы имитировал выполнение поступившего на сервер запроса.
# Здесь request - словарь с набором данных запроса; method - тип запроса (строка: 'get' или 'post' и т.д.).
# Например:html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')должен быть обработан запрос как GET-запрос
# с параметром url и значением 'https://site.ru/home'. Параметр url является обязательным в словаре request для каждого
# запроса.В методе render_request() необходимо выполнить проверку: является ли указанный метод (method) разрешенным
# (присутствует в коллекции methods). Если это не так, то генерировать исключение командой:raise TypeError('данный
# запрос не может быть выполнен')Если проверка проходит, то выполнить соответствующий метод (или get(), или post(),
# или put() и т.д. с возвращением результата их работы). Подсказка: для получения ссылки на нужный метод можно
# воспользоваться магическим методом __getattribute__() или аналогичной функцией getattr()).Наконец, в дочернем классе
# DetailView следует переопределить метод get() для нужной нам обработки GET-запросов. В этом методе нужно выполнить
# проверку, что параметр request является словарем. Если это не так, то генерировать исключение:
# raise TypeError('request не является словарем')Сделать проверку, что в словаре request присутствует ключ url.
# Если его нет, то генерировать исключение:raise TypeError('request не содержит обязательного ключа url')
# Если же все проверки проходят, то вернуть строку в формате:"url: <request['url']>"
class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {request['url']}"

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        return getattr(self, method.lower(), False)(request)
        return self.__getattribute__(method.lower())(request)


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')  # url: https://site.ru/home
print(html)


################################################################
class DetailView(GenericView):  # def __init__(self, methods=('GET',)):
    def render_request(self, request, method):
        dic = {'GET': self.get, 'POST': self.post, 'PUT': self.put, 'DELETE': self.delete}
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        return dic[method](request)


################################################################
# Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). Как пример,
# объявите в программе класс с именем:Singletonкоторый бы позволял создавать только один экземпляр (все последующие
# экземпляры должны ссылаться на первый). Как это делать, вы должны уже знать из этого курса.Затем, объявите еще один
# класс с именем:Gameкоторый бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:
# game = Game(name)где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с
# соответствующим содержимым.Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не
# так, то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).
class Singleton:
    instance = None
    instance_basic = None

    def __new__(cls, *args, **kwargs):
        # если создать экз Singleton то дочерний класс будет ссылать на него и не создастся экз дочерненго класса, тогда
        if cls == Singleton:
            if cls.instance_basic is None:
                cls.instance_basic = super().__new__(cls)  # обращение к базовому классу
            return cls.instance_basic

        if not cls.instance:
            cls.instance = super().__new__(cls)  # обращение к базовому классу
            # cls.instance_basic = object.__new__(cls)
        return cls.instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            # для того чтобы name принимал только первое значение и не перезаписывать каждый раз новое name, а Singleton
            # не будет давать создать новый объект
            self.name = name


################################################################
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


################################################################
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


class Game(Singleton):
    def __init__(self, name):
        if not hasattr(self, "name"):
            self.name = name


################################################################
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Game(Singleton):
    _instance = None

    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name


################################################################
class Singleton:
    obj = None

    def __new__(cls, *args, **kwargs):
        cls.obj = cls.obj or super().__new__(cls)
        return cls.obj


class Game(Singleton):
    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name


################################################################
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name


################################################################
class Singleton:
    ''' странно вообще, что классу гейм приходится наследоваться от синглтона
        но даже если пришлось это делать, то в чем суть держать в атрибутах синглота ссылки на
        экзепляры других классов, при этом в решении Сергея каждрый раз надо добавлять в класс синглотан новую
                 ссылку на поддержку другого класса.'''

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'obj'):
            cls.obj = object.__new__(cls)  # решение с нормальной реализации данного патерна
        return cls.obj


class Game(Singleton):

    def __init__(self, name):
        self.name = getattr(self, 'name', name)


'''class Singleton:
    """решение с использования делегирования, а не наследования, понятнее и логичнее"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'obj'):
            cls.obj = object.__new__(cls)
        return cls.obj

class Game:
    __new__ = Singleton.__new__

    def __init__(self, name):
        self.name = getattr(self, 'name', name)'''


################################################################
# Подвиг 8. Вам необходимо создать множество классов для валидации (проверки) корректности данных. Для этого ваш
# непосредственный начальник (Senior) предлагает вам объявить в программе базовый класс с именем:Validator
# обеспечивающий базовый функционал для проверки корректности данных. В частности, в этом классе нужно объявить
# следующий метод:def _is_valid(self, data): ...По задумке этот метод должен возвращать булево значение True, если
# данные (data) корректны и False - в противном случае.Так как базовый класс Validator - это общий класс для всех
# видов проверок, то метод _is_valid() будет просто возвращать True.Кроме того, объекты класса Validator:
# v = Validator()   # инициализатор в классе Validator прописывать не нужнодолжны вызываться подобно функциям:
# v(data)и если данные (data) некорректны, то генерировать исключение:raise ValueError('данные не прошли валидацию')
# Проверка корректности выполняется с помощью метода _is_valid(). После этого, в программе нужно объявить два дочерних
# класса:IntegerValidator - для проверки, что data - целое число в заданном диапазоне;FloatValidator - для проверки,
# что data - вещественное число в заданном диапазоне.Объекты этих классов предполагается создавать командами:
# integer_validator = IntegerValidator(min_value, max_value)float_validator = IntegerValidator(min_value, max_value)
# где min_value, max_value - допустимый диапазон чисел [min_value; max_value]Также в этих классах нужно переопределить
# метод:def _is_valid(self, data): ...который бы возвращал True, если data является числом верного типа (либо int, либо
# float в зависимости от валидатора) и находится в заданном диапазоне [min_value; max_value]. Иначе, возвращается False.

class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == int and data in range(self.min_value, self.max_value + 1):
            return True
        else:
            return False


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == float and data in range(self.min_value, self.max_value + 1):
            return True
        else:
            return False

    ################################################################
    def _is_valid(self, data):
        return isinstance(data, int) and self.min_value <= data <= self.max_value


################################################################
class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return True if type(data) == self.type and self.min_value <= data <= self.max_value else False

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self.type = int


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self.type = float


################################################################
# Большой подвиг 9. Используя механизм наследования, вам поручено разработать функционал по построению моделей нейронных
# сетей. Общая схема модели очень простая:Базовый класс Layer имеет локальный атрибут next_layer, который ссылается
# на следующий объект слоя нейронной сети (объект класса Layer или любого объекта дочерних классов). У последнего слоя
# значение next_layer = None.Создавать последовательность слоев предполагается командами:
# first_layer = Layer()next_layer = first_layer(Layer())next_layer = next_layer(Layer())То есть, сначала создается
# объект first_layer класса Layer, а затем он вызывается как функция для образования связки со следующим слоем. При
# этом возвращается ссылка на следующий слой и переменная next_layer ссылается уже на этот следующий слой нейронной
# сети. И так можно создавать столько слоев, сколько необходимо.В каждом объекте класса Layer также должен
# формироваться локальный атрибут:name = 'Layer'Но сам по себе класс Layer образует только связи между слоями.
# Никакой другой функциональности он не несет. Чтобы это исправить, в программе нужно объявить еще два дочерних класса:
# Input - формирование входного слоя нейронной сети;Dense - формирование полносвязного слоя нейронной сети.
# Конечно, создавать нейронную сеть мы не будем. Поэтому, в классе Input нужно лишь прописать инициализатор так,
# чтобы его объекты создавались следующим образом:inp = Input(inputs)где inputs - общее число входов (целое число).
# Также в объектах класса Input должен автоматически формироваться атрибут:name = 'Input'(Не забывайте при этом,
# вызывать инициализатор базового класса Layer).Объекты второго дочернего класса Dense предполагается создавать
# командой:dense = Dense(inputs, outputs, activation)где inputs - число входов в слой; outputs - число выходов слоя
# (целые числа); activation - функция активации (строка, например: 'linear', 'relu', 'sigmoid'). И в каждом объекте
# класса Dense также должен автоматически формироваться атрибут:name = 'Dense'Все эти классы совместно можно
# использовать следующим образом (эти строчки пример, писать не нужно):network = Input(128)
# layer = network(Dense(network.inputs, 1024, 'linear'))layer = layer(Dense(layer.inputs, 10, 'softmax'))
# Здесь создается три слоя нейронной сети. Наконец, для перебора всех слоев с помощью цикла for, необходимо объявить
# отдельный класс NetworkIterator для итерирования (перебора) слоев нейронной сети следующим образом:
# for x in NetworkIterator(network):    print(x.name)Здесь создается объект класса NetworkIterator. На вход
# передается первый объект (слой) нейронной сети. Объект этого класса является итератором, который в цикле for
# последовательно возвращает объекты (слои) нейронной сети.

class Layer:
    def __init__(self, name='Layer'):
        self.name = name
        self.next_layer = None

    def __call__(self, layer, *args, **kwargs):
        self.next_layer = layer
        return layer


class Input(Layer):
    def __init__(self, inputs, name='Input'):
        self.inputs = inputs
        super().__init__('Input')


class Dense(Layer):
    def __init__(self, inputs, outputs, activation, name='Dense'):
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        super().__init__(name)


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        while self.network:
            yield self.network
            self.network = self.network.next_layer


nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))


################################################################
class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        self.start = self.network
        return self

    def __next__(self):
        if not self.start:
            raise StopIteration
        self.network, self.start = self.start, self.start.next_layer
        return self.network

    ################################################################
    class NetworkIterator:
        def __init__(self, network):
            self.network = network

        def __iter__(self):
            self.start = self.network
            return self

        def __next__(self):
            if not self.start:
                raise StopIteration
            out = self.start
            self.start = self.start.next_layer
            return out


################################################################
class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        self.start = self.network
        return self

    def __next__(self):
        out = self.start
        while self.start:
            self.start = self.start.next_layer
            return out
        raise StopIteration

    ################################################################

    def __iter__(self):
        self.start = self.network
        return self

    def __next__(self):
        out = self.start
        if out:
            self.start = self.start.next_layer
            return out
        else:
            raise StopIteration

    ################################################################
    # __good_____
    def __iter__(self):
        return self

    def __next__(self):
        out = self.network
        if out:
            self.network = self.network.next_layer
            return out
        raise StopIteration

    ##############################################################


################################################################
class Layer:
    def __init__(self):
        self.name = 'Layer'
        self.next_layer = None

    def __call__(self, next_layer):
        return self.__add_layer(next_layer)

    def __add_layer(self, next_layer):
        if self.next_layer is None:
            self.next_layer = next_layer
            return self.next_layer
        else:
            return self.next_layer(next_layer)


class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        self.it = self.network
        return self

    def __next__(self):
        if self.it is None:
            raise StopIteration
        out = self.it
        self.it = self.it.next_layer
        return out


################################################################
class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        while self.network:
            yield self.network
            self.network = self.network.next_layer


################################################################
################################################
# Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, ..., xN)где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).
# С объектами этого класса должны выполняться команды:v1 = Vector(1, 2, 3)v2 = Vector(3, 4, 5)
# v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:raise TypeError('размерности векторов
# не совпадают')В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих
# координат вектора.На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:
# v = VectorInt(1, 2, 3, 4)v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты
# должны быть целыми числами')При операциях сложения и вычитания с объектом класса VectorInt:v = v1 + v2  # v1 -
# объект класса VectorIntv = v1 - v2  # v1 - объект класса VectorIntдолжен формироваться объект v как объект класса
# Vector, если хотя бы одна координата является вещественной. Иначе, v должен быть объектом класса VectorInt.

class Vector:
    def __init__(self, *args, **kwargs):
        self.coords = args

    def __check_args(self, other):
        if len(self.coords) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self.__check_args(other)
        return Vector(*[i + j for i, j in zip(self.coords, other.get_coords())])
        # return Vector(*[val + other.coords[i] for i, val in enumerate(self.coords)])

    def __sub__(self, other):
        self.__check_args(other)
        return Vector(*[val - other.coords[i] for i, val in enumerate(self.coords)])

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *args):
        if any(map(lambda x: type(x) != int, args)):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def __add__(self, other):
        if any(map(lambda x: type(x) == float, other.coords)):
            return super().__add__(other)
        self.__check_args(other)
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        return VectorInt(*[val + other.coords[i] for i, val in enumerate(self.coords)])


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)


################################################################
class Vector:
    _allowed_types = (int, float)

    def __init__(self, *args, **kwargs):
        self.__check_allowed_types(args)
        self.coords = args

    def __check_allowed_types(self, args):
        if not all(type(i) in self._allowed_types for i in args):
            raise ValueError('неверный тип координат')

    def __check_args(self, other):
        if len(self.coords) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')

    def __is_vector(self, other):
        if not isinstance(other, Vector):
            raise TypeError('операнд должен быть obj Vector или дочернего класса')

    def __add__(self, other):
        self.__is_vector(other)
        self.__check_args(other)
        coords = tuple(i + j for i, j in zip(self.coords, other.get_coords()))
        # coords = tuple(map(sum, zip(self.coords, other.coords)))
        return self.__make_coords(coords)

    def __make_coords(self, coords):
        try:
            return self.__class__(*coords)  # запись в дочерний класс/текущий, * - распаковываем кортеж
        except ValueError:
            return Vector(*coords)  # запись в класс Vector т.к. не пропускает _check_allowed_types при создании
            # дочернего класса с координатами типа float
        # принцип SOLID не используются атрибуты дочернего класса

    def __sub__(self, other):
        self.__is_vector(other)
        self.__check_args(other)
        coords = tuple(i - j for i, j in zip(self.coords, other.get_coords()))
        return self.__make_coords(coords)

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    _allowed_types = (int,)


################################################################
from operator import add, sub


class Vector:
    type_coords = (int, float)
    error_message = 'числами'

    def __init__(self, *args):
        self.__check_data(args)
        self.coords = [*args]

    def get_coords(self):
        return tuple(self.coords)

    def __check_data(self, lst):
        if not all(type(x) in self.type_coords for x in lst):
            raise ValueError(f'координаты должны быть {self.error_message}')

    def __len__(self):
        return len(self.coords)

    def __check_vector(self, other):
        if len(self) != len(other):
            raise TypeError('размерности векторов не совпадают')

    def __make_calc(self, other, op) -> list:
        self.__check_vector(other)
        return [op(*el) for el in zip(self.coords, other.coords)]

    # Здесь op является оператором, переданным в метод __make_calc, который может быть либо функцией add (сложение) либо
    # функцией sub (вычитание) из модуля operator.op(*el) для выполнения операции поэлементного сложения или вычитания.
    @staticmethod
    def make_vector(lst):
        try:
            return VectorInt(*lst)
        except ValueError:
            return Vector(*lst)

    def __add__(self, other):
        res = self.__make_calc(other, add)
        return self.make_vector(res)

    def __sub__(self, other):
        res = self.__make_calc(other, sub)
        return self.make_vector(res)


class VectorInt(Vector):
    type_coords = (int,)
    error_message = 'целыми числами'


################################################################
class Vector:
    def __init__(self, *args):
        self.coords = args

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        coords = tuple(map(sum, zip(self.coords, other.coords)))
        return self.__make_vector(coords)

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')
        coords = tuple(x - y for (x, y) in zip(self.coords, other.coords))
        return self.__make_vector(coords)

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__(*args)
        if not all(type(i) is int for i in args):
            raise ValueError('координаты должны быть целыми числами')


################################################################
class Vector:
    def __init__(self, *args):
        self.coord = list(args)

    def __add__(self, other):
        self._is_valid(other)
        return Vector(*[self.coord[i] + other.coord[i] for i in range(len(self.coord))])

    def __sub__(self, other):
        self._is_valid(other)
        return Vector(*[self.coord[i] - other.coord[i] for i in range(len(self.coord))])

    def _is_valid(self, other):
        if len(self.coord) != len(other.coord):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return tuple(self.coord)


class VectorInt(Vector):
    def __init__(self, *args):
        if not self.int_valid(args):
            raise ValueError('координаты должны быть целыми числами')
        self.coord = list(args)

    def __add__(self, other):
        self._is_valid(other)
        if self.int_valid(other.coord):
            return VectorInt(*[self.coord[i] + other.coord[i] for i in range(len(self.coord))])
        return super().__add__(other)

    def __sub__(self, other):
        self._is_valid(other)
        if self.int_valid(other.coord):
            return VectorInt(*[self.coord[i] - other.coord[i] for i in range(len(self.coord))])
        return super().__sub__(other)

    def int_valid(self, args):
        return all([type(i) == int for i in args])


################################################################
class Vector:

    def __init__(self, *args):
        self.coords = list(args)

    def get_coords(self):
        return tuple(self.coords)

    def validate(func):
        def wrapper(instance, other, *args):
            if len(instance) != len(other):
                raise TypeErro('размерности векторов не совпадают')
            elif type(instance) == VectorInt:  # случай, когда второй параметр принадлежит к типу VectorInt
                instance, other = other, instance  # для первого парам. (если он VectorInt) замена не требуется,
                return func(instance, other)  # т.к. type(self) = Vector в методах add и sub
            else:
                return func(instance, other)

        return wrapper

    def __len__(self):
        return len(self.coords)

    @validate
    def __add__(self, other):
        return type(self)(*map(sum, zip(self.coords, other.coords)))

    @validate
    def __sub__(self, other):
        return type(self)(*map(lambda x, y: x - y, self.coords, other.coords))  # type(self) будет оцениваться
        # как Vector или VectorInt Цель использования type(self) состоит в обработке случая, когда второй параметр
        # (other) принадлежит классу VectorInt. В этом случае декоратор меняет местами позиции instance и other перед
        # вызовом фактического метода оператора. Это позволяет правильно выполнять сложение или вычитание, независимо
        # от того, является ли экземпляр типом VectorInt или другого класса.


class VectorInt(Vector):

    def __init__(self, *args):
        if list(map(int, list(args))) == list(args):
            super().__init__()
            self.coords = list(args)
        else:
            raise ValueError('координаты должны быть целыми числами')


################################################################
# 4.2 Функция issubclass(). Наследование от встроенных типов
class List(list):
    def __str__(self):
        return ' '.join(map(str, self))


# self  наследуется от list, а в листе есть iter

l = List([1, 2, 3])
print(l)  # 1 2 3


################################################################
# Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится
# задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:__init__()__setitem__()
# append()так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных,
# генерировать исключение командой:raise TypeError('можно передавать только целочисленные значения')
class ListInteger(list):
    def __init__(self, values):
        for i in values:
            self._check_int(i)
        super().__init__(values)

    def __setitem__(self, key, value):
        self._check_int(value)
        super().__setitem__(key, value)

    def append(self, value):
        self._check_int(value)
        super().append(value)

    @staticmethod
    def _check_int(value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.4  # TypeError


################################################################
class ListInteger(list):
    def __init__(self, iterable):
        super().__init__(map(self._check_int, iterable))

    def __setitem__(self, key, value):
        super().__setitem__(key, self._check_int(value))

    def append(self, value):
        super().append(self._check_int(value))

    @staticmethod
    def _check_int(value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        return value


################################################################
# при проверке типа в __init__ создаю копию входного iterable на случай, если это итератор (чтобы при проверке он
# попросту не закончился)
from copy import copy
from typing import Iterable, Any


class ListInteger(list):
    def __init__(self, iterable: Iterable[int]):
        self._validate_iterable(iterable)
        super().__init__(iterable)

    def __setitem__(self, key: int, value: int):
        self._validate_type(value)
        super().__setitem__(key, value)

    def append(self, __object: int) -> None:
        self._validate_type(__object)
        super().append(__object)

    def _validate_iterable(self, iterable: Iterable[int]):
        for value in copy(iterable):
            self._validate_type(value)

    @staticmethod
    def _validate_type(value: Any, type_=int):
        if type(value) is not type_:
            raise TypeError('можно передавать только целочисленные значения')


################################################################
class ListInteger(list):
    def __init__(self, *args):
        [self.check_type(i) for i in list(*args)]
        super().__init__(*args)

    def __setitem__(self, key, value):
        self.check_type(value)
        super().__setitem__(key, value)

    def append(self, value) -> None:
        self.check_type(value)
        super().append(value)

    @staticmethod
    def check_type(i):
        if type(i) is not int:
            raise TypeError('можно передавать только целочисленные значения')


################################################################
# Подвиг 4. Разрабатывается интернет-магазин. Каждый товар предполагается представлять классом Thing, объекты которого
# создаются командой:thing = Thing(name, price, weight)где name - наименование товара (строка); price - цена
# (вещественное число); weight - вес товара (вещественное число). В каждом объекте этого класса создаются аналогичные
# атрибуты: name, price, weight.Класс Thing необходимо определить так, чтобы его объекты можно было использовать в
# качестве ключей словаря, например:d = {}d[thing] = thingИ для каждого уникального набора данных name, price, weight
# должны формироваться свои уникальные ключи.Затем, вам необходимо объявить класс словаря DictShop, унаследованный от
# базового класса dict. В этом новом словаре ключами могут выступать только объекты класса Thing. При попытке указать
# любой другой тип, генерировать исключение командой:raise TypeError('ключами могут быть только объекты класса Thing')
# Объекты класса DictShop должны создаваться командами:dict_things = DictShop() # пустой словарь
# dict_things = DictShop(things) # словарь с набором словаря thingsгде things - некоторый словарь. В инициализаторе
# следует проверять, чтобы аргумент thing был словарем, если не так, то выбрасывать исключение:
# raise TypeError('аргумент должен быть словарем')И проверять, чтобы все ключи являлись объектами класса Thing. Если
# это не так, то генерировать исключение:raise TypeError('ключами могут быть только объекты класса Thing')
# Дополнительно в классе DictShop переопределить метод:__setitem__()с проверкой, что создаваемый ключ является
# объектом класса Thing. Иначе, генерировать исключение:raise TypeError('ключами могут быть только объекты класса
# Thing')
class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __eq__(self, other):
        if isinstance(other, Thing):
            return (self.name == other.name and self.price == other.price and self.weight == other.weight)
        return False


# Если все три условия выполняются (имя, цена и вес равны), то возвращается значение True, указывая на то, что объекты
# self и other равны(указание что это один и тот же объект с одним и тем же ключём у словаря).В противном случае, если
# other не является экземпляром класса Thing, возвращается значение False,
# указывая на то, что объекты различны или несравнимы по заданным критериям.
# ни к чему не приводит без метода __eq__, именно этот метод сравнивает объекты при одинаковых атрибутах и записывает в
# словарь только уникальные товары
class DictShop(dict):
    def __init__(self, dictions=None):
        if dictions is None:
            super().__init__()
        else:
            if not isinstance(dictions, dict):
                raise TypeError('аргумент должен быть словарем')
            if not all(map(lambda x: isinstance(x, Thing), dictions)):
                # for key in dictions:
                #     if not isinstance(key, Thing):
                raise TypeError('ключами могут быть только объекты класса Thing')
            super().__init__(dictions)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)


################################################################
class Thing:
    def __init__(self, name, price, weight):
        self.name, self.price, self.weight = name, price, weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __eq__(self, other):
        return hash(self) == hash(other)


class DictShop(dict):
    def __init__(self, dictionaries=None):
        if dictionaries:
            if not isinstance(dictionaries, dict):
                raise TypeError('аргумент должен быть словарем')
            if not all(map(lambda x: isinstance(x, Thing), dictionaries)):
                raise TypeError('ключами могут быть только объекты класса Thing')
        else:
            dictionaries = {}
            # super().__init__(dictionaries)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)


################################################################
# Подвиг 5. Объявите в программе следующие классы без содержимого (используйте оператор pass):
# Protists, Plants, Animals, Mosses, Flowering, Worms, Mammals, Human, Monkeysи постройте схему наследования в
# соответствии со следующей иерархией древа жизни:Затем, объявите в программе классы:# Monkey - наследуется от Monkeys
# и служит для описания обезьян;# Person - наследуется от Human и служит для описания человека;# Flower -
# наследуется от Flowering и служит для описания цветка;# Worm - наследуется от Worms и служит для описания червей.
# Объекты этих классов должны создаваться командами: obj = Monkey(name, weight, old) Затем, используя функции
# isinstance() и генератор списков (List comprehensions), сформируйте следующие списки из указанных объектов:
# lst_animals - все объекты, относящиеся к животным (Animals); lst_plants - все объекты, относящиеся к растениям
# (Plants); lst_mammals - все объекты, относящиеся к млекопитающим (Mammals).
class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]

# lst_animals =[i for i in lst_objs if isinstance(i,Animals)]
lst_animals = [*filter(lambda x: isinstance(x, Animals), lst_objs)]  # быстрее работает
lst_plants = [i for i in lst_objs if isinstance(i, Plants)]
lst_mammals = [i for i in lst_objs if isinstance(i, Mammals)]

################################################################
task = '''Monkey: "мартышка", 30.4, 7
Monkey: "шимпанзе", 24.6, 8
Person: "Балакирев", 88, 34
Person: "Верховный жрец", 67.5, 45
Flower: "Тюльпан", 0.2, 1
Flower: "Роза", 0.1, 2
Worm: "червь", 0.01, 1
Worm: "червь 2", 0.02, 1'''.split('\n')

lst_objs = []
for el in task:
    cls_name, pars = el.split(': ')
    name, weight, yo = pars.split(', ')
    weight, yo = float(weight), int(yo)
    lst_objs.append(globals()[cls_name](name, weight, yo))


# globals - это функция, которая возвращает динамический словарь, в котором ключами являются имена переменных, которые
# объявлены в глобальном пространстве имен, а значениями являются объекты, на которые ссылаются переменные из ключей.
# Функция globals не ищет переменные, скорее наоборот, тогда когда мы обращаемся к какой-то переменной в программе,
# программа ищет ее в словаре globals. Таким образом мы можем даже объявлять переменные через словарь globals:
# a = 1 b = 2 c = 3 globals()['d'] = 4 # Присваиваем переменой d значение 4. Аналог строки d = 4
# print(d) # Обращаемся к переменной которую объявили при помощи globals. Ошибки NameNotFoundError не возникает,
# в консоль выводится число 4


def form_lst(cls_name):
    return [el for el in lst_objs if isinstance(el, cls_name)]


lst_animals = form_lst(Animals)
lst_plants = form_lst(Plants)
lst_mammals = form_lst(Mammals)
globals()['f'] = 123
print(f)  # 123


################################################################
class Constractor:
    def __init__(self, name, weight, old):
        self.name, self.weight, self.old = name, weight, old


class Monkey(Monkeys, Constractor): pass


class Person(Human, Constractor): pass


class Flower(Flowering, Constractor): pass


class Worm(Worms, Constractor): pass


lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]

lst_animals = [elem for elem in lst_objs if issubclass(elem.__class__, Animals)]
lst_plants = [elem for elem in lst_objs if issubclass(elem.__class__, Plants)]
lst_mammals = [elem for elem in lst_objs if issubclass(elem.__class__, Mammals)]
#  Функция isinstance() вернет True, если проверяемый объект object является экземпляром указанного класса (классов)
#  или его подкласса (прямого, косвенного или виртуального).
print(isinstance(a1, Animals), issubclass(a1.__class__, Animals))  # вернет True True
################################################################
lst = ['Monkey: "мартышка", 30.4, 7',
       'Monkey: "шимпанзе", 24.6, 8',
       'Person: "Балакирев", 88, 34',
       'Person: "Верховный жрец", 67.5, 45',
       'Flower: "Тюльпан", 0.2, 1',
       'Flower: "Роза", 0.1, 2',
       'Worm: "червь", 0.01, 1',
       'Worm: "червь 2", 0.02, 1']


def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])


d = {cls.__name__: cls for cls in all_subclasses(Protists)}
lst_objs = []
for row in lst:
    cls_name, params = row.split(':')
    if cls_name == 'Flower':
        cls_name = 'Flowering'
    elif cls_name == 'Person':
        cls_name = 'Human'
    cls = d[cls_name]
    lst_objs.append(cls(*params.split(',')))

lst_animals = list(filter(lambda x: isinstance(x, Animals), lst_objs))
lst_plants = list(filter(lambda x: isinstance(x, Plants), lst_objs))
lst_mammals = list(filter(lambda x: isinstance(x, Mammals), lst_objs))


################################################################
# Подвиг 6. Известно, что с объектами класса tuple можно складывать только такие же объекты (кортежи). Например:
# t1 = (1, 2, 3)# t2 = t1 + (4, 5) # (1, 2, 3, 4, 5)# Если же мы попытаемся прибавить любой другой итерируемый объект,
# например, список:# t2 = t1 + [4, 5]# то возникнет ошибка. Предлагается поправить этот функционал и создать свой
# собственный класс Tuple, унаследованный от базового класса tuple и поддерживающий оператор: t1 = Tuple(iter_obj)
# t2 = t1 + iter_obj  # создается новый объект класса Tuple с новым (соединенным) набором данных
# где iter_obj - любой итерируемый объект (список, словарь, строка, множество, кортеж и т.п.)
class Tuple(tuple):
    def __init__(self, iter_obj):
        self.iter_obj = tuple(iter_obj)

    def __add__(self, other):
        if not isinstance(other, tuple):
            res = self.iter_obj + tuple(other)
        else:
            res = self.iter_obj + other
        return Tuple(res)


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"


################################################################
class Tuple(tuple):
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj

    def __add__(self, other):
        if not isinstance(other, tuple):
            res = tuple(self) + tuple(other)
        else:
            res = tuple(self) + other
        return self.__class__(res)


################################################################
class Tuple(tuple):

    def __add__(self, other):
        tuple_obj = super()
        new_tuple = tuple_obj.__add__(tuple(other))
        return self.__class__(new_tuple)
    # Т.к. мы наследовались от tuple, в методе __add__(self, other): self - уже кортеж, т.к. мы не переопределяли
    # __init__ в нашем классе, а __init__ класса tuple создает кортеж.other - любой итерируемый тип данных
    # tuple_obj = super() - функция super() возвращает прокси-объект (временный объект суперкласса), который позволяет
    # нам получить доступ к методам базового класса - tuple в нашем случае.new_tuple = tuple_obj.__add__(tuple(other))
    # - вызывается метод  __add__ класса tuple, в который мы передаем кортеж tuple(other). Этот метод __add__
    # возвращает нам новый кортеж, полученный в результате сложения кортежей self и other.return self.__class__
    # (new_tuple) - переопределенный метод __add__ класса Tuple создает новый экземпляр класса Tuple и возвращает его.
    # P.s. если што, я сам пиво, поэтому на правильность объяснения не претендую, но надеюсь, это кому-то поможет


################################################################
class Tuple(tuple):

    def __add__(self, other):
        return self.__class__(super().__add__(tuple(other)))


################################################################
class Tuple(tuple):

    def __add__(self, other):
        return self.__class__((*self, *other))


################################################################
class Tuple(tuple):

    def __add__(self, other):
        return self.__class__(tuple(self) + tuple(other))


################################################################
# Подвиг 7 (на повторение). Необходимо в программе объявить класс VideoItem для представления одного видео (например,
# в youtube). Объекты этого класса должны создаваться командой:video = VideoItem(title, descr, path)
# де title - заголовок видео (строка); descr - описание видео (строка); path - путь к видеофайлу. В каждом объекте
# класса VideoItem должны создаваться соответствующие атрибуты: title, descr, path.Затем, нужно создать класс для
# формирования оценки видео в баллах от 0 до 5. Для этого нужно объявить еще один класс с именем VideoRating, объекты
# которого создаются командой:rating = VideoRating()В каждом объекте класса VideoRating должен быть локальный
# приватный атрибут с именем __rating, содержащий целое число от 0 до 5 (по умолчанию 0). А для записи и считывания
# значения из этого приватного атрибута должно быть объект-свойство (property) с именем rating.Так как атрибут
# __rating - это целое число в диапазоне [0; 5], то в момент присвоения ему какого-либо значения необходимо
# проверять, что присваиваемое значение - целое число в диапазоне [0; 5]. Если это не так, то генерировать
# исключение командой:raise ValueError('неверное присваиваемое значение')Далее, в каждом объекте класса VideoItem
# должен быть локальный атрибут rating - объект класса VideoRating.

class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value not in range(0, 6):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating)  # 0
v.rating.rating = 5
print(v.rating.rating)  # 5
title = v.title
descr = v.descr


# v.rating.rating = 6  # ValueError
################################################################
class VideoItem:

    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:

    def __init__(self):
        self.__rating = 0

    def __setattr__(self, key, value):
        if key == "_VideoRating__rating":
            if value < 0 or value > 5:
                raise ValueError('неверное присваиваемое значение')
        super().__setattr__(key, value)

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value


################################################################
# Подвиг 9 (на повторение). Объявите в программе базовый класс с именем IteratorAttrs для перебора всех локальных
# атрибутов объектов класса. Напомню, что для этого используются два магических метода:
# __iter__() - для получения объекта-итератора (в данном случае - это сам объект self)__next__() - для перебора
# локальных атрибутов объекта self (используйте для этого словарь __dict__)Метод __next__() на каждой итерации
# должен возвращать кортеж в формате: (имя атрибута, значение).Подсказка: здесь можно определить один метод __iter__()
# как функцию-генератор.Объявите дочерний класс SmartPhone, объекты которого создаются командой:
# phone = SmartPhone(model, size, memory)где model - модель смартфона (строка); size - габариты (ширина, длина) в
# виде кортежа двух чисел; memory - размер ОЗУ (памяти), как целое число. В каждом объекте класса SmartPhone должны
# создаваться соответствующие локальные атрибуты: model, size, memory.Благодаря наследованию от базового класса
# IteratorAttrs, с объектами класса SmartPhone должен выполняться оператор for:
class IteratorAttrs:
    def __iter__(self):
        yield from self.__dict__.items()


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

    def __iter__(self):
        return super().__iter__()


phone = SmartPhone("iPhone", 10, 1024)
print(phone)
for attr, value in phone:
    print(attr, value)


################################################################
class IteratorAttrs:
    def __iter__(self):
        for i in self.__dict__.items():
            yield i


################################################################
class IteratorAttrs:
    def __iter__(self):
        return iter(self.__dict__.items())


################################################################
class IteratorAttrs:
    def __iter__(self):
        self.items = list(self.__dict__.items())
        return self

    def __next__(self):
        if self.items:
            return self.items.pop(0)
        else:
            raise StopIteration


################################################################
class IteratorAttrs:
    def __iter__(self):
        self.indx = -1
        return self

    def __next__(self):
        self.indx += 1
        if self.indx < len(self.__dict__) - 1:
            return list(self.__dict__.items())[self.indx]
        else:
            raise StopIteration


################################################################
class IteratorAttrs:
    __index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index <= len(self.__dict__) - 2:
            key = list(self.__dict__)[self.__index]
            value = self.__dict__[key]
            self.__index += 1
            return key, value
        else:
            raise StopIteration


################################################################
# Через служебный класс-итератор. Чтобы не расслабляться, в задачах на написание итераторов не иду простым путём=) Да,
# через yield или просто вернув в __iter__ последовательность получается быстрее, проще и красивее. Но для себя обратил
# внимание, что очень полезно для понимания процесса именно в деталях итераторы прописывать.
class Iterator:
    def __init__(self, obj):
        self._iterable = list(obj.__dict__.items())
        self._current = 0
        self._length = len(self._iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < self._length:
            attr, value = self._iterable[self._current]
            self._current += 1
            return attr, value
        raise StopIteration


class IteratorAttrs:
    def __iter__(self):
        return Iterator(self)


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model, self.size, self.memory = model, size, memory


################################################################
class IteratorAttrs:

    def __iter__(self):
        self.lst = [*self.__dict__.items()]  # [('model', 'iPhone'), ('size', 10), ('memory', 1024)]
        self.start = -1
        return self

    def __next__(self):
        if self.start < len(self.lst) - 1:
            self.start += 1
            return self.lst[self.start]
        raise StopIteration


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


################################################################
# ____4.4 Наследование. Атрибуты private и protected______
class Phone:
    def __init__(self, model):
        self.__model = model  # iPhone 123

    def get_info(self):
        return self.__model


class SmartPhone(Phone):
    def __init__(self, model, memory):
        super().__init__(model)
        self.__memory = memory

    def get_info(self):
        return self.__memory  # 1024


phone = SmartPhone('iPhone 123', 1024)
print(phone.get_info())  # 1024

# в момент вызова метода get_info() произойдет ошибка, так как локальный атрибут __model отсутствует в классе SmartPhone
# приватная переменная __model доступна только внутри класса Phone и недоступна в классе SmartPhone
################################################################
# Подвиг 5 Создайте в программе список с именем animals, который содержит три объекта класса Animal со следующими
# данными:
# Васька; дворовый кот; 5Рекс; немецкая овчарка; 8Кеша; попугай; 3


################################################################
s = 'Васька; дворовый кот; 5'
'Рекс; немецкая овчарка; 8'
'Кеша; попугай; 3'
animals = [Animal(*line.split('; ')) for line in s.splitlines()]
################################################################
animals = [Animal(*[int(x) if x.isdigit() else x for x in line.split('; ')]) for line in s.splitlines()]
animals = [Animal(*map(lambda x: int(x) if x.isdigit() else x, line.split('; '))) for line in s.splitlines()]


################################################################
class StringParser:
    def __init__(self, separator: str):
        self.sep = separator

    def __call__(self, cls):
        def wrapper(string):
            name, kind, old = string.strip().split(self.sep)
            return cls(name, kind, int(old))

        return wrapper


class Property:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        if instance is None:
            return property()
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Animal:
    name = Property()
    kind = Property()
    old = Property()

    def __init__(self, name, kind, old):
        self.name = name
        self.kind = kind
        self.old = old


if __name__ == '__main__':
    raw_data = """Васька; дворовый кот; 5
                Рекс; немецкая овчарка; 8
                Кеша; попугай; 3"""

    ParsAnimal = StringParser(separator='; ')(Animal)
    animals = list(map(ParsAnimal, raw_data.splitlines()))


################################################################
class Discriptor_animal:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        if instance is None:
            return property()
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Animal:
    name = Discriptor_animal()
    kind = Discriptor_animal()
    old = Discriptor_animal()

    def __init__(self, name: str, kind: str, old: int) -> None:
        self.name: str = name
        self.kind: str = kind
        self.old: int = old


################################################################
# Подвиг 6. Объявите класс Furniture (мебель), объекты которого создаются командой:f = Furniture(name, weight)
# где name - название предмета (строка); weight - вес предмета (целое или вещественное число).
# В каждом объекте класса Furniture должны создаваться защищенные локальные атрибуты с именами _name и _weight. В
# самом классе Furniture нужно объявить приватные методы:__verify_name() - для проверки корректности имени;
# __verify_weight() - для проверки корректности веса.Метод __verify_name() проверяет, что имя должно быть строкой,
# если это не так, то генерируется исключение командой:raise TypeError('название должно быть строкой')
# Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля), если это не так,
# то генерируется исключение командой:raise TypeError('вес должен быть положительным числом')
# Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight (а также при их
# создании).На основе базового класса Furniture объявить следующие дочерние классы:Closet - для представления шкафов;
# Chair - для представления стульев;Table - для представления столов.Объекты этих классов должны создаваться командами:
# obj = Closet(name, weight, tp, doors)   # tp: True - шкаф-купе; False - обычный шкаф; doors - число дверей (целое
# число)obj = Chair(name, weight, height)       # height - высота стула (любое положительное число)
# obj = Table(name, weight, height, square) # height - высота стола; square - площадь поверхности (любые положительные
# числа)В каждом объекте этих классов должны создаваться соответствующие защищенные атрибуты:
# - в объектах класса Closet: _name, _weight, _tp, _doors- в объектах класса Chair: _name, _weight, _height
# - в объектах класса Table: _name, _weight, _height, _squareВ каждом классе (Closet, Chair, Table) объявить метод:
# get_attrs()который возвращает кортеж из значений локальных защищенных атрибутов объектов этих классов.
class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __setattr__(self, key, value):
        if key == '_name':
            self.__verify_name(value)
        if key == '_weight':
            self.__verify_weight(value)
        super().__setattr__(key, value)
        # self.__dict__[key] = value #  Получается, что выгоднее добавлять атрибуты через словарь ))

    def get_attrs(self):
        return tuple(self.__dict__.values())
        # return tuple(i for i in self.__dict__.values())

    @staticmethod
    def __verify_name(name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight):
        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())


################################################################
class Furniture:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __setattr__(self, key, value):
        verify = {'_name': self.__verify_name, '_weight': self.__verify_weight}
        if key in verify:
            verify[key](value)
        object.__setattr__(self, key, value)

    # поскольку __setattr__ находится в родительском классе, то вызывается метод _Furniture__verify_name.
    # А вот если перенести __setattr__ в дочерний класс, то оттуда уже обратиться к self.__verify_name не получится


################################################################
class Furniture:
    def __init__(self, name, weight):
        self.set_name(name)
        self.set_weight(weight)

    def set_name(self, name):
        self.__verify_name(name)
        self._name = name

    def set_weight(self, weight):
        self.__verify_weight(weight)
        self._weight = weight


################################################################
# Подвиг 7 (введение в паттерн слушатель). Своей работой вы немного впечатлили начальство и оно поручило вам доделать
# паттерн слушатель (listener). Идея этого паттерна очень проста и основа реализуется следующим образом:
# Здесь в объектах класса Subject можно зарегистрировать (добавить) множество объектов класса Observer (наблюдатель,
# слушатель). Это делается с помощью метода add_observer(). Затем, когда данные (self.__data) меняются путем вызова
# метода change_data() класса Subject, то у всех слушателей автоматически вызывается метод update(). В этом методе
# можно прописать самую разную логику работы при изменении данных в каждом конкретном слушателе.В проекте данный
# паттерн предполагается использовать для отображения информации о погоде в различных форматах:- текущая температура;
# - текущее атмосферное давление;- текущая влажность воздуха.Для этого сами данные определяются классом:
# А вам поручается разработать дочерние классы, унаследованные от класса Observer, с именами:TemperatureView -
# слушатель для отображения информации о температуре;PressureView - слушатель для отображения информации о давлении;
# WetView - слушатель для отображения информации о влажности.Каждый из этих классов должен переопределять метод
# update() базового класса так, чтобы выводилась в консоль информация в формате:TemperatureView: "Текущая температура
# <число>"PressureView: "Текущее давление <число>"WetView: "Текущая влажность <число>"Важно: для вывода информации в
# консоль используйте функцию print() с одним аргументом в виде F-строки.
class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


class TemperatureView(Observer):
    def update(self, data):
        if data:
            print(f'Текущая температура {data.temp}')


class PressureView(Observer):
    def update(self, data):
        if data:
            print(f'Текущее давление {data.press}')


class WetView(Observer):
    def update(self, data):
        if data:
            print(f'Текущая влажность {data.wet}')


subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))  # Текущая температура 23# Текущее давление 150# Текущая влажность 83
subject.remove_observer(wet)
subject.change_data(Data(24, 148, 80))  # Текущая температура 24# Текущее давление 148


################################################################
class Observer:
    def update(self, data):
        print(f'{self.message} {getattr(data, self.attribute)}')  # getattr(object, 'name')


class TemperatureView(Observer):
    message = 'Текущая температура'
    attribute = 'temp'


class PressureView(Observer):
    message = 'Текущее давление'
    attribute = 'press'


class WetView(Observer):
    message = 'Текущая влажность'
    attribute = 'wet'


################################################################
class Viev(Observer):
    name = None
    attr = None

    def update(self, data):
        print(f'{self.name} {data.__dict__[self.attr]}')  #
        # self.__dict__ доступ к словарю, который хранит все атрибуты объекта экземпляра.


class TemperatureView(Viev):
    name = "Текущая температура"
    attr = 'temp'


class PressureView(Viev):
    name = 'Текущее давление'
    attr = 'press'


class WetView(Viev):
    name = 'Текущая влажность'
    attr = 'wet'


################################################################
class Observer:
    attribute = ''
    text = ''

    def update(self, data):
        if isinstance(data, Data):
            self.data = data.__dict__[self.attribute]
            print(f"{self.text} {self.data}")


class TemperatureView(Observer):
    attribute = 'temp'
    text = 'Текущая температура'


################################################################
# Подвиг 8. Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:
# air = Aircraft(model, mass, speed, top)где model - модель самолета (строка); mass - подъемная масса самолета
# (любое положительное число); speed - максимальная скорость (любое положительное число); top - максимальная высота
# полета (любое положительное число).В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами:
# _model, _mass, _speed, _top и соответствующими значениями. Если передаваемые аргументы не соответствуют указанным
# критериям (строка, любое положительное число), то генерируется исключение командой:
# raise TypeError('неверный тип аргумента')Далее, в программе объявите следующие дочерние классы:
# PassengerAircraft - пассажирский самолет;WarPlane - военный самолет.Объекты этих классов создаются командами:
# pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число пассажирских мест (целое положительное
# число)wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение (словарь); ключи - название оружия,
# значение - количествоВ каждом объекте классов PassengerAircraft и WarPlane должны формироваться локальные атрибуты
# с именами _chairs и _weapons соответственно. Инициализация остальных атрибутов должна выполняться через инициализатор
# базового класса.В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых аргументов
# chairs и weapons. Если тип данных не совпадает, то генерировать исключение командой:
# raise TypeError('неверный тип аргумента')Создайте в программе четыре объекта самолетов со следующими данными:
# PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
# PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
# WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
# WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}# Все эти объекты представить в виде списка planes.

class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def check(self, key, value):
        if key == '_model':
            if type(value) != str:
                raise TypeError('неверный тип аргумента')
        elif key in ('_mass', '_speed', '_top'):
            if not isinstance(value, (int, float)) or value <= 0:
                raise TypeError('неверный тип аргумента')

    def __setattr__(self, key, value):
        self.check(key, value)
        super().__setattr__(key, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        if any([chairs <= 0, type(chairs) != int]):
            # if not isinstance(chairs, int) or chairs <= 0:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __str__(self):
        return f'PassengerAircraft: {self._model}, {self._mass}, {self._speed}, {self._top}, {self._chairs}'


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __str__(self):
        return f'WarPlane: {self._model}, {self._mass}, {self._speed}, {self._top}, {self._weapons}'


t = '''PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}'''
import ast

planes = []
for el in t.split('\n'):
    cls_name, pars = el.split(': ', maxsplit=1)
    model, mass, speed, top, last = pars.split(', ', maxsplit=4)
    mass, speed, top = float(mass), float(speed), float(top)
    if cls_name == 'PassengerAircraft':
        last = int(last)
    elif cls_name == 'WarPlane':
        # last = {"ракета": 4, "бомба": 10}
        last = {j.split(': ')[0]: j.split(': ')[1] for j in last.split(',')}
        # last = ast.literal_eval(last)
    planes.append(globals()[cls_name](model, mass, speed, top, last))

print(planes)  # в виде адресов в памяти [<__main__.PassengerAircraft object at 0x000002E7C6A88A50>, <__main__.Pa..
for i in planes:
    print(i)  # PassengerAircraft: SuperJet, 1145.0, 8640.0, 11034.0, 80....

planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]


################################################################
class Aircraft:
    def __init__(self, model, mass, speed, top):
        if not isinstance(model, str) or \
                not isinstance(mass, (int, float)) or mass <= 0 or \
                not isinstance(speed, (int, float)) or speed <= 0 or \
                not isinstance(top, (int, float)) or top <= 0:
            raise TypeError('неверный тип аргумента')


################################################################
t = '''PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}'''
import ast

planes = []
for el in t.split('\n'):
    cls_name, pars = el.split(': ', maxsplit=1)
    model, mass, speed, top, last = pars.split(', ', maxsplit=4)
    mass, speed, top = float(mass), float(speed), float(top)
    if cls_name == 'PassengerAircraft':
        last = int(last)
    elif cls_name == 'WarPlane':
        # last = {"ракета": 4, "бомба": 10}
        last = {j.split(': ')[0]: j.split(': ')[1] for j in last.split(',')}
        # last = ast.literal_eval(last)
    planes.append(globals()[cls_name](model, mass, speed, top, last))

print(planes)  # в виде адресов в памяти [<__main__.PassengerAircraft object at 0x000002E7C6A88A50>, <__main__.Pa..
for i in planes:
    print(i)  # PassengerAircraft: SuperJet, 1145.0, 8640.0, 11034.0, 80....


################################################################
def int_positive_validator(value):
    return type(value) == int and value > 0


def any_positive_validator(value):
    return type(value) in (int, float) and value > 0


def str_validator(value):
    return type(value) == str


def dict_validator(value):
    return type(value) == dict


class Value:
    def __init__(self, validator=None, exception=TypeError('неверный тип аргумента')):
        self.validator = validator
        self.exception = exception

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator is not None:
            if not self.validator(value):
                raise self.exception

        instance.__dict__[self.name] = value


class Aircraft:
    _model = Value(str_validator)
    _mass = Value(any_positive_validator)
    _speed = Value(any_positive_validator)
    _top = Value(any_positive_validator)

    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    _chairs = Value(int_positive_validator)

    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    _weapons = Value(dict_validator)

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons


################################################################
class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == '_model':
            if type(value) != str:
                raise TypeError('неверный тип аргумента')
        elif key in ('_mass', '_speed', '_top'):
            if not isinstance(value, (int, float)) or value <= 0:
                raise TypeError(f'неверный тип аргумента')
        object.__setattr__(self, key, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, key, value):
        if key == '_chairs':
            if type(value) != int or value <= 0:
                raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, key, value):
        if key == '_weapons':
            if type(value) != dict:
                raise TypeError('неверный тип аргумента')
            else:
                for k, v in value.items():
                    if type(k) != str or type(v) != int:
                        raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


################################################################
class Aircraft:
    def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float)):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == '_model' and isinstance(value, str):
            object.__setattr__(self, key, value)
        elif key in ('_mass', '_speed', '_top') and isinstance(value, (int, float)) and value > 0:
            object.__setattr__(self, key, value)
        elif key == '_chairs' and isinstance(value, int) and value > 0:
            object.__setattr__(self, key, value)
        elif key == '_weapons' and isinstance(value, dict) and \
                all(map(lambda name_weapon: isinstance(name_weapon, str), value.keys())) and \
                all(map(lambda quantity: isinstance(quantity, int), value.values())):
            object.__setattr__(self, key, value)
        else:
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):  # пассажирский самолет
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):  # военный самолет
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons


################################################################
class Aircraft:
    checkers = {}

    def __init__(self, *args):
        self.checkers.update({'_model': self._isstr, '_mass': self._isp,
                              '_speed': self._isp, '_top': self._isp})
        self._model, self._mass, self._speed, self._top = args

    def __setattr__(self, name, v):
        if not self.checkers.get(name, lambda x: True)(v):
            raise TypeError('неверный тип аргумента')
        super().__setattr__(name, v)

    # В данном коде, выражение self.checkers.get(name, lambda x: True) возвращает функцию-проверку типа атрибута объекта.
    # Если такая функция найдена, то она вызывается с переданным значением v внутри условия if not.Это проверяет, что тип
    # значения v соответствует ожидаемому типу для конкретного атрибута name класса Aircraft или его подклассов.
    # Если тип не соответствует, возникает исключение TypeError('неверный тип аргумента').Функции _isstr, _isp, _isip и
    # _isweapon использованы как функции-проверки типов, которые принимают значение v и возвращают булевое значение
    # (True или False) в зависимости от того, является ли тип v правильным. Когда вы передаете лямбда-функцию в метод
    # get, это означает, что если ключ не найден в словаре, будет выполнена переданная лямбда-функция и ее результат
    # будет возвращен вместо значения по умолчанию. Вероятно, этот код использует get для проверки наличия ключа в
    # словаре, и если ключ отсутствует, он возвращает True. get(name, True). Оба варианта вернут значение
    # для ключа name, если оно есть, иначе они вернут True. В данном случае оба варианта дают одинаковый результат.
    def _isstr(self, v):
        return type(v) == str

    def _isp(self, v):
        return type(v) in (int, float) and v > 0

    def _isip(self, v):
        return type(v) is int and v > 0


class PassengerAircraft(Aircraft):
    def __init__(self, *args):
        super().__init__(*args[:-1])
        self.checkers.update({'_chairs': self._isip})
        self._chairs = args[-1]


class WarPlane(Aircraft):
    def __init__(self, *args):
        super().__init__(*args[:-1])
        self.checkers.update({'_weapons': self._isweapon})
        self._weapons = args[-1]

    def _isweapon(self, v):
        return type(v) is dict and all(self._isstr(i) and self._isip(j) for i, j in v.items())


data = '''PassengerAircraft: "МС-21", 1250, 8000, 12000.5, 140
PassengerAircraft: "SuperJet", 1145, 8640, 11034, 80
WarPlane: "Миг-35", 7034, 25000, 2000, {"ракета":4,"бомба":10}
WarPlane: "Су-35", 7034, 34000, 2400, {"ракета":4,"бомба":7}'''

planes = [eval(c)(*(eval(v) for v in p)) for i in data.split('\n') \
          for c, j in [i.split(': ')] for p in [j.split(', ')]]

print(planes)  # [<__main__.PassengerAircraft object at 0x000001663FF822D0>, <__main__.PassengerAircraf...

################################################################
# Подвиг 9 (на повторение). Необходимо объявить функцию-декоратор class_log для класса, которая бы создавала логирование
# вызовов методов класса. Например следующие строчки программы:vector_log = []  @class_log(vector_log)
# декорируют класс Vector и в список vector_log добавляются имена методов, которые были вызваны при использовании этого
# класса. В частности, после выполнения команд:v = Vector(1, 2, 3)v[0] = 10в списке vector_log должны быть два метода:
# ['__init__', '__setitem__']Ваша задача реализовать декоратор с именем class_log.

# Напоминание. Ранее вы уже создавали функцию-декоратор для класса следующим образом:
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         setattr(cls, k, integer_params_decorated(v))
#     return cls
# Здесь у нас на вход принимается ссылка на класс, потому что мы декорируем класс. В нашем случае, это будет ссылка на
# класс Vector. Далее, имея эту ссылку, мы можем пройтись по коллекции __dict__ этого класса (cls.__dict__),
# __dict__ - это словарь, который хранит имя атрибута (к) класса и его значение (v). Т.к. методы - это тоже атрибуты
# класса, только в виде функций, то в значениях (v) хранится ссылка на функцию, т.е. на этот метод. И далее, методом
# callable() мы проверяем, что если это действительно функция, мы его имя и значение помещаем в переменную methods.
# Т.е. фильтруем коллекцию __dict__ и в methods оставляем только функции (методы). После этого мы перебираем эту
# отфильтрованную коллекцию methods, и с помощью setattr как бы ещё раз создаём в нашем классе эти методы с названием k,
# но только теперь мы их декорируем декоратором integer_params_decorated(v) (здесь v - это ссылка на функцию (метод)).
# И вот уже в этом декораторе мы прописываем логику, что при вызове этот метод нужно добавить в список логов. При этом
# обратите внимание, методы просто становятся декорированные. Это не значит, что как только вы его декорировали, он
# сразу улетает в список логов. Декоратор срабатывает только при вызове функции, в нашем случае методов. Т.е. пока
# методы не вызываются, у нас класс просто превращается в такой вид:
# class Vector:
#     @integer_params_decorated()
#     def __init__(self):
#         pass
# А вот срабатывать этот декоратор будет только при вызове функции (метода). И соответственно, логика, прописанная в
# этом декораторе, будет выполняться только при вызове метода

# здесь 2 декоратора - 1 декоратор класса, 2 декоратор функции, только декоратор функции используем не через синтаксис
# @decorator а обычным вызовом class.method = decorator(class.method). В декораторе класса у нас есть такой код :
# for k, v in cls.__dict__.items():
#       if callable(v):
#           setattr(cls, k, decorator(v))
# return cls Здесь мы берем все аттрибуты класса (именно класса, а не экземпляра класса) из словаря __dict__
# перебираем их и проверяем если аттрибут является вызываем (т.е. методом) callable(v) если аттрибут является методом
# то мы переназначаем на его имя k  декорированный декоратором функции decorator(v) метод v . Мы бы могли сделать
# аналогичный функционал без декоратора класса если бы каждый метод класса обернули декоратором @decorator(vector_log).
# Правда для этого надо немного изменить декоратор для того что бы он мог принимать аргумент.vector_log = []
vector_log = []


def class_log(lst):
    def dec_class(cls):  # class Vector
        method = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in method.items():  # в methods помещаются все вызываемые методы из класса cls (__init__, __setitem__)
            setattr(cls, k, dec_method(v, lst))  # v = dec_method(v, lst)

        return cls

    return dec_class


def dec_method(func_method, lst):
    def wrapper(*args, **kwargs):
        lst.append(func_method.__name__)
        return func_method(*args, **kwargs)

    return wrapper


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)


#######################################################################
def class_log(lst):
    def dec_class(cls):
        for name, method in cls.__dict__.items():
            if callable(method):
                setattr(cls, name, dec_method(method, lst))

            def dec_method(func_method, lst):
                def wrapper(*args, **kwargs):
                    lst.append(func_method.__name__)
                    return func_method(*args, **kwargs)

                return wrapper

        return cls

    return dec_class


################################################################################################################################
def class_log(lst):
    def dec_class(cls):
        for name, method in cls.__dict__.items():
            if callable(method):
                setattr(cls, name, dec_method(method, lst))
        return cls

    return dec_class


def dec_method(func_method, lst):
    def wrapper(*args, **kwargs):
        lst.append(func_method.__name__)
        return func_method(*args, **kwargs)

    return wrapper


################################################################
#  class_decorators
class class_log:
    def __init__(self, lst):
        self.storage = lst

    def __call__(self, cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, self.decorated(v))
        return cls

    def decorated(self, func):
        def wrapper(*args):
            self.storage.append(func.__name__)
            return func(*args)

        return wrapper


################################################################
def class_log(log_descriptor):
    def decorator(method):
        def wrapper(*args, **kwargs):
            log_descriptor.append(method.__name__)
            return method(*args, **kwargs)

        return wrapper

    def class_decorator(cls):
        for k, v in cls.__dict__.items():
            if callable(v):
                setattr(cls, k, decorator(v))
        return cls

    return class_decorator


################################################################
# Сделал декоратор класса, который декорирует все методы, которые могут быть вызваны...
def class_log(vector_log):
    def decor(cls):
        methods = {name: method for name, method in cls.__dict__.items() if callable(method)}

        def counter(method):

            def wrapper(self, *args):
                if method.__name__ not in vector_log:
                    vector_log.append(method.__name__)
                return method(self, *args)

            return wrapper

        for method_name in methods:
            setattr(cls, method_name, counter(methods[method_name]))

        return cls

    return decor


################################################################
# Здесь мы модифицировали наш старый декоратор таким образом, чтобы он выполнял декорируемую функцию iters раз, а затем
# выводил среднее время выполнения. Однако чтобы добиться этого, пришлось воспользоваться природой функций в Python.
# Функция benchmark() на первый взгляд может показаться декоратором, но на самом деле таковым не является. Это обычная
# функция, которая принимает аргумент iters, а затем возвращает декоратор. В свою очередь, он декорирует функцию
# fetch_webpage(). Поэтому мы использовали не выражение @benchmark, а @benchmark(iters=10) — это означает, что тут
# вызывается функция benchmark() (функция со скобками после неё обозначает вызов функции), после чего она возвращает
# сам декоратор.Да, это может быть действительно сложно уместить в голове, поэтому держите правило:
# Декоратор принимает функцию в качестве аргумента и возвращает функцию.В нашем примере benchmark() не удовлетворяет
# этому условию, так как она не принимает функцию в качестве аргумента. В то время как функция actual_decorator(),
# которая возвращается benchmark(), является декоратором.


def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)

################################################################
# Подвиг 10 (на повторение). В программе объявлены два класса и глобальная переменная:
# CURRENT_OS = 'windows'   # 'windows', 'linux'Вам необходимо объявить класс с именем FileDialogFactory
# (фабрика классов), который бы при выполнении команды:dlg = FileDialogFactory(title, path, exts)
# возвращал объект класса WindowsFileDialog, если CURRENT_OS равна строке 'windows', в противном случае - объект
# класса LinuxFileDialog. Объект самого класса FileDialogFactory создаваться не должен.Для реализации такой логики,
# объявите внутри класса FileDialogFactory два статических метода:def create_windows_filedialog(title, path, exts)
# - для создания объектов класса WindowsFileDialog;def create_linux_filedialog(title, path, exts) - для создания
# объектов класса LinuxFileDialog.Эти методы следует вызывать в магическом методе __new__() класса FileDialogFactory.
# Подумайте, как это правильно сделать, чтобы не создавался объект самого класса, а лишь возвращался объект или класса
# WindowsFileDialog, или класса LinuxFileDialog.
CURRENT_OS = 'windows'  # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(*args, **kwargs)
        else:
            return cls.create_linux_filedialog(*args, **kwargs)

    def __init__(self, title, path, exts):
        self.title = title
        self.path = path
        self.exts = exts

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))


################################################################
class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        dlg_cls = {'windows': WindowsFileDialog, 'linux': LinuxFileDialog}
        return dlg_cls[CURRENT_OS](*args, **kwargs)

    def create_windows_filedialog(self, title, path, exts):
        pass

    def create_linux_filedialog(self, title, path, exts):
        pass


################################################################
class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == 'windows':
            instance = super().__new__(WindowsFileDialog)
            # ссылка на объект который вернет метод super() с переданным в качестве параметра WindowsFileDialog
            return instance.__init__(*args, **kwargs)
        else:
            instance = super().__new__(LinuxFileDialog)
            return instance.__init__(*args, **kwargs)


################################################################
class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        return getattr(cls, f"create_{CURRENT_OS.lower()}_filedialog")(*args)

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)


################################################################
class FileDialogFactory:
    def __new__(cls, *args):
        return {'windows': cls.create_windows_filedialog(*args), 'linux': cls.create_linux_filedialog(*args)}[
            CURRENT_OS]

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)
    # в словаре создаются сразу все объекты, лучше было бы в словаре хранить ссылку на класс (в вашем случае - ссылки
    # на функции)


################################################################
class FileDialogFactory:
    def __new__(cls, *args):
        return cls.create_filedialog({'windows': WindowsFileDialog, 'linux': LinuxFileDialog}[CURRENT_OS], *args)

    @staticmethod
    def create_filedialog(cls, title, path, exts):
        return cls(title, path, exts)


################################################################
class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == 'windows':
            return cls.create_filedialog(WindowsFileDialog, *args, **kwargs)
        else:
            return cls.create_filedialog(LinuxFileDialog, *args, **kwargs)

    @staticmethod
    def create_filedialog(cls, title, path, exts):
        return cls(title, path, exts)


################################################################
# ____4.6 Множественное наследование__Egorof____

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class Discount:
    def apply_discount(self, discount):
        self.price -= self.price * discount


class DiscountedProduct(Product, Discount):
    pass


product1 = DiscountedProduct('Телефон', 10000)
product1.apply_discount(0.1)
print(product1.get_price())  # 9000


################################################################
# создать класс User, который принимает имя пользователя и пароль при инициализации, и имеет метод get_info(),
# который возвращает строку в виде Имя пользователя: {self.username}Создайте класс Authentication, состоящий из одного
# метода authenticate(). Данный метод принимает имя пользователя и пароль, и возвращает True, если пользователь
# аутентифицирован успешно, и False, если аутентификация не удалась.Создайте пустой класс AuthenticatedUser, который
# наследуется от классов Authentication и User
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_info(self):
        return f'Имя пользователя: {self.username}'


class Authentication(User):
    def authenticate(self, username, password):
        return True if username == self.username and password == self.password else False


class AuthenticatedUser(Authentication, User):
    pass


# class AuthenticatedUser(User, Authentication):
#     #TypeError: Cannot create a consistent method resolution order (MRO) for bases User, Authentication
# Ошибка, с которой вы столкнулись, TypeError: Cannot create a consistent method resolution order (MRO) for bases User,
# Authentication, возникает из-за того, как работает множественное наследование и порядок разрешения методов (MRO) в
# Python.В Python, когда класс наследует от нескольких базовых классов, порядок этих классов определяет MRO.
# MRO определяет порядок, в котором Python ищет методы и атрибуты в иерархии наследования.В вашем коде, когда вы
# определяете класс AuthenticatedUser(Authentication, User), Python использует алгоритминеаризации C3 для определения
# MRO. Алгоритм C3 гарантирует, что MRO сохраняет порядок базовых классов, сохраняет консистентность и разрешает
# любые конфликты.Однако в этом случае MRO не может быть определен, потому что у классов Authentication и User есть
# общий базовый класс (object), и они находятся на одном уровне в иерархии наследования.то создает неоднозначность при
# расчете MRO и приводит к ошибке TypeError.Чтобы исправить эту проблему, вы можете изменить порядок базовых классов в
# определении AuthenticatedUser на class AuthenticatedUser(User, Authentication).аким образом, вы приоритезируете класс
# User перед классом Authentication в MRO, и ошибка больше не должна возникать.
# Алгоритм C3 (C3 linearization algorithm) - это алгоритм, используемый Python для определения порядка разрешения
# методов (MRO) при множественном наследовании. Он был разработан для обеспечения консистентного и предсказуемого
# порядка разрешения методов в иерархии классов. Алгоритм C3 решает проблему неоднозначности, которая может возникнуть
# при наличии общих базовых классов и разных путей наследования. Он строит линеаризацию, то есть линейный порядок, в
# котором должны быть рассмотрены методы и атрибуты при вызове из экземпляра класса. Вкратце, алгоритм C3 работает
# следующим образом:# Создается линейный список, называемый "линеаризацией", который будет содержать порядок
# разрешения методов.Берется первый класс в списке наследования и добавляется в линеаризацию. Для каждого класса в
# списке наследования проверяется его базовые классы.Если базовый класс уже присутствует в линеаризации или встречается
# позже в списке наследования, он игнорируется.Если базовый класс не присутствует в линеаризации и не встречается
# позже в списке наследования, он добавляется в линеаризацию. 6.аги 3-5 повторяются для каждого класса в списке
# наследования.Полученная линеаризация является MRO.Алгоритм C3 гарантирует, что MRO сохраняет порядок базовых классов,
# сохраняет консистентность и разрешает любые конфликты при множественном наследовании.

assert issubclass(AuthenticatedUser, User) is True
assert issubclass(AuthenticatedUser, Authentication) is True

user1 = AuthenticatedUser('user1', 'password1')
assert user1.get_info() == 'Имя пользователя: user1'
assert user1.authenticate('user1', 'password2') is False
assert user1.authenticate('user1', 'password1') is True

ted = AuthenticatedUser('ted_lawyer', 'alligator3')
print(ted.get_info())  # Имя пользователя: ted_lawyer


################################################################
#  Создайте базовый класс Person, у которого есть:метод __init__, принимающий имя и возраст человека. Их необходимо
#  сохранить в атрибуты экземпляра nameи age соответственнометод display_person_info , который печатает информацию в
#  следующем виде:Person: {name}, {age}Затем создайте класс Company , у которого есть:метод __init__, принимающий
#  название компании и город ее основания. Их необходимо сохранить в атрибуты экземпляра company_name  и location
#  соответственнометод display_company_info , который печатает информацию в следующем виде:
#  Company: {company_name},  {location}И в конце создайте класс Employee , который:унаследован от классов
#  Person и Company имеет метод __init__, принимающий имя человека, его возраст, название компании и город основания.
#  Необходимо делегировать создание атрибутов nameи age  классу Person , а атрибуты company_name  и location должен
#  создать класс Company
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super(Employee, self).__init__(name, age)
        Company.__init__(self, company_name, location)


emp = Employee('Jessica', 28, 'Google', 'Atlanta')
emp.display_person_info()
emp.display_company_info()


################################################################
class Person:
    def __init__(self, *args):
        self.name, self.age = args

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, *args):
        self.company_name, self.location = args

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee(Person, Company):
    def __init__(self, *args):
        Person.__init__(self, *args[:2])
        Company.__init__(self, *args[2:])


################################################################

class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super().__init__(name, age)
        Company.__init__(self, company_name, location)


################################################################
# 4.7 MRO - порядок разрешения методов

class O: ...


class A(O): ...


class B(O): ...


class C(O): ...


class D(O): ...


class E(O): ...


class K1(C, A, B): ...


class K2(A, D): ...


class K3(B, D, E): ...


class Z(K1, K2, K3): ...


print(Z.mro())
"""[<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.C'>, 
<class '__main__.K2'>, <class '__main__.A'>, <class '__main__.K3'>, 
<class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.O'>, <class 'object'>]"""


def get_mro(class_name):
    print(*[cl.__name__ for cl in class_name.mro()], sep=' -> ')


# Z -> K1 -> C -> K2 -> A -> K3 -> B -> D -> E -> O -> object

get_mro(Z)
get_mro(K3)


class Music(object): pass


class Rock(Music): pass


class Gothic(Music): pass


class Metal(Rock): pass


class GothicRock(Rock, Gothic): pass


class GothicMetal(Metal, Gothic): pass


class The69Eyes(GothicRock, GothicMetal): pass


print(The69Eyes.mro())


def get_mro(class_name):
    print(*[cl.__name__ for cl in class_name.mro()], sep=' -> ')


get_mro(The69Eyes)


# [<class '__main__.Z'>, <class '__main__.K1'>, <class '__main__.C'>, <class '__main__.K2'>, <class '__main__.A'>,
# <class '__main__.K3'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.O'>,
# <class 'object'>]
# Z -> K1 -> C -> K2 -> A -> K3 -> B -> D -> E -> O -> object
# K3 -> B -> D -> E -> O -> object

# [<class '__main__.The69Eyes'>, <class '__main__.GothicRock'>, <class '__main__.GothicMetal'>, <class '__main__.
# Metal'>, <class '__main__.Rock'>, <class '__main__.Gothic'>, <class '__main__.Music'>, <class 'object'>]

# The69Eyes -> GothicRock -> GothicMetal -> Metal -> Rock -> Gothic -> Music -> object
################################################################
# __Balakiref___ 4.6 Множественное наследование____
class A:
    def __init__(self):
        print("A")
        super().__init__()


class B:
    def __init__(self):
        print("B")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C")
        super().__init__()


c = C()  # C A B


##############################################################
class O:
    def method(self):
        print('O', end=' ')


class A(O):
    def method(self):
        super().method()
        print('A', end=' ')


class B(O):
    def method(self):
        super().method()
        print('B', end=' ')


class C(A, B):
    def method(self):
        super().method()
        print('C', end=' ')


c = C()
c.method()  # O B A C - обратный порядок относительно C->A->B->O->object
print()
print('->'.join([x.__name__ for x in C.mro()]))  # C->A->B->O->object


################################################################
class A:
    def __init__(self, name, old):
        # super().__init__()
        self.name = name
        self.old = old


class B:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class C(B, A):
    def __init__(self, name, old, weight, height):
        super().__init__(name, old)
        self.weight = weight
        self.height = height


person = C("Balakirev", 33, 80, 185)


# последовательность вызова классов
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

################################################################
# Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам.
# Выполним такой пример.Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:
# Digit, Integer, Float, Positive, NegativeКаждый объект этих классов должен создаваться однотипной командой вида:
# obj = Имя_класса(value)где value - числовое значение. В каждом классе следует делать свою проверку на корректность
# значения value:- в классе Digit: value - любое число;- в классе Integer: value - целое число;- в классе Float:
# value - вещественное число;- в классе Positive: value - положительное число;- в классе Negative:
# value - отрицательное число.Если проверка не проходит, то генерируется исключение командой:
# raise TypeError('значение не соответствует типу объекта')После этого объявите следующие дочерние классы:
# PrimeNumber - простые числа; наследуется от классов Integer и Positive;FloatPositive - наследуется от классов Float
# и Positive.Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными
# допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.Затем, используя функции
# isinstance() и filter(), сформируйте следующие списки из указанных объектов:lst_positive - все объекты,
# относящиеся к классу Positive;lst_float - все объекты, относящиеся к классу Float.
class Digit:
    def __init__(self, value):
        if type(value) not in [int, float, complex]:
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        if type(value) not in [int]:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if type(value) not in [float]:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value < 0:  # не положительное число;
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value > 0:  # не отрицательное число.
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        # Дополнительная проверка на простое число
        if not self.is_prime(value):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


class FloatPositive(Float, Positive): ...


digits = [PrimeNumber(3), PrimeNumber(5), PrimeNumber(7), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))

lst_float = list(filter(lambda x: Float in x.__class__.__mro__, digits))
print(PrimeNumber.__class__.__mro__)  # (<class 'type'>, <class 'object'>)
print(Float in PrimeNumber.__mro__)  # False
print(PrimeNumber.__mro__)  # (<class '__main__.PrimeNumber'>, <class '__main__.Integer'>,..

print(len(lst_positive))
print(lst_positive)
print(len(lst_float))
print(lst_float)


################################################################
class Digit:
    def __init__(self, value):
        self._value = value

    def __setattr__(self, name, value):
        if not self._check_value(value):
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(name, value)

    def _check_value(self, value):
        return type(value) in (int, float)


class Integer(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and type(value) is int


class Float(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and type(value) is float


class Positive(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and value > 0


class Negative(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and value < 0


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(1), PrimeNumber(2), PrimeNumber(3),
          FloatPositive(1.2), FloatPositive(1.3), FloatPositive(1.4),
          FloatPositive(1.5), FloatPositive(1.6)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))


################################################################
def type_error(value, types=(int, float), fltr=lambda x: True):
    if not (isinstance(value, types) and fltr(value)):
        raise TypeError('значение не соответствует типу объекта')


# Параметр fltr=lambda x: True в функции type_error определяет фильтрующую функцию, которая определяет, удовлетворяет
# ли значение дополнительным критериям помимо его типа.В предоставленном коде параметр fltr используется в некоторых
# подклассах класса Digit, чтобы ограничить принимаемые значения. Он позволяет настраивать фильтрацию на основе
# конкретных условий.Например, в подклассе Positive параметр fltr определен как lambda x: x > 0, что означает, что
# только значения, большие нуля, будут проходить через фильтр. Аналогично, в подклассе Negative параметр fltr
# определен как lambda x: x < 0, поэтому только значения меньше нуля будут проходить через фильтр.В других подклассах,
# таких как PrimeNumber и FloatPositive, параметр fltr не используется, и все значения соответствующих типов
# (Integer и Float соответственно) будут приняты без дополнительной фильтрации.fltr=lambda x: True - это параметр по
# умолчанию, который используется, когда нет необходимости в пользовательской фильтрации. Он обеспечивает возможность
# вызова функции type_error без явного указания фильтрующей функции.

class Digit:
    def __init__(self, value):
        type_error(value)


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)
        type_error(value, int)


class Float(Digit):
    def __init__(self, value):
        super().__init__(value)
        type_error(value, float)


class Positive(Digit):
    def __init__(self, value):
        super().__init__(value)
        type_error(value, fltr=lambda x: x > 0)


class Negative(Digit):
    def __init__(self, value):
        super().__init__(value)
        type_error(value, fltr=lambda x: x < 0)


class PrimeNumber(Integer, Positive): ...


class FloatPositive(Float, Positive): ...


digits = [PrimeNumber(17), PrimeNumber(7), PrimeNumber(22987633823298),
          FloatPositive(.258), FloatPositive(.432), FloatPositive(1.0),
          FloatPositive(99999999.9), FloatPositive(8333333333333333.2)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))


################################################################
class Digit:
    check_value = lambda x, value: isinstance(value, (float, int))

    def raise_err(self):
        raise TypeError('значение не соответствует типу объекта')

    def __init__(self, value):
        self.check_value(value) or self.raise_err()
        self.value = value


class Integer(Digit):
    check_value = lambda x, value: isinstance(value, int) and value > 0


class Float(Digit):
    check_value = lambda x, value: isinstance(value, float) and value > 0


class Positive(Digit):
    check_value = lambda x, value: value > 0


class Negative(Digit):
    check_value = lambda x, value: value < 0


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(1), PrimeNumber(2), PrimeNumber(3),
          FloatPositive(1.2), FloatPositive(1.3), FloatPositive(1.4),
          FloatPositive(1.5), FloatPositive(1.6)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))

################################################################
# cмотрите, вы вынесли всю логику в один класс Digit - повод для гордости =)Если нужно будет, в перспективе разработать
# еще 3-4 класса, снова придется править исходный класс? =)В большинстве случаев вам поступит исходный класс и
# править его никто не даст, только наследоваться от него.реализация в рамках задачи отличная, но в целом подход
# неправильный=)

################################################################
from typing import Any
from abc import ABC, abstractmethod


class DigitInterface(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def verify_value(self, value):
        pass


class Digit(DigitInterface):
    __value: Any

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        if not self.verify_value(value):
            raise TypeError('значение не соответствует типу объекта')
        self.__value = value

    def verify_value(self, value) -> bool:
        if type(self) is Digit:
            return isinstance(value, (int, float))
        return True


class Integer(Digit):
    def verify_value(self, value) -> bool:
        return isinstance(value, int) and super().verify_value(value)


class Float(Digit):
    def verify_value(self, value) -> bool:
        return isinstance(value, float) and super().verify_value(value)


class Positive(Digit):
    def verify_value(self, value) -> bool:
        return value > 0 and super().verify_value(value)


class Negative(Digit):
    def verify_value(self, value) -> bool:
        return value < 0 and super().verify_value(value)


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(3), PrimeNumber(1),
          PrimeNumber(4), FloatPositive(1.5),
          FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]
lst_positive = [obj for obj in digits if isinstance(obj, Positive)]
lst_float = [obj for obj in digits if isinstance(obj, Float)]


################################################################
class Digit:
    value_types = lambda _, x: type(x) in (int, float)

    def __init__(self, value):
        if not self.value_types(value):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Integer(Digit):
    value_types = lambda _, x: type(x) == int


class Float(Digit):
    value_types = lambda _, x: type(x) == float


class Positive(Digit):
    value_types = lambda _, x: x > 0


class Negative(Digit):
    value_types = lambda _, x: x < 0


class PrimeNumber(Integer, Positive):
    value_types = lambda _, x: Integer.value_types(_, x) and Positive.value_types(_, x)


class FloatPositive(Float, Positive):
    value_types = lambda _, x: Float.value_types(_, x) and Positive.value_types(_, x)


is_simple = lambda x: not any(map(lambda i: not x % i, range(2, int(x ** .5) + 1)))
digits = [(FloatPositive(n / 10), PrimeNumber(n))[is_simple(n)] for n in range(5, 5 + 8)]
lst_positive = [*filter(lambda x: isinstance(x, Positive), digits)]
lst_float = [*filter(lambda x: isinstance(x, Float), digits)]


################################################################
# Подвиг 5. В программе объявлены два класса:Затем, создается объект класса Book (книга) и отображается в консоль:
# book = Book("Python ООП", "Балакирев", 2022)
# print(book)В результате, на экране увидим что то вроде:<__main__.Book object at 0x0000015FBA4B3D00>
# Но нам требуется, чтобы здесь отображались локальные атрибуты объекта с их значениями в формате:
# <атрибут_1>: <значение_1><атрибут_2>: <значение_2>...<атрибут_N>: <значение_N>Для этого вам дают задание
# разработать два класса:ShopGenericView - для отображения всех локальных атрибутов объектов любых дочерних
# классов (не только Book);ShopUserView - для отображения всех локальных атрибутов, кроме атрибута _id,
# объектов любых дочерних классов (не только Book).То есть, в этих классах нужно переопределить два магических
# метода: __str__() и __repr__().
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __repr__(self):
        lst = []
        for k, v in self.__dict__.items():
            lst.append(f'{k}: {v}\n')
        return ''.join(lst)


class ShopUserView:
    def __str__(self):
        lst = []
        for k, v in self.__dict__.items():
            if k != '_id':
                lst.append(f'{k}: {v}\n')
        return ''.join(lst)


class Book(ShopItem, ShopUserView, ShopGenericView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)


# _id: 1
# _title: Python ООП
# _author: Балакирев
# _year: 2022


################################################################
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    Exclude = tuple()

    def __str__(self):
        # return '\n'.join('{0}: {1}'.format(attr, v) for attr, v in self.__dict__.items() if attr not in self.Exclude)
        return '\n'.join(f'{attr[0]}: {attr[1]}' for attr, v in self.__dict__.items() if attr not in self.Exclude)

    def __repr__(self):
        return self.__str__()


class ShopUserView(ShopGenericView):
    Exclude = ('_id',)


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)  # <__main__.Book object at 0x000001898F35C150>


################################################################
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:

    def __repr__(self):
        return '\n'.join(map(lambda x: f'{x[0]}: {x[1]}', list(self.__dict__.items())))


class ShopUserView:  # кроме атрибута _id

    def __str__(self):
        return '\n'.join(map(lambda x: f'{x[0]}: {x[1]}', list(self.__dict__.items())[1:]))


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)


####################################################################
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __iter__(self):
        for i in self.__dict__.items():
            yield i

    def __str__(self):
        return '\n'.join(map(lambda x: f'{x[0]}: {x[1]}', self))


class ShopUserView(ShopGenericView):
    def __iter__(self):
        for data in list(self.__dict__.items())[1::]:
            yield data


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


################################################################
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    _no = []

    def __repr__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items() if k not in self._no)


class ShopUserView(ShopGenericView):
    _no = ['_id']


class Book(ShopItem):
    def __init__(self, *args):
        super().__init__()
        self._title, self._author, self._year = args[:3]


################################################################
# __Egorof___4.8 Миксины___________________________________
class Mixin:
    def mixin_method(self):
        print("This is a mixin method.")


class MyClass(Mixin):
    def my_method(self):
        self.mixin_method()


obj = MyClass()
obj.my_method()  # Output: This is a mixin method.


################################################################
class BasePizza:
    BASE_PIZZA_PRICE = 15

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = ['cheese']

    def __str__(self):
        return f"{self.name} with {self.toppings}, ${self.price:.2f}"


class PepperoniMixin:
    def add_pepperoni(self):
        print("Adding pepperoni!")
        self.price += 5
        self.toppings += ['pepperoni']


class MushroomMixin:
    def add_mushrooms(self):
        print("Adding mushrooms!")
        self.price += 3
        self.toppings += ['mushrooms']


class OnionMixin:
    def add_onion(self):
        print("Adding onion!")
        self.price += 2
        self.toppings += ['onion']


class BaconMixin:
    def add_bacon(self):
        print("Adding bacon!")
        self.price += 6
        self.toppings += ['bacon']


class OlivesMixin:
    def add_olives(self):
        print("Adding olives!")
        self.price += 1
        self.toppings += ['olives']


class OlivesPizza(BasePizza, OlivesMixin):

    def __init__(self):
        super().__init__('Море оливок', BasePizza.BASE_PIZZA_PRICE)
        self.add_olives()


class PepperoniPizza(BasePizza, PepperoniMixin):

    def __init__(self):
        super().__init__('Колбасятина', BasePizza.BASE_PIZZA_PRICE)
        self.add_pepperoni()


class MushroomOnionBaconPizza(BasePizza, MushroomMixin, OnionMixin, BaconMixin):

    def __init__(self):
        super().__init__('Грибной пяточок с луком', BasePizza.BASE_PIZZA_PRICE)
        self.add_mushrooms()
        self.add_onion()
        self.add_bacon()


pizza = MushroomOnionBaconPizza()
print(pizza)


# Adding mushrooms!
# Adding onion!
# Adding bacon!
# Грибной пяточок с луком with ['cheese', 'mushrooms', 'onion', 'bacon'], $26.00
################################################################
class ToStringMixin:
    def __str__(self):
        return f"{self.__class__.__name__}({str(self.__dict__)})"


class MyClass(ToStringMixin):
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = MyClass(1, 2)
print(obj)  # Output: MyClass({'x': 1, 'y': 2})


################################################################
# использования миксина для подсчета количества экземпляров класса:
class CountInstancesMixin:
    count = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.count += 1


# ?? self.__class__ в данном коде является ссылкой на класс объекта, который вызывает этот код.В этом примере self
# представляет экземпляр класса, который был создан, а self.__class__ является атрибутом этого экземпляра, содержащим
# ссылку на его класс.В классе CountInstancesMixin, self.__class__ используется для доступа к переменной класса count
# и инкрементации ее значения при создании каждого нового экземпляра.self.__class__ может быть полезен, например, в
# тех случаях, когда вы хотите создать метод, который будет работать со всеми экземплярами класса, а не только с
# конкретным экземпляром, для которого он был вызван.Переменная count в классе CountInstancesMixin является
# переменной класса, а не экземпляра. Это означает, что она разделяется между всеми экземплярами класса и доступна
# через ссылку на класс, такую как self.__class__ или ClassName.count, где ClassName - имя класса.Когда вы создаете
# новый экземпляр класса, метод __init__() класса CountInstancesMixin вызывается через механизм наследования, и
# переменная count инкрементируется для класса, к которому относится экземпляр.Таким образом, любой экземпляр класса
# Cat или Dog может изменить значение переменной count для своего класса. Например, если вы создадите новый экземпляр
# класса Cat, переменная count будет увеличена на единицу для класса Cat. Если вы создадите новый экземпляр класса Dog,
# переменная count будет увеличена на единицу для класса Dog.
class Cat(CountInstancesMixin):
    def __init__(self, name):
        self.name = name
        super().__init__()


class Dog(CountInstancesMixin):
    def __init__(self, name):
        self.name = name
        super().__init__()


obj1 = Cat("Барсик")
obj2 = Cat("Гипард")

obj3 = Dog("Жучка")

print(Cat.count)  # Output: 2
print(Dog.count)  # Output: 1


################################################################
# аналог
class Cat:
    count = 0  # Class variable

    def __init__(self):
        Cat.count += 1


class Dog:
    count = 0  # Class variable

    def __init__(self):
        Dog.count += 1


# Creating instances of Cat and Dog classes
cat1 = Cat()
cat2 = Cat()
dog1 = Dog()

print(Cat.count)  # Output: 2
print(Dog.count)  # Output: 3


################################################################
class Mixin1(object):
    def test(self):
        print("Mixin1")


class Mixin2(object):
    def test(self):
        print("Mixin2")


class BaseClass(object):
    def test(self):
        print("BaseClass")


class MyClass(BaseClass, Mixin1, Mixin2):
    pass


obj = MyClass()
obj.test()


# порядок разрешения методов при вызове метода .test()  - MyClass => BaseClass => Mixin1 => Mixin2
################################################################
# Не понял прикола раскладывать топпинги по разным классам, поэтому положил все в один класс.
class CountryPizza(BasePizza, ToppingMixin):
    def __init__(self):
        super().__init__('Деревенская пицца', BasePizza.BASE_PIZZA_PRICE)
        self.add_ham()
        self.add_pepper()
        self.add_olives()
        self.add_pepperoni()
        self.add_mushrooms()
        self.add_chicken()


################################################################
# Для этого создайте класс PermissionMixin, который будет иметь следующие методы:__init__(self): метод инициализации,
# который создает множество permissions для хранения разрешений. В него мы будем сохранять действия, которые будут
# доступны пользователям, например Чтение, Запись, Выполнение и т.д.grant_permission(self, permission): метод для
# назначения разрешения. Добавляет переданное разрешение в множество permissionsrevoke_permission(self, permission):
# метод для отмены разрешения. Удаляет переданное разрешение из множества permissionshas_permission(self, permission):
# метод для проверки наличия разрешения. Возвращает True, если переданное разрешение присутствует в множестве
# permissions, и False в противном случае.Создайте класс User, который будет наследоваться от PermissionMixin и
# ииметь следующие атрибуты:name: имя пользователя.email: email пользователя.
class PermissionMixin:
    def __init__(self):
        self.permissions = set()

    def grant_permission(self, permission):
        self.permissions.add(permission)

    def revoke_permission(self, permission):
        self.permissions.discard(permission)

    def has_permission(self, permission):
        return permission in self.permissions


class User(PermissionMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email


################################################################
# Ваша задача научить классы конвертиться к json-строке при помощи миксина под названием JsonSerializableMixin,
# который добавляет метод to_json() в любой класс, использующий этот миксин. Метод to_json() конвертирует словарь
# атрибутов экземпляра в строку JSON, используя стандартную библиотеку json в Python.Онлайн инструмент преобразования
# JSON-строки в объект, не забудьте убрать апострофы по краям строки
import json


class JsonSerializableMixin:
    def to_json(self):
        attributes = self.__dict__  # получаем атрибуты экземпляра класса в виде словаря
        return json.dumps(attributes)


class Car(JsonSerializableMixin):
    def __init__(self, make: str, color: str):
        self.make = make
        self.color = color


class Book(JsonSerializableMixin):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Person(JsonSerializableMixin):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


################################################################
# Класс DictMixin представляет собой миксин, который добавляет в класс, наследующий его, метод to_dict(). Этот метод
# позволяет преобразовать объект в словарь. Внутри класса DictMixin вы можете создавать сколько угодно служебных методов
# и атрибутов, которые помогут вам справиться с задачей. Главное, это реализовать метод to_dict(), он являться
# точкой входа для взаимодействия с вашим миксином и он должен вернуть представление вашего объекта в виде словаря.
# Обратите внимание на вложенность атрибутов.
class DictMixin:
    def to_dict(self):
        dct = {}
        for k, v in self.__dict__.items():
            if isinstance(v, DictMixin):
                dct[k] = v.to_dict()
            elif isinstance(v, list):
                lst = []
                for i in v:
                    lst.append(i.to_dict())
                    dct[k] = lst
            else:
                dct[k] = v
        return dct

    # for раскрывает словарь, где i - ключ, а j - значения! и если в j обычные значения - нам их нужно просто добавить
    # в наш словарь "а" (это блок else),а если в j появляется экземпляр класса - нужно его так же распотрошить, как и
    # основной экземпляр, к которому мы изначально применяем цикл (в нем же все то же самое будет происходить).
    # Сложность была со списком - решил добавлением переменной "р".
    # вариант без проверок  разбить на задачи поменьше - сначала сделайте и выведите словарь без проверок:
    # a = {}
    # for i, j in self.__dict__.items():
    #     a[i] = j
    # return a


class Phone(DictMixin):
    def __init__(self, number):
        self.number = number


class Person(DictMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(DictMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(DictMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


################################################################
class DictMixin:
    def __repr__(self):
        return str(self.__dict__)

    def to_dict(self):
        return eval(self.__repr__())


# eval преобразует строку в код питона. В данном случае условная строка "{'key': 'val'}" преобразуется в словарь. Ну а
# repr - это репрезентация объекта в консоли и возвращает строку. По умолчанию адрес в памяти, но тут метод переназначен
# если кратко, то есть два метода, которые отвечают за представление объекта в строковом виде, это __str__ и __repr__.
# Разница между ними в том, что __str__ не срабатывает, если объект находится внутри другого объекта, в таких случаях
# вызывается __repr__. Поэтому, если там надо изменить то, как объект будет представляется внутри другого объекта, нам
# нужно переопределять именно метод __repr__. Ну а про то, что при отсутствии метода __str__ вызывается метод __repr__
# вы наверняка и так знаете.Используя это, я сделал так, что в строковом представлении объект отображается как словарь
# атрибутов, а классы вложенные в этот словарь в свою очередь так же представляются как аналогичные словари(объект
# внутри другого объекта). Ну а функция eval все это преобразовывает из строкового вида в тип объекта.

################################################################
import json


class DictMixin:

    def to_dict(self):
        a = json.dumps(self.__dict__, indent=2, default=lambda x: x.__dict__)
        s = json.loads(a)
        return s


################################################################
class DictMixin:
    def to_dict(self) -> dict:
        dct = self.__dict__
        for k, v in dct.items():
            if isinstance(v, DictMixin):
                dct[k] = v.to_dict()
            if isinstance(v, list):
                for i, k in enumerate(v):
                    if isinstance(k, DictMixin):
                        v[i] = k.to_dict()
        return dct


################################################################
class DictMixin:
    def to_dict(self):
        result = dict()
        for i in self.__dict__:
            if hasattr(self.__dict__[i], '__dict__'):
                result.setdefault(i, self.__dict__[i].to_dict())
            elif isinstance(self.__dict__[i], (list, tuple)):
                for j in self.__dict__[i]:
                    result.setdefault(i, []).append(j.to_dict())
            else:
                result.setdefault(i, self.__dict__[i])
        return result


################################################################
class DictMixin:
    def to_dict(self):
        dct = dict(self.__dict__)
        for attr, value in dct.items():
            if isinstance(value, DictMixin):
                dct[attr] = value.to_dict()
            elif isinstance(value, list):
                dct[attr] = [obj.to_dict() for obj in value]
        return dct


################################################################
class DictMixin:
    def to_dict(self):
        for key, value in self.__dict__.items():
            if isinstance(value, (Phone, Company, Address)):
                self.__dict__[key] = value.__dict__
            if type(value) == list:
                for i in range(len(value)):
                    value[i] = value[i].to_dict()

        return self.__dict__


################################################################
import json


class DictMixin:
    def to_dict(self):
        return json.loads(json.dumps(self, default=vars))


################################################################
# Рекурсивный обход словаря и списков внутри него.
class DictMixin:

    @staticmethod
    def make_dict(obj_dict: dict) -> dict:
        result = {}
        for key, value in obj_dict.items():
            if hasattr(value, '__dict__'):
                value = DictMixin.make_dict(value.__dict__)
            elif isinstance(value, (set, list, tuple)):
                value = type(value)([DictMixin.make_dict(val.__dict__)
                                     if hasattr(val, '__dict__') else val for val in value])
            result[key] = value
        return result

    def to_dict(self):
        return self.make_dict(self.__dict__)


################################################################
class DictMixin:

    def to_dict(self):
        answer = dict()
        for atr in self.__dict__.items():
            if not isinstance(atr[1], (str, int, float)):
                if isinstance(atr[1], list):
                    value = []
                    for x in atr[1]:
                        value.append(DictMixin.to_dict(x))
                else:
                    value = DictMixin.to_dict(atr[1])
            else:
                value = atr[1]
            answer[atr[0]] = value
        return answer


################################################################
class DictMixin:
    def to_dict(self):
        return self.flatten(self.__dict__)

    def flatten(self, my_dict):
        res = {}

        for k, v in my_dict.items():
            if isinstance(v, DictMixin):  # Если прошёл -> рекурсия
                res[k] = self.flatten(v.__dict__)
            elif type(v) == list:  # Если лист -> всё что наберёт в рекурсии в []
                res[k] = [self.flatten(i.__dict__) for i in v]
            else:  # В ином случает - это просто пара ключ-значение
                res[k] = v

        return res


################################################################
class DictMixin:

    def to_dict(self):
        new_dict = dict()
        for key, value in self.__dict__.items():
            if isinstance(value, __class__):
                value = self.get_obj(value)
            if isinstance(value, list):
                value = [self.get_obj(obj) for obj in value]
            new_dict[key] = value
        return new_dict

    def get_obj(self, obj):
        new_dict = dict()
        for key, value in obj.__dict__.items():
            if isinstance(value, __class__):
                value = self.get_obj(value)
            new_dict[key] = value
        return new_dict


################################################################
# Сериализация класса - 2
# Теперь давайте выполним сериализацию объектов, атрибутами которых могут быть другие объекты. Для этого переделайте
# миксин JsonSerializableMixin, так чтобы он мог сериализовать такие объекты. Внутри миксина JsonSerializableMixin
# обязательно должен быть метод to_json(), который возвращает итоговую строку сериализации объекта. Все остальное
# вы можете создавать по своему усмотрению. # Напишите определение класса JsonSerializableMixin
import json


class JsonSerializableMixin:

    def to_dict(self):
        dct = {}
        for k, v in self.__dict__.items():
            if isinstance(v, JsonSerializableMixin):
                dct[k] = v.to_dict()
            elif isinstance(v, list):
                lst = []
                for trim in v:
                    if isinstance(trim, (int, str, float)):
                        lst.append(trim)
                    else:
                        lst.append(trim.to_dict())
                dct[k] = lst
            else:
                dct[k] = v
        return dct

    def to_json(self):
        # если здесь прописать такую же логику как и в to_dict и return json.dumps(dct) проверку не проходит???
        return json.dumps(self.to_dict())


class Person(JsonSerializableMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(JsonSerializableMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(JsonSerializableMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


################################################################
import json


class JsonSerializableMixin(json.JSONEncoder):

    def default(self, obj):
        return obj.__dict__

    def to_json(self):
        return json.dumps(self, cls=JsonSerializableMixin)


# Класс JsonSerializableMixin является подклассом json.JSONEncoder, который обеспечивает сериализацию объектов в формат
# JSON.Метод default(self, obj) определен в классе JsonSerializableMixin. Он вызывается при сериализации объекта и
# возвращает словарь (obj.__dict__) содержащий все атрибуты объекта. Это позволяет преобразовать объект Python в
# JSON-совместимый словарь.Метод to_json(self) также определен в JsonSerializableMixin. Он использует json.dumps()
# для сериализации текущего объекта в строку JSON. Параметр cls=JsonSerializableMixin указывает, что при сериализации
# должен использоваться метод default() из этого класса.Таким образом, когда вызывается метод to_json() объекта, он
# будет преобразован в JSON-строку с помощью json.dumps(), а метод default() будет использоваться для преобразования
# атрибутов объекта в словарь.
#########################################################################
class JsonSerializableMixin:

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda x: x.__dict__)


json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None,
           indent=None, separators=None, default=None, sort_keys=False, **kw)


# #obj - объект Python,
# skipkeys=False - игнорирование неизвестных типов ключей в словарях,
# ensure_ascii=True - экранирование не-ASCII символов,
# check_circular=True - проверка циклических ссылок,
# allow_nan=True - представление значений nan, inf, -inf в JSON,
# cls=None - метод, для сериализации дополнительных типов,
# indent=None - количество отступов при сериализации,
# separators=None - разделители используемые в JSON,
# default=None - функция для объектов, которые не могут быть сериализованы,
# sort_keys=False - сортировка словарей.

# json.dumps - это функция, предоставляемая модулем json, которая преобразует объект Python в строку в формате JSON.
# self.__dict__ получает словарь атрибутов текущего объекта. Он содержит все имена атрибутов в качестве ключей и их
# соответствующие значения.Параметр default функции json.dumps определяет функцию, которая будет использоваться для
# преобразования несериализуемых объектов, с которыми встречается процесс сериализации. В данном случае используется
# лямбда-функция lambda x: x.__dict__. Эта лямбда-функция возвращает словарь атрибутов несериализуемого объекта.
# Путем передачи self.__dict__ и функции по умолчанию в json.dumps, объект сериализуется в строку в формате JSON.
##################################################################
class JsonSerializableMixin:

    def __repr__(self):
        return str(self.__dict__)

    def to_json(self):
        return json.dumps(eval(self.__repr__()))


################################################################\
class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self, default=vars)


# В контексте данного кода, default=vars является аргументом функции json.dumps(). Он определяет функцию, которая будет
# вызываться для сериализации объектов, которые не могут быть сериализованы стандартным способом.В данном случае,
# default=vars указывает на функцию vars(), которая возвращает словарь, содержащий атрибуты объекта. То есть, если
# объект не может быть прямо сериализован, json.dumps() будет использовать vars() для получения словаря его атрибутов,
# который затем будет сериализован в формат JSON.
####################################################################
# без import json
class JsonSerializableMixin:
    def to_json(self):
        return __import__('json').dumps(self.__dict__, default=lambda x: x.__dict__)


######################
# Подвиг 8 (введение в паттерн миксинов - mixins). Часто множественное наследование используют для наполнения
# дочернего класса определенным функционалом. То есть, с указанием каждого нового базового класса, дочерний класс
# приобретает все больше и больше возможностей. И, наоборот, убирая часть базовых классов, дочерний класс теряет
# соответствующую часть функционала. Например, паттерн миксинов активно используют в популярном фреймворке Django.
# В частности, когда нужно указать дочернему классу, какие запросы от клиента он должен обрабатывать
# (запросы типа GET, POST, PUT, DELETE и т.п.). В качестве примера реализуем эту идею в очень упрощенном виде, но
# сохраняя суть паттерна миксинов.

class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# Здесь в каждом классе выполняется имитация обработки запросов. За GET-запрос отвечает метод get() класса RetriveMixin,
# за POST-запрос - метод post() класса CreateMixin, за PUT-запрос - метод put() класса UpdateMixin.
# Далее, вам нужно объявить класс с именем GeneralView, в котором следует указать атрибут (на уровне класса):
allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')  # для перечня разрешенных запросов. А также объявить метод


# render_request со следующей сигнатурой:
def render_request(self, request): ...


# Здесь request - это словарь (объект запроса), в котором обязательно должны быть два ключа:
# 'url' - адрес для обработки запроса; 'method' - метод запроса: 'GET', 'POST', 'PUT', 'DELETE' и т. д.
# В методе render_request() нужно сначала проверить, является ли указанный запрос в словаре request разрешенным
# (присутствует в списке allowed_methods). И если это не так, то генерировать исключение командой:
# raise TypeError(f"Метод {request.get('method')} не разрешен.") Иначе, вызвать метод по его имени:
# method_request = request.get('method').lower()  # имя метода, малыми буквами Подсказка: чтобы получить ссылку на
# метод с именем method_request, воспользуйтесь магическим методом __getattribute__().Для использования полученных
# классов, в программе объявляется следующий дочерний класс:
class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT',)


# Воспользоваться им можно, например, следующим образом (эти строчки в программе не писать):
view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
print(html)  # GET: https://stepik.org/course/116336/
# Если в запросе указать другой метод:
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})


# то естественным образом возникнет исключение (реализовывать в программе не нужно, это уже встроено в сам язык Python):
# AttributeError: 'DetailView' object has no attribute 'put'
# так как дочерний класс DetailView не имеет метода put. Поправить это можно, если указать соответствующий базовый класс:
class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT',)


# Теперь, при выполнении команд:
view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html)


# будет выведено:
# PUT: https: // stepik.org / course / 116336 /  # Это и есть принцип работы паттерна миксинов.

class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        # url' - адрес для обработки запроса; 'method' - метод запроса: 'GET', 'POST', 'PUT', 'DELETE' и
        if request.get('method') not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method_request = request.get('method').lower()
        return self.__getattribute__(method_request)(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT',)


view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html)


################################################################
class GeneralView:
    # allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if request.get('method') not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method_request = request.get('method').lower()  # 'get'
        # return self.__getattribute__(method_request)(request)
        try:
            method = getattr(self, method_request)  # обращение к атрибуту класса get ->def get(self, request):
            return method(request)
        except AttributeError:
            raise AttributeError(f"'{self.__class__.__name__}' object has not attribute")


################################################################
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')  # на случай если нет классе DetailView

    def render_request(self, request):
        method = request.get('method').upper()
        if method not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method_request = self.__getattribute__(method.lower())  # 'get'
        # method_request = getattr(self, method.lower())
        if method_request:
            return method_request(request)


################################################################
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method = request.get('method').upper()
        method_request = super().__getattribute__(method.lower())
        if method_request:
            return method_request(request)


################################################################
# Подвиг 9. Объявите класс с именем Money (деньги), объекты которого создаются командой:
# money = Money(value)где value - любое число (целое или вещественное). Если указывается не числовое значение, то
# генерируется исключение командой:raise TypeError('сумма должна быть числом')В каждом объекте этого класса должен
# формироваться локальный атрибут _money с соответствующим значением. Также в классе Money должно быть объект-свойство
# (property):money - для записи и считывания значения из атрибута _money.В связке с классом Money работает еще
# один класс:# class MoneyOperators:
# Он определяет работу арифметических операторов. В данном примере описан алгоритм сложения двух объектов класса Money
# (или объектов его дочерних классов).Обратите внимание, как реализован метод __add__() в этом классе. Он универсален
# при работе с любыми объектами класса Money или его дочерних классов. Здесь атрибут __class__ - это ссылка на
# класс объекта self. С помощью __class__ можно создавать объекты того же класса, что и self.
# Вам необходимо добавить в класс MoneyOperators аналогичную реализацию оператора вычитания.На основе двух классов
# (Money и MoneyOperators) предполагается создавать классы кошельков разных валют. Например, так:

class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)  # __class__ можно создавать объекты того же класса, что и self.

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)
        if type(other) != type(other):
            raise TypeError('Разные типы объектов')
        return self.__class__(self.money - other.money)


class Money:
    def __init__(self, money):
        self.money = money

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        if type(money) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self._money = money


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
m = m1 + m2  # TypeError

################################################################
from operator import add, sub
from typing import Callable, Union


class Money:
    def __init__(self, value: Union[int, float]) -> None:
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self.money = value

    money = property(lambda self: self._money)

    @money.setter
    def money(self, value: Union[int, float]) -> None:
        self._money = value

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.money}"


class MoneyOperators:
    def __op(self, other: Union[int, float, Money], op: Callable) -> Money:
        if type(other) in (int, float):
            return self.__class__(op(self.money, other))

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(op(self.money, other.money))

    def __add__(self, other: Union[int, float, Money]) -> Money:
        return self.__op(other, add)

    def __sub__(self, other: Union[int, float, Money]) -> Money:
        return self.__op(other, sub)


class MoneyR(Money, MoneyOperators): ...


class MoneyD(Money, MoneyOperators): ...


m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
m = m1 + m2  # TypeError

################################################################
from operator import add, sub


class MoneyOperators:
    def _operate(self, other, oper):
        if type(other) in (int, float):
            return self.__class__(oper(self.money, other))

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(oper(self.money, other.money))

    def __add__(self, other):
        return self._operate(other, add)

    def __sub__(self, other):
        return self._operate(other, sub)


class Money:
    def __init__(self, value):
        self.money = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('сумма должна быть числом')
        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


################################################################
class MoneyOperators:

    def get_other(self, other):
        if type(other) in (int, float):
            return other

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')
        return other.money

    def __add__(self, other):
        other = self.get_other(other)
        return self.__class__(self.money + other)

    def __sub__(self, other):
        other = self.get_other(other)
        return self.__class__(self.money - other)

    def __radd__(self, other):
        other = self.get_other(other)
        return self + other

    def __rsub__(self, other):
        other = self.get_other(other)
        return self.__class__(other - self.money)


class Money:
    __slots__ = '_money'

    def __init__(self, money):
        self.money = money

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError('Cумма должна быть числом')
        object.__setattr__(self, key, value)

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value


################################################################
# __4.9 Slots__Egorof___
# После указания __slots__ добавление новых атрибутов в экземпляр класса, кроме уже указанных, невозможно
class PointSlots:
    __slots__ = ('x', 'y')  # Перечисляем все возможные атрибуты экземпляров класса

    def __init__(self, x, y):
        self.x = x
        self.y = y


p2 = PointSlots(3, 4)
p2.new_attr = 10  # AttributeError: 'PointSlots' object has no attribute 'new_attr'


# Также при использовании __slots__ пропадает возможность получить словарь __dict__ с атрибутами

class PointSlots:
    __slots__ = ('x', 'y')  # Перечисляем все возможные атрибуты экземпляров класса

    def __init__(self, x, y):
        self.x = x
        self.y = y


p2 = PointSlots(3, 4)
print(p2.__dict__)  # AttributeError: 'PointSlots' object has no attribute '__dict__'
# 2. Скорость работы программы
# Используемая коллекция для хранения имён переменных в __slots__ позволяет ускорить работу программы по сравнению с
# используемым по умолчанию словарём (__dict__ ). Замерим время работы программы с помощью модуля timeit:

from timeit import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_time_point():
    p1 = Point(3, 4)
    p1.x = 100
    p1.x
    del p1.x


def test_time_pointslots():
    p1 = PointSlots(3, 4)
    p1.x = 100
    p1.x
    del p1.x


print('No __slots__ stopped:', timeit(test_time_point))
print('__slots__ stopped:', timeit(test_time_pointslots))


# Вывод:# No __slots__ stopped: 1.048502679914236
# __slots__ stopped: 0.9827403570525348# Использование __slots__ позволяет уменьшить время работы программы.
# # Использование памяти
# Уменьшение количества занимаемой памяти при использовании __slots__ связано с тем, что в __slots__ хранятся только
# значения из пространства имён, а при использовании __dict__ в память добавляется размер коллекции __dict__ :

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Point(3, 4)
print('No slots:', s.__sizeof__(), s.__dict__.__sizeof__())  # No slots: 32 88
d = PointSlots(3, 4)
print('Slots', d.__sizeof__())  # Slots 32


# Экземпляр класса, использующий __slots__ снижает количество используемой памяти,# так как содержит только
# пространство имён объекта.# # Таким образом использовать __slots__ важно в тех случаях, когда:
# Есть необходимость в фиксированном количестве используемых имён переменных в объектах.
# Необходимо ускорение работы программы.# Имеются ограничения по объему используемой памяти.
################################################################
class Phone:
    __slots__ = ['brand', 'model', '__dict__']


phone1 = Phone()
phone1.brand = 'Apple'
phone1.model = 'iPhone 14'

print(phone1.brand)  # Apple
print(phone1.model)  # iPhone 14
phone1.price = 1000
print(phone1.price)  # 1000


################################################################
class Person:
    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"


################################################################
# Есть еще одно интересное свойство. Если мы хотим расширить все-таки наш класс, и предоставить возможность добавлять
# аттрибуты, то в слотс можно добавить атрибут __dict__. Тогда при создании нового атрибута он будет заноситься в этот
# словарь. Гибридная структура т.с.

class Example:
    __slots__ = 'x', 'y', '__dict__'

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


p = Example(1, 2)
p.z = 5
print(p.z)  # выводит 5
print(p.__dict__)  # выводит {'z': 5}


################################################################
class Good:
    __slots__ = ['_price']

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value * 2


obj = Good(5)
print(obj.price)  # 5
obj.price = 10
print(obj.price)  # 20


# obj = Good(5)  # Здесь _price задается напрямую в методе __init__, а не через сеттер. Поэтому значение не удваивается.
# Вот здесь обратите внимание, что _price с подчеркиванием, то есть это не сеттер:
# def __init__(self, price): self._price = price

################################################################
# Вы работаете над проектом управления устройствами в доме. Вам нужно создать иерархию классов для различных типов
# устройств и реализовать методы для управления ими. В качестве части проекта, вам нужно использовать механизмы slots
# и property для определения и защиты атрибутов классов.Создайте класс Device, который будет служить базовым классом
# для всех устройств в доме. Класс "Device" должен иметь "slots" для защищенных атрибутов "_name", "_location" и
# "_status"(по умолчанию ON). Для атрибут "_name" создайте свойство только для чтения, а для атрибутов "_location" и
# "_status" - свойства для чтения и записи. Добавьте метод "turn_on" для изменения статуса устройства на "ON" и метод
# "turn_off" для изменения статуса на "OFF".Создайте класс Light, который будет наследоваться от класса "Device" и
# представлять устройства освещения. Для этого определите слоты для атрибутов "_brightness" и "_color". Для атрибута
# "_brightness" создайте свойство для чтения и записи, а для атрибута "_color" - только для чтения. Создайте класс
# Thermostat, который будет наследоваться от класса "Device" и представлять устройства управления температурой. В
# классе Thermostat определите слоты для атрибутов "_current_temperature" и "_target_temperature". Оба атрибута должны
# управляться свойствами для чтения и записи.Создайте класс SmartTV, который будет наследоваться от класса "Device"
# и представлять устройства для просмотра телевизионных каналов. В классе SmartTV определите слоты для атрибута
# "_channel". Создайте свойства для управления чтением и записью атрибута _channel.
class Data_Desc:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class None_Data_Desc:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Device:
    __slots__ = "_name", "_location", "_status"
    name = None_Data_Desc()
    location = Data_Desc()
    status = Data_Desc()

    def __init__(self, name, location):
        self._name = name
        self.location = location
        self.status = 'ON'

    def turn_on(self):
        self.status = 'ON'

    def turn_off(self):
        self.status = 'OFF'


class Light(Device):
    __slots__ = "_brightness", "_color"
    brightness = Data_Desc()
    color = None_Data_Desc()

    def __init__(self, name, location, brightness, color):
        super().__init__(name, location)
        self.brightness = brightness
        self._color = color


class Thermostat(Device):
    __slots__ = "_current_temperature", "_target_temperature"
    current_temperature = Data_Desc()
    target_temperature = Data_Desc()

    def __init__(self, name, location, current_temperature, target_temperature):
        super().__init__(name, location)
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature


class SmartTV(Device):
    __slots__ = '_channel'
    channel = Data_Desc()

    def __init__(self, name, location, channel):
        super().__init__(name, location)
        self.channel = channel


################################################################
class Value:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Device:
    __slots__ = "_name", "_location", "_status"
    location, status = Value(), Value()

    def __init__(self, *args):
        self._name, self.location, self.status = (*args, 'ON')

    def turn_on(self):
        self.status = 'ON'

    def turn_off(self):
        self.status = 'OFF'

    @property
    def name(self):
        return self._name


class Light(Device):
    __slots__ = "_brightness", "_color"
    brightness = Value()

    def __init__(self, *args):
        super().__init__(*args[:2])
        self.brightness, self._color = args[2:]

    @property
    def color(self):
        return self._color


class Thermostat(Device):
    __slots__ = "_current_temperature", "_target_temperature"
    current_temperature, target_temperature = Value(), Value()

    def __init__(self, *args):
        super().__init__(*args[:2])
        self.current_temperature, self.target_temperature = args[2:]


class SmartTV(Device):
    __slots__ = "_channel"
    channel = Value()

    def __init__(self, *args):
        super().__init__(*args[:2])
        self.channel = args[2]


################################################################
# __4.7 Коллекция __slots_____Balakirev

pt1.__sizeof__() + pt1.__dict__.__sizeof__()  # 120
# если убрать __dict__ тоже весит 32.

pt2.__sizeof__()  # 32


# __slots__ имеет такой же id, что и в самом классе, значит, это атрибут уровня класса
# А __slots__  в pt2 весит 40 сам по себе.  Вот тут я что-то засомневался. Он не занимает память когда не вызывается или как?
################################################################
# Если колекция __slots__ есть в базовом или в дочернем классе, то свойства с именем, которые не указаны в __slots__
# попадут в колекцию __dict__, а не вызовут ошибку как в случае, если __slots__ есть и в дочернем и базовом классе

class A:
    pass


class B(A):
    __slots__ = ('c', 'd')

    def __init__(self, c, d):
        self.c = c
        self.d = d


b = B(3, 5)
b.a = 8
print(b.__slots__, b.__dict__)  # ('c', 'd') {'a': 8}
print(b.a, b.c)  # 8 3


# Аналогично, если __slots__ в базовом классе:

class A:
    __slots__ = ('c', 'd')


class B(A):
    def __init__(self, c, d):
        self.c = c
        self.d = d


b = B(3, 5)
b.a = 8
print(b.__slots__, b.__dict__)  # ('c', 'd') {'a': 8}
print(b.a, b.c)  # 8 3


# __slots__ = ('c', 'd') in A and B
class A:
    __slots__ = ('c', 'd')


class B(A):
    __slots__ = ('c', 'd')

    def __init__(self, c, d):
        self.c = c
        self.d = d


b = B(3, 5)
b.a = 8  # AttributeError: 'B' object has no attribute 'a'


################################################################
class Money:
    __slots__ = '_money',

    def __init__(self, value):
        self._money = value


class MoneyR(Money):
    pass


m = MoneyR(10)
m.s = 100
print(m.s)  # 100


# коллекция __slots__ накладывает ограничения на атрибуты объектов базового класса Money, но не дочернего класса MoneyR
# программа выполнится без ошибок, т.к. коллекция __slots__ отсутствует в классе MoneyR, то в его объектах можно
# создавать любые локальные атрибуты
################################################################
class Money:
    __slots__ = '_money',

    def __init__(self, value):
        self._money = value


class MoneyR(Money):
    __slots__ = '_value',


m = MoneyR(10)
m._money = 100
m._value = 20


# если в классе MoneyR прописать __slots__ = '_value', '_money', а в базовом классе убрать определение __slots__, то
# поведение объекта m дочернего класса MoneyR не изменится
# программа выполнится без ошибок, так как коллекция __slots__ дочернего класса расширяет коллекцию __slots__ базового
# класса и атрибуты с именами _money и _value допустимы
################################################################
# Подвиг 4. Объявите класс Person, в объектах которого разрешены только локальные атрибуты с именами (ограничение
# задается через коллекцию __slots__):_fio - ФИО сотрудника (строка);_old - возраст сотрудника (целое положительное
# число);_job - занимаемая должность (строка).Сами объекты должны создаваться командой:p = Person(fio, old, job)
# Создайте несколько следующих объектов этого класса с информацией:Суворов, 52, полководец
# Рахманинов, 50, пианист, композитор
# Балакирев, 34, программист и преподаватель
# Пушкин, 32, поэт и писатель
# Сохраните все эти объекты в виде списка с именем persons.
class Person:
    __slots__ = '_fio', '_job', '_old'

    def __init__(self, fio, old, job):
        self._fio = fio
        self._job = job
        self._old = old


text = 'Суворов, 52, полководец\n' \
       'Рахманинов, 50, пианист, композитор\n' \
       'Балакирев, 34, программист и преподаватель\n' \
       'Пушкин, 32, поэт и писатель'

persons = [Person(i, v, k) for i, v, *k in map(lambda x: x.split(','), text.split('\n'))]
persons = [Person(i[0], i[1], i[1:]) for i in map(lambda x: x.split(','), text.split('\n'))]
persons = [Person(*i) for i in map(lambda x: x.split(', ', maxsplit=2), text.splitlines())]
# str.splitlines() делит текст по символу '\n'
persons = [Person(*x.split(", ", maxsplit=2)) for x in text.splitlines()]
persons = [*map(lambda row: Person(*row.split(', ', 2)), text.split('\n'))]
print(persons)  # [<__main__.Person object at 0x000


################################################################
class Person:
    __slots__ = "_fio", "_old", "_job"

    def __init__(self, *args):
        for i, j in enumerate(self.__slots__):
            self.__setattr__(j, args[i])


################################################################
# Подвиг 5. Объявите класс Planet (планета), объекты которого создаются командой:
# p = Planet(name, diametr, period_solar, period)где name - наименование планеты; diametr - диаметр планеты
# (любое положительное число); period_solar - период (время) обращения планеты вокруг Солнца
# (любое положительное число); period - период обращения планеты вокруг своей оси (любое положительное число).
# В каждом объекте класса Planet должны формироваться локальные атрибуты с именами: _name, _diametr, _period_solar,
# _period и соответствующими значениями.Затем, объявите класс с именем SolarSystem (солнечная система).
# В объектах этого класса должны быть допустимы, следующие локальные атрибуты
# (ограничение задается через коллекцию __slots__):_mercury - ссылка на планету Меркурий (объект класса Planet);
# _venus - ссылка на планету Венера (объект класса Planet);_earth - ссылка на планету Земля (объект класса Planet);.....
# Объект класса SolarSystem должен создаваться командой:s_system = SolarSystem()и быть только один (одновременно в
# программе два и более объектов класса SolarSystem недопустимо). Используйте для этого паттерн Singleton.
# В момент создания объекта SolarSystem должны автоматически создаваться перечисленные локальные атрибуты и
# ссылаться на соответствующие объекты класса Planet со следующими данными по планетам:
# Создайте в программе объект s_system класса SolarSystem
class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._period = period
        self._diametr = diametr
        self._period_solar = period_solar


class SolarSystem:
    __slots__ = '_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune'
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)


s_system = SolarSystem()

################################################################
task = """_mercury - ссылка на планету Меркурий (объект класса Planet);
_venus - ссылка на планету Венера (объект класса Planet);
_earth - ссылка на планету Земля (объект класса Planet);
_mars - ссылка на планету Марс (объект класса Planet);
_jupiter - ссылка на планету Юпитер (объект класса Planet);
_saturn - ссылка на планету Сатурн (объект класса Planet);
_uranus - ссылка на планету Уран (объект класса Planet);
_neptune - ссылка на планету Нептун (объект класса Planet).""".splitlines()


class SolarSystem:
    __instance = None
    __slots__ = tuple([a.split(' - ')[0] for a in task])


################################################################
# Подвиг 6. Объявите класс с именем Star (звезда), в объектах которого разрешены только локальные атрибуты с именами
# (ограничение задается через коллекцию __slots__):_name - название звезды (строка);
# _massa - масса звезды (любое положительное число); часто измеряется в массах Солнца;
# _temp - температура поверхности звезды в Кельвинах (любое положительное число).Объекты этого класса должны
# создаваться командой:star = Star(name, massa, temp)На основе класса Star объявите следующие дочерние классы:
# WhiteDwarf - белый карлик;YellowDwarf - желтый карлик;RedGiant - красный гигант;Pulsar - пульсар.
# В каждом объекте этих классов должны быть разрешены (дополнительно к атрибутам базового класса Star)
# только следующие локальные атрибуты:_type_star - название типа звезды (строка);_radius - радиус звезды
# (любое положительное число); часто измеряется в радиусах Солнца.Соответственно, объекты этих классов должны
# создаваться командой:star = Имя_дочернего_класса(name, massa, temp, type_star, radius)Создайте в программе
# следующие объекты звезд:RedGiant: Альдебаран; 5; 3600; красный гигант; 45
# WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
# WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
# YellowDwarf: Солнце; 1; 6000; желтый карлик; 1Все эти объекты сохраните в виде списка stars. Затем, с помощью
# функций isinstance() и filter() сформируйте новый список с именем white_dwarfs, состоящий только из белых карликов
# (WhiteDwarf).
class Star:
    __slots__ = '_name', '_massa', '_temp'

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class WhiteDwarf(Star):
    __slots__ = '_type_star', '_radius'

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class YellowDwarf(Star):
    __slots__ = '_type_star', '_radius'

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class RedGiant(Star):
    __slots__ = '_type_star', '_radius'

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class Pulsar(Star):
    __slots__ = '_type_star', '_radius'

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


str_in = """RedGiant: Альдебаран; 5; 3600; красный гигант; 45
WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
YellowDwarf: Солнце; 1; 6000; желтый карлик; 1"""

stars = [globals()[i[0]](*i[1].split('; ')) for line in str_in.splitlines() for i in [line.split(': ')]]
print(stars)  # [<__main__.RedGiant object at 0x0000018E8CAAB240>, <_...
white_dwarfs = [*filter(lambda x: isinstance(x, WhiteDwarf), stars)]
print(white_dwarfs)  # [<__main__.WhiteDwarf object at 0x000001...
################################################################
gen = (line.split(': ') for line in str_in.splitlines())
stars = [globals()[i[0]](*i[1].split('; ')) for i in gen]
################################################################
stars = []
for el in task2:
    cls_name, cls_args = el.split(': ')
    stars.append(globals()[cls_name](*cls_args.split('; ')))

white_dwarfs = [wd for wd in stars if isinstance(wd, WhiteDwarf)]


################################################################
class Star:
    __slots__ = '_name', '_massa', '_temp'

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class Basicstars(Star):
    __slots__ = '_type_star', '_radius'

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class WhiteDwarf(Basicstars):    __slots__ = ()


class YellowDwarf(Basicstars):    __slots__ = ()


class RedGiant(Basicstars):    __slots__ = ()


class Pulsar(Basicstars):    __slots__ = ()


str_in = """RedGiant: Альдебаран; 5; 3600; красный гигант; 45
WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
YellowDwarf: Солнце; 1; 6000; желтый карлик; 1"""


def parse(line):
    cls, data = line.split(': ')
    return eval(f'{cls}(*{data.split("; ")})')
    # return globals()[cls](*data.split("; "))


stars = [*map(parse, str_in.splitlines())]
white_dwarfs = [*filter(lambda x: isinstance(x, WhiteDwarf), stars)]

################################################################
from itertools import starmap


class Star:
    __slots__ = '_name', '_massa', '_temp'

    def __init__(self, *args):
        [setattr(self, attr, value) for attr, value in zip(self.__slots__, args)]


class WhiteDwarf(Star):
    __slots__ = '_type_star', '_radius'

    def __init__(self, *args):
        super().__init__(args[:3])
        [setattr(self, attr, value) for attr, value in zip(self.__slots__, args[3:])]


class Pulsar(WhiteDwarf):
    __slots__ = ()


class YellowDwarf(WhiteDwarf):
    __slots__ = ()


class RedGiant(WhiteDwarf):
    __slots__ = ()


text = """RedGiant: Альдебаран; 5; 3600; красный гигант; 45
WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
YellowDwarf: Солнце; 1; 6000; желтый карлик; 1"""
stars = map(lambda line: line.split(': '), text.split('\n'))
stars = [*starmap(lambda cls, args: globals()[cls](*args.split('; ')), stars)]
# itertools.starmap(function, iterable) - Применить функцию для каждого кортежа из списка кортежей
white_dwarfs = [*filter(lambda obj: type(obj) == WhiteDwarf, stars)]


################################################################
# Подвиг 7. Объявите класс Note (нота), объекты которого создаются командой:
# note = Note(name, ton)где name - название ноты (допустимые значения: до, ре, ми, фа, соль, ля, си); ton - тональность
# ноты (целое число). Тональность (ton) принимает следующие целые значения:-1 - бемоль (flat);0 - обычная нота (normal);
# 1 - диез (sharp).Если в названии (name) или тональности (ton) передаются недопустимые значения, то генерируется
# исключение командой:raise ValueError('недопустимое значение аргумента')В каждом объекте класса Note должны
# формироваться локальные атрибуты с именами _name и _ton с соответствующими значениями.Объявите класс с именем Notes,
# в объектах которого разрешены только локальные атрибуты с именами (ограничение задается через коллекцию __slots__):
# _do - ссылка на ноту до (объект класса Note);_re - ссылка на ноту ре (объект класса Note);_mi - ссылка на ноту ми
# (объект класса Note);_fa - ссылка на ноту фа (объект класса Note);_solt - ссылка на ноту соль (объект класса Note);
# _la - ссылка на ноту ля (объект класса Note);_si - ссылка на ноту си (объект класса Note).Объект класса Notes должен
# создаваться командой:notes = Notes()и быть только один (одновременно в программе два и более объектов класса
# Notes недопустимо). Используйте для этого паттерн Singleton. В момент создания объекта Notes должны автоматически
# создаваться перечисленные локальные атрибуты и ссылаться на соответствующие объекты класса Note (тональность (ton)
# у всех нот изначально равна 0).Обеспечить возможность обращения к нотам по индексам: 0 - до; 1 - ре; ... ; 6 - си.
# Например:nota = notes[2]  # ссылка на ноту ми notes[3]._ton = -1 # изменение тональности ноты фа Если указывается
# недопустимый индекс (не целое число, или число, выходящее за интервал [0; 6]), то генерируется исключение командой:
# raise IndexError('недопустимый индекс')
class Note:
    __сyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            if value not in self.__сyrillic_notes:
                raise ValueError('недопустимое значение аргумента')
        if key == '_ton':
            if value not in (0, 1, -1):
                raise ValueError('недопустимое значение аргумента')
        super().__setattr__(key, value)
        # object.__setattr__(self, key, value)

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, value):
    #     if value not in self.__сyrillic_notes:
    #         raise ValueError('недопустимое значение аргумента')
    #     self._name = value
    #
    # @property
    # def ton(self):
    #     return self._ton
    #
    # @ton.setter
    # def ton(self, value):
    #     if value not in [0, 1]:
    #         raise ValueError('недопустимое значение аргумента')
    #     self._ton = value


class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    __сyrillic_notes = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __del__(self):
        Notes.__instance = None

    def __init__(self):
        for k, v in zip(self.__slots__, self.__сyrillic_notes):
            setattr(self, k, Note(v, 0))
        # self._do = Note('до', ton=0)
        # self._re = Note('ре', ton=0)
        # self._mi = Note('ми', ton=0)
        # self._fa = Note('фа', ton=0)
        # self._solt = Note('соль', ton=0)
        # self._la = Note('ля', ton=0)
        # self._si = Note('си', ton=0)

    def __getitem__(self, key):
        if not (0 <= key <= 6):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[key])

    def __setitem__(self, key, value):
        if 0 >= value >= 6 or type(value) != int:
            raise IndexError('недопустимый индекс')
        setattr(self, self.__slots__[key], value)


notes = Notes()

print(notes)  # <__main__.Notes object at ........
print(notes.__dir__())  # ['__module__', '__slots__', '_Notes__сyrillic...
print(notes.__slots__)  # ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
nota = notes[2]
print(nota._ton)
notes[3]._ton = -1
print(notes[3]._ton)


################################################################
class Note:
    __slots__ = '_name', '_ton'

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in ("до", "ре", "ми", "фа", "соль", "ля", "си"):
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        for attr, note in zip(self.__slots__, ("до", "ре", "ми", "фа", "соль", "ля", "си")):
            object.__setattr__(self, attr, Note(note, 0))

    def __getitem__(self, item):
        if item not in range(0, 7):
            raise IndexError('недопустимый индекс')
        return object.__getattribute__(self, self.__slots__[item])

    def __del__(self):
        self.__class__._instance = None


################################################################
class Note:
    note_names = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    note_tones = (-1, 0, 1)

    def __init__(self, *args):
        self._name, self._ton = args

    def __setattr__(self, name, v):
        if name == '_name' and v in self.note_names or name == '_ton' and v in self.note_tones:
            return super().__setattr__(name, v)
        raise ValueError('недопустимое значение аргумента')


class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'

    # Если нет __init__, он не будет зваться при каждом Notes()
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super().__new__(cls)
            for var, name in zip(cls.__slots__, Note.note_names):
                setattr(cls.__instance, var, Note(name, 0))
        return cls.__instance

    def __getitem__(self, key):
        if 0 <= key < len(self.__slots__):
            return getattr(self, self.__slots__[key])
        raise IndexError('недопустимый индекс')


################################################################
NOTES = {'do': 'до', 're': 'ре', 'mi': 'ми', 'fa': 'фа', 'solt': 'соль', 'la': 'ля', 'si': 'си'}


class Note:
    __slots__ = ('_name', '_ton')

    def __init__(self, name, ton):
        self._name, self._ton = name, ton

    def __setattr__(self, key, value):
        if value not in {'_name': set(NOTES.values()), '_ton': {-1, 0, 1}}.get(key, []):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __obj = None
    __slots__ = tuple(f'_{k}' for k in NOTES)

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self):
        for k, v in NOTES.items():
            setattr(self, f'_{k}', Note(v, 0))

    def __getitem__(self, item):
        return getattr(self, self.__slots__[item])


################################################################
class Note:
    __slots__ = '_name', '_ton'
    __names__ = 'до,ре,ми,фа,соль,ля,си'.split(',')

    def __init__(self, *args):
        [setattr(self, attr, value) for attr, value in zip(self.__slots__, args)]

    def __setattr__(self, attr, value):
        if value not in {'_name': self.__names__, '_ton': (-1, 0, 1)}.get(attr):
            raise ValueError('недопустимое значение аргумента')
        super().__setattr__(attr, value)


class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        [setattr(self, a, Note(n, 0)) for a, n in zip(self.__slots__, Note.__names__)]

    def __getitem__(self, key):
        if key not in range(7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[key])


################################################################
# Подвиг 8 (на повторение). В программе объявлен базовый класс Function (функция) следующим образом: class Function:...
# Здесь в инициализаторе создаются два локальных атрибута:_amplitude - амплитуда функции;_bias - смещение функции
# по оси ординат (Oy).Далее, в методе __call__() берется значение функции в точке x через метод _get_function(),
# который должен быть определен в дочерних классах, умножается на амплитуду функции и добавляется ее смещение.
# Следующий метод __add__() позволяет менять смещение функции, изменяя атрибут _bias на указанное значение other.
# Обратите внимание, в методе __add__() происходит создание нового объекта командой:obj = self.__class__(self)
# Здесь __class__ - это ссылка на класс, к которому относится объект self. Благодаря этому в базовом классе можно
# создавать объекты соответствующих дочерних классов. В момент создания объекта ему передается параметр self как
# аргумент. Так будет создаваться копия объекта, т.е. новый объект с тем же набором и значениями локальных атрибутов.
# Чтобы обеспечить этот функционал, объявите дочерний класс с именем Linear (линейная функция y = k*x + b), объекты
# которого должны создаваться командами:obj = Linear(k, b)linear = Linear(obj)  # этот вариант используется в
# базовом классе в методе __add__()В первом случае происходит создание объекта линейной функции с параметрами k и b.
# Во втором - создание объекта со значениями параметров k и b, взятыми из объекта obj.В каждом объекте класса Linear
# должны создаваться локальные атрибуты с именами _k и _b с соответствующими значениями.В результате будет создан
# универсальный базовый класс Function для работы с произвольными функциями от одного аргумента.Применять эти классы
# можно следующим образом (эти строчки в программе писать не нужно):f = Linear(1, 0.5)
# Пропишите в базовом классе Function еще один магический метод для изменения масштаба (амплитуды) функции, чтобы
# был доступен оператор умножения:f = Linear(1, 0.5)
class Function:
    def __init__(self):
        self._amplitude = 1.0  # амплитуда функции
        self._bias = 0.0  # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')
        # __class__ - это ссылка на класс, к которому относится объект self. Благодаря этому в базовом классе можно
        # создавать объекты соответствующих дочерних классов. В момент создания объекта ему передается параметр self
        # как аргумент. Так будет создаваться копия объекта, т.е. новый объект с тем же набором и значениями локальных
        # атрибутов.
        obj = self.__class__(self)
        obj._bias = self._bias + other  # 0+10=10
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')
        obj = self.__class__(self)
        # obj = __import__('copy').deepcopy(self)
        obj._amplitude *= other
        return obj


class Linear(Function):
    def __init__(self, *args):
        super().__init__()
        if isinstance(args[0], self.__class__):
            self._k = args[0]._k
            self._b = args[0]._b
        else:
            self._k = args[0]
            self._b = args[1]

    def _get_function(self, x):
        return self._k * x + self._b


f = Linear(1, 0.5)
f2 = f + 10  # изменение смещения (атрибут _bias)
# print(f2)  # self._bias 0+10=10
y1 = f(0)  # 0.5
print(y1)  # 0.5
y2 = f2(0)  # 10.5
print(y2)
f = Linear(1, 0.5)
f2 = f * 5  # изменение амплитуды (атрибут _amplitude)
y1 = f(0)  # 0.5
y2 = f2(0)  # 2.5
print(y2)


####################################################################
class Linear(Function):

    # в этом инициализаторе надо предусмотреть, что на вход может подаваться либо два числа
    # либо экземпляр класса, из которого надо выудить эти два числа
    def __init__(self, *args):
        super().__init__()
        if isinstance(args[0], self.__class__):
            self._k = args[0]._k
            self._b = args[0]._b
        else:
            self._k = args[0]
            self._b = args[1]


################################################################
class Linear(Function):
    def __init__(self, *args):
        super().__init__()
        if len(args) == 2 and type(args[0]) in (int, float) and type(args[1]) in (int, float):
            self._k = args[0]
            self._b = args[1]

        elif type(args[0]) == Linear:
            self._k = args[0]._k
            self._b = args[0]._b


################################################################
class Linear(Function):
    def __init__(self, *args):
        super().__init__()
        try:
            self._k = args[0]
            self._b = args[1]
        except AttributeError:
            self._k = args[0]._k
            self._b = args[0]._b


################################################################
class Function:
    def __init__(self):
        self._amplitude = 1.0  # амплитуда функции
        self._bias = 0.0  # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)  # без self.__class__(self._k, self._b)!!
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')
        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj


class Linear(Function):
    def __init__(self, *args):
        super().__init__()
        self._k, self._b = args if len(args) > 1 else (args[0]._k, args[0]._b)

    def _get_function(self, x):
        return self._k * x + self._b


################################################################
class Shop:
    ID_SHOP_ITEM = 0


sp = Shop()
sp.ID_SHOP_ITEM += 1
print(Shop.ID_SHOP_ITEM)  # 0
# в строчке sp.ID_SHOP_ITEM += 1 создается новая локальная переменная ID_SHOP_ITEM со значением 1
# Чтобы менялся атрибут класса, можно прописать sp.__class__.ID_SHOP_ITEM += 1 или Shop.ID_SHOP_ITEM += 1
################################################################

################################################################

################################################################

################################################################################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################


################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################


################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################

################################################################
