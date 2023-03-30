# _____________Balakirev____________________
# __________Песнь 10. Магические методы __setattr__, __getattribute__, __getattr__ и __delattr________________________________
class Magic:
    def __getattribute__(self, item):
        """Автоматически вызывается, когда идёт обращение к атрибуту через экземпляр класса
        self-ссылка на экземпляр,
        item- атрибут к которому идёт обращение + можно запрещать обращаться к атрибуту экз. класса"""
        if item == 'Имя атрибута':
            raise ValueError('Запрещено обращаться к этому атрибуту')

    def __getattr__(self, item):
        """Автоматически вызывается, когда идёт обращение к несуществующему атрибуту экз. класса
        тогда можно вернуть False, чтобы исключить вызов ошибки"""
        return False

    def __setattr__(self, key, value):
        """Автоматически вызывается, когда идёт присваивание к атрибуту экз. класса
        key-имя атрибута, value - значение, которое присваивается атрибуту
        тогда можно запретить содвать атрибут или присваиваиваьт значение"""
        if key == 'Имя атрибута':
            raise AttributeError('Запрет созавать такой атрибут')
        object.__setattr__(self, key, value)
        # или
        super().__setattr__(key, value)

    def __delattr__(self, item):
        """Автоматически вызывается, когда удаляется атрибут у экз класса тогда можно запретить удаление"""
        if item == 'Имя атрибута':
            raise ValueError('Этот атрибут удалить нельзя')
        object.__delattr__(self, item)


# 3.1 Методы __setattr__, __getattribute__, __getattr__ и __delattr__
# Подвиг 3. Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:
# book = Book()book = Book(название, автор, число страниц, год издания)В каждом объекте класса Book автоматически должны
# формироваться следующие локальные свойства:title - заголовок книги (строка, по умолчанию пустая строка);
# author - автор книги (строка, по умолчанию пустая строка);pages - число страниц (целое число, по умолчанию 0);
# year - год издания (целое число, по умолчанию 0).Объявите в классе Book магический метод __setattr__ для проверки
# типов присваиваемых данных локальным свойствам title, author, pages и year. Если типы не соответствуют локальному
# атрибуту (например, title должна ссылаться на строку, а pages - на целое число), то генерировать исключение командой:
# raise TypeError("Неверный тип присваиваемых данных.")

class Book:
    dict_title = {'title': str, 'author': str, 'pages': int, 'year': int}

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if self.dict_title.get(key, False) == type(value):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)


########################################################################
class Book:
    dict_title = {str: ['title', 'author'], int: ['pages', 'year']}

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.dict_title[type(value)]:
            # if key in self.dict_title.get(type(value), []):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


########################################################################
# Подвиг 4. Вы создаете интернет-магазин. Для этого нужно объявить два класса:Shop - класс для управления магазином в
# целом;Product - класс для представления отдельного товара.Объекты класса Shop следует создавать командой:
# shop = Shop(название магазина)В каждом объекте класса Shop должно создаваться локальное свойство:
# goods - список товаров (изначально список пустой).А также в классе объявить методы:add_product(self, product)
# - добавление нового товара в магазин (в конец списка goods);remove_product(self, product) - удаление товара
# product из магазина (из списка goods);Объекты класса Product следует создавать командой:p = Product(название,
# вес, цена)В них автоматически должны формироваться локальные атрибуты:id - уникальный идентификационный номер
# товара (генерируется автоматически как целое положительное число от 1 и далее);name - название товара (строка);
# weight - вес товара (целое или вещественное положительное число);price - цена (целое или вещественное положительное
# число).В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых данных
# локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.). Если проверка не проходит,
# то генерировать исключение командой:raise TypeError("Неверный тип присваиваемых данных.")Также в классе Product с
# помощью магического(их) метода(ов) запретить удаление локального атрибута id. При попытке это сделать генерировать
# исключение:raise AttributeError("Атрибут id удалять запрещено.")

class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)
            # ind = self.goods.index(product)
            # self.goods.pop(ind)


class Product:
    uid = 1

    def __init__(self, name, weight, price):
        self.id = Product.uid
        Product.uid += 1
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if type(value) == str and key == 'name':
            object.__setattr__(self, key, value)
        elif type(value) == int and key in ['weight', 'price', 'id'] and value > 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price},{p.id}")


########################################################################
class Product:
    next_id = 1

    @classmethod
    def set_next_id(cls):
        cls.next_id += 1

    def __init__(self, name, weight, price):
        self.id = self.next_id
        self.name = name
        self.weight = weight
        self.price = price
        self.set_next_id()

    def __setattr__(self, key, value):
        d = {'id': int, 'name': str, 'weight': (int, float), 'price': (int, float)}
        if not isinstance(value, d.get(key)) or ((key in ('weight', 'price')) and (value < 0)) or (
                (key == 'id' and value < 1)):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, key)


########################################################################
# Подвиг 5. Необходимо создать программу для обучающего курса. Для этого объявляются три класса:
# Course - класс, отвечающий за управление курсом в целом;Module - класс, описывающий один модуль (раздел) курса;
# LessonItem - класс одного занятия (урока).Структура курса на уровне этих классов, приведена на рисунке ниже:
# Объекты класса LessonItem должны создаваться командой:lesson = LessonItem(название урока, число практических
# занятий, общая длительность урока)Соответственно, в каждом объекте класса LessonItem должны создаваться
# локальные атрибуты:title - название урока (строка);practices - число практических занятий (целое положительное число);
# duration - общая длительность урока (целое положительное число).Необходимо с помощью магических методов реализовать
# следующую логику взаимодействия с объектами класса LessonItem:1. Проверять тип присваиваемых данных локальным
# атрибутам. Если типы не соответствуют требованиям, то генерировать исключение командой:raise TypeError("Неверный
# тип присваиваемых данных.")2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать
# значение False.3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.
# Объекты класса Module должны создаваться командой:module = Module(название модуля)Каждый объект класса Module должен
# содержать локальные атрибуты:name - название модуля;lessons - список из уроков (объектов класса LessonItem),
# входящих в модуль (изначально список пуст).Также в классе Module должны быть реализованы методы:
# add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
# remove_lesson(self, indx) - удаление урока по индексу в списке lessons.Наконец, объекты класса Course создаются
# командой:course = Course(название курса)И содержат следующие локальные атрибуты:name - название курса (строка);
# modules - список модулей в курсе (изначально список пуст).Также в классе Course должны присутствовать следующие
# методы:add_module(self, module) - добавление нового модуля в конце списка modules;remove_module(self, indx)
# - удаление модуля из списка modules по индексу в этом списке.

class LessonItem:  # класс одного занятия (урока)
    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if (key == 'practices' or key == 'duration') and type(value) == int:
            object.__setattr__(self, key, value)
        elif key == 'title' and type(value) == str:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ['title', 'practices', 'duration']:
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


# ***magic!***

class Module:  # класс, описывающий один модуль (раздел) курса
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):  # добавление в модуль (в конец списка lessons) нового урока (объекта кл LessonItem);
        self.lessons.append(lesson)

    def remove_lesson(self, indx):  # удаление урока по индексу в списке lessons.
        self.lessons.pop(indx)
        # del self.lessons[indx]


class Course:  # класс, отвечающий за управление курсом в целом:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):  # добавление нового модуля в конце списка modules;
        self.modules.append(module)

    def remove_module(self, indx):  # удаление модуля из списка modules по индексу в этом списке.
        self.modules.pop(indx)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)


#######################################################################
class LessonItem:  # класс одного занятия (урока)
    __attrs = {'title': str, 'practices': int, 'duration': int}

    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if type(value) != self.__attrs[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif (key == 'practices' or key == 'duration') and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.__attrs:
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(self, item)


########################################################################
class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        del self.modules[indx]


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        del self.lessons[indx]


class LessonItem:
    __attr = {
        'title': lambda x: isinstance(x, str),
        'practices': lambda x: isinstance(x, int) and x > 0,
        'duration': lambda x: isinstance(x, int) and x > 0}  # lambda x: isinstance(x, str) x=value

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.__attr and not self.__attr[key](value):
            # lambda x: isinstance(x, str) x=value
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)
        # object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ('title', 'practices', 'duration'):
            raise ValueError("Нельзя это удалить")
        super().__delattr__(item)


########################################################################
class LessonItem:
    title: str
    practices: int
    duration: int

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if not isinstance(value, self.__annotations__.get(key)) or type(value) == int and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        return super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in self.__annotations__:
            super().__delattr__(item)


#######################################################################
class LessonItem:
    attrs = {'title': lambda x: type(x) is str}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if not self.attrs.get(key, lambda x: (isinstance(x, int)) and (x > 0))(value):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

    ########################################################################
    def __setattr__(self, key, value):
        dct = {'title': isinstance(value, str),
               'practices': isinstance(value, int) and value > 0,
               'duration': isinstance(value, int) and value > 0}
        if dct[key]:
            return object.__setattr__(self, key, value)
        raise TypeError("Неверный тип присваиваемых данных.")


########################################################################
# дескрипторы мне больше нравятся для валидации.
class Value:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not self.validate(value):
            raise TypeError("Неверный тип присваиваемых данных.")
        instance.__dict__[self.name] = value

    def validate(self, value) -> bool:
        raise NotImplemented


class String(Value):
    def validate(self, value) -> bool:
        return isinstance(value, str) and len(value) > 0


class PositiveInteger(Value):
    def validate(self, value) -> bool:
        return isinstance(value, int) and value >= 0


class LessonItem:
    title = String()
    practices = PositiveInteger()
    duration = PositiveInteger()

    def __init__(self, title: str, practices: int, duration: int):
        self.title, self.practices, self.duration = title, practices, duration

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        raise AttributeError("Атрибут удалять запрещено.")


#######################################################################
# Подвиг 6. Вам необходимо написать программу описания музеев. Для этого нужно объявить класс Museum, объекты которого
# формируются командой:mus = Museum(название музея)В объектах этого класса должны формироваться следующие локальные
# атрибуты:name - название музея (строка);exhibits - список экспонатов (изначально пустой список).
# Сам класс Museum должен иметь методы:add_exhibit(self, obj) - добавление нового экспоната в музей
# (в конец списка exhibits);remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj
# - на экспонат)get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка
# (нумерация с нуля).Экспонаты представляются объектами своих классов. Для примера объявите в программе следующие
# классы экспонатов:Picture - для картин;Mummies - для мумий;Papyri - для папирусов.
# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
# p = Picture(название, художник, описание)  локальные атрибуты: name - название; author - художник;
# descr - описание m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии;
# location - место находки; descr - описание pr = Papyri(название папируса, датировка, описание)
# локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
# Метод get_info_exhibit() класса Museum должен возвращать значение атрибута descr указанного экспоната в формате:
# "Описание экспоната {name}: {descr}"
class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        x = self.exhibits[indx]
        return f'Описание экспоната {x.name}: {x.descr}'


class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr


########################################################################
class Museum:
    def __init__(self, name):
        self.name = name
        self.__exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    @property
    def exhibits(self):
        return self.__exhibits

    @exhibits.setter
    def exhibit(self, obj):
        self.__exhibits = obj

    def get_info_exhibit(self, indx):
        # # x = self.exhibits[indx]
        return f'Описание экспоната {self.exhibits[indx].name}: {self.__exhibits[indx].descr}'


########################################################################
class Exhibit:
    overridable_attr = None

    def __init__(self, name, overridable, descr):
        self.name = name
        self.overridable = overridable
        self.descr = descr

    def __setattr__(self, key, value):
        if key == 'overridable':
            key = self.overridable_attr
        object.__setattr__(self, key, value)


class Picture(Exhibit):
    overridable_attr = 'author'


class Mummies(Exhibit):
    overridable_attr = 'location'


class Papyri(Exhibit):
    overridable_attr = 'date'


class Museum:
    def __init__(self, name: str):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        exhibit = self.exhibits[indx]
        return f"Описание экспоната {exhibit.name}: {exhibit.descr}"


########################################################################
class Arg:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.name = self.param

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Expon:
    def __init__(self, name: str, arg: str, descr: str):
        self.name = name
        self.arg = arg
        self.descr = descr

    def get_info_exhibit(self):
        return f"Описание экспоната {self.name}: {self.descr}"


class Picture(Expon):
    arg = Arg("author")


class Mummies(Expon):
    arg = Arg("location")


class Papyri(Expon):
    arg = Arg("date")


class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj: (Picture, Mummies, Papyri)):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj: (Picture, Mummies, Papyri)):
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        if indx < len(self.exhibits):
            return self.exhibits[indx].get_info_exhibit()


#######################################################################
class Exhibit:

    def __init__(self, name, information, descr):
        self.name = name
        self.information = information
        self.descr = descr


class Picture(Exhibit):

    def __init__(self, name, name_author, descr):
        super().__init__(name, name_author, descr)


class Mummies(Exhibit):

    def __init__(self, name, place, descr):
        super().__init__(name, place, descr)


class Papyri(Exhibit):

    def __init__(self, name, date, descr):
        super().__init__(name, date, descr)


########################################################################
# Подвиг 7 (на повторение). Объявите класс SmartPhone, объекты которого предполагается создавать командой:
# sm = SmartPhone(марка смартфона)Каждый объект должен содержать локальные атрибуты:model - марка смартфона (строка);
# apps - список из установленных приложений (изначально пустой).Также в классе SmartPhone должны быть объявлены
# следующие методы:add_app(self, app) - добавление нового приложения на смартфон (в конец списка apps);
# remove_app(self, app) - удаление приложения по ссылке на объект app.При добавлении нового приложения проверять,
# что оно отсутствует в списке apps (отсутствует объект соответствующего класса).Каждое приложение должно определяться
# своим классом. Для примера объявите следующие классы:AppVK - класс приложения ВКонтаке;
# appYouTube - класс приложения YouTube;AppPhone - класс приложения телефона.
class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        # if app.name not in self.apps.name and len(self.apps) != 0:
        if all(app.name != i.name for i in self.apps):
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


app_1 = AppVK()  # name = "ВКонтакте"
app_2 = AppYouTube(1024)  # name = "YouTube", memory_max = 1024
app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365,
                  "Работа": 112})  # name = "Phone", phone_list = словарь с контактами
sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)


########################################################################
class SmartPhone:
    def __init__(self, model):
        self.model, self.apps = model, []

    def add_app(self, app):
        if app.__class__ not in (i.__class__ for i in self.apps):
            self.apps.append(app)

        if not len(tuple(filter(lambda x: type(x) == type(app), self.apps))):
            self.apps.append(app)

        if not type(app) in map(type, self.apps):
            self.apps.append(app)

        if not isinstance(app, tuple(type(i) for i in self.apps)):
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app) if app in self.apps else ...


class AppVK:
    def __init__(self, name="ВКонтакте"):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max, name="YouTube"):
        self.name, self.memory_max = name, memory_max


class AppPhone:
    def __init__(self, phone_list: dict, name="Phone"):
        self.name, self.phone_list = name, phone_list


#######################################################################
# Подвиг 8. Объявите класс Circle (окружность), объекты которого должны создаваться командой:
# circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности
# В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:
# __x, __y - координаты центра окружности (вещественные или целые числа);
# __radius - радиус окружности (вещественное или целое положительное число).
# Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):
# x, y - для изменения и доступа к значениям __x, __y, соответственно;
# radius - для изменения и доступа к значению __radius.При изменении значений приватных атрибутов через
# объекты-свойства нужно проверять, что присваиваемые значения - числа (целые или вещественные).
# Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля).
# Сделать все эти проверки нужно через магические методы. При некорректных переданных числовых значениях, прежние
# значения меняться не должны (исключений никаких генерировать при этом не нужно).Если присваиваемое значение не
# числовое, то генерировать исключение командой:raise TypeError("Неверный тип присваиваемых данных.")
class Circle:
    def __init__(self, x, y, radius):
        # self.__x = self.__y = self.__radius = None
        self.radius = radius
        self.x = x
        self.y = y

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if type(value) in (float, int) and key != 'radius':
            super().__setattr__(key, value)
        elif key == 'radius' and value > 0:
            object.__setattr__(self, key, value)
        elif type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius


circle = Circle(10.5, 7, 22)
circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует


########################################################################
class property:
    def __set_name__(self, owner, name):
        setattr(self, "name", "_" + owner.__qualname__ + "__" + name)

    def __get__(self, instance, owner):
        if instance is None:  # чтобы обойти проверку на property
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Circle:
    x = property()
    y = property()
    radius = property()

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __setattr__(self, key, value):
        if key in ("x", "y", "radius") \
                and type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == "radius" and value <= 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


###############################################################################################################################################
class IntFloat:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        if not instance:  # этот костыль нужен, чтобы проверку на декоратор @property пройти.
            return property()
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        Если провеку на тип написать отдельным методом (__setattr__),
        то он срабатывает во время присвоения имён (__set_name__), оно нам не надо.
        Поэтому именно тут проверка на тип присваиваемых данных.
        """
        if type(value) in (float, int) and self.name != '__radius':
            setattr(instance, self.name, value)
        elif self.name == '__radius' and value > 0:
            setattr(instance, self.name, value)
        elif type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")

        # if not isinstance(value, (int, float)):
        #     raise TypeError("Неверный тип присваиваемых данных.")
        # if not (self.name == "__radius" and value < 0):
        #     setattr(instance, self.name, value)


class Circle:
    x = IntFloat()
    y = IntFloat()
    radius = IntFloat()

    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius

    def __getattr__(self, item):
        return False


########################################################################
# Подвиг 9. Объявите в программе класс Dimensions (габариты) с атрибутами:
# MIN_DIMENSION = 10 MAX_DIMENSION = 1000 Каждый объект класса Dimensions должен создаваться командой:
# d3 = Dimensions(a, b, c)   # a, b, c - габаритные размерыи содержать локальные атрибуты:
# __a, __b, __c - габаритные размеры (целые или вещественные числа).Для работы с этими локальными атрибутами в
# классе Dimensions следует прописать следующие объекты-свойства:a, b, c - для изменения и считывания соответствующих
# локальных атрибутов __a, __b, __c.При изменении значений __a, __b, __c следует проверять, что присваиваемое значение
# число в диапазоне [MIN_DIMENSION; MAX_DIMENSION]. Если это не так, то новое значение не присваивается (игнорируется).
# С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в
# объектах класса Dimensions. При попытке это сделать генерировать исключение:
# raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

class Discription:
    def __set_name__(self, owner, name):
        self.name = '_' + name
        # self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        # Нужно еще иметь ввиду что в этом тесте идет обращение к атрибуту класса.assert type(Dimensions.a) == property
        # and type(Dimensions.b) == property and type(Dimensions.c) == property, "класс Dimensions должен иметь
        # объекты-свойства с именами: a, b, c"Это значит, что в дескрипторе instanse будет None. И он будет пытаться
        # вызвать атрибут у NoneType, что приведет к AtrebuteError.Я добавил проверку
        # def __get__(self, instance, owner):
        # if instance:   return getattr(instance, self.name)
        if not instance:
            return property()
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and value in list(range(Dimensions.MIN_DIMENSION, Dimensions.MAX_DIMENSION + 1)):
            setattr(instance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    a = Discription()
    b = Discription()
    c = Discription()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key == 'MIN_DIMENSION' or key == 'MAX_DIMENSION':
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        super().__setattr__(key, value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError


########################################################################
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)

    @classmethod
    def verify_value(cls, value):
        return type(value) in (int, float) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.verify_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.verify_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.verify_value(value):
            self.__c = value


########################################################################
class Property:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'
        self.min = owner.MIN_DIMENSION
        self.max = owner.MAX_DIMENSION

    def __get__(self, instance, owner):
        if instance:
            return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.min <= value <= self.max:
            setattr(instance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Property()
    b = Property()
    c = Property()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)


def type(arg):
    return property


#######################################################################
# Дескрипторы
class Desc:
    def __set_name__(self, owner, name):
        self.instance_name = '_' + owner.__name__ + '__' + name

    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__[self.instance_name]
        else:
            return property()

    def __set__(self, instance, val):
        if type(val) in (int, float) and instance.MIN_DIMENSION <= val <= instance.MAX_DIMENSION:
            instance.__dict__[self.instance_name] = val


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Desc()
    b = Desc()
    c = Desc()


########################################################################
class Number:
    def __init__(self, min_val: int, max_val: int):
        self.min_val, self.max_val = min_val, max_val

    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)

    def validate(self, value) -> bool:
        return isinstance(value, (int, float)) and self.min_val <= value <= self.max_val


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Number(MIN_DIMENSION, MAX_DIMENSION)
    b = Number(MIN_DIMENSION, MAX_DIMENSION)
    c = Number(MIN_DIMENSION, MAX_DIMENSION)

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __setattr__(self, key, value):
        if key in {'MIN_DIMENSION', 'MAX_DIMENSION'}:
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        super(Dimensions, self).__setattr__(key, value)


########################################################################
class Descriptor:

    def __set_name__(self, owner, name):
        self.protected_name = '_' + owner.__name__ + '__' + name

    def __get__(self, obj, objtype=None):
        if obj:
            return getattr(obj, self.protected_name)
        return property()  # как заставить Дескриптор прикинуться пропертью.

    def __set__(self, obj, value):
        if type(value) in (int, float):
            if obj.MIN_DIMENSION <= value <= obj.MAX_DIMENSION:
                setattr(obj, self.protected_name, value)


#######################################################################
# Подвиг 10. Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно быть три слота для фильтров.
# Каждый слот строго для своего класса фильтра:Mechanical - для очистки от крупных механических частиц;
# Aragon - для последующей очистки воды;Calcium - для обработки воды на третьем этапе.Объекты классов фильтров должны
# создаваться командами:filter_1 = Mechanical(дата установки)filter_2 = Aragon(дата установки)
# filter_3 = Calcium(дата установки)Во всех объектах этих классов должен формироваться локальный атрибут:
# date - дата установки фильтров (для простоты - положительное вещественное число).Также нужно запретить изменение
# этого атрибута после создания объектов этих классов (только чтение). В случае присвоения нового значения, прежнее
# значение не менять. Ошибок никаких не генерировать.Объекты класса GeyserClassic должны создаваться командой:
# g = GeyserClassic()А сам класс иметь атрибут:MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)
# и следующие методы:add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num
# (номер слота: 1, 2 и 3), если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно
# установить только объекты класса Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium.
# Иначе слот должен оставаться пустым.remove_filter(self, slot_num) - извлечение фильтра из указанного слота
# (slot_num: 1, 2, и 3);get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки
# (по возрастанию номеров слотов);water_on(self) - включение воды: возвращает True, если вода течет и False - в
# противном случае.Метод water_on() должен возвращать значение True при выполнении следующих условий:
# - все три фильтра установлены в слотах;- все фильтры работают в пределах срока службы (значение (time.time() - date)
# должно быть в пределах [0; MAX_DATE_FILTER])
import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = {}

    def add_filter(self, slot_num, filter):
        if slot_num not in self.slots:
            if slot_num == 1 and isinstance(filter, Mechanical):
                self.slots[slot_num] = filter
            elif slot_num == 2 and isinstance(filter, Aragon):
                self.slots[slot_num] = filter
            elif slot_num == 3 and isinstance(filter, Calcium):
                self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        if slot_num in self.slots:
            del self.slots[slot_num]

    def get_filters(self):
        return map(lambda x: x[1], sorted(self.slots.items(), key=lambda x: x[0]))

    def water_on(self):
        if len(self.slots) == 3 and all(
                int(time.time() - date.date) in range(0, self.MAX_DATE_FILTER + 1) for date in self.slots.values()):
            return True
        return False


class Mechanical:

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__ and isinstance(value, (float, int)):
            object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        super().__setattr__(key, value)


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
f1, f2, f3 = my_water.get_filters()
# print(f1,f2,f3)# f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно


########################################################################
class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots_class = ('Mechanical', 'Aragon', 'Calcium')
        self.slots = {(1, self.slots_class[0]): None, (2, self.slots_class[1]): None, (3, self.slots_class[2]): None}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.slots and not self.slots[key]:
            self.slots[key] = filter

    def remove_filter(self, slot_num):
        if type(slot_num) == int and 0 <= slot_num <= 3:
            key = (slot_num, self.slots_class[slot_num - 1])
            if key in self.slots:
                self.slots[key] = None

    def get_filters(self):
        return tuple(self.slots.values())

    def water_on(self):
        end = time.time()
        for value in self.slots.values():
            if value is None:
                return False
            start = value.date
            if end - start > self.MAX_DATE_FILTER:
                return False
        return True


###############################################################################################################################################
class Filter:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            super().__setattr__(key, value)


class Mechanical(Filter): pass


class Aragon(Filter): pass


class Calcium(Filter): pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    d = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self) -> None:
        self.slots = [None] * 3

    def add_filter(self, slot_num, filter):
        if self.d[slot_num] == type(filter):
            self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        return all([i != None and 0 <= time.time() - i.date <= self.MAX_DATE_FILTER for i in self.slots])


########################################################################!!!!!!!!!!!!best

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = {1: 'Mechanical', 2: 'Aragon', 3: 'Calcium'}

    def add_filter(self, slot_num, filter):
        if self.slots[slot_num] == filter.__class__.__name__:
            self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num] = self.slots[slot_num].__class__.__name__  # обратно возвращаем строку 'Mechanical'
        # вместо класса Mechanical

    def get_filters(self):
        return self.slots.values()

    def water_on(self):
        return all(isinstance(i, Filter) and 0 <= (time.time() - i.date) <= self.MAX_DATE_FILTER
                   for i in self.slots.values())


########################################################################
class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.dct_filters = {(1, 'Mechanical'): 0, (2, 'Aragon'): 0, (3, 'Calcium'): 0}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.dct_filters:
            if self.dct_filters[key] == 0:
                self.dct_filters[key] = filter

    def remove_filter(self, slot_num):
        for (slot, tp) in self.dct_filters:
            if slot == slot_num:
                self.dct_filters[(slot, tp)] = 0
                return

    def get_filters(self):
        return tuple(v for v in self.dct_filters.values())

    def water_on(self):
        end = time.time()
        for filter in self.dct_filters.values():
            if filter == 0:
                return False
            else:
                start = filter.date
                if end - start > self.MAX_DATE_FILTER:
                    return False
        return True


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        if item == 'date':
            raise ValueError('Private attribute')
        return super().__getattribute__(item)


########################################################################
class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.__FILTER_LST = []

    def add_filter(self, slot_num, filter):
        if slot_num == filter.SLOT and filter not in [type(i) for i in self.__FILTER_LST]:
            self.__FILTER_LST.append(filter)

    def remove_filter(self, slot_num):
        for i in self.__FILTER_LST:
            if i.SLOT == slot_num:
                self.__FILTER_LST.remove(i)

    def get_filters(self):
        return tuple(sorted(self.__FILTER_LST, key=lambda x: x.SLOT))

    def water_on(self):
        if len(self.__FILTER_LST) == 3:
            for i in self.__FILTER_LST:
                if not 0 <= time.time() - i.date <= self.MAX_DATE_FILTER:
                    return False
            return True
        return False


class Mechanical:
    SLOT = 1

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__:
            object.__setattr__(self, key, value)


#######################################################################
class Descriptor:
    """Descriptor"""

    def __set_name__(self, owner, date):
        self.date = '_' + date

    def __get__(self, instance, owner):
        return getattr(instance, self.date)

    def __set__(self, instance, value):
        if self.date not in instance.__dict__ and type(value) in (float, int) and str(self.date) == '_date':
            setattr(instance, self.date, value)


class Mechanical:
    date = Descriptor()

    def __init__(self, date):
        self.date = date


class Aragon:
    date = Descriptor()

    def __init__(self, date):
        self.date = date


class Calcium:
    date = Descriptor()

    def __init__(self, date):
        self.date = date


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self._slots = {1: None, 2: None, 3: None}
        self._slots_type = {1: Mechanical, 2: Aragon, 3: Calcium}

    def add_filter(self, slot_num, filter):
        if not self._slots[slot_num]:
            if type(filter) == self._slots_type[slot_num]:
                self._slots[slot_num] = filter

    def remove_filter(self, slot_num):
        self._slots[slot_num] = None

    def get_filters(self):
        return tuple(v for k, v in self._slots.items())

    def water_on(self):
        flag = 0
        if self._slots[1] and 0 <= (time.time() - self._slots[1].date) <= GeyserClassic.MAX_DATE_FILTER:
            flag += 1
        if self._slots[2] and 0 <= (time.time() - self._slots[2].date) <= GeyserClassic.MAX_DATE_FILTER:
            flag += 1
        if self._slots[3] and 0 <= (time.time() - self._slots[3].date) <= GeyserClassic.MAX_DATE_FILTER:
            flag += 1
        return flag == 3


########################################################################
class Filter:
    def __init__(self, date=None):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and isinstance(value, (float, int)) and 'date' not in self.__dict__:
            super().__setattr__(key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    FILTER_TYPES = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self):
        self.slots = [None] * 3

    def add_filter(self, slot_num, filter):
        if self.slots[slot_num - 1] is None and type(filter) == self.FILTER_TYPES[slot_num]:
            self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        return (all(self.slots) and all([time.time() - t.date <= self.MAX_DATE_FILTER for t in self.slots]))


########################################################################
# __________________Магический метод __call__. Функторы и классы-декораторы______________
# __call__ нужна, когда мы хотим, чтобы экземпляры класса вели себя как функции.
# Магический метод __call__ - позволяет вызывать объекты класса подобно функциям, в котором определен метод __call__()
#                            - нужен для замыканий и декораторов
# - определяется для возможности вызова экземпляра класса как функции со своими аргументами!, а при вызове класса всегда
# вызывается метод __call__ из метакласса type.
class Derivate:
    """Пример как заменить декоратор функции через как бы класс декоратор"""

    def __init__(self, func):  # передаётся функция, которую расширяем как бы декоратором
        self.__fn = func

    def __call__(self, *args, **kwargs):
        """Автоматически запускается, когда происходит вызов класса, тогда можно экз. класса вызывать как функцию
         со () и передавать аргументы в этот экземпляр"""
        return self.__fn(*args)  # args - который передаётся в зкз класса


# способ 1: превратив Derivate в класс-декоратор
@Derivate
def f(x):
    return x[1:-1]  # обрезает по 1 значению по краям списка


# способ 2: превратить функцию в экз класса тогда вызывая экз. сработает __call__, в этот __call__ передастся арг. []
# f = Derivate(f)
# Вызов декорируемой функции
print(f([0, 1, 2, 3, 4]))  # передаём арг [] в __cal__


# ________________________________________________________________
class Stripchars:
    """Замена замыкания функций (убрать ненужные символы в строке)"""

    def __init__(self, chars='!'):
        self.chars = chars
        # символы которые нужно убрать по умолчанию или которые передаюся в качестве арг. при вызове класса

    def __call__(self, *args, **kwargs):  # передаётся строка 'Hello, world'
        if not isinstance(args[0], str):
            raise TypeError('Не является строкой')
        return args[0].strip(self.chars)  # обрезает по краям символы


s = Stripchars(',')
res = s(',Hello, world!')  # передаём арг  в __cal__
print(res)  # Hello, world!
#######################################################################
# Подвиг 2. Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться
# командой:rnd = RandomPassword(psw_chars, min_length, max_length)где psw_chars - строка из разрешенных в пароле
# символов; min_length, max_length - минимальная и максимальная длина генерируемых паролей.Непосредственная генерация
# одного пароля должна выполняться командой:psw = rnd()где psw - ссылка на строку длиной в диапазоне
# [min_length; max_length] из случайно выбранных символов строки psw_chars.С помощью генератора списка
# (list comprehension) создайте список lst_pass из трех сгенерированных паролей объектом rnd класса RandomPassword,
# созданного с параметрами: min_length = 5max_length = 20psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
from random import randint, choice


class RandomPassword:

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        num = randint(self.min_length, self.max_length)
        # password = ''
        # for i in range(num):
        #     password += choice(self.psw_chars)
        # return password

        # return ''.join([choice(self.psw_chars) for i in range(num)])
        return ''.join([self.psw_chars[randint(0, len(self.psw_chars) - 1)] for i in range(num)])


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
# psw = rnd()
lst_pass = [rnd() for _ in range(3)]
print(lst_pass)


########################################################################
# через замыкание
def randomPassword(psw_chars, min_length, max_length):
    def rnd():
        return ''.join([choice(psw_chars) for i in range(min_length, max_length)])

    return rnd


rnd = randomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for _ in range(3)]


###############################################################################################################################################
def __call__(self, *args, **kwargs):
    num = randint(self.min_length, self.max_length)
    return ''.join(choices(self.psw_chars, k=num))  # k=1 - количество выбираемых случайных элементов.


########################################################################
# Подвиг 3. Для последовательной обработки файлов из некоторого списка, например:
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png",
# "my.html", "data.shtml"]Необходимо объявить класс ImageFileAcceptor, который бы выделял только файлы с
# указанными расширениями.Для этого предполагается создавать объекты класса командой:
# acceptor = ImageFileAcceptor(extensions)где extensions - кортеж с допустимыми расширениями файлов,
# например: extensions = ('jpg', 'bmp', 'jpeg').А, затем, использовать объект acceptor в стандартной функции
# filter языка Python следующим образом:image_filenames = filter(acceptor, filenames)Пример использования класса
# (эти строчки в программе писать не нужно):filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg",
# "forest.jpeg", "eq_1.png", "eq_2.png"]acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, filename, *args, **kwargs):
        start = filename.rfind('.')
        ext = '' if start == -1 else filename[start + 1:]
        return ext in self.extensions

        # return filename.rsplit('.')[1] in self.extensions

        # return filenames.endswith(self.extensions) #нельзя т.к. если мы выберем расширение html,
        # то заданный фильтр пропустит и файл с расширением .shtml

        # for i in self.extensions:
        #     if i == filenames[-len(i):]:
        #         return filenames


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)  # filter(func, iterable)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]


########################################################################
# Подвиг 4. Предположим, мы разрабатываем класс для обработки формы авторизации на стороне сервера. Для этого был
# создан следующий класс с именем LoginForm:Здесь name - это заголовок формы (строка);
# validators - список из валидаторов для проверки корректности поля. В методе post параметр request - это словарь с
# ключами 'login' и 'password' и значениями (строками) для логина и пароля соответственно.
# Вам необходимо в программе объявить классы валидаторов:LengthValidator - для проверки длины данных в диапазоне
# [min_length; max_length];CharsValidator - для проверки допустимых символов в строке.
# Объекты этих классов должны создаваться командами:lv = LengthValidator(min_length, max_length) #
# min_length - минимально допустимая длина; max_length - максимально допустимая длина
# cv = CharsValidator(chars) # chars - строка из допустимых символовДля проверки корректности данных каждый валидатор
# должен вызываться как функция:res = lv(string)res = cv(string)и возвращать True, если string удовлетворяет
# условиям валидатора и False - в противном случае.

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:  # если вообще не заданы валидаторы то используем любые логин и пароли
            return True
        for v in self.validators:
            if not v(self.login) or not v(self.password):  # логин и пароль пропускаются через валидаторы
                return False
        return True  # если все авдидаторы пройдены без False


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return self.min_length <= len(args[0]) <= self.max_length
    # return isinstance(string, str) and self.min_length <= len(string) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        return set(args[0]).issubset(self.chars)
        # return set(args[0]) <= set(self.chars)
        # return all(symbol in self.chars for symbol in string)


from string import ascii_lowercase, digits

min_length = 3
max_length = 50
chars = ascii_lowercase + digits
string = 'hello word'
lv = LengthValidator(min_length, max_length)  # min_length - мин доп длина; max_length - максимально допустимая длина
cv = CharsValidator(chars)  # chars - строка из допустимых символов
res = lv(string)
res = cv(string)

lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")


########################################################################
# Подвиг 5. Объявите класс DigitRetrieve для преобразования данных из строки в числа. Объекты этого класса создаются
# командой:dg = DigitRetrieve()Затем, их предполагается использовать, например следующим образом:
# d1 = dg("123")   # 123 (целое число)То есть, целые числа в строке следует приводить к целочисленному типу данных, а
# все остальные - к значению None.С помощью объектов класса DigitRetrieve должно выполняться преобразование чисел
# из списка строк следующим образом:
# st = ["123", "abc", "-56.4", "0", "-5"]digits = list(map(dg, st))  # [123, None, None, 0, -5]
class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        if args[0][0] == '-' and args[0][1:].isdigit():
            return int(args[0])
        elif args[0].isdigit():
            return int(args[0])
        return None
        # try:
        #     return int(args[0])
        # except:
        #     return None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)


#######################################################################
class DigitRetrieve:
    def __call__(self, num):
        if num.isdigit() or num.startswith('-') and num[1:].isdigit():
            return int(num)


########################################################################
import re


class DigitRetrieve:
    def __call__(self, value):
        if re.fullmatch(r'-?\d+', value):
            return int(value)


########################################################################
class DigitRetrieve:
    def __call__(self, value):
        if value.lstrip('-').isdigit():
            return int(value)


#######################################################################
class DigitRetrieve:
    def __call__(self, st, *args, **kwargs):
        if (st[1:] if st.startswith('-') else st).isdigit():
            return int(st)


# решение с регулярками - оно еще медленнее работает) так что на первом месте этот вариант со срезами
# (собственно, я сперва полагал что раз при создании срезов создается новый объект, то это будет отнимать достаточно
# времени, в то время как в варианте с исключениями такого нет), посерединке вариант с исключениями и на последнем месте
# через регулярку
########################################################################
# Подвиг 6. Предположим, вам необходимо создать программу по преобразованию списка строк, например:
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]в следующий фрагмент HTML-разметки (многострочной строки,
# кавычки выводить не нужно):'''<ul><li>Пункт меню 1</li><li>Пункт меню 2</li><li>Пункт меню 3</li></ul>'''
# Для этого необходимо объявить класс RenderList, объекты которого создаются командой:
# render = RenderList(type_list)где type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и
# "ol" - для списка с тегом <ol>). Если значение параметра type_list другое (не "ul" и не "ol"),
# то формируется список с тегом <ul>.Затем, предполагается использовать объект render следующим образом:
# html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    @property
    def type_list(self):
        return self.__type_list

    @type_list.setter
    def type_list(self, type_list):
        if type_list == "ol":
            self.__type_list = "ol"
        elif type(type_list) == str:
            self.__type_list = "ul"

    def __call__(self, *args, **kwargs):
        return "\n".join([f'<{self.type_list}>', *map(lambda x: f'<li>{x}</li>', args[0]), f'</{self.type_list}>'])
        return f'<{self.type_list}>\n' \
               f'<li>Пункт меню 1</li>\n' \
               f'<li>Пункт меню 2</li>\n' \
               f'<li>Пункт меню 3</li>\n' \
               f'</{self.type_list}>\n'

        new_list = '\n'.join([f"<li>{el}</li>" for el in lst])
        return f'<{self.type_list}>\n{new_list}\n</{self.type_list}>'


type_list = "ol"
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList(type_list)
html = render(lst)


####################################################################################################################
def __call__(self, lst, *args, **kwargs):
    res = f"<{self.type_list}>\n"
    for item in lst:
        res += f"<li>{item}</li>\n"
    res += f"</{self.type_list}>"
    return res


########################################################################
# Подвиг 7. Необходимо объявить класс-декоратор с именем HandlerGET, который будет имитировать обработку GET-запросов
# на стороне сервера. Для этого сам класс HandlerGET нужно оформить так, чтобы его можно было применять к любой функции
# как декоратор. Например:#
# @HandlerGET def contact(request):
# return "Сергей Балакирев"Здесь request - это произвольный словарь с данными текущего запроса, например, такой:
# {"method": "GET", "url": "contact.html"}. А функция должна возвращать строку.Затем, при вызове декорированной функции:
# res = contact({"method": "GET", "url": "contact.html"})должна возвращаться строка в формате:"GET: <данные из функции>"
# В нашем примере - это будет:"GET: Сергей Балакирев"Если ключ method в словаре request отсутствует, то по умолчанию
# подразумевается GET-запрос. Если же ключ method принимает другое значение, например, "POST", то декорированная
# функция contact должна возвращать значение None.Для реализации имитации GET-запроса в классе HandlerGET следует
# объявить вспомогательный метод со следующей сигнатурой:def get(self, func, request, *args, **kwargs): ...
# Здесь func - ссылка на декорируемую функцию; request - словарь с переданными данными при вызове декорированной
# функции. Именно в этом методе следует формировать возвращаемую строку в указанном формате: "GET: Сергей Балакирев"
class HandlerGET:
    def __init__(self, func):
        self.func = func

    def get(self, func, request, *args, **kwargs):
        # print(request)  # ({'method': 'GET', 'url': 'contact.html'},)
        if request[0].get('POST') == 'GET':
            return None
        if request[0].get('method', 'GET') == 'GET':
            return f'GET: {func(request)}'
        # return f'GET: {self.func(request)}'

    def __call__(self, *args, **kwargs):
        return self.get(self.func, args)


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})


########################################################################
class HandlerGET:
    def __init__(self, func):
        self.func = func

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def __call__(self, request, *args, **kwargs):
        # print(request)  # {'method': 'GET', 'url': 'contact.html'}
        if request.get('method', 'GET') == 'GET':
            return self.get(self.func, request, *args, **kwargs)
        else:
            return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)


########################################################################
class HandlerGET:

    def __init__(self, func):
        self._func = func

    def __call__(self, request):
        return self.get(self._func, request)

    def get(self, func, request, *args, **kwargs):
        method = request.get('method', 'GET')
        if method != 'GET':
            return None
        return f'GET: {func(request)}'


#######################################################################
class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, requests, *rgs, **kwargs):
        if 'method' in requests and requests['method'] != 'GET':
            return None
        else:
            return self.get(self.func, requests)

    def get(self, func, request, *args, **kwargs):
        return 'GET: ' + func(request)


########################################################################
def HandlerGET(func):
    def wrapper(request, *args, **kwargs):
        if 'method' in request and request['method'] != "GET":
            return None
        else:
            return f"GET: {func(request, *args, **kwargs)}"

    return wrapper


########################################################################
# __________ Декоратор с параметрами______________________________________________________
class Decorator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, func):
        def wrapper(x, y=1):
            return func(x) + y * (self.a + self.b)

        return wrapper


@Decorator(4, 8)
def my_func(x):
    return x


#######################################################################
def digits_dec(num=0):
    def decorator(func):
        def wrapper(x):
            result = x ** num
            return result

        return wrapper

    return decorator


@digits_dec(2)  # по умолчанию берет степень НОЛЬ измените на @digits_dec(2)
def a(x):
    return x


print(a(11))

########################################################################
# Подвиг 8 (развитие подвига 7). Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять
# к функциям следующим образом:# @Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
# def contact(request):#     return "Сергей Балакирев"# Здесь аргумент methods декоратора Handler содержит список
# разрешенных запросов для обработки. Сама декорированная функция вызывается по аналогии с предыдущим подвигом:
# # res = contact({"method": "POST", "url": "contact.html"})# В результате функция contact должна возвращать
# строку в формате:# "<метод>: <данные из функции>"# В нашем примере - это будет:# "POST: Сергей Балакирев"
# Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если ключ method
# принимает значение отсутствующее в списке methods декоратора Handler, например, "PUT", то декорированная функция
# contact должна возвращать значение None.# Для имитации GET и POST-запросов в классе Handler необходимо объявить
# два вспомогательных метода с сигнатурами:# def get(self, func, request, *args, **kwargs) -
# для имитации обработки GET-запроса# def post(self, func, request, *args, **kwargs) -
# для имитации обработки POST-запроса# В зависимости от типа запроса должен вызываться соответствующий метод
# (его выбор в классе можно реализовать методом __getattribute__()). На выходе эти методы должны формировать
# строки в заданном формате.# P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.
# Небольшая справка# Для реализации декоратора с параметрами на уровне класса в инициализаторе
# __init__(self, methods) прописываем параметр для декоратора, а магический метод __call__() объявляем как
# полноценный декоратор на уровне функции.

from functools import wraps


class Handler:
    def __init__(self, methods=None):
        self.method = methods
        # print(self.method) # ('GET', 'POST')

    def __call__(self, func, *args, **kwargs):
        @wraps(func)  # чтобы имя функции contact не заменялось на wrapper
        def wrapper(request, *args, **kwargs):
            # print(request) # {'method': 'POST', 'url': 'contact.html'}
            if request.get('method', 'GET') in self.method:
                if request.get('method', 'GET') == 'GET':
                    return self.get(func, request, *args, **kwargs)
                return self.post(func, request, *args, **kwargs)
                # self.__getattribute__(method)(func, request)
            else:
                return None

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'{request["method"]}: {func(request)}'


@Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"

    ###############################################################################################################################################
    def __call__(self, func, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            if request.get('method', 'GET') in self.__method:
                method = request.get('method', 'GET').lower()  # перевести GET/POST в  get/post
                return self.__getattribute__(method)(func, request)

        # автоматически вызов def get или def post и передаём в них (func, request) #
        # self.__getattribute__(method) - то это будет ссылка на ф. Во вторых скобках указываем аргументы для этой фу
        # найти и подставить атрибут-метод method)(......) т.е. все лишь зависимый поиск атрибута по
        # агрументу x self.____getattribute__(x)
        return wrapper

    ########################################################################
    def __call__(self, func) -> Any:
        def wrapper(request: dict):
            name_method: str = request.get('method', 'GET')
            if name_method not in self.methods:
                return None
            return getattr(self, str.lower(name_method))(func, request)
            # return getattr(self, str(name_method.lower()))(func, request)

        return wrapper


########################################################################
# Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе
# строки из целых чисел, записанных через пробел, например:"12 -5 10 83"на выходе возвращался список из целых чисел:
# [12, -5, 10, 83]Назовите декорированную функцию input_dg и вызовите ее командой:
class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        lst = self.func().split()
        return [*map(int, lst)]


@InputDigits
def input_dg():
    return input()


# input_dg = InputDigits(input_dg)
res = input_dg()


########################################################################
class InputDigits:

    def __call__(self, *args, **kwargs):
        return [int(i) for i in input().split()]


input_dg = InputDigits()
res = input_dg()


########################################################################
# Подвиг 10 (развитие подвига 9). Объявите класс-декоратор InputValues с параметром render - функция или объект для
# преобразования данных из строк в другой тип данных. Чтобы реализовать такой декоратор в инициализаторе __init__()
# следует указать параметр render, а магический метод __call__() определяется как функция-декоратор:
# class InputValues: В качестве рендера объявите класс с именем RenderDigit, который бы преобразовывал строковые
# данные в целые числа. Объекты этого класса создаются командой:render = RenderDigit()и применяются следующим образом:
# d1 = render("123")   # 123 (целое число)d2 = render("45.54")   # None (не целое число)Декорируйте стандартную функцию
# input декоратором InputValues и объектом рендера класса RenderDigit так, чтобы на выходе при вводе целых чисел
# через пробел возвращался список из введенных значений. А на месте не целочисленных данных - значение None.
# Например, при вводе строки:"1 -5.3 0.34 abc 45f -5"должен возвращаться список:[1, None, None, None, None, -5]
# Назовите декорированную функцию input_dg и вызовите ее командой:res = input_dg()
class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.__render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return [self.__render(i) for i in func().split()] # [1 -5.3 0.34 abc 45f -5]

        return wrapper


class RenderDigit:

    def __call__(self, string, *args, **kwargs):
        if string.replace('-', '').isdigit():
            # if string.rstrip('-').isdigit():
            return int(string)
        # return None


render = RenderDigit()


@InputValues(render)
def input_dg():
    return input('input: ')


# input_dg = InputValues(render)(input)
res = input_dg()
print(res)


#######################################################################
#
class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.__render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func().split()))
        # return [*map(self.__render, func().split())]

        return wrapper


class RenderDigit:

    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return None
        # if string.replace('-', '').isdigit():
        #     return int(string)
        # return None


render = RenderDigit()


@InputValues(render)
def input_dg():
    return input()


# input_dg = InputValues(render)(input)
# input_dg = InputValues(RenderDigit())(input)
res = input_dg()
print(res)


########################################################################
class RenderDigit:
    def __call__(self, *args, **kwargs):
        try:
            return int(args[0])
        except ValueError:
            return


