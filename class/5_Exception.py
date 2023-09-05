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
# Перед вами имеется часть готового кода. Ваша задача дописать функцию get_user: она должна принимать логин пользователя
# и возвращать имя пользователя из словаря users. Если логин отсутствует, необходимо возбуждать исключение
# UserNotFoundError с текстом User not found
class UserNotFoundError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'


users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}


def get_user(username):
    log = users.get(username, None)
    if not log:
        raise UserNotFoundError('User not found')
    return log['name']


try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)


########################################################
def get_user(username):
    if username in users:
        return users[username]
    return UserNotFoundError('User not found')


############################################################
# ____Balakiref____
########################################################
def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x


res_1 = get_number('-5')
res_2 = get_number('5.78')
res_3 = get_number('8(912)000-000-00')


############################################################
# Подвиг 5. В программе объявлен класс Point:И создается объект этого класса:
# pt = Point(1, 2)Далее, вам нужно обратиться к атрибуту z объекта pt и, если такой атрибут
# существует, то вывести его значение на экран. Иначе вывести строку (без кавычек):
# "Атрибут с именем z не существует"
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


pt = Point(1, 2)
try:
    z.pt
    # getattr(Point, z.pt)
except:
    print("Атрибут с именем z не существует")


########################################################
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __getattr__(self, item):
        try:
            return super().__getattr__(item)
        except AttributeError:
            return f"Атрибут с именем {item} не существует"


pt = Point(1, 2)
print(pt.z)

############################################################
print(getattr(pt, 'z', 'Атрибут с именем z не существует'))


########################################################
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return f"Атрибут с именем {name} не существует"


############################################################
# Подвиг 7. В программе вводятся в одну строчку через пробел некоторые данные, например:
# 1 -5.6 2 abc 0 False 22.5 hello world"Эти данные разбиваются по пробелу и представляются в
# виде списка строк:lst_in = input().split()Ваша задача посчитать сумму всех целочисленных
# значений, присутствующих в списке lst_in. Результат (сумму) вывести на экран.
# Подсказка: отбор только целочисленных значений можно выполнить с помощь функции filter() с
# последующим их преобразованием в целые числа с помощью функции map() и, затем, вычислением их суммы с
# помощью функции sum(). Для отбора целочисленных значений рекомендуется объявить вспомогательную функцию,
# которая бы возвращала True для строк, в которых присутствует целое число и False - для всех остальных строк.
string = "8 11 abcd -7.5 2.0 -5"

lst_in = string.split()


def check(num):
    try:
        if type(int(num)) == int:
            return True
    except ValueError:
        return False


s = filter(check, lst_in)
res = sum(map(int, s))
print(res)
########################################################
lst_in = string.split()
res = 0
for i in lst_in:
    try:
        res += int(i)
    except ValueError:
        continue


############################################################
def check(num):
    try:
        return int(num)
    except ValueError:
        return 0


res = sum(map(check, lst_in))
########################################################
# Подвиг 8. В программе вводятся в одну строчку через пробел некоторые данные, например:
# "1 -5.6 True abc 0 23.56 hello"Эти данные разбиваются по пробелу и представляются в виде списка строк:
# lst_in = input().split()Ваша задача сформировать новый список с именем lst_out, в котором строки с целыми
# числами будут представлены как целые числа (тип int), строки с вещественными числами, как вещественные
# (тип float), а остальные данные - без изменений.Например:
# lst_out = [1, -5.6, 'True', 'abc', 0, 23.56, 'hello']  #
# после обработки введенной строки "1 -5.6 True abc 0 23.56 hello"
# Реализовать эту задачу следует с помощью функции map() и объявления вспомогательной функции с механизмом
# обработки исключений для непосредственного преобразования данных в целые или вещественные числа.
string = "hello 1 world -2 4.5 True"

lst_in = string.split()


def check(num):
    try:
        return int(num)
    except ValueError:
        try:
            return float(num)
        except ValueError:
            return num


lst_out = list(map(check, lst_in))
print(lst_out)


############################################################
# цикл проходит по всем типам, которые могут быть переданы в функцию
def convert(value):
    for T in (int, float, str):
        try:
            return T(value)
        except:
            pass


lst_out = [convert(x) for x in lst_in]
print(lst_out)


########################################################
# Подвиг 9. Объявите в программе класс Triangle, объекты которого создаются командой:tr = Triangle(a, b, c)
# где a, b, c - длины сторон треугольника (любые положительные числа). В каждом объекте класса Triangle должны
# формироваться локальные атрибуты _a, _b, _c с соответствующими значениями.Если в качестве хотя бы одной величины
# a, b, c передается не числовое значение, или меньше либо равно нулю, то должно генерироваться исключение командой:
# raise TypeError('стороны треугольника должны быть положительными числами')Если из переданных значений a, b, c
# нельзя составить треугольник (условие: каждая сторона должна быть меньше суммы двух других), то генерировать
# исключение командой:raise ValueError('из указанных длин сторон нельзя составить треугольник')
# Затем, на основе следующего набора данных:input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2),
# (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]необходимо сформировать объекты класса Triangle, но только в том случае,
# если не возникло никаких исключений. Все созданные объекты представить в виде списка с именем lst_tr.
# input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]


class Triangle:
    def __init__(self, a, b, c):
        if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a <= 0 or b <= 0 or c <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a > b + c or b > a + c or c > a + b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')
        # if max(a, b, c) > sum((a, b, c)) / 2:

        # a, b, c = sorted([a, b, c])
        # return c < a + b
        self._a = a
        self._b = b
        self._c = c


lst_tr = []
for data in input_data:
    try:
        tr = Triangle(*data)
    except (ValueError, TypeError):
        pass
    else:
        lst_tr.append(tr)


############################################################
class Triangle:
    def __init__(self, a, b, c):
        self.__check_args(a, b, c)
        self.__check_triangle(a, b, c)
        self._a = a
        self._b = b
        self._c = c

    def __check_args(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg < 0:
                raise TypeError('стороны треугольника должны быть положительными числами')

    def __check_triangle(self, a, b, c):
        if (a >= c + b) or (c >= a + b) or (b >= a + c):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


########################################################
class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._check_triangle()

    def __setattr__(self, key, value):
        if type(value) not in (int, float) or value < 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        super().__setattr__(key, value)

    def _check_triangle(self):
        if self._a > self._c + self._b or self._b > self._c + self._a or self._c > self._a + self._b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]


def check_class(x):
    try:
        return Triangle(*x)
    except:
        return False


lst_tr = list(filter(lambda x: isinstance(x, Triangle), (map(check_class, input_data))))


############################################################
# Подвиг 10. Объявите в программе класс FloatValidator, объекты которого создаются командой:
# fv = FloatValidator(min_value, max_value)где min_value, max_value - минимальное и максимальное допустимое значение
# (диапазон [min_value; max_value]).Объекты этого класса предполагается использовать следующим образом:
# fv(value)где value - проверяемое значение. Если value не вещественное число или не принадлежит диапазону
# [min_value; max_value], то генерируется исключение командой:raise ValueError('значение не прошло валидацию')
# По аналогии, объявите класс IntegerValidator, объекты которого создаются командой:
# iv = IntegerValidator(min_value, max_value)и используются командой:iv(value)Здесь также генерируется исключение:
# raise ValueError('значение не прошло валидацию')если value не целое число или не принадлежит диапазону
# [min_value; max_value].После этого объявите функцию с сигнатурой:def is_valid(lst, validators): ...
# где lst - список из данных; validators - список из объектов-валидаторов (объектов классов
# FloatValidator и IntegerValidator).Эта функция должна отбирать из списка все значения, которые прошли хотя бы по
# одному валидатору. И возвращать новый список с элементами, прошедшими проверку.
class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != float or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class IntegerValidator(FloatValidator):
    def __call__(self, value):
        if type(value) != int or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    res = []
    for l in lst:
        for v in validators:
            try:
                v(l)
                res.append(l)
                break
            except ValueError:
                continue
    return res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]


########################################################
class BaseValidator:
    _type = None

    def __init__(self, *args):
        self.min_value, self.max_value = args

    def __call__(self, value):
        if type(value) != self._type or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class FloatValidator(BaseValidator):
    _type = float


class IntegerValidator(BaseValidator):
    _type = int


def is_valid(lst, validators):
    res = []
    for l in lst:
        for validator in validators:
            try:
                validator(l)
                res.append(l)
            except ValueError:
                continue
            else:
                break
    return res


#################################################################3
class Validator:
    value_types = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if self.value_types and \
                (type(value) not in self.value_types or
                 not self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')
        return True


class FloatValidator(Validator):
    value_types = (float,)


class IntegerValidator(Validator):
    value_types = (int,)


def is_valid(lst, validators):
    def validate(x):
        for val in validators:
            try:
                return val(x)
            except ValueError:
                continue
        return False

    return [*filter(validate, lst)]


# функция validate возвращает True как только значение прошло один
# (любой) валидатор, на этом обход данного значения по валидаторам заканчивается и идет переход к следующему значению;
# либо же если ни один из валидаторов не пройден - возвращается False. таким образом эта функция подходит для
# использования в filter. При этом, если значение прошло один из валидаторов, оно не попадает на проверку в следующие,
# благодаря этому исключено дублирование.
fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]


############################################################
class BaseValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, data, *args, **kwargs):
        return self._is_valid(data)

    def _is_valid(self, data):
        raise NotImplementedError


class FloatValidator(BaseValidator):

    def _is_valid(self, data):
        if type(data) == float and self.min_value <= data <= self.max_value:
            return True
        raise ValueError('значение не прошло валидацию')


class IntegerValidator(BaseValidator):

    def _is_valid(self, data):
        if type(data) == int and self.min_value <= data <= self.max_value:
            return True
        raise ValueError('значение не прошло валидацию')


def is_valid(lst: list, validators: list) -> list:
    results = []
    for value in lst:
        for validate in validators:
            try:
                validate(value)
                results.append(value)
            except ValueError:
                continue
            break
    return results


########################################################
class Validator:
    types = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if not (type(value) == self.types and self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')
        # return True


class FloatValidator(Validator): types = float


class IntegerValidator(Validator): types = int


def is_valid(lst, validators):
    res = []
    for val in lst:
        for vld in validators:
            try:
                vld(val)
                res.append(val)
            except:
                continue
            break
    return res


############################################################
class Validator:
    value_type = None

    def __init__(self, *args):
        self.min_value, self.max_value = args

    def __call__(self, value):
        if self.value_type == type(value) and self.min_value <= value <= self.max_value:
            return True
        raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    value_type = float


class IntegerValidator(Validator):
    value_type = int


def is_valid(values, validators):
    def _check(value):
        for validator in validators:
            try:
                return validator(value)
            except ValueError:
                pass
        return False

    return [*filter(_check, values)]


########################################################
# Подвиг 4. В программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова, булевы
# величины (True/False). Необходимо прочитать эти значения из входного потока. Если оба значения являются числами,
# то вычислить их сумму, иначе соединить их в одну строку с помощью оператора + (конкатенации строк). Результат вывести
# на экран (в блоке finally).
try:
    x, y = input().split()
    try:
        res = int(x) + int(y)
    except:
        try:
            res = float(x) + float(y)
        except:
            res = x + y
finally:
    print(res)

############################################################
x, y = input().split()
try:
    x, y = map(int, (x, y))
except ValueError:
    try:
        x, y = map(float, (x, y))
    except ValueError:
        pass
finally:
    print(x+y)
########################################################
x, y = input().split()
try:
    try:
        result = int(x) + int(y)
    except ValueError:
        result = float(x) + float(y)
except ValueError:
    result = x + y
finally:
    print(result)
############################################################
try:
    ins = input().split()
    d = sum([int(i) if i.isdigit() else float(i) for i in ins])
except:
    d = "".join([str(i) for i in ins])
finally:
    print(d)
########################################################
x = input().split()
try:
    res = sum(map(int, x))
except:
    try:
        res = sum(map(float, x))
    except:
        res = ''.join(x)
finally:
    print(res)
############################################################
ab = input().split()
for try_type in (int, float):
    try:
        summa = sum(map(try_type, ab))
    except (ValueError, TypeError):
        pass
    finally:
        if 'summa' in globals():
            print(summa)
            break
else:
    print(''.join(ab))
########################################################
#Подвиг 5. Объявите в программе класс Point, объекты которого должны создаваться командами:
# pt = Point()pt = Point(x, y)где x, y - произвольные числа (координаты точки). В каждом объекте класса Point должны
# формироваться локальные атрибуты _x, _y с соответствующими значениями. Если аргументы не указываются
# (первая команда), то _x = 0, _y = 0.Далее, в программе вводятся два значения в одну строчку через пробел.
# Значениями могут быть числа, слова, булевы величины (True/False). Необходимо прочитать эти значения из входного
# потока. Если оба значения являются числами, то формировать объект pt командой:pt = Point(x, y)Если хотя бы одно из
# значений не числовое, то формировать объект pt командой:pt = Point()Реализовать этот функционал с помощью блоков
# try/except. А в блоке finally вывести на экран сообщение в формате (без кавычек):
# Point: x = <значение x>, y = <значение y>"
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f"{self.__class__.__name__}: x = {self._x}, y = {self._y}"
a,b = input().split()
try:
    int(a) and int(b)
    pt = Point(a,b)
except ValueError:
    try:
        float(a) and float(b)
        pt = Point(a,b)
    except ValueError:
        pt = Point()
finally:
    print(pt)
############################################################
def get_div(x, y):
    try:
        res = x / y
        print(f'id res внутри try: {id(res)}')  # id res внутри try: 2110589675888
        return res
    except ZeroDivisionError:
        res = 100
        return res
    finally:
        res = -1
        print(f'id res внутри finally: {id(res)}')  # id res внутри finally: 140713085821672
        print(f"finally: {res}")


res = get_div(1, 2)  # finally: -1
print(res)  # 0.5
res = get_div(10, 0)  # finally: -1
print(res)  # 100
########################################################
# Подвиг 7. В практике программирования блок else используют как элемент отладки программы: в него прописывают текст
# программы, в котором заведомо не произойдет исключений, отлавливаемых в блоке try. Выполним на практике такой пример
# Вам необходимо объявить функцию с сигнатурой:def get_loss(w1, w2, w3, w4): ...где w1, w2, w3, w4 - любые числа.
# Функция должна возвращать значение, вычисленное по формуле:y = 10 * w1 // w2 - 5 * w2 * w3 + w4
# Здесь фрагмент вычисления w1 // w2 содержит потенциальную ошибку деления на ноль, поэтому его следует делать в блоке
# try. А в блоке else продолжить вычисления, где не используются операции деления.
# Если происходит деление на ноль, то функция должна возвращать строку:"деление на ноль"
def get_loss(w1, w2, w3, w4):
    try:
        x = w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        return 10 * x - 5 * w2 * w3 + w4

############################################################
#Подвиг 8. Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой:
# r = Rect(x, y, width, height)где x, y - координаты верхнего левого угла (любые числа); width, height -
# ширина и высота прямоугольника (положительные числа). Ось абсцисс (Ox) направлена вправо, ось ординат (Oy)
# направлена вниз.В каждом объекте класса Rect должны формироваться локальные атрибуты с именами: _x, _y, _width,
# _height и соответствующими значениями. Если переданные аргументы x, y (не числа) и width, height не положительные
# числа, то генерировать исключение командой:raise ValueError('некорректные координаты и параметры прямоугольника')
# В классе Rect реализовать метод:def is_collision(self, rect): ...который проверяет пересечение текущего
# прямоугольника с другим (с объектом rect). Если прямоугольники пересекаются, то должно генерироваться исключение
# командой:raise TypeError('прямоугольники пересекаются')Сформировать в программе несколько объектов класса Rect со
# следующими значениями:
# 0; 0; 5; 3
# 6; 0; 3; 5
# 3; 2; 4; 4
# 0; 8; 8; 1
# Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще один список lst_not_collision, в котором
# должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.
# P.S. В программе требуется объявить только класс и списки. На экран выводить ничего не нужно.
# Подсказка. Для определения пересечения двух прямоугольников, у которых стороны параллельны осям координат
# (как в этом подвиге) достаточно проверить, что верхняя грань первого прямоугольника находится ниже нижней грани
# второго, или нижняя грань первого прямоугольника выше верхней грани второго. И то же самое для вертикальных граней.

########################################################
class Rect:
    def __init__(self, x, y, width, height):
        if not all(isinstance(val, (int, float)) for val in (x, y, width, height)) or width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        if (self._x < rect._x + rect._width and self._x + self._width > rect._x and
            self._y < rect._y + rect._height and self._y + self._height > rect._y):
            raise TypeError('прямоугольники пересекаются')

numbers = [
    '0; 0; 5; 3',
    '6; 0; 3; 5',
    '3; 2; 4; 4',
    '0; 8; 8; 1']

lst_rect = [Rect(*map(int, i.split('; '))) for i in numbers]
#lst_rect= [Rect(*[int(j) for j in i.split('; ')]) for i in numbers ]
lst_not_collision = []

for i, rect in enumerate(lst_rect):
    is_collision = False
    for j, other_rect in enumerate(lst_rect):
        if i != j:
            try:
                rect.is_collision(other_rect)
            except TypeError:
                is_collision = True
                break
    if not is_collision # добавить rect если не соприкасается ни с одним из other_rect
        lst_not_collision.append(rect)

############################################################
class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if type(val) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('width', 'height') and value <=0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        object.__setattr__(self,key,value)
########################################################
lst_not_collision = []

for rect in lst_rect:
    for other_rect in lst_rect:
        if rect != other_rect:
            try:
                rect.is_collision(other_rect)
            except TypeError:
                break
    else:
        lst_not_collision.append(rect)

print(lst_not_collision[0]) # 0 8
print(len(lst_not_collision)) # 1
############################################################
class Rect:
    def __init__(self, x: (int, float), y: (int, float), width: (int, float), height: (int, float)):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if key in ('_x', '_y') and not isinstance(value, (int, float)):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_width', '_height') and not (isinstance(value, (int, float)) and value > 0):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        super().__setattr__(key, value)

    def is_collision(self, rect: object):
        Ax1 = self._x
        Ay1 = self._y
        Ax2 = self._x + self._width
        Ay2 = self._y + self._height
        Bx1 = rect._x
        By1 = rect._y
        Bx2 = rect._x + rect._width
        By2 = rect._y + rect._height
        if Ax1 < Bx2 and Ax2 > Bx1 and Ay1 < By2 and Ay2 > By1:
            raise TypeError('прямоугольники пересекаются')


if __name__ == '__main__':
    lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
    lst_not_collision = []
    for i in range(len(lst_rect)):
        try:
            for j in range(len(lst_rect)):
                if lst_rect[i] != lst_rect[j]:
                    lst_rect[i].is_collision(lst_rect[j])
        except TypeError:
            continue
        else:
            lst_not_collision.append(lst_rect[i])
########################################################
    for rect in lst_rect:
        try:
            for other_rect in lst_rect:
                if rect != other_rect:
                    rect.is_collision(other_rect)
        except TypeError:
            continue
        else:
            lst_not_collision.append(rect)
############################################################
class Rect:
    def __init__(self, x, y, width, height):
        if not all(isinstance(val, (int, float)) for val in (x, y, width, height)) or width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        if (self._x < rect._x + rect._width and self._x + self._width > rect._x and
            self._y < rect._y + rect._height and self._y + self._height > rect._y):
            raise TypeError('прямоугольники пересекаются')

numbers = [
    '0; 0; 5; 3',
    '6; 0; 3; 5',
    '3; 2; 4; 4',
    '0; 8; 8; 1']

lst_rect = [Rect(*map(int, i.split('; '))) for i in numbers]
#lst_rect= [Rect(*[int(j) for j in i.split('; ')]) for i in numbers ]
lst_not_collision = []
########################################################
class Rect:
    def __init__(self, *args):
        if not all([*map(lambda x: isinstance(x, (int, float)), args),
                    *map(lambda x: x > 0, args[2:])]):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x, self._y, self._width, self._height = args[:4]
        self._x2, self._y2 = self._x + self._width, self._y + self._height

    def is_collision(self, r):
        if self._x2 >= r._x and self._y2 >= r._y and r._x2 >= self._x and r._y2 >= self._y:
            raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []
for r1 in lst_rect:
    try:
        for r2 in lst_rect:
            if r1 != r2:
                r1.is_collision(r2)
        lst_not_collision.append(r1)
    except TypeError:
        pass
    # else:
    #     lst_not_collision.append(r1)
############################################################
### 5.3 Распространение исключений (propagation exceptions)
class Geom:
    def __init__(self, width, color):
        if type(width) not in (int, float) or type(color) != str or width < 0:
            raise ValueError('неверные параметры фигуры')

        self._width = width
        self._color = color


class Ellipse(Geom):
    def __init__(self, x1, y1, x2, y2, width=1, color='red'):
        super().__init__(width, color)

        if not self._is_valid(x1) or not self._is_valid(y1) or not self._is_valid(x2) or not self._is_valid(y2):
            raise ValueError('неверные координаты фигуры')

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def _is_valid(self, x):
        return type(x) in (int, float)

try:
    x1, y1, x2, y2, w = map(float, input().split())
    el = Ellipse(x1, y1, x2, y2, w)
except ValueError as e:
    print(e)
#Выберите все верные утверждения, связанные с этой программой.
#все исключения, формируемые в классе Geom, можно обрабатывать внутри класса Ellipse
#Верное. Поскольку класс Ellipse является подклассом Geom, он может обрабатывать исключения, которые возникают в его
# родительском классе.

#При вводе положительных числовых значений объект класса Ellipse будет создан успешно.
# Верное. Если введены корректные числовые значения, которые удовлетворяют условиям проверок в конструкторах классов,
# то объект класса Ellipse будет успешно создан.

#если бы переменная w ссылалась на строку, то в классе Geom было бы сгенерировано исключение, которое поднялось бы до
# класса Ellipse и обработано в основной программе в блоке try
#Верное. При попытке создать объект Ellipse с переменной w, ссылавшейся на строку, в классе Geom будет сгенерировано
# исключение ValueError. Это исключение поднимется до класса Ellipse, и будет обработано в блоке try, где объект
# Ellipse создается.
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
