# ________Egorof___2.5 Публичные, приватные, защищенные атрибуты и методы________________________
class Student:
    def __init__(self, __name, __age, __branch):
        self.__name = __name
        self.__age = __age
        self.__branch = __branch

    def __display_details(self):
        print(f'Имя: {self.__name}')
        print(f'Возраст: {self.__age}')
        print(f'Направление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()


obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()
print(dir(obj))  # ['_Student__age', '_Student__branch', '_Student__display_details', '_Student__name'
print(obj._Student__age)  # не прямой доступ к приватному атрибуту

################################################################
class PizzaMaker:
    def __make_pepperoni(self):
        pass

    def _make_barbecue(self):
        pass


maker = PizzaMaker()
print(PizzaMaker.__dict__.keys())#dict_keys(['__module__', '_PizzaMaker__make_pepperoni', '_make_barbecue',
maker._make_barbecue() #protected
maker._PizzaMaker__make_pepperoni() #private
################################################################
#_________Balakirev________________________
################################################################
#Создайте объект clock класса Clock и установите время, равным 4530.
class Clock:
    def __init__(self, tm):
        self.__time = 0
        if self.check_time(tm):
            self.__time = tm

    def set_time(self, tm):
        if self.check_time(tm):
            self.__time = tm

    @staticmethod
    def check_time(tm):
        if 0 <= tm < 100000 and type(tm) == int:
            return True
        else:
            return False

    def get_time(self):
        return self.__time


clock = Clock(4530)
clock.set_time(45)
print(clock.get_time())

###############################################################
class Clock:
    def __init__(self, tm):
        self.__time = None
        if self.__check_time(tm):
            self.__time = tm

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    @classmethod
    def __check_time(cls, tm):
        return True if 0 <= tm < 100000 and type(tm) == int else False

    def get_time(self):
        return self.__time


clock = Clock(4530)
clock.set_time(45)
print(clock.get_time())  # 45
################################################################
# Подвиг 4. Объявите класс с именем Money и определите в нем следующие переменные и методы:
# - приватная локальная переменная money (целочисленная) для хранения количества денег (своя для каждого объекта класса
# Money);- публичный метод set_money(money) для передачи нового значения приватной локальной переменной money
# (изменениевыполняется только если метод check_money(money) возвращает значение True);
# - публичный метод get_money() для получения текущего объема средств (денег);
# - публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
# - приватный метод класса check_money(money) для проверки корректности объема средств в параметре money (возвращает True
# если значение корректно и False - в противном случае).
class Money:
    def __init__(self, money):
        self.money = None
        if self.check_money(money):
            self.__money = money
        # self.set_money(money)

    def set_money(self, money):
        if self.check_money(money):
            self.__money = money

    @classmethod#задумался, зачем  метод, который каждый раз получает новые значения делать методом класса ?
    def check_money(cls, money):
        return True if money >= 0 and type(money) is int else False
# Проблема isinstance в том, что в основе bool лежит int , поэтому тут сработает код:
# mn = Money(True)
# mn.get_money()  # True То есть можно присвоить логическую переменную вместо целочисленной.

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()  # 100
m2 = mn_2.get_money()  # 120
###############################################################
class Money:

    def __init__(self, money):  # Инициал. лок. св-ва экз. класса
        self.set_money(money)  # через сеттер set_money устанавливаем лок. св-ва экз. класса

    def set_money(self, money):  # сеттер set_money. устанавливает лок. св-ва экз. класса
        if self.__check_money(money):  # обращение к приватному методу для проверки корректности ввода данных
            self.__money = money  # Если метод вернет True то устанавливаем приватное лок. св-ва экз. класса

    def get_money(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__money

    def add_money(self, mn):  # метод добавляет к текущему лок. св-ву экз. класса средства от объекта mn.__money
        self.__money += mn.get_money()

    @staticmethod
    def __check_money(money):  # метод проверяет корректность ввода данных
        return type(money) == int and money >= 0  # Если целое число и money больше либо равно 0 то вернет True
################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

################################################################

###############################################################

























