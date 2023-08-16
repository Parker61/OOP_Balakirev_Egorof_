# ___4.5 Полиморфизм и абстрактные методы
# 4.5 Полиморфизм и абстрактные методы___


# Подвиг 3. В программе объявлены два класса:
# class Mentor:
# Первый класс описывает студентов, а второй - менторов. Вам поручается на основе базового класса Mentor разработать еще два дочерних класса:
# # Lector - для описания лекторов;# Reviewer - для описания экспертов.# # Объекты этих классов должны создаваться
# командами:# # lector = Lector(fio, subject)# reviewer = Reviewer(fio, subject)
# где fio - ФИО (строка); subject - предмет (строка). Инициализации этих параметров (fio, subject) должна выполняться
# базовым классом Mentor.# В самих классах Lector и Reviewer необходимо объявить метод:
# def set_mark(self, student, mark): ...# для простановки оценки (mark) студенту (student). Причем, в классе Lector
# оценки добавляются в список _lect_marks объекта класса Student, а в классе Reviewer - в список _house_marks.
# Используйте для этого методы add_lect_marks() и add_house_marks() класса Student.# Также в классах Lector и Reviewer
# должен быть переопределен магический метод:# __str__() для формирования следующей информации об объектах:
# - для объектов класса Lector: Лектор <ФИО>: предмет <предмет> - для объектов класса Reviewer: Эксперт <ФИО>:
# предмет <предмет>

class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject


class Lector(Mentor):
    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f'Лектор {self._fio}: предмет {self._subject}'


class Reviewer(Mentor):
    def set_mark(self, student, mark):
        student.add_house_marks(mark)

    def __str__(self):
        return f'Эксперт {self._fio}: предмет {self._subject}'


# __str__ и set_mark и представляют собой полиморфиз

lector = Lector("Балакирев С.М.", "Информатика")
reviewer = Reviewer("Гейтс Б.", "Информатика")
students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
persons = [lector, reviewer]
lector.set_mark(students[0], 4)
lector.set_mark(students[1], 2)
reviewer.set_mark(students[0], 5)
reviewer.set_mark(students[1], 3)
for p in persons + students:
    print(p)


# # в консоли будет отображено:
# # Лектор Балакирев С.М.: предмет Информатика
# # Эксперт Гейтс Б.: предмет Информатика
# # Студент Иванов А.Б.: оценки на лекциях: [4]; оценки за д/з: [5]
# # Студент Гаврилов С.А.: оценки на лекциях: [2]; оценки за д/з: [3]

################################################################################
class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

    def __str__(self):
        return f'{self._name} {self._fio}: предмет {self._subject}'


class Lector(Mentor):
    _name = 'Лектор'

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)


class Reviewer(Mentor):
    _name = 'Эксперт'

    def set_mark(self, student, mark):
        student.add_house_marks(mark)


################################################################################################
# Подвиг 4. Вам необходимо объявить базовый класс ShopInterface с абстрактным методом:def get_id(self): ...
# В самом методе должно генерироваться исключение командой:raise NotImplementedError('в классе не переопределен метод
# get_id')Инициализатор в классе ShopInterface прописывать не нужно.Далее объявите дочерний класс ShopItem
# (от базового класса ShopInterface), объекты которого создаются командой:item = ShopItem(name, weight, price)
# где name - название товара (строка); weight - вес товара (любое положительное число); price - цена товара
# (любое положительное число).В каждом объекте класса ShopItem должны формироваться локальные атрибуты с именами
# _name, _weight, _price и соответствующими значениями. Также в объектах класса ShopItem должен автоматически
# формироваться локальный приватный атрибут __id с уникальным (для каждого товара) целым значением.
# В классе ShopItem необходимо переопределить метод get_id() базового класса так, чтобы он (метод) возвращал
# значение атрибута __id.
class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):

    def __init__(self, name, weight, price):
        self._name, self._weight, self._price = name, weight, price
        self.__id = id(self)

    def get_id(self):
        return self.__id


################################################################################
class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    last_id = 1

    def __init__(self, name, weight, price):
        self._name, self._weight, self._price = name, weight, price
        self.__id = self.last_id
        type(self).last_id += 1

    # type вернёт ссылку на класс, к которому принадлежит объект (self - ссылка на объект).
    def get_id(self):
        return self.__id


################################################################################################
class ShopItem(ShopInterface):
    last_id = 1

    def __init__(self, name, weight, price):
        self._name, self._weight, self._price = name, weight, price
        self.__id = self.last_id
        __class__.last_id += 1


################################################################################
class ShopItem(ShopInterface):
    last_id = 1

    def __init__(self, name, weight, price):
        self._name, self._weight, self._price = name, weight, price
        self.__id = __class__.last_id
        __class__.last_id += 1


################################################################################################
# self.__id = hash((self._name, self._weight, self._price))
################################################################################
class ShopItem(ShopInterface):
    last_id = 0

    def __new__(cls, *args, **kwargs):
        cls.last_id += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self._name, self._weight, self._price = name, weight, price
        self.__id = __class__.last_id


################################################################################################
# Подвиг 5. Ранее вы уже создавали классы валидации в виде иерархии базового класса Validator и дочерних:
# StringValidator# IntegerValidator# FloatValidator# для валидации (проверки) корректности данных. Повторим этот
# функционал с некоторыми изменениями.# # Итак, вначале нужно объявить базовый класс Validator, в котором должен
# отсутствовать инициализатор (магический метод __init__) и объявлен метод со следующей сигнатурой:#
# def _is_valid(self, data): ...# # По идее, этот метод возвращает булево значение True, если данные (data)
# корректны с точки зрения валидатора, и False - в противном случае. Но в базовом классе Validator он должен
# генерировать исключение командой: # raise NotImplementedError('в классе не переопределен метод _is_valid')
# Затем, нужно объявить дочерний класс FloatValidator для валидации вещественных чисел. Объекты этого класса
# создаются командой:# # float_validator = FloatValidator(min_value, max_value)# где min_value - минимально
# допустимое значение; max_value - максимально допустимое значение.# Пользоваться объектами класса FloatValidator
# предполагается следующим образом:# # res = float_validator(value)# где value - проверяемое значение (должно быть
# вещественным и находиться в диапазоне [min_value; max_value]). Данный валидатор должен возвращать True, если значение
# value проходит проверку, и False - в противном случае.
class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

    def __call__(self, value):
        return self._is_valid(value)


# call должен быть в базовом классеТ.к. Если количество валидаторов будет увеличиваться, то в каждом придется объявлять
# метод call SOLID!

class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, value):
        return type(value) == float and self.min_value <= value <= self.max_value

    # def __call__(self, value):
    #     return self._is_valid(value)


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])

################################################################################
from functools import wraps
from typing import Callable


def abcstract_method(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwds):
        raise NotImplementedError("в классе не переопределен метод _is_valid")

    return wrapper


# @wraps(method) - это декоратор, который используется для сохранения метаданных (например, имя функции, аргументы)
# оригинальной функции method. Он обеспечивает то, что обертка wrapper будет иметь те же атрибуты, что и оригинальная
# функция.В данном случае, декоратор @wraps(method) применяется к функции wrapper, которая является оберткой для
# абстрактного методаis_validв классеValidator. Это позволяет сохранить метаданные (например, имя функции)
# оригинального метода _is_valid`, чтобы они были доступны в обертке.В данном коде использование @wraps(method) не
# обязательно, так как в данном случае нет явной необходимости сохранять метаданные оригинального методаis_valid`.

class Validator:
    @abcstract_method
    def _is_valid(self, data):
        pass

    def __call__(self, data) -> bool:
        return self._is_valid(data)


class FloatValidator(Validator):
    def __init__(self, min_value: float, max_value: float) -> None:
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, float) and (self._min_value <= data <= self._max_value)


################################################################################################
class Validator:
    def _is_valid(self, data): raise NotImplementedError('в классе не переопределен метод _is_valid')

    def __call__(self, data): return self._is_valid(data)


class NumericValidator(Validator):
    data_type = None

    def __init__(self, min_value, max_value):
        self.min_value, self.max_value = min_value, max_value

    def _is_valid(self, data):
        return type(data) == self.data_type and self.min_value <= data <= self.max_value


class IntegerValidator(NumericValidator): data_type = int


class FloatValidator(NumericValidator): data_type = float


################################################################################
# Абстрактные методы класса - это методы, которые объявлены в абстрактном классе, но не имеют реализации в самом классе.
# Вместо этого, подклассы абстрактного класса должны предоставить реализацию для этих абстрактных методов.
# Абстрактный класс является классом, который содержит один или несколько абстрактных методов. Абстрактный класс не
# может быть инстанциирован напрямую, он служит вачестве базового класса для других классов. Подклассы абстрактного
# класса должны реализовать все его абстрактные методы, иначе они также должны быть объявлены как абстрактные классы.
# Абстрактные методы обеспечивают интерфейс для классов-наследников, определяя, какие методы должны быть реализованы
# в каждом изих. Это позволяет создавать общий контракт для классов-наследников гарантирует, что определенные методы
# будут доступны в каждом из них.Пример объявления абстрактного метода Python:
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass


################################################################
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self): ...

    @abstractmethod
    def disconnect(self): ...

    @abstractmethod
    def execute(self): ...


class MySQLDatabase(Database):
    def connect(self):
        print('Connecting to MySQL database...')

    def disconnect(self):
        print('Disconnecting from MySQL database...')

    def execute(self, query):
        print(f"Executing query '{query}' in MySQL database...")


class PostgreSQLDatabase(Database):
    def connect(self):
        print('Connecting to PostgreSQL database...')

    def disconnect(self):
        print('Disconnecting from PostgreSQL database...')

    def execute(self, query):
        print(f"Executing query '{query}' in PostgreSQL database...")


################################################################################################
# Подвиг 6 (про модуль abc). В языке Python есть еще один распространенный способ объявления абстрактных методов класса
# через декоратор abstractmethod модуля abc:from abc import ABC, abstractmethodЧтобы корректно работал декоратор
# # abstractmethod сам класс должен наследоваться от базового класса ABC. Например, так:
# # class Transport(ABC):
#     @abstractmethod
#     def go(self):
#         """Метод для перемещения транспортного средства"""
# #     @classmethod
#     @abstractmethod
#     def abstract_class_method(cls):
#         """Абстрактный метод класса"""
# Мы здесь имеем два абстрактных метода внутри класса Transport, причем, первый метод go() - это обычный метод, а второй
# abstract_class_method() - это абстрактный метод уровня класса. Обратите внимание на порядок использования декораторов
# classmethod и abstractmethod. Они должны быть записаны именно в такой последовательности.Теперь, если объявить
# какой-либо дочерний класс, например:
class Bus(Transport):
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed

    def go(self):
        print("bus go")

    @classmethod
    def abstract_class_method(cls):
        pass


# То в нем обязательно нужно переопределить абстрактные методы go и abstract_class_method класса Transport. Иначе,
# объект класса Bus не будет создан (возникнет исключение TypeError).Используя эту информацию, объявите базовый
# класс Model (модель), в котором нужно объявить один абстрактный метод с сигнатурой:def get_pk(self): ...
# и один обычный метод:def get_info(self): ...который бы возвращал строку "Базовый класс Model".На основе класса Model
# объявите дочерний класс ModelForm, объекты которого создаются командой:form = ModelForm(login, password)
# где login - заголовок перед полем ввода логина (строка); password - заголовок перед полем ввода пароля (строка).
# В каждом объекте класса ModelForm должны формироваться локальные атрибуты с именами _login и _password, а также
# автоматически появляться локальный атрибут _id с уникальным целочисленным значением для каждого объекта класса
# ModelForm.В классе ModelForm переопределите метод:def get_pk(self): ...который должен возвращать значение атрибута _id

# С помощью модуля abc можно определять не только абстрактные методы, но и абстрактные объекты-свойства (property)
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @property
    @abstractmethod
    def speed(self):
        """Абстрактный объект-свойство"""


################################################################
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmetho
    def get_pk(self): ...

    # @abstractmethod # if было так прописано то нужно было бы переопределять в дочернем классе get_info
    def get_info(self): return f"Базовый класс Model"


class ModelForm(Model):
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = id(self)

    def get_pk(self): return self._id

    # def get_info(self): return f"class ModelForm"


form = ModelForm("Логин", "Пароль")
print(form.get_pk())
################################################################################
# @abstractmethod позволяет проверить, все ли абстрактные методы переопределены в наследнике абстрактног
# о класса. Или в наследнике наследника какого-нибудь метакласса.
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def asdf(self):
        pass


class B(A):
    pass


b = B()
# Запуск этого кода выдаёт ValueError "TypeError: Can't instantiate abstract class B with abstract method asdf".
# Видимо, основной плюс в этом. Можно не использовать АВС, а raise NotImplementedError делать при вызове функции,
# которая не была переопределена. Но проверить, все ли абстрактные методы переопределены, не вызывая их - заморочь без
# ABC.# То есть, класс АВС просто сам делает  ValueError "TypeError: Can't instantiate abstract class B
# with abstract method вместо того чтобы прописывать это самому без наследования от  АВС не будет работать декоратор
# abstractmethod, который нужен для проверки имплементации функции в дочерних классах. Одновременно он запрещает
# создание объектов абстрактного класса, как в других языках - java
################################################################################################
from itertools import count  # Создать бесконечную равномерно распределенную последовательность
from abc import ABC, abstractmethod


class Model(ABC):
    _autoincrement = count()

    @abstractmethod
    def get_pk(self):
        '''Get primary key'''

    def get_info(self):
        return 'Базовый класс Model'


class ModelForm(Model):
    def __init__(self, login, password):
        self._id = next(self._autoincrement)
        self._login = login
        self._password = password

    def get_pk(self):
        return self._i


################################################################################
class ModelForm(Model):
    __ID = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.manage_id()

    @classmethod
    def manage_id(cls):
        cls.__ID += 1
        return cls.__ID

    def get_pk(self):
        return self._id


################################################################################################
# Подвиг 7. Используя информацию о модуле abc из предыдущего подвига 6, объявите базовый класс с именем StackInterface
# со следующими абстрактными методами:def push_back(self, obj) - добавление объекта в конец стека;
# def pop_back(self) - удаление последнего объекта из стека.На основе этого класса объявите дочерний класс с именем
# Stack. Объекты этого класса должны создаваться командой:st = Stack()и в каждом объекте этого класса должен
# формироваться локальный атрибут:_top - ссылка на первый объект стека (для пустого стека _top = None).В самом классе
# Stack переопределить абстрактные методы базового класса:def push_back(self, obj) - добавление объекта в конец стека;
# def pop_back(self) - удаление последнего объекта из стека.Сами объекты стека должны определяться классом StackObj и
# создаваться командой:obj = StackObj(data)где data - информация, хранящаяся в объекте (строка). В каждом объекте
# класса StackObj должны автоматически формироваться атрибуты:_data - информация, хранящаяся в объекте (строка);
# _next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None).from abc import ABC,
# abstractmethod


class StackObj:
    def __init__(self, data):
        self._data = data
        self.next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self.last = None

    def push_back(self, obj):
        if not self._top:
            self._top = obj
        else:
            self.last.next = obj
        self.last = obj
        obj.next = None

    def pop_back(self):
        if self._top is None:
            return None
        if self._top == self.last:
            res = self.last
            self._top = self.last = None
        else:
            h = self._top
            while h.next != self.last:
                h = h.next
            res = h.next
            self.last = h
            self.last.next = None
        return res


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print(del_obj)


################################################################################
class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def __iter__(self):
        h = self._top
        while h:
            yield h
            h = h.next

    def push_back(self, obj: StackObj):
        if not self._top:
            self._top = obj
            return
        *_, last = self
        last.next = obj

    # таким образом мы распаковываем итератор в наши значения.К примеру:
    # x, *arg, y = (1, 2, 3, 4, 5)  # x = 1, y = 5
    # *arg, y, x = (1, 2, 3, 4, 5)  # x= 5, y = 4

    def pop_back(self):
        if not self._top:
            return None
        if not self._top.next:
            obj = self._top
            self._top = None
            return obj
        *_, p_last, last = self
        p_last.next = None
        return last


################################################################################################
class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def get_obj(self, end=True):  # end=True - вернем последний, иначе - предпоследний
        prev = last = self._top
        while last._next:
            prev, last = last, last._next
        return [prev, last][end]

    def push_back(self, obj_):
        if self._top is None:  # стек пуст
            self._top = obj_
        else:  # найдем последний и добавим новый объект
            self.get_obj()._next = obj_

    def pop_back(self):
        if self._top is None:  # стек пуст
            res = None
        elif self._top._next is None:  # в стеке один объект
            res = self._top
            self._top = None
        else:
            prev = self.get_obj(end=False)  # найдем предпоследний
            res = prev._next  # выведем последний объект
            prev._next = None  # и удалим последний объект
        return res


class StackObj:
    def __init__(self, data):
        self._data, self._next = data, None


################################################################################
from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self):
        '''push_back'''

    @abstractmethod
    def pop_back(self):
        '''pop_back'''

    @classmethod
    @abstractmethod
    def get_info(cls):
        return "Базовый класс StackInterface"


class Stack(StackInterface, list):
    def __init__(self):
        super().__init__()
        self._top = None

    def push_back(self, obj_):
        if not self:
            self._top = obj_
        else:
            self[-1]._next = obj_
        super().append(obj_)

    def pop_back(self):
        if len(self) == 1:
            self._top = None
        else:
            self[-2]._next = None
        return super().pop()


class StackObj:
    def __init__(self, data):
        self._data, self._next = data, None

    # Причем метод
    # @classmethod
    # @abstractmethod
    # def get_info(cls):
    #     return "Базовый класс StackInterface"
    # Не был переопределен в дочернем классе  Stack, а ошибки не было

    ################################################################################################
    def push_back(self, obj):
        if self.last:
            self.last.next = obj
            self.last = obj
        else:
            self.last = self._top = obj


################################################################################
# без last
# Когда есть указатель на хвост списка операция добавления в конец оценивается О(1), а когда нет указателя О(n).
class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if not self._top:
            self._top = obj
        else:
            h = self._top
            while h.next != None:
                h = h.next
            h.next = obj

    def pop_back(self):
        if not self._top.next:
            res = self._top
            self._top = None
        else:
            h = self._top
            while h.next.next != None:
                h = h.next
            res = h.next
            h.next = None
        return res


################################################################################################
# Чтобы не гонять в цикле весь односвязный список, сделаем его двухсвязным
class StackObj:
    def __init__(self, data):
        self._data, self._next, self._prev = data, None, None


class Stack(StackInterface):
    def __init__(self):
        self._top = self._tail = None

    def push_back(self, obj):
        if self._top:
            self._tail._next = obj
            obj._prev = self._tail
        else:
            self._top = obj
        self._tail = obj

    def pop_back(self):
        last = self._tail
        if self._tail and self._tail._prev:
            # last = self._tail
            self._tail = self._tail._prev
            self._tail._next = None
        else:
            self.__init__()
        return last


################################################################################
class StackObj:
    def __init__(self, data):
        self._data, self._next, self._prev = data, None, None


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self.tail = None

    def push_back(self, obj):
        if self._top:
            self.tail._next = obj
            obj.prev = self.tail
        else:
            self._top = obj
        self.tail = obj

    def pop_back(self):
        last = self.tail
        if not self._top:
            return None
        if self._top == self.tail:
            self.tail = self._top = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return last


################################################################################################
# Подвиг 8. С помощью модуля abc можно определять не только абстрактные методы, но и абстрактные объекты-свойства
# (property). Делается это следующим образом:
# from abc import ABC, abstractmethod
#
#
# class Transport(ABC):
#     @abstractmethod
#     def go(self):
#         """Метод для перемещения транспортного средства"""
#
#     @property
#     @abstractmethod
#     def speed(self):
#         """Абстрактный объект-свойство"""
# Используя эту информацию и информацию о модуле abc из подвига 6, объявите базовый класс с именем CountryInterface со
# следующими абстрактными методами и свойствами:name - абстрактное свойство (property), название страны (строка);
# population - абстрактное свойство (property), численность населения (целое положительное число);
# square - абстрактное свойство (property), площадь страны (положительное число);get_info() - абстрактный метод
# для получения сводной информации о стране.На основе класса CountryInterface объявите дочерний класс Country,
# объекты которого создаются командой:country = Country(name, population, square)В самом классе Country должны быть
# переопределены следующие свойства и методы базового класса:name - свойство (property) для считывания названия
# страны (строка);population - свойство (property) для записи и считывания численности населения
# (целое положительное число);square - свойство (property) для записи и считывания площади страны
# (положительное число);get_info() - метод для получения сводной информации о стране в виде строки:
# "<название>: <площадь>, <численность населения>"
from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self): ...

    @property
    @abstractmethod
    def population(self): ...

    @property
    @abstractmethod
    def square(self): ...

    @abstractmethod
    def get_info(self): ...


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info())  # Россия: 354005483.0, 150000000

################################################################################
from abc import ABC, abstractmethod, abstractproperty


class CountryInterface(ABC):

    @abstractmethod
    def name(self):
        '''Не определено объект-свойство для записи и считывания название страны'''

    @abstractmethod
    def population(self):
        '''Не определено объект-свойство для записи и считывания численности населения'''

    @abstractmethod
    def square(self):
        '''Не определено объект-свойство для записи и считывания площади страны'''

    @abstractmethod
    def get_info(self):
        '''Не определен метод get_info для получения сводной информации о стране.'''


class Country(CountryInterface):

    def __init__(self, name, population, square):
        self._name = name
        self.population = population
        self.square = square

    # population и square - это свойства. Так как для них определен сеттер, то то при инициализации значение присваивается
    # атрибуту, определенному в сеттере. Если сеттера нет тогда значение свойству нужно присваивать напрямую через
    # подчеркивание (как для _name - там только геттер)
    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = population

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, square):
        self._square = square

    def get_info(self):
        return f'{self.name}: {self.square}, {self.population}'


################################################################################################
class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, new_value):
        setattr(instance, self.name, new_value)


class Country(CountryInterface, ABC):
    name, population, square = Descriptor(), Descriptor(), Descriptor()

    def __init__(self, *args):
        self.name, self.population, self.square = args

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


################################################################################
# Подвиг 9 (на повторение). Вам поручают разработать класс для представления маршрутов в навигаторе. Для этого
# требуется объявить класс с именем Track, объекты которого могут создаваться командами:tr = Track(start_x, start_y)
# tr = Track(pt1, pt2, ..., ptN)где start_x, start_y - начальная координата маршрута (произвольные числа);
# pt1, pt2, ..., ptN - набор из произвольного числа точек (координат) маршрута (объекты класса PointTrack).
# При передаче аргументов (start_x, start_y) координата должна представляться первым объектом класса PointTrack.
# Наборы всех точек (объектов PointTrack) должны сохраняться в локальном приватном атрибуте объекта класса Track:
# __points - список из точек (координат) маршрута.Далее, каждая точка (координата) должна определяться классом
# PointTrack, объекты которого создаются командой:pt = PointTrack(x, y)где x, y - числа (целые или вещественные).
# Если передается другой тип данных, то должно генерироваться исключение командой:
# raise TypeError('координаты должны быть числами')В классе PointTrack переопределите магический метод __str__,
# чтобы информация об объекте класса возвращалась в виде строки:"PointTrack: <x>, <y>"Например:
pt = PointTrack(1, 2)
print(pt)  # PointTrack: 1, 2


# В самом классе Track должно быть свойство (property) с именем:points - для получения кортежа из точек маршрута.
# Также в классе Track должны быть методы:def add_back(self, pt) - добавление новой точки в конец маршрута
# (pt - объект класса PointTrack);def add_front(self, pt) - добавление новой точки в начало маршрута
# (pt - объект класса PointTrack);def pop_back(self) - удаление последней точки из маршрута;def pop_front(self)
# - удаление первой точки из маршрута.Пример использования классов (эти строчки в программе писать не нужно):
class Track:
    def __init__(self, *args):
        self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)


################################################################################################
class Track:
    def __init__(self, *args):
        self.__points = list(args)

    def __setattr__(self, name, val):
        if isinstance(val[0], PointTrack):
            super().__setattr__(name, val)
        else:
            super().__setattr__(name, [PointTrack(val[0], val[1])])

    # В данном коде super().__setattr__(name, [PointTrack(val[0], val[1])]) используется для вызова метода __setattr__
    # родительского класса и установки значения атрибута name равным [PointTrack(val[0], val[1])].Это делается для
    # обеспечения правильной инициализации атрибута __points в классе Track. Если переданный аргумент val не является
    # экземпляром класса PointTrack, то создается новый объект PointTrack с координатами val[0] и val[1], и этот объект
    # становится значением атрибута __points. Таким образом, при создании объекта класса Track можно передать либо
    # начальные координаты маршрута (start_x и start_y), либо набор точек маршрута (pt1, pt2, ..., ptN).
    # В обоих случаях аргументы будут корректно преобразованы в объекты класса PointTrack и сохранены в
    # атрибуте __points.
    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        self.valid(x, y)
        self.x = x
        self.y = y

    @staticmethod
    def valid(x, y):
        if type(x) not in (int, float) or type(y) not in (int, float):
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'


################################################################################
class Track:

    def __init__(self, *args):
        if all(isinstance(arg, (int, float)) for arg in args):
            self.__points = [PointTrack(*args)]
        if all(isinstance(arg, PointTrack) for arg in args):
            self.__points = [*args]

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        return self.__points.pop()

    def pop_front(self):
        return self.__points.pop(0)


class PointTrack:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if key in ('x', 'y'):
            if not isinstance(value, (int, float)):
                raise TypeError('координаты должны быть числами')
        super().__setattr__(key, value)

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


################################################################################################
# Понимаю, что с двусвязными списками никто не хочет замарачиваться. Но настоящие герои всегда идут в обход
# (с)Бармалей из фильма "Айболит-66" :)Не поленился и сравнил:
# Количество итераций = 200_000 (по 100_000 добавлений в начало и конец). Двусвязный список: 0.9304535388946533
# Количество итераций = 200_000 (по 100_000 добавлений в начало и конец). Список (list): 16.014753818511963
class PointTrack:
    __slots__ = ('__x', '__y', '__next', '__prev')

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__next = self.__prev = None

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    def __setattr__(self, key, value):
        if key in ('_PointTrack__next', '_PointTrack__prev') and not (isinstance(value, PointTrack) or value is None):
            raise TypeError(f"Ошибочный атрибут указателя {value}")
        elif key in ('_PointTrack__x', '_PointTrack__y') and not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')
        object.__setattr__(self, key, value)

    def __repr__(self):
        return f'PointTrack: {self.__x}, {self.__y}'


class Track:

    def __init__(self, *args):
        if type(args[0]) in (int, float) and type(args[1]) in (int, float):
            self.top = self.tail = PointTrack(args[0], args[1])
            slice = 2
        else:
            slice = 0
            self.top = self.tail = None
        for pt in args[slice:]:
            self.add_back(pt)
        self.__points = []

    def add_back(self, point):
        if not self.tail:
            self.top = self.tail = point
            return
        point.prev = self.tail
        self.tail.next = point
        self.tail = point

    def add_front(self, point):
        if not self.top:
            self.top = self.tail = point
            return
        self.top.prev = point
        point.next = self.top
        self.top = point

    def pop_front(self):
        if not self.top:
            return None
        point = self.top
        self.top = self.top.next
        self.top.prev = None
        return point

    def pop_back(self):
        if not self.tail:
            return None
        point = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return point

    @property
    def points(self):
        point = self.top
        lst = [point]
        while point.next:
            point = point.next
            lst.append(point)
        return tuple(lst)


################################################################################
class PointTrack:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if key in ("x", "y") and type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')
        return object.__setattr__(self, key, value)

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *args):
        self.__points = []
        if len(args) == 2:
            self.__points.append(PointTrack(*args))
        else:
            for p in args:
                self.__points.append(p)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


################################################################################################
# По описанию методов класса Track на ум пришёл односвязный список.
class Stack:
    def __init__(self):
        self._top = self._end = None

    def push_back(self, obj):
        if self._top is None:
            self._top = self._end = obj
        else:
            self._end._next = obj
            self._end = obj

    def push_front(self, obj):
        if self._top is None:
            self._top = self._end = obj
        else:
            obj._next = self._top
            self._top = obj

    def pop_back(self):
        if self._top is None:
            raise IndexError('Стек пуст')
        current = self._top
        if self._top == self._end:
            self._top = self._end = None
        else:
            while current._next != self._end:
                current = current._next
            current._next = None
            current, self._end = self._end, current
        return current

    def pop_front(self):
        if self._top is None:
            raise IndexError('Стек пуст')
        current = self._top
        if self._top == self._end:
            self._top = self._end = None
        else:
            self._top = current._next
        return current

    def __len__(self):
        k = 0
        for _ in self:
            k += 1
        return k

    def __iter__(self):
        x = self._top
        while x is not None:
            yield x
            x = x._next

    def __str__(self):
        return str([str(x) for x in self])


class Track:
    def __init__(self, *args):
        self.__points = Stack()
        if len(args) == 2 and all(type(x) != PointTrack for x in args):
            self.add_back(PointTrack(*args))
        else:
            for p in args:
                self.add_back(p)

    def add_back(self, obj):
        if not isinstance(obj, PointTrack):
            raise TypeError('Объект не является PointTrack')
        self.__points.push_back(obj)

    def add_front(self, obj):
        if not isinstance(obj, PointTrack):
            raise TypeError('Объект не является PointTrack')
        self.__points.push_front(obj)

    def pop_back(self):
        self.__points.pop_back()

    def pop_front(self):
        self.__points.pop_front()

    @property
    def points(self):
        return tuple(self.__points)

    def __str__(self):
        return str(self.__points)


class PointTrack:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self._next = None

    def __setattr__(self, key, value):
        if key in 'xy' and not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')
        object.__setattr__(self, key, value)

    def __str__(self): return f"PointTrack: {self.x}, {self.y}"


################################################################################
# Подвиг 10 (на повторение, релакс). Объявите класс с именем Food (еда), объекты которого создаются командой:
# food = Food(name, weight, calories)где name - название продукта (строка); weight - вес продукта (любое
# положительное число); calories - калорийная ценность продукта (целое положительное число).Объявите следующие
# дочерние классы с именами:BreadFood - хлеб;SoupFood - суп;FishFood - рыба.Объекты этих классов должны создаваться
# командами:bf = BreadFood(name, weight, calories, white) # white - True для белого хлеба, False - для остальных
# sf = SoupFood(name, weight, calories, dietary) # dietary - True для диетического супа, False - для других видов
# ff = FishFood(name, weight, calories, fish) # fish - вид рыбы (семга, окунь, сардина и т.д.)В каждом объекте этих
# дочерних классов должны формироваться соответствующие локальные атрибуты с именами:BreadFood: _name,
# _weight, _calories, _whiteSoupFood: _name, _weight, _calories, _dietaryFishFood: _name, _weight, _calories, _fish
class Food:
    def __init__(self, name, weight, calories):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish = fish


bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")


################################################################################################
class Food:
    pAttrs = tuple(("_name", "_weight", "_calories"))
    cAttrs = tuple()

    def __init__(self, *args):
        self.__dict__.update(dict(zip(self.pAttrs + self.cAttrs, args)))


class BreadFood(Food): cAttrs = tuple(("_white",))


class SoupFood(Food): cAttrs = tuple(("_dietary",))


class FishFood(Food): cAttrs = tuple(("_fish",))


################################################################################
from typing import Union

from dataclasses import dataclass  # Модуль dataclasses в Python, создание типов данных


# Атрибуты класса - переменные для использования в этих сгенерированных методах определяются с использованием аннотаций
# типов. Декоратор @dataclass помимо прочего, добавит метод __init__(),

@dataclass
class Food:
    _name: str

    _weight: Union[int, float]

    _calories: int


@dataclass
class BreadFood(Food):
    _white: bool


@dataclass
class SoupFood(Food):
    _dietary: bool


@dataclass
class FishFood(Food):
    _fish: str


################################################################################################
class Food:
    add_attr = None

    def __init__(self, *args):
        self._name, self._weight, self._calories = args[:3]
        if self.add_attr:
            setattr(self, self.add_attr, args[3])


class BreadFood(Food):
    add_attr = '_white'


class SoupFood(Food):
    add_attr = '_dietary'


class FishFood(Food):
    add_attr = '_fish'


################################################################################
class Food:
    attr = None

    def __init__(self, n, w, c, x=None):
        self._name = n
        self._weight = w
        self._calories = c
        if x is not None:
            setattr(self, self.attr, x)


class BreadFood(Food):
    attr = '_white'


class SoupFood(Food):
    attr = '_dietary'


class FishFood(Food):
    attr = '_fish'
################################################################################################

################################################################################

################################################################################################

################################################################################

################################################################################################

################################################################################

################################################################################################

################################################################################

################################################################################################

################################################################################

################################################################################################

################################################################################

################################################################################################

################################################################################

################################################################################################

################################################################################

################################################################################################
