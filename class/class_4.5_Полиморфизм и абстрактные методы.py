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
# # class Bus(Transport):
#     def __init__(self, model, speed):
#         self._model = model
#         self._speed = speed
# #     def go(self):
#         print("bus go")
# #     @classmethod
#     def abstract_class_method(cls):
#         pass
# То в нем обязательно нужно переопределить абстрактные методы go и abstract_class_method класса Transport. Иначе,
# объект класса Bus не будет создан (возникнет исключение TypeError).Используя эту информацию, объявите базовый
# класс Model (модель), в котором нужно объявить один абстрактный метод с сигнатурой:def get_pk(self): ...
# и один обычный метод:def get_info(self): ...который бы возвращал строку "Базовый класс Model".На основе класса Model
# объявите дочерний класс ModelForm, объекты которого создаются командой:form = ModelForm(login, password)
# где login - заголовок перед полем ввода логина (строка); password - заголовок перед полем ввода пароля (строка).
# В каждом объекте класса ModelForm должны формироваться локальные атрибуты с именами _login и _password, а также
# автоматически появляться локальный атрибут _id с уникальным целочисленным значением для каждого объекта класса
# ModelForm.В классе ModelForm переопределите метод:def get_pk(self): ...который должен возвращать значение атрибута _id

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
