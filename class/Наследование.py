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
# 4.3 Наследование. Функция super() и делегирование
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
