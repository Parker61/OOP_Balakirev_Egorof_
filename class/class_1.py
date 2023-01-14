

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
    def open(self,file):
        self.filename=file

    def play(self):
        print(f'Воспроизведение {self.filename}')


media1=MediaPlayer()
media2=MediaPlayer()
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
#Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.В классе Counter нужно определить
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
        setattr(self, attribute, value) #Функция полезна в динамическом программировании, где имя атрибута не
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
#Создайте класс Point. У этого класса должны быть
# метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр класса соответственн
# о в атрибуты x и y метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние
# между двумя точками по теореме Пифагора. В случае, если в данный метод передается не экземпляр класса Point
# необходимо вывести сообщение "Передана не точка"

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self,object):
        # if isinstance(self.x, Point) and isinstance(self.y, Point):
        if isinstance(object, Point):
            return ((self.x - object.x)**2 + (self.y - object.y)**2)**0.5
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
#Функция hasattr() проверяет существование атрибута с именем name в объекте object.
   def get_distance(self,t):
        if hasattr(t,'x') and hasattr(t,'y'):
            return ((self.x-t.x)**2+(self.y-t.y)**2)**0.5
        else:
            print('Передана не точка')
########################################################################
#Подвиг 5. Объявите класс с именем Graph и методами:
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
        a,b=self.LIMIT_Y
        print(*(filter(lambda x: a <= x <= b, self.data)))
########################################################################
#Подвиг 7. Имеется следующий класс для считывания информации из входного потока:
#Которым, затем, можно воспользоваться следующим образом:
# sr = StreamReader()
# data, result = sr.readlines()
# Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
# def create(self, fields, lst_values): ...
# который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields) и список
# строк lst_in (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с
# именами полей из fields и соответствующими значениями из lst_values.Если создание локальных свойств проходит
# успешно, то метод create() возвращает True, иначе - False. Если число полей и число строк не совпадает,
# то метод create() возвращает False и локальные атрибуты создавать не нужно.
#понимания учащимися разницы между локальными атрибутами и атрибутами классов
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
class StreamData:   # здесь объявляется класс StreamData
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):  # Если кол-во элементов fields и lst_values не равны то return False и
            return False                    # локальные свойства не создадутся
        else:
            self.__dict__ = dict(zip(fields, lst_values))  # локальные свойства экз-ра класса будут создоваться
                                                           # из эл-тов fields и lst_values и устан. в  self.__dict__
            return True  # возвращает True
########################################################################
#Подвиг 9. Из входного потока читаются строки данных с помощью команды:
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
#Подвиг 10. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
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
    self.d.setdefault(eng, []).append(rus) # но здесь перезапись кода
########################################################################
#2.2 Инициализация объекта. Метод init  Egorof
########################################################################
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.price = price
        self.model = model
        # self.laptop_name = brand + ' ' + model
        self.laptop_name=self.brand+" "+self.model
        #self.laptop_name = f'{brand} {model}'

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
        self.goals+=count

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
#Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:
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
print(pt.__dict__['points']) #[(1, 1, 'black'), (3, 3, 'yellow'), (5, 5, 'yellow'), (7, 7, 'yellow'),
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
print(points[:10]) #[(1, 1, 'black'), (3, 3, 'yellow'), (5, 5, 'yellow')
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
#Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты
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
#Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:
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
    if not all(type(i) in (int, float) for i in [self.a, self.b, self.c]):
    # if not all(map(lambda x: x > 0, [self.a, self.b, self.c])):
    # if not all(type(i) in (int, float) and i > 0 for i in [self.a, self.b, self.c]):
        return 1
    lst = sorted([self.a, self.b, self.c])
    if lst[0] + lst[1] < lst[2]:
        return 2
    return 3
########################################################################
class TriangleChecker:
    def __init__(self, a, b, c):
        self.lst = [a, b, c]

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
        abc = sorted(self.args)
        if sum(abc[:2]) <= abc[-1]:
            return 2
        return 3
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
