# ___5  Исключения Exception____Egorof_____________________

# Для тех, кому понравилась функция MRO() из темы про наследования:

def smth(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')


smth(ZeroDivisionError)  # ZeroDivisionError -> ArithmeticError -> Exception -> BaseException -> object
smth(FloatingPointError)  # FloatingPointError -> ArithmeticError -> Exception -> BaseException -> object
smth(KeyError)  # KeyError -> LookupError -> Exception -> BaseException -> object
smth(IndexError)  # IndexError -> LookupError -> Exception -> BaseException -> object
smth(ValueError)  # ValueError -> Exception -> BaseException -> object
smth(TypeError)  # TypeError -> Exception -> BaseException -> object
smth(AttributeError)  # AttributeError -> Exception -> BaseException -> object
smth(StopIteration)  # StopIteration -> Exception -> BaseException -> object
smth(SyntaxError)  # SyntaxError -> Exception -> BaseException -> object
############################################################
print(1)
print(2)
try:
    print(3)
    print(1 / 0)
except ArithmeticError as ex:
    print(f'Ошибка {ex}!', type(ex))
print(4)
########################################################
# отлов рекурсии
try:
    def func(phrase):
        print(phrase)
        func(phrase)


    func('Это рекурсия, детка!')
except RecursionError:
    print('ошибочка')


############################################################
# Реализуйте класс Wallet, аналог денежного кошелька, содержащий информацию о валюте и остатке имеющихся средств на
# счете. В данном классе должны быть реализованы:метод __init__, который создает атрибуты currency и balance.
# Значения атрибутов currency и balance поступают при вызове метода __init__. При этом значение атрибута currency
# должно быть строкой, состоящей только из трех заглавных букв. Для этого необходимо сделать именно в такой
# последовательности следующие проверки:В случае, если передается не строка, нужно возбуждать исключение TypeError с
# текстом "Неверный тип валюты" ;В случае, если передается строка, длина которой не равна трем символам, нужно
# возбуждать исключение NameError с текстом "Неверная длина названия валюты"В случае, если строка из трех символов
# состоит из незаглавных букв, нужно возбуждать исключение ValueError с текстом "Название должно состоять только из
# заглавных букв"метод __eq__, для возможности сравнивания балансов кошельков. Операция сравнения доступна только для
# кошельков с одинаковой валютой. Если валюты различаются, необходимо возбудить исключение ValueError с текстом
# "Нельзя сравнить разные валюты". При попытке сравнить экземпляр класса Wallet с другими объектами необходимо
# возбудить исключение TypeError с текстом "Wallet не поддерживает сравнение с <объектом>";методы __add__ и __sub__
# для возможности суммирования и вычитания кошельков. Складывать и вычитать мы можем только с другим экземпляром класса
# Wallet и только в случае, когда у них совпадает валюта (атрибуты currency). Результатом такого сложения должен быть
# новый экземпляр класса Wallet, у которого валюта совпадает с валютой операндов и значение баланса равно
# сумме/вычитанию их балансов (при вычитании баланс может оказаться отрицательным). Если попытаются сложить с
# объектом не являющимся экземпляром Wallet или значения валют у объектов не совпадают,  необходимо возбудить
# исключение ValueError с текстом "Данная операция запрещена"

class Wallet:
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance

    def __setattr__(self, key, value):
        if key == 'currency':
            if type(value) != str:
                raise TypeError("Неверный тип валюты")
            elif len(value) != 3:
                raise NameError("Неверная длина названия валюты")
            elif not value.isupper():  # value != value.upper():
                raise ValueError("Название должно состоять только из заглавных букв")

        object.__setattr__(self, key, value)

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        if other.currency != self.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return other.balance == self.balance

    def __add__(self, other):
        if not isinstance(other, Wallet) or other.currency != self.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or other.currency != self.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance - other.balance)


########################################################
def first_func():
    print('Начало работы функции first_func')
    try:
        second_func()
    except Exception as ex:
        print(f'Внимание! Обработано исключение: {ex} на уровне first_func')
    print('Конец работы функции first_func')


def second_func():
    print('Начало работы функции second_func')
    try:
        third_func()
    except Exception as ex:
        print(f'Внимание! Обработано исключение: {ex} на уровне second_func')
    print('Конец работы функции second_func')


def third_func():
    print('Начало работы функции third_func')
    try:
        1 / 0
    except Exception as ex:
        print(f'Внимание! Обработано исключение: {ex} на уровне third_func')
    print('Конец работы функции third_func')


print(1)
print(2)
first_func()
print(3)


############################################################
def function_1():
    print('Start')
    1 / 0
    print('End')


def function_2():
    try:
        function_1()
    except ZeroDivisionError:
        print("Отловили ZeroDivisionError")


function_2()
# «Start»
# «Отловили ZeroDivisionError»
# Мы получили исключение и вместе с ним вышли на уровень выше, где его обработали, строка с End не исполняется. Если бы мы обрабатывали исключение на месте, то строка бы выполнилась.

########################################################
""" Коспект
try: попробует сделать что-то с возможной ошибкой
except error : может быть несколько вариантов ошибок или несколько except
else: выполнится только если ошибки не будет
finally: выполнится всё равно будет найдена ошибка или нет
"""
s = "hello"
# если try найдёт первый except, то остальные выйдут с блока как break
try:
    s + 12
except KeyError:
    print("KeyError found")  # вызов если найдена ошибка типа KeyError
except TypeError:
    print("TypeError found")  # вызов если найдена ошибка типа TypeError
except Exception:  # вызов если найдена любая ошибка Exception или except: если Base Exception
    print("All Exceptions")
except(KeyError, TypeError, NameError):  # вызов если найдена ошибки типа KeyError, TypeError, NameError
    print("3 Error found")

else:  # выполниться после try если не будет найдена ошибка
    print("else called")
finally:  # выполниться после try несмотря на то будет ли найдена ошибка
    print("finally called")

# TypeError found
# finally called
############################################################
try:
    1 / 0
except Exception as ex:
    print(ex.__class__.__name__)


# ZeroDivisionError
########################################################
# ButtonЕще одним объектом модуля tkinter является класс Button , который создает на экране кнопку.
# Обычно к кнопке нужно привязать функцию, и затем после каждого нажатия на кнопку будет срабатывать привязанная
# функция. Давайте создадим аналог класса Button ЗаданиеВаша задача  создать класс CustomButton, у которого есть:
# метод __init__, принимающий один обязательный аргумент текст кнопки, его необходимо сохранить в атрибут text. И
# также в метод  может поступать произвольное количество именованных аргументов. Их необходимо сохранять в атрибуты
# экземпляра под тем же названиемметод config, который принимает произвольное количество именованных атрибутов.
# Он должен создать атрибут с указанным именем или, если этот атрибут уже присутствовал в экземпляре, изменить его
# на новое значениеметод click, который должен выполнить следующую строчкуself.command()Здесь command является не
# методом, а атрибутом, который вызывают. В момент выполнения этой строчки может произойти две неприятные ситуации
# атрибут command может отсутствовать у экземпляра и тогда возникнет исключение AttributeErrorатрибут command может не
# поддерживать оператор вызова и тогда возникнет исключение TypeErrorЭти ситуации вам необходимо обработать в блоке
# try-except.При первом варианте нужно вывести сообщение «Кнопка не настроена», при втором - «Кнопка сломалась»
class CustomButton:
    def __init__(self, text, **kwargs):
        ...
        # self.text = text
        # self.config(**kwargs)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def config(self, **kwargs):
        self.__dict__.update(kwargs)
        # self.__dict__ = self.__dict__ | kwargs

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')


def func():
    print('Оно живое')


btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
btn.click()  # Кнопка не настроена
btn.config(command=func)
btn.click()  # Оно живое


#############################################################
class CustomButton:
    def __init__(self, text, **kwargs):
        self.text = text
        self.__dict__.update(kwargs)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')


########################################################
try:
    1 / 0
except Exception as error:
    print(f'repr error: {repr(error)} , type error: {type(error)}, str error: {str(error)}')


# repr error: ZeroDivisionError('division by zero') , type error: <class 'ZeroDivisionError'>, str error: division by zero

# repr = type + str )
# так удобно ловить все исключения, потом выводить класс исключения + сообщение об ошибке, или по отдельности.
############################################################
def function_1():
    raise ValueError("Oops, something went wrong")


def function_2():
    try:
        function_1()
    except Exception as e:
        print("Exception caught:", e)


function_2()


# 1.вызов function_2()
# 2.в нём трай function_1()
# 3.фанк1 сразу райзит ОшибкуЗначения с текстом
# 4.эксептим её в соответствующем блоке фанк2 присваивая её значение переменной е  (except Exception as e:)
# 5.выполняем логику блока эксепт: вызываем принт с 2 значениями и сепом по умолчанию(текст,  переменная е, sep=' ')

########################################################
def function_1():
    try:
        x = 1 / 0
        print('The end')
    except ZeroDivisionError:
        print("Can't divide by zero")
        raise ValueError("Oops, something went wrong")


def function_2():
    try:
        function_1()
    except ValueError as e:
        print("ValueError caught:", e)


function_2()
# Can't divide by zero
# ValueError caught: Oops, something went wrong
############################################################
try:
    raise KeyboardInterrupt
except ZeroDivisionError:
    print("Отловили ZeroDivisionError")
except KeyboardInterrupt:
    print("Отловили KeyboardInterrupt")
finally:
    print("Сайонара")
# Отловили KeyboardInterrupt
# Сайонара
########################################################
my_dict = {'key1': 1, 'key2': 2}
try:
    value = my_dict['key3']
except Exception as e:
    raise e


# KeyError: 'key3'
############################################################
# Ваша задача создать класс Customer, который содержит:метод __init__, принимающий на вход имя пользователя и
# необязательный аргумент баланс его счета(по умолчанию 0). Эти значения необходимо сохранить в атрибуты name и balance
# статический метод check_type , принимающий на вход одно значение. Если оно не является числом (не принадлежит классу
# int или float) необходимо вызывать исключение TypeError('Банк работает только с числами'). Это все, метод check_type
# должен только вызывать исключение в случае неправильного типа, возвращать она ничего не должнаметод withdraw  ,
# принимающий на вход значение для списания. Необходимо сперва проверить переданное значение на тип при помощи метода
# check_type  . Если исключений не возникло, необходимо проверить что у покупателя достаточно средств на балансе.
# Если денег хватает, то необходимо уменьшить баланс. Если средств не хватает , нужно вызвать исключение ValueError
# ('Сумма списания превышает баланс')метод deposit  , принимающий на вход значение для зачисления на баланс.
# При помощи метода check_type  проверьте, что передано число. Если исключений не возникло, увеличьте значение
# баланса покупателя на указанную сумму
class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        # issubclass(value, [int, float])
        if type(value) not in (int, float):
            raise TypeError('Банк работает только с числами')

    def withdraw(self, value):
        self.check_type(value)
        if self.balance >= value:
            self.balance -= value
        else:
            raise ValueError('Сумма списания превышает баланс')

    def deposit(self, value):
        self.check_type(value)
        self.balance += value

#########################################################
# Напишите функцию sum_numbers, которая принимает один аргумент numbers. Это должен быть список, состоящий из целых и
# вещественных чисел. Функция sum_numbers должна возвращать сумму всех элементов списка, но прежде чем находить сумму
# необходимо выполнить следующие проверки:Аргумент numbers должен быть именно списком, если передан другой тип,
# необходимо выкинуть исключение TypeError('Аргумент numbers должен быть списком')numbers не должен быть пустым,
# иначе возбуждаем исключение ValueError("Пустой список")внутри numbers должны быть только типы int и float, иначе
# возбуждаем исключение TypeError('Неправильный тип элемента')
def sum_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Аргумент numbers должен быть списком')
    if not numbers == 0:
        raise ValueError("Пустой список")
    if any(map(lambda x: type(x) not in (int, float), numbers)):
        # if not all(map(lambda x: type(x) in (int, float), numbers)):
        raise TypeError('Неправильный тип элемента')
    else:
        return sum(numbers)
############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################

############################################################

########################################################
