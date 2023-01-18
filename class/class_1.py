################################  1.3 Классы и объекты. Атрибуты классов и объектов / Egorof /


class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


setattr(Goods, 'price', 2048)
setattr(Goods, 'inflation', 100)


# Goods.price = 2048
# Goods.inflation = 100

########################################################################################################
# Подвиг 5. Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:
# model: "Тойота"color: "Розовый"number: "П111УУ77"
# Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.

class Car:
    pass


setattr(Car, 'model', 'Тойота')
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', 'П111УУ77')

print(Car.__dict__['color'])


########################################################################################################
class Car:
    pass
    # ... #точки - это ellipsis. Оператор имеющий несколько значений в зависимости от контекста. Конкретно здесь -
    # это указание на то, что код можно/нужно будет дописать в последствии. Вроде как считается боле питоничным
    # использовать в этой ситуации именно его, а не pass. Ну, и применить его можно там, где pass применить нельзя:
    # x = 3
    # print(x) if x < 4 else ...
    # выражение ничего не будет делать, если условие не выполняется, с pass такого написать не получится, будет ошибка.


lst = list(map(str.strip, sys.stdin.readlines()))
d = {k: v for i in lst for k, v in [i.split(":")]}
# {'model': ' "Тойота"', 'color': ' "Розовый"', 'number': ' "П111УУ77"'}

# d = {'model': ' "Тойота"', 'color': ' "Розовый"', 'number': ' "П111УУ77"'}
# for i in d:
#     setattr(Car, i, d[i])

[setattr(Car, k, v) for k, v in d.items()]
[setattr(Car, *i) for i in d.items()]

print(Car.__dict__)
print(Car.__dict__['color'])


########################################################################
# Подвиг 6. Объявите класс с именем Notes и определите в нем следующие атрибуты:
# uid: 1005435title: "Шутка"author: "И.С. Бах"pages: 2
# Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута author.

class Notes:
    ...


lst = list(map(str.strip, sys.stdin.readlines()))
d = {k: v for i in lst for k, v in [i.split(":")]}
d = {'uid': ' 1005435', 'title': ' "Шутка"', 'author': ' "И.С. Бах"', 'pages': ' 2'}

[setattr(Notes, *i) for i in d.items()]
print(getattr(Notes, 'author', 'no name'))


################################################################################################################################################
# Подвиг 7. Объявите класс с именем Dictionary и определите в нем следующие атрибуты:
# rus: "Питон"
# eng: "Python"
# Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута rus_word. Если такого атрибута
# в классе нет, то функция getattr() должна возвращать булево значение False.
class Dictionary:
    ...


lst = list(map(str.strip, sys.stdin.readlines()))
d = {k: v for i in lst for k, v in [i.split(":")]}
d = {'rus': ' "Питон"', 'eng': ' "Python"'}

[setattr(Dictionary, *i) for i in d.items()]
print(getattr(Dictionary, 'author', 'no name'))

print(getattr(Dictionary, 'rus_word', False))


################################################################################################################################################
# Подвиг 8. Объявите класс с именем TravelBlog и объявите в нем атрибут:
# total_blogs: 0
# Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:
#
# name: 'Франция'
# days: 6
# Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
#
# Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два локальных свойства:
#
# name: 'Италия'
# days: 5
# Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.

class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = 'Франция'
tb1.days = 6

TravelBlog.total_blogs += 1
# print(getattr(TravelBlog, 'total_blogs')) #1

tb2 = TravelBlog()
setattr(tb2, 'name', 'Италия')  # setattr() работает не только с классами, но и с их экземплярами.
setattr(tb2, 'days', '5')
TravelBlog.total_blogs += 1


# print(getattr(TravelBlog, 'total_blogs')) # 2
################################################################################################################################################
class TravelBlog:
    total_blogs = 0

    def __init__(self, name, days):
        self.name = name
        self.days = days
        self.__class__.total_blogs += 1


tb1 = TravelBlog('Франция', 6)
tb2 = TravelBlog('Италия', 5)


########################################################################
class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
[setattr(tb1, *i) for i in (('name', 'Франция'), ('days', 6))]
TravelBlog.total_blogs += 1
tb2 = TravelBlog()
[setattr(tb2, *i) for i in (('name', 'Италия'), ('days', 5))]
TravelBlog.total_blogs += 1


########################################################################
# увеличиваем счетчик при создании экземпляра, уменьшаем при удалении экземпляра

class TravelBlog:
    total_blogs = 0

    def __init__(self, name, days):
        self.name = name
        self.days = days
        self.__class__.total_blogs += 1

    def __del__(self):
        self.__class__.total_blogs -= 1


if __name__ == '__main__':
    tb1 = TravelBlog('Франция', 6)
    tb2 = TravelBlog('Италия', 5)


########################################################################
class TravelBlog:
    total_blogs = 0

    def __init__(self, name, days):
        TravelBlog.total_blogs += 1
        self.name = name
        self.days = days


tb1 = TravelBlog('Франция', 6)
tb2 = TravelBlog('Италия', 5)


########################################################################
# #Подвиг 9. Объявите класс с именем Figure и двумя атрибутами:
# # type_fig: 'ellipse'
# color: 'red'
# Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:
# # start_pt: (10, 5)
# end_pt: (100, 20)
# color: 'blue'
# Удалите из экземпляра класса свойство color и выведите на экран список всех локальных свойств (без значений) объекта
# fig1 в одну строчку через пробел в порядке, указанном в задании.#
class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color
print(*fig1.__dict__)


################################
class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = '(10, 5)'
fig1.end_pt = '(100, 20)'
fig1.color = 'blue'

delattr(Figure, 'color')
print(*fig1.__dict__)
print(*fig1.__dict__.keys())
[print(k, end=' ') for k, v in fig1.__dict__.items()]


########################################################################
# #Подвиг 10. Объявите класс с именем Person и атрибутами:
# # name: 'Сергей Балакирев'
# job: 'Программист'
# city: 'Москва'
# Создайте экземпляр p1 этого класса и проверьте, существует ли у него локальное свойство с именем job.
# Выведите True, если оно присутствует в объекте p1 и False - если отсутствует.
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print('job' in p1.__dict__)  # hasattr вернёт True, так как через пространство имен p1 мы получаем доступ к атрибуту


# класса, а нам нужно проверить, есть ли локальное свойство экземпляра класса
########################################################################
class Person:
    ...


my_dict = {'name': 'Сергей Балакирев', 'job': 'Программист', 'city': 'Москва'}
[setattr(Person, k, v) for k, v in my_dict.items()]
print(Person.__dict__)

p1 = Person()
print('job' in p1.__dict__)


######################################################################## self ########################################

# Подвиг 4. Объявите класс с именем MediaPlayer с двумя методами:
# open(file) - для открытия медиа-файла с именем file (создает локальное свойство filename со значением аргумента
# file в объекте класса MediaPlayer)
# play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение <название медиа-файла>")
# Создайте два экземпляра этого класса с именами: media1 и media2. Вызовите из них метод open() с аргументом
# "filemedia1" для объекта media1 и "filemedia2" для объекта media2. После этого вызовите через объекты метод play().
# При этом, на экране должно отобразиться две строки (без кавычек):
# "Воспроизведение filemedia1" "Воспроизведение filemedia2"
class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')

media1.play()
media2.play()


########################################################################  Egorof
# В предыдущей задачи вы могли обратить внимание на то, что выводится всегда одно и тоже имя робота
# в методе say_hello . Давайте это исправим при помощи атрибута экземпляра name . Для этого
# переопределяем класс Robot, в котором должны быть реализованы
# метод set_name , принимающий имя робота и сохраняющий его в атрибуте экземпляра name
# етод say_hello , Метод должен проверить, если у ЭК атрибут name . Если атрибут name  присутствует, необходимо
# напечатать фразу «Hello, human! My name is <name>». Если атрибут name  отсутствует у экземпляра, печатайте сообщение
# «У робота нет имени» метод say_bye ,  печатающий на экран фразу «See u later alligator»

class Robot:
    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print(f'У робота нет имени')

    def say_bye(self):
        print('See u later alligator')

    def set_name(self, name):
        self.name = name


c3po = Robot()
c3po.say_hello()  # печатает У робота нет имени
c3po.set_name('R2D2')
c3po.say_hello()  # печатает Hello, human! My name is R2D2
c3po.say_bye()  # печатает See u later alligator


########################################################################
class Robot:
    name = None

    def say_hello(self):
        if self.name:
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')

    def set_name(self, name):
        self.name = name


########################################################################
# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.В классе Counter нужно определить
# метод start_from, который принимает один необязательный аргумент - значение, с которого начинается подсчет, по
# умолчанию равно 0Также нужно создать метод increment, который увеличивает счетчик на 1.Затем необходимо создать
# метод display, который печатает фразу "Текущее значение счетчика = <value>" и метод reset,  который обнуляет
# экземпляр счетчика
class Counter:
    # def __init__(self):
    #     self.start = None

    def start_from(self, start=0):
        self.start = start

    def increment(self):
        self.start += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.start}')

    def reset(self):
        self.start = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display()  # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display()  # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display()  # печатает "Текущее значение счетчика = 4"


########################################################################
# Создайте класс Constructor, в котором реализованы
# метод add_atribute , принимающий на вход название атрибута в виде строки и его значение. При помощи
# функции setattr необходимо создать или изменить атрибут для ЭК, у которого этот метод был вызван
# метод display ,  печатающий на экран словарь __dict__ у ЭК
class Constructor:
    def add_attribute(self, attribute, value):
        setattr(self, attribute, value)  # Функция полезна в динамическом программировании, где имя атрибута не
        # статично. В этом случае мы не можем использовать оператор точки.

    # def add_attribute(self, *args):
    #     setattr(self, *args)

    def display(self):
        print(f'{self.__dict__}')


obj1 = Constructor()
obj1.display()  # печатает {}
obj1.add_attribute('color', 'red')
obj1.add_attribute('width', 20)
obj1.display()  # печатает {'color': 'red', 'width': 20}

obj2 = Constructor()
obj2.display()  # печатает {}
obj2.add_attribute('height', 100)
obj2.display()  # печатает {'height': 100}


########################################################################
class Constructor:
    def add_atribute(self, name, value):
        self.__dict__[name] = value

    def display(self):
        print(self.__dict__)


########################################################################
# Создайте класс Point. У этого класса должны быть
# метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр класса соответственн
# о в атрибуты x и y метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние
# между двумя точками по теореме Пифагора. В случае, если в данный метод передается не экземпляр класса Point
# необходимо вывести сообщение "Передана не точка"

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, object):
        # if isinstance(self.x, Point) and isinstance(self.y, Point):
        if isinstance(object, Point):
            return ((self.x - object.x) ** 2 + (self.y - object.y) ** 2) ** 0.5
        else:
            print(f'Передана не точка')


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)  # вернёт 5.0
p1.get_distance(10)  # Распечатает "Передана не точка"


########################################################################
def get_distance(self, obj: 'Point'):
    """Метод принимает объект и возвращает расстояние между
    двумя объектами (точками)."""
    try:
        return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
    except AttributeError:
        print('Передана не точка')
    ########################################################################
    # Функция hasattr() проверяет существование атрибута с именем name в объекте object.


def get_distance(self, t):
    if hasattr(t, 'x') and hasattr(t, 'y'):
        return ((self.x - t.x) ** 2 + (self.y - t.y) ** 2) ** 0.5
    else:
        print('Передана не точка')


########################################################################
# Подвиг 5. Объявите класс с именем Graph и методами:
# set_data(data) - передача набора данных data для последующего отображения (data - список числовых данных);
# draw() - отображение данных (в том же порядке, что и в списке data)и атрибутом:LIMIT_Y = [0, 10]
# Метод set_data() должен формировать локальное свойство data объекта класса Graph. Атрибут data должен ссылаться на
# переданный в метод список. Метод draw() должен выводить на экран список в виде строки из чисел, разделенных пробелами
# и принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).Создайте объект graph_1 класса Graph,
# вызовите для него метод set_data() и передайте список:[10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
# Затем, вызовите метод draw() через объект graph_1. На экране должна появиться строка с соответствующим набором
# чисел, записанных через пробел. Например (вывод без кавычек):"10 0 2 5 7"
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        for i in self.data:
            if i in list(range(*self.LIMIT_Y)) + [self.LIMIT_Y[-1]]:
                print(i, end=' ')


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


########################################################################
def draw(self):
    print(*(filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[-1], self.data)))
    print(' '.join(map(str, filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[-1], self.data))))

    ########################################################################
    def draw(self):
        a, b = self.LIMIT_Y
        print(*(filter(lambda x: a <= x <= b, self.data)))


########################################################################
# Подвиг 7. Имеется следующий класс для считывания информации из входного потока:
# Которым, затем, можно воспользоваться следующим образом:
# sr = StreamReader()
# data, result = sr.readlines()
# Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
# def create(self, fields, lst_values): ...
# который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields) и список
# строк lst_in (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с
# именами полей из fields и соответствующими значениями из lst_values.Если создание локальных свойств проходит
# успешно, то метод create() возвращает True, иначе - False. Если число полей и число строк не совпадает,
# то метод create() возвращает False и локальные атрибуты создавать не нужно.
# понимания учащимися разницы между локальными атрибутами и атрибутами классов
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for key, value in zip(fields, lst_values):
                # for key, value in dict(zip(fields, lst_values)).items():
                if setattr(self, key, value):
                    continue
                else:
                    False
        else:
            return False
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        # lst_in = list(map(str.strip, sys.stdin.readlines()))
        lst_in = [10, 'Питон - основы мастерства', 512]
        sd = StreamData()  # экземпляр класса
        res = sd.create(self.FIELDS, lst_in)  # True or False
        return sd, res


sr = StreamReader()
data, result = sr.readlines()

print(data, result)  # <__main__.StreamData object at 0x000002C5BE85F410> True
print(data.__dict__)  # {'id': 10, 'title': 'Питон - основы мастерства', 'pages': 512}


# вывод списка атрибутов объекта data
# для этого и нужно делать проверку "print(data.__dict__)". Чтобы убедиться что в экземпляре класса появились все
# атрибуты со значениями.(data.__dict__ --> не должен быть пустым, а содержать как написано в условии <<локальные
# свойства с именами полей из FIELDS и соответствующими значениями из lst_in.>>)Ваш метод класса "create()"
# создает два атрибута со значениями списков.К примеру:FIELDS = ('id', 'title', 'pages')
# lst_in = [10, 'eeeee', 124]Нужно создать три атрибута 'id', 'title' , 'pages' со значениями [10, 'eeeee', 124]
# соответственно (self.id = 10, self.title = 'eeeee', self.pages = 124)
########################################################################
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for i, k in enumerate(fields):
            setattr(self, k, lst_values[i])
        return True

    ########################################################################
    def create(self, fields, lst_values):
        self.__dict__ = dict(zip(fields, lst_values))
        return len(lst_values) == len(fields)


########################################################################
class StreamData:

    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for k, v in zip(fields, lst_values):
                self.__dict__[k] = v
                self.k = v  # не работает т.к. 'к' каждый раз перезаписывается на новое значение и в итоге пока
                # не дойдёт до последнего значения
            return True
        return False


########################################################################
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            self.__dict__.update(dict(zip(fields, lst_values)))
        return bool(self.__dict__)


########################################################################
class StreamData:  # здесь объявляется класс StreamData
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):  # Если кол-во элементов fields и lst_values не равны то return False и
            return False  # локальные свойства не создадутся
        else:
            self.__dict__ = dict(zip(fields, lst_values))  # локальные свойства экз-ра класса будут создоваться
            # из эл-тов fields и lst_values и устан. в  self.__dict__
            return True  # возвращает True


########################################################################
# Подвиг 9. Из входного потока читаются строки данных с помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# в формате: id, name, old, salary (записанные через пробел). Например:
# 1 Сергей 35 1200002 Федор 23 120003 Иван 13 1200...То есть, каждая строка - это элемент списка lst_in.
# Необходимо в класс DataBase:
# class DataBase:
# lst_data = []
# FIELDS = ('id', 'name', 'old', 'salary')
# добавить два метода:select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b]
# (включительно) по их индексам (не id, а индексам списка); также учесть, что граница b может превышать
# длину списка.insert(self, data) - для добавления в список lst_data новых данных из переданного списка
# строк data;
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a: b + 1]

    def insert(self, data):
        for i in data:
            self.lst_data.append(dict(zip(self.FIELDS, i.split())))


db = DataBase()
db.insert(lst_in)
db.select(0, 50)

print(DataBase.lst_data)
print(DataBase.__dict__)
########################################################################
# Подвиг 10. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
# add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже
# существует, то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать);
# если связка eng-rus уже существует, то второй раз ее добавлять не нужно, например:  add('go', 'идти'),
# add('go', 'идти');remove(self, eng) - для удаления связки по указанному английскому слову;
# translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов,
# соответствующих переводу английского слова, даже если в списке всего одно слово).Все добавления и удаления
# связок должны выполняться внутри каждого конкретного объекта класса Translator, т.е. связки хранить
# локально внутри экземпляров классов класса Translator.Создайте экземпляр tr класса Translator и вызовите
# метод add для следующих связок:# tree - дерево
# car - машинаcar - автомобильleaf - листriver - рекаgo - идтиgo - ехатьgo - ходитьmilk - молоко
# Затем методом remove() удалите связку для английского слова car. С помощью метода translate() переведите
# слово go. Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['tree - дерево', 'car - машина', 'car - автомобиль', 'leaf - лист', 'river - река', 'go - идти', 'go - ехать',
          'go - ходить', 'milk - молоко']


class Translator:

    def add(self, eng, rus):
        if 'd' not in self.__dict__:
            self.d = {}
        self.d.setdefault(eng, [])
        if rus not in self.d[eng]:
            self.d[eng].append(rus)

    def remove(self, eng):
        self.__dict__.pop(eng)

    def translate(self, eng):
        return self.__dict__[eng]


tr = Translator()
for i in lst_in:
    tr.add(*map(str.strip, i.split('-')))
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')
print(tr.translate('go'))


########################################################################
########################################################################
def add(self, eng, rus):
    if 'd' not in self.__dict__:
        self.d = {}
    if eng not in self.d:
        self.d[eng] = [rus]
    else:
        self.d[eng].append(rus)
        # self.d[eng] += [rus]


########################################################################
def add(self, eng, rus):
    if 'd' not in self.__dict__:
        self.d = {}
    self.d.setdefault(eng, []).append(rus)  # но здесь перезапись кода


########################################################################
# 2.2 Инициализация объекта. Метод init  Egorof
########################################################################
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.price = price
        self.model = model
        # self.laptop_name = brand + ' ' + model
        self.laptop_name = self.brand + " " + self.model
        # self.laptop_name = f'{brand} {model}'


#
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price)  # выводит 57000
# print(hp.laptop_name)  # выводит "hp 15-bw0xx"
laptop1 = Laptop('lenovo', 'z-570-dx', 10)
laptop2 = Laptop('lenovo', 'z-570-dx', 20)


########################################################################
class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, count=1):
        self.goals += count

    def make_assist(self, count=1):
        self.assists += count

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()  # выводит "Messi Leo - голы: 700, передачи: 500"

kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()  # выводит "Kokorin Alex - голы: 1, передачи: 0"


########################################################################
class Zebra:
    def __init__(self):
        self.pr = 'Полоска белая'

    def which_stripe(self):
        if self.pr == 'Полоска белая':
            print(self.pr)
            self.pr = 'Полоска черная'

        elif self.pr == 'Полоска черная':
            print(self.pr)
            self.pr = 'Полоска белая'


z1 = Zebra()
z1.which_stripe()  # печатает "Полоска белая"
z1.which_stripe()  # печатает "Полоска черная"
z1.which_stripe()  # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()  # печатает "Полоска белая"


########################################################################
def __init__(self):
    self.stripe = ["Полоска белая", "Полоска черная"]


def which_stripe(self):
    print(self.pr[0])
    self.pr[0], self.pr[1] = self.pr[1], self.pr[0]


########################################################################
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return True if self.age >= 18 else False


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult())  # выводит "True"


########################################################################

########################################################################
##########      1.5 Инициализатор __init__ и финализатор __del__
########################################################################
# Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')Здесь первые два значения - это координаты точки на плоскости (локальные свойства x,
# y), а третий необязательный аргумент - цвет точки (локальное свойство color). Если цвет не указывается,
# то он по умолчанию принимает значение black.Создайте тысячу таких объектов с координатами (1, 1), (3, 3),
# (5, 5), ... то есть, с увеличением на два для каждой новой точки. Каждый объект следует поместить в список
# points (по порядку). Для второго объекта в списке points укажите
# список points должен находится вне объявленного класса и должен содержать не значение переменных
# [[1, 1, 'black], [3, 3, 'yellow'], [5, 5, 'black'], ............],а ссылку на создаваемый экземпляр
# [<__main__.Point object at 0x7f4c8218ca60>, <__main__.Point object at 0x7f4c821c1ca0>,
# Грубо говоря мы добавляем в список объявленный класс со значениями.!!!
class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) for i in range(1, 2000, 2)]
points[1].color = 'yellow'


################################
class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
for i in range(1, 2000, 2):
    if i >= 3:
        points.append(Point(i, i, color='yellow'))
    else:
        points.append(Point(i, i))
################################
points = [Point(i, i) if i < 3 else Point(i, i, color='yellow') for i in range(1, 2000, 2)]


################################################################ несовсем по заданию
class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color
        self.points = [(self.x, self.y, self.color)]

    def set_points(self):
        self.x += 2
        self.y += 2
        self.color = 'yellow'
        self.points.append((self.x, self.y, self.color))


pt = Point(1, 1)
for i in range(999):
    pt.set_points()
print(pt.__dict__['points'])  # [(1, 1, 'black'), (3, 3, 'yellow'), (5, 5, 'yellow'), (7, 7, 'yellow'),


#######################################################################
class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
pt = Point(1, 1)
points.append((pt.x, pt.y, pt.color))
for i in range(2, 2000, 2):
    points.append((pt.x + i, pt.y + i, 'yellow'))
print(points[:10])  # [(1, 1, 'black'), (3, 3, 'yellow'), (5, 5, 'yellow')


########################################################################
class Point:
    points = []

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


pt = Point(1, 1)

Point.points.append((pt.x, pt.y, pt.color))

for i in range(2, 2000, 2):
    Point.points.append((pt.x + i, pt.y + i, 'yellow'))
print(Point.points[:10])  # [(1, 1, 'black'), (3, 3, 'yellow'), (5, 5, 'yellow')
########################################################################
# Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты
# Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные
# числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний
# левый) в виде кортежей (a, b) и (c, d) соответственно.Сформируйте 217 объектов этих классов: для каждого текущего
# объекта класс выбирается случайно (или Line, или Rect, или Ellipse). Координаты также генерируются случайным
# образом (числовые значения). Все объекты сохраните в списке elements.В списке elements обнулите координаты объектов
# только для класса Line.

from random import randint as r_int, choice as r_choice


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
# elements.append(Line(0,0,0,0))
for i in range(217):
    a, b, c, d = r_int(1, 10), r_int(1, 10), r_int(1, 10), r_int(1, 10)
    elements.append(r_choice([Line, Rect, Ellipse])(a, b, c, d))

for i in elements:
    if isinstance(i, Line):
        # if type(i) == Line:
        i.sp = i.ep = (0, 0)
        # Line.sp = Line.ep = (0, 0) #так не работает


########################################################################
# Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:
# tr = TriangleChecker(a, b, c)
# Здесь a, b, c - длины сторон треугольника.# В классе TriangleChecker необходимо объявить метод is_triangle(),
# который бы возвращал следующие коды:1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно
# число меньше или равно нулю;2 - указанные числа a, b, c не могут являться длинами сторон треугольника;3 - стороны
# a, b, c образуют треугольник.Проверку параметров a, b, c проводить именно в таком порядке.Прочитайте из входного
# потока строку, содержащую три числа, разделенных пробелами, командой:
# a, b, c = map(int, input().split())Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные
# значения a, b, c. Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) not in (int, float) or type(self.b) not in (int, float) or type(self.c) not in (
                int, float) or self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1
        elif self.a + self.b < self.c or self.b + self.c < self.a or self.a + self.c < self.b:
            return 2
        else:
            return 3


tr = TriangleChecker(3, 4, 5)
print(tr.is_triangle())


########################################################################
def is_triangle(self):
    if not all(map(lambda x: type(x) in (int, float), [self.a, self.b, self.c])):
        return 1
    # if not all(type(i) in (int, float) for i in [self.a, self.b, self.c]):
    if not all(map(lambda x: x > 0, [self.a, self.b, self.c])):
        # if not all(type(i) in (int, float) and i > 0 for i in [self.a, self.b, self.c]):
        return 1
    lst = sorted([self.a, self.b, self.c])
    if lst[0] + lst[1] < lst[2]:
        return 2
    return 3


########################################################################
class TriangleChecker:
    def __init__(self, a, b, c):
        self.lst = [a, b, c]  ## []

    def is_triangle(self):
        for num in self.lst:
            if not isinstance(num, int) or num <= 0:
                return 1
        if max(self.lst) >= sum(self.lst) - max(self.lst):
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


########################################################################
class TriangleChecker:
    def __init__(self, a, b, c):
        self.s = [a, b, c]

    def is_triangle(self):
        if min(self.s) <= 0:
            return 1
        if max(self.s) * 2 >= sum(self.s):
            return 2
        return 3


########################################################################
class TriangleChecker:
    def __init__(self, *args):
        self.args = args

    def is_triangle(self):
        if not all(type(i) in (int, float) and i > 0 for i in self.args):
            # if any(type(i) in (int, float) and i <= 0 for i in self.args):
            return 1
        a = sorted(self.args)
        if sum(a[:2]) <= a[-1]:
            return 2
        return 3

    ########################################################################
    def is_triangle(self):
        # print(self.__dict__.values())  # dict_values([3, 4, 5])
        lst = self.__dict__.values()
        for i in lst:
            if not isinstance(i, (int, float)) or i <= 0:
                return 1

        a, b, c = sorted(lst)  # 3 4 5
        if c >= a + b:
            return 2
        return 3


########################################################################
# Подвиг 6. Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:
# data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать
# копию переданного списка);
# is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);
# В этом классе объявите следующие методы:
# set_data(self, data) - для передачи нового списка данных в текущий график;
# show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
# show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое ...
# show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая..
# set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.
# Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить
# сообщение:"Отображение данных закрыто"Прочитайте из входного потока числовые данные с помощью команды:
# Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод set_show()
# со значением fl_show = False и вызовите метод show_table(). На экране должны отобразиться две соответствующие строки.
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        # self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data):
        self.data = data[:]
        # self.data = data.copy()

    def show_table(self):
        if self.is_show == False:
            self.closed_get()
        else:
            print(*self.data)

    def closed_get(self):
        print(f'Отображение данных закрыто')

    def show_graph(self):
        if self.is_show == False:
            self.closed_get()
        else:
            print('Графическое отображение данных:', *self.data)

    def show_bar(self):
        if self.is_show == False:
            self.closed_get()
        else:
            print('Столбчатая диаграмма:', *self.data)

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()


########################################################################
class Graph:
    def __init__(self, data):
        self.data = data
        self.is_show = True

    def check_show(func):
        def wrapper(self):
            if self.is_show == False:
                return print('Отображение данных закрыто')
            else:
                return func(self)

        return wrapper

    def set_data(self, data):
        self.data = data

    @check_show
    def show_table(self):
        return ' '.join(map(str, self.data))

    @check_show
    def show_graph(self):
        print(f"Графическое отображение данных: {self.show_table()}")

    @check_show
    def show_bar(self):
        print(f'Столбчатая диаграмма: {self.show_table()}')

    def set_show(self, fl_show):
        self.is_show = fl_show


########################################################################
# Подвиг 7. Объявите в программе следующие несколько классов:CPU - класс для описания процессоров;Memory - класс для
# описания памяти;MotherBoard - класс для описания материнских плат.Обеспечить возможность создания объектов
# каждого класса командами:cpu = CPU(наименование, тактовая частота)mem = Memory(наименование, размер памяти)
# mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)Обратите внимание при создании объекта
# класса MotherBoard можно передавать несколько объектов класса Memory, максимум N - по числу слотов памяти на
# материнской плате (N = 4).Объекты классов должны иметь следующие локальные свойства:для класса CPU: name -
# наименование; fr - тактовая частота;для класса Memory: name - наименование; volume - объем памяти;
# для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число
# лотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - список из объектов класса
# Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).Класс MotherBoard должен иметь
# метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате в виде следующего
# списка из четырех строк:['Материнская плата: <наименование>','Центральный процессор: <наименование>,
# <тактовая частота>','Слотов памяти: <общее число слотов памяти>','Память: <наименование_1> - <объем_1>;
# <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']Создайте объект mb класса MotherBoard с
# одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
class CPU:
    def __init__(self, name: str, fr: int):
        self.name = name  # наименование процессора
        self.fr = fr  # тактовая частота


class Memory:
    def __init__(self, name: str, volume: int):
        self.name = name  # наименование памяти
        self.volume = volume  # объем памяти


class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]
        # self.mem_slots = [mem for i, mem in enumerate(mem_slots) if i < self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.name}, {self.CPU.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память:' + '; '.join(map(lambda x: f'{self.Memory.name}-{self.volume}', self.mem_slots))]


# вызов стороннего класса ч/з 2 варианта CPU {self.name}, {self.CPU.fr} и Memory {self.Memory.name}-{self.volume}

mb = MotherBoard('Motherboard', CPU('intel', 1000), Memory('asrock', 1), Memory('asrock', 2))


########################################################################
class MotherBoard:
    def __init__(self, name: str, cpu_obj: CPU, mem_slots: list, total_mem_slots=4):
        self.name = name  # наименование платы
        self.cpu = cpu_obj  # ссылка на объект класса CPU, cpu_obj - объект класса CPU
        self.mem_slots = mem_slots  # список из объектов класса Memory
        self.total_mem_slots = total_mem_slots  # общее число слотов памяти

        def get_config(self):
            st_memory = []
            for m in self.mem_slots:
                st_memory.append(f"{m.name} - {m.volume}")

            lst_config = [f"Материнская плата: {self.name}",
                          f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                          f"Слотов памяти: {self.total_mem_slots}",
                          f"Память: {'; '.join(st_memory)}"
                          ]
            return lst_config

    m1 = Memory("Kingstone_1", 1024)
    m2 = Memory("Kingstone_2", 2048)
    mb = MotherBoard(name="GIGABYTE", cpu=CPU("Pentium", 2600), mem_slots=[m1, m2])


########################################################################
# Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:cart = Cart()
# Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки (объекты классов
# Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.В классе Cart объявить методы:add(self, gd)
# - добавление в корзину товара, представленного объектом gd;remove(self, indx) - удаление из корзины товара по
# индексу indx;get_list(self) - получение из корзины товаров в виде списка из строк:['<наименовние_1>: <цена_1>',
# '<наименовние_2>: <цена_2>',..'<наименовние_N>: <цена_N>']Объявите в программе следующие классы для описания
# товаров:Table - столы;TV - телевизоры;Notebook - ноутбуки;Cup - кружки.Объекты этих классов должны создаваться
# командой:gd = ИмяКласса(name, price)Каждый объект классов товаров должен содержать локальные свойства:
# name - наименование;price - цена.Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV),
# один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        # del self.goods[indx]
        # self.goods.remove(indx)
        self.goods.pop(indx)

    def get_list(self):
        return [f"{obj.name}: {obj.price}" for obj in self.goods]  # ['sums: 11', 'LG: 34', 'ikea: 45'
        # return list(map(lambda x: f'{x.name}: {x.price}', self.goods))   #['sums: 11', 'LG: 34', 'ikea: 45'


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
lst = [TV("sums", 11), TV("LG", 34), Table("ikea", 45), Notebook("msi", 53), Notebook("apple", 52), Cup("keep", 43)]
for i in lst:
    cart.add(i)


# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1 = Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)
# cart.add(tv1)
# cart.add(tv2)
# cart.add(table)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)

# cart.add(TV('Samsung', 12990))
# cart.add(TV('Sony', 39990))
# cart.add(Table('Решка', 6350))
# cart.add(Notebook('Acer', 35990))
# cart.add(Notebook('Asus', 75990))
# cart.add(Cup('Керамика', 350))
########################################################################
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # первый аргумент - имя класса
        # второй - кортеж с классами, откуда наследоваться
        # третий - словарь с атрибутами ключ-значение

    def __str__(self):
        return f'{self.name}: {self.price}'

    @classmethod
    def create(cls, product_name):
        return type(product_name, (cls,), {})


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def get_list(self):
        return [str(gd) for gd in self.goods]

    def remove(self, indx):
        self.goods.pop(indx)


TV = Product.create("TV")
Table = Product.create("Table")
Notebook = Product.create("Notebook")
Cup = Product.create("Cup")

cart = Cart()
gd = TV("рубин", 500)
cart.add(gd)
gd = TV("стекло", 300)
cart.add(gd)
gd = Table("фанера", 1000)
cart.add(gd)
gd = Notebook("Эльбрус", 9000)
cart.add(gd)
gd = Notebook("Байкал", 8000)
cart.add(gd)
gd = Cup("дешёвая", 100)
cart.add(gd)


########################################################################
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f"{good.name}: {good.price}" for good in self.goods]


class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Products):
    pass


class TV(Products):
    pass


class Notebook(Products):
    pass


class Cup(Products):
    pass


cart = Cart()
cart.add(TV('LG 32LP500B6LA', 750))
cart.add(TV("Samsung UE50AU7570UXRU", 2000))
cart.add(Table("ArtGlass", 160))
cart.add(Notebook("ASUS TUF Gaming Dash F15 FX516PM-HN023", 6400))
cart.add(Notebook("Lenovo Legion 5 15IMH6 (82NL0035RK)", 4000))
cart.add(Cup("Beeztees Игрушка Рождественская кружка", 15))


#######################################################################
class Good:
    def __init__(self, name, price):
        self.name, self.price = name, price

    def __str__(self):
        return f'{self.name}: {self.price}'


class Table(Good): pass


class TV(Good): pass


class Notebook(Good): pass


class Cup(Good): pass


class Cart:
    goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        return self.goods.pop(indx)

    def get_list(self):
        return list(map(Good.__str__, self.goods))


cart = Cart()
cart.add(TV('LG', 50000))


########################################################################
class Merchandise:
    def __init__(self, name, price):
        self.name, self.price = name, price

    def __str__(self):
        return f'{self.name}: {self.price}'


class Table(Merchandise): pass


class TV(Merchandise): pass


class Notebook(Merchandise): pass


class Cup(Merchandise): pass


class Cart:
    def __init__(self, goods):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return list(map(str, self.goods))


goods = [TV("samsung", 1111), TV("LG", 1234), Table("ikea", 2345),
         Notebook("msi", 5433), Notebook("apple", 542), Cup("keepcup", 43)]
cart = Cart(goods)
########################################################################
# Подвиг 9. Вам необходимо реализовать односвязный список (не список языка Python, объекты в списке не хранить, а
# формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:Для этого объявите в программе
# класс ListObject, объекты которого создаются командой:obj = ListObject(data) Каждый объект класса ListObject должен
# содержать локальные свойства:next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет,
# то next_obj = None);data - данные объекта в виде строки.В самом классе ListObject должен быть объявлен метод:
# link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj
# объекта self должен ссылаться на obj).Прочитайте список строк из входного потока командой:
# lst_in = list(map(str.strip, sys.stdin.readlines()))Затем сформируйте односвязный список, в объектах которых
# (в атрибуте data) хранятся строки из списка lst_in (первая строка в первом объекте, вторая - во втором и  т.д.).
# На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.
# #Нужно создать экземпляры класса ListObject в количестве равном числу строк в переменной lst_in. Имя имеет только
# первый экземпляр. Остальные существуют в виде ссылки, которая прописана в предыдущем экземпляре. Ну это если совсем
# грубо. Получается такая конструкция, в которой к экземплярам (кроме первого) нельзя обратиться напрямую, а только
# вызвав из предыдущего экземпляр

# создать пустой список , потом циклом пройтись по lst_in и наполнить тот наш пустой список обьектами класса(то есть
# нужно их тут создать). Далее другим циклом пройтись по этому нашему списку(в котором теперь у нас лежат наши обьекты)
# , вызывая при этом метод link для каждого нашего обьекта( и передавая соответственно нужные ему аргументы), другими
# словами наполняя ссылками сами обьекты: l[i].link(l[i+1]) , где l это как раз таки наш список с обьектами, но будьте
# внимательными чтобы индекс не выходил за пределы списка, а так же, что нужно оставить последнему обьекту ссылку на
# None(проще говоря делайте цикл на количество строк в этом списке и потом сделайте условие if i < len(l)-1: )
import sys


class ListObject:
    def __init__(self, data: str):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['1. Первые шаги в ООП', '1.1 Как правильно проходить этот курс', '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов', '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del', '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
lst = []
for i in lst_in:
    obj = ListObject(i)
    lst.append(obj)

for i in range(len(lst)):
    if i < len(lst) - 1:
        lst[i].link(lst[i + 1])

head_obj = lst[0]
########################################################################
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):  # если будет срез - то большие затраты памяти тк создаётся копия lst
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)  # obj_new добавляем в конец объекта obj
    obj = obj_new
########################################################################
class ListObject:
    def __init__(self, data: str):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj.link(ListObject(lst_in[i]))
    obj = obj.next_obj
########################################################################
objects = [ListObject(x) for x in lst_in]
for i in range(len(lst_in)-1):
    objects[i].link(objects[i+1])

head_obj = objects[0]
########################################################################
lst = [ListObject(i) for i in lst_in]
for i in range(len(lst_in) - 1):
    lst[i].link((lst[i + 1]))
head_obj = lst[0]
########################################################################
#Большой подвиг 10. Объявите два класса:Cell - для представления клетки игрового поля;GamePole - для управления
# игровым полем, размером N x N клеток.С помощью класса Cell предполагается создавать отдельные клетки командой:
# c1 = Cell(around_mines, mine)Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина
# (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться
# локальные свойства:around_mines - число мин вокруг клетки (начальное значение 0);mine - наличие мины в текущей клетке
# (True/False);fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).
# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
# pole_game = GamePole(N, M)Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется
# объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта
# класса GamePole.В классе GamePole должны быть также реализованы следующие методы:init() - инициализация поля с новой
# расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается
# символ #).При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для
# первоначальной инициализации игрового поля.В классе GamePole могут быть и другие вспомогательные методы.Создайте
# экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.


########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################
#######################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################
#######################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################
#######################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################
#######################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################
#######################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################

########################################################################
