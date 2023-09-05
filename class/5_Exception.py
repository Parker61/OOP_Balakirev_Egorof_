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
except UserNotFound
    print(e)
else:
    print(username)


########################################################
def get_user(username):
    if username in users:
        return users[username]
    return UserNotFoundError('User not found')


########################################################
# Создайте класс BankAccount, который представляет банковский счет, у которого есть:метод __init__, принимающий баланс
# (атрибут balance)метод deposit для пополнения баланса. Если пользователь пытается внести отрицательную сумму на счет,
# должно возникать исключение NegativeDepositError("Нельзя пополнить счет отрицательным значением"):метод withdraw
# для вывода денег. Если пользователь пытается снять больше денег, чем есть на счете, должно возникать исключение
# InsufficientFundsError("Недостаточно средств для снятия")Исключения NegativeDepositError и InsufficientFundsError
# вам также необходимо создать

class BaseException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    # def __str__(self):
    #     if self.message:
    #         return f'{self.message}'


class NegativeDepositError(BaseException): ...


class InsufficientFundsError(BaseException): ...


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError("Нельзя пополнить счет отрицательным значением")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств для снятия")
        self.balance -= amount


try:
    raise InsufficientFundsError("Недостаточно средств")
except Exception as e:
    if not isinstance(e, InsufficientFundsError):
        raise ValueError('Реализуйте исключение InsufficientFundsError')


################################
class NegativeDepositError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class InsufficientFundsError(Exception):
    def __str__(self):
        return "Недостаточно средств для снятия"


############################################################
class NegativeDepositError(Exception):
    ...


class InsufficientFundsError(Exception):
    ...


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError("Нельзя пополнить счет отрицательным значением")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств для снятия")
        self.balance -= amount


################################
# Для следующего задания нам нужно реализовать базовым класс исключения PasswordInvalidError, который наследуется от
# стандартного класса исключений Exception. Этот класс можно использовать для обработки любых общих ошибок, связанных
# с неверными паролями.От него нужно унаследовать следующие классы:PasswordLengthError представляет ошибку, связанную
# с недостаточной длиной пароля;PasswordContainUpperError представляет ошибку, связанную с отсутствием заглавных букв
# в пароле;PasswordContainDigitError представляет ошибку, связанную с отсутствием цифр в пароле.
# Создайте класс User с атрибутами username и password(пароль по умолчанию None). Класс должен иметь метод
# set_password, который принимает пароль и устанавливает его как значение атрибута password. Метод set_password должен
# также проверять, соответствует ли пароль заданным требованиям безопасности:Длина пароля должна быть не менее 8
# символов (в противном случае генерируется исключение PasswordLengthError с текстом Пароль должен быть не менее 8
# символов);Пароль должен содержать хотя бы одну заглавную букву (в противном случае генерируется исключение
# PasswordContainUpperError с текстом Пароль должен содержать хотя бы одну заглавную букву);Пароль должен содержать
# хотя бы одну цифру (в противном случае генерируется исключение PasswordContainDigitError с текстом Пароль должен
# содержать хотя бы одну цифру);
class PasswordInvalidError(Exception): ...


class PasswordLengthError(PasswordInvalidError): ...


class PasswordContainUpperError(PasswordInvalidError): ...


class PasswordContainDigitError(PasswordInvalidError): ...


class User:
    def __init__(self, username):
        self.username = username

    def set_password(self, password):
        if len(password) < 8:
            raise PasswordLengthError('Пароль должен быть не менее 8 символов')
        if not any(filter(lambda x: x.isupper() == True, password)):
            raise PasswordContainUpperError('Пароль должен содержать хотя бы одну заглавную букву')
        if not any(map(lambda x: x.isdigit() == True, password)):
            raise PasswordContainDigitError('Пароль должен содержать хотя бы одну цифру')
        self.password = password

    ########################################################################
    def set_password(self, password: str):
        if len(password) < 8:
            raise PasswordLengthError()
        if password.islower():
            raise PasswordContainUpperError()
        elif password.isalpha():
            raise PasswordContainDigitError
        self.password = password


################
# ____Balakiref________________________________

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
    print(x + y)
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
# Подвиг 5. Объявите в программе класс Point, объекты которого должны создаваться командами:
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


a, b = input().split()
try:
    int(a) and int(b)
    pt = Point(a, b)
except ValueError:
    try:
        float(a) and float(b)
        pt = Point(a, b)
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
# Подвиг 8. Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой:
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
# lst_rect= [Rect(*[int(j) for j in i.split('; ')]) for i in numbers ]
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
    if not is_collision  # добавить rect если не соприкасается ни с одним из other_rect
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
        if key in ('width', 'height') and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        object.__setattr__(self, key, value)


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

print(lst_not_collision[0])  # 0 8
print(len(lst_not_collision))  # 1


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
# lst_rect= [Rect(*[int(j) for j in i.split('; ')]) for i in numbers ]
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


# Выберите все верные утверждения, связанные с этой программой.
# все исключения, формируемые в классе Geom, можно обрабатывать внутри класса Ellipse
# Верное. Поскольку класс Ellipse является подклассом Geom, он может обрабатывать исключения, которые возникают в его
# родительском классе.

# При вводе положительных числовых значений объект класса Ellipse будет создан успешно.
# Верное. Если введены корректные числовые значения, которые удовлетворяют условиям проверок в конструкторах классов,
# то объект класса Ellipse будет успешно создан.

# если бы переменная w ссылалась на строку, то в классе Geom было бы сгенерировано исключение, которое поднялось бы до
# класса Ellipse и обработано в основной программе в блоке try
# Верное. При попытке создать объект Ellipse с переменной w, ссылавшейся на строку, в классе Geom будет сгенерировано
# исключение ValueError. Это исключение поднимется до класса Ellipse, и будет обработано в блоке try, где объект
# Ellipse создается.
########################################################
# Подвиг 3. Объявите функцию с сигнатурой:def input_int_numbers(): ...которая бы считывала строку из введенных целых
# чисел, записанных через пробел, и возвращала кортеж из введенных чисел (в виде целых чисел, а не строк).
# Если хотя бы одно значение не является целым числом, то генерировать исключение, командой:raise TypeError('все
# числа должны быть целыми')Вызовите эту функцию в цикле до тех пор, пока пользователь не введет в строке все
# целочисленные значения (то есть, цикл завершается, когда функция отработает штатно, без генерации исключения).
# Выведите на экран прочитанные значения, записанные в виде строки через пробел.


def input_int_numbers():
    flag = True
    while flag:
        try:
            res = tuple(map(str.strip, input().split()))
            try:
                res2 = tuple(map(int, res))
            except ValueError:
                raise TypeError('все числа должны быть целыми')
            else:
                flag = False
        except:
            continue

    return print(*res)


input_int_numbers()


########################################################
def input_int_numbers():
    while True:
        try:
            try:
                print(*tuple(map(int, input().split())))
            except ValueError:
                raise TypeError('все числа должны быть целыми')
        except:
            continue
        else:
            break


input_int_numbers()


############################################################
def input_int_numbers():
    while True:
        try:
            res = tuple(map(str.strip, input().split()))
            try:
                res2 = tuple(map(int, res))
            except ValueError:
                raise TypeError('все числа должны быть целыми')
            else:
                break
        except:
            continue

    return print(*res2)


########################################################
def input_int_numbers():
    try:
        return tuple(map(int, input().split()))
    except ValueError as err:
        raise TypeError('все числа должны быть целыми')


flag = True
while flag:
    try:
        tmp = input_int_numbers()
    except TypeError as err:
        continue
    else:
        flag = False
        print(*tmp)


############################################################
def input_int_numbers():
    while True:
        try:
            print(*tuple(map(int, input().split())))
            break
        except ValueError:
            continue


input_int_numbers()


########################################################
# Подвиг 4. Объявите класс с именем ValidatorString, объекты которого создаются командой:
# vs = ValidatorString(min_length, max_length, chars)где min_length, max_length - минимально и максимально допустимая
# длина строки (целые числа, формируемые диапазон [min_length; max_length]); chars - строка из набора символов
# (хотя бы один из них должен присутствовать в проверяемой строке). Если chars - пустая строка, то проверку на
# вхождение символов не делать.В самом классе ValidatorString объявите метод:def is_valid(self, string): ...
# который проверяет строку string на соответствие критериям: string должна быть строкой, с длиной в диапазоне
# [min_length; max_length] и в string присутствует хотя бы один символ из chars. Если хотя бы один из этих критериев
# не выполняется, то генерируется исключение командой:raise ValueError('недопустимая строка')
# Затем, объявите класс с именем LoginForm, объекты которого создаются командой:lg = LoginForm(login_validator,
# password_validator)где login_validator - валидатор для логина (объект класса ValidatorString);
# password_validator - валидатор для пароля (объект класса ValidatorString).В самом классе LoginForm объявите
# следующий метод:def form(self, request): ...где request - объект запроса (словарь). В словаре request должен
# быть ключ 'login' со значением введенного логина (строки) и ключ 'password' со значением введенного пароля (строка).
# Если хотя бы одного ключа нет, то генерировать исключение командой:raise TypeError('в запросе отсутствует логин
# или пароль')В противном случае (если проверка для request прошла), проверять корректность полученного формой
# логина и пароля с помощью валидаторов, указанных в параметрах login_validator и password_validator, при создании
# объекта формы.Если логин/пароль введены верно, то в объекте класса LoginForm локальным атрибутам _login и _password
# присвоить соответствующие значения.
class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if self.chars and not any(filter(lambda x: x in self.chars, string)):
            raise ValueError('недопустимая строка')
        if not (self.min_length <= len(string) <= self.max_length):
            raise ValueError('недопустимая строка')
        return True


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')
        if self.login_validator.is_valid(request['login']):
            self._login = request['login']
        if self.password_validator.is_valid(request['password']):
            self._password = request['password']


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)


############################################################
class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if not len(string) in range(self.min_length, self.max_length + 1) or \
                self.chars and not any(c in self.chars for c in string):
            raise ValueError('недопустимая строка')
        return string


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        if not all(w in request for w in ('login', 'password')):
            raise TypeError('в запросе отсутствует логин или пароль')
        self._login = self.login_validator.is_valid(request.get('login'))
        self._password = self.password_validator.is_valid(request.get('password'))


while True:
    try:
        try:
            login, password = input().split()
        except ValueError:
            print("should be login and password!")
            continue

        lg.form({'login': login, 'password': password})
        # print(lg._login)
        break

    except TypeError:
        print('в запросе отсутствует логин или пароль')
    except ValueError as e:
        print(f'{e}')  # недопустимая строка
    continue

print(lg._login)


########################################################
def form(self, request):
    try:
        self._login = self.login_validator.is_valid(request['login'])
        self._password = self.password_validator.is_valid(request['password'])
    except KeyError:
        raise TypeError('в запросе отсутствует логин или пароль')


############################################################
class ValidatorString:
    def __init__(self, min_length, max_length, chars=''):
        self.min_length, self.max_length, self.chars = min_length, max_length, chars

    def is_valid(self, string):
        try:
            assert isinstance(string, str)
            assert any(i in self.chars for i in string) if self.chars else True
            assert self.min_length <= len(string) <= self.max_length
            return string
        except AssertionError:
            raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.lv, self.pv = login_validator, password_validator

    def form(self, request):
        try:
            assert isinstance(request.get('login', False), str)
            assert isinstance(request.get('password', False), str)
        except AssertionError:
            raise TypeError('в запросе отсутствует логин или пароль')
        else:
            self._login = self.lv.is_valid(request.get('login'))
            self._password = self.pv.is_valid(request.get('password'))


########################################################
class ValidatorString:
    def __init__(self, *args):
        self.min_length, self.max_length, self.chars = args[:3]

    def is_valid(self, string):
        if not all((isinstance(string, str), self.min_length <= len(string) <= self.max_length,
                    bool(set(self.chars).intersection(string) if self.chars else 1))):
            raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, *args):
        self.validators = args[:2]

    def form(self, request):
        keys = ('login', 'password')
        if not all(map(lambda key: key in request, keys)):
            raise TypeError('в запросе отсутствует логин или пароль')
        [val.is_valid(request[key]) for key, val in zip(keys, self.validators)]
        [setattr(self, f'_{key}', request[key]) for key in keys]


############################################################
# Подвиг 5. Вы начинаете разрабатывать свой сервис по тестированию. Для этого вам поручается разработать базовый класс
# Test для всех видов тестов, объекты которого создаются командой:test = Test(descr)где descr - формулировка теста
# (строка). Если длина строки descr меньше 10 или больше 10 000 символов, то генерировать исключение командой:
# raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')В самом классе Test должен быть объявлен
# абстрактный метод:def run(self): ...который должен быть переопределен в дочернем классе. Если это не так, то должно
# генерироваться исключение командой:raise NotImplementedErrorДалее, объявите дочерний класс с именем TestAnsDigit для
# тестирования правильного введенного числового ответа на вопрос теста. Объекты класса TestAnsDigit должны создаваться
# командой:test_d = TestAnsDigit(descr, ans_digit, max_error_digit)
# где ans_digit - верный числовой ответ на тест; max_error_digit - максимальная погрешность в указании числового
# ответа (необходимо для проверки корректности вещественных чисел, по умолчанию принимает значение 0.01).
# Если аргумент ans_digit или max_error_digit не число (также проверить, что max_error_digit больше или равно нулю),
# то генерировать исключение командой:raise ValueError('недопустимые значения аргументов теста')
# В классе TestAnsDigit переопределите метод:def run(self): ...который должен читать строку из входного потока
# (ответ пользователя) командой:ans = float(input()) # именно такой командой, ее прописывайте в методе run()
# возвращать булево значение True, если введенный числовой ответ ans принадлежит диапазону [ans_digit-max_error_digit;
# ans_digit+max_error_digit]. Иначе возвращается булево значение False.
# Теперь нужно воспользоваться классом TestAnsDigit. Для этого в программе вначале читается сам тест с помощью команд:
# descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
# ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
# Далее, вам необходимо создать объект класса TestAnsDigit с аргументами descr, ans, а аргумент max_error_digit должен
# принимать значение по умолчанию 0.01.Запустите тест командой run() и выведите на экран результат его работы
# (значение True или False). Если в процессе создания объекта класса TestAnsDigit или в процессе работы метода run()
# возникли исключения, то они должны быть обработаны и на экран выведено сообщение, содержащееся в исключении.


class Test:
    def __init__(self, descr):
        if not (10 <= len(descr) <= 10000):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())  # именно такой командой, ее прописывайте в методе run()
        return True if self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit else False


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
try:
    test = TestAnsDigit(descr, ans)
    res = test.run()
    print(res)
except ValueError as e:
    print(e)
########################################################
from numbers import Real


class Test:
    def __init__(self, descr: str):
        self.descr = descr

    def __setattr__(self, key, value):
        if key == 'descr' and (len(value) < 10 or len(value) > 10_000):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        super().__setattr__(key, value)

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit, self.max_error_digit = ans_digit, max_error_digit

    def __setattr__(self, key, value):
        if key in ('ans_digit', 'max_error_digit'):
            if not isinstance(value, Real):  # Real - это абстрактный базовый класс из модуля numbers, который
                # представляет вещественные числа. Этот класс используется для проверки, является ли значение
                # переменной value вещественным числом или нет.
                raise ValueError('недопустимые значения аргументов теста')
            if key == 'max_error_digit' and value < 0:
                raise ValueError('недопустимые значения аргументов теста')
        super().__setattr__(key, value)

    def run(self):
        ans = float(input())  # именно такой командой, ее прописывайте в методе run()
        low = self.ans_digit - self.max_error_digit
        height = self.ans_digit + self.max_error_digit

        return low <= ans <= height


descr, ans = map(str.strip, input().split('|'))
try:
    testAnsDigit = TestAnsDigit(descr, float(ans))
    print(testAnsDigit.run())
except Exception as e:
    print(e)


############################################################
class Test:
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10_000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans, err=0.01):
        super().__init__(descr)
        if not all([*map(lambda x: isinstance(x, (int, float)), (ans, err)), err >= 0]):
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit, self.max_error_digit = ans, err

    def run(self):
        return abs(self.ans_digit - float(input())) <= self.max_error_digit


descr, ans = map(str.strip, input().split('|'))
try:
    testAnsDigit = TestAnsDigit(descr, float(ans))
    print(testAnsDigit.run())
except Exception as e:
    print(e)
########################################################
# Подвиг 7. В программе выполняется считывание числовых данных из входного потока, командой:
# digits = list(map(float, input().split()))Эти данные следует представить в виде объекта класса TupleLimit.
# Сам класс должен наследоваться от класса tuple, а его объекты создаваться командой:tl = TupleLimit(lst, max_length)
# где lst - коллекция (список или кортеж) из данных; max_length - максимально допустимая длина коллекции TupleLimit.
# Если длина lst превышает значение max_length, то должно генерироваться исключение командой:
# raise ValueError('число элементов коллекции превышает заданный предел')В самом классе TupleLimit переопределить
# магические методы __str__() и __repr__() для отображения объекта класса TupleLimit в виде строки из набора данных lst,
# записанных через пробел. Например:"1.0 2.5 -5.0 11.2"Создайте в программе объект класса TupleLimit для прочитанных
# данных digits и параметром max_length = 5. Выведите на экран объект в случае его успешного создания. Иначе,
# выведите сообщение обработанного исключения.
# Чтобы передавать в инициализатор некоторых базовых типов вроде str, tuple и list более одного аргумента,
# нужно переопределить их __new__ метод.

digits = list(map(float, input().split()))


class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        return super().__new__(cls, tuple(lst))

    def __init__(self, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        self.lst = lst
        self.max_length = max_length

    def __str__(self):
        return ' '.join(map(str, self.lst))

    # def __repr__(self):
    #     return ' '.join(map(repr, self.lst))


try:
    res = TupleLimit(digits, 5)
    print(res)
except ValueError as e:
    print(e)


############################################################
class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __str__(self):
        return ' '.join(map(str, self))

    def __repr__(self):
        return str(self)


########################################################
class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        instance = super().__new__(cls, lst)
        instance.max_length = max_length
        return instance

    def __repr__(self):
        return ' '.join(map(str, self))


############################################################
class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __repr__(self):
        return ' '.join(str(x) for x in self)


########################################################
class TupleLimit(tuple):
    def __new__(cls, value, max_length):
        if isinstance(value, (list, tuple)) and len(value) <= max_length:
            instance = super().__new__(cls, value)
            return instance
        else:
            raise ValueError('число элементов коллекции превышает заданный предел')

    def __repr__(self):
        return super().__repr__().strip(")(").replace(', ', ' ')


############################################################
class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, tuple(lst))

    def __str__(self):
        return ' '.join(map(str, self))


try:
    digits = list(map(float, input().split()))
    res = TupleLimit(digits, 5)
    print(res)
except ValueError as e:
    print(e)


########################################################
# 5.4 __Инструкция raise и пользовательские исключения
# после выполнения оператора raise программа останавливает свою работу, если исключение не обрабатывается
# после оператора raise следует указывать объект класса, унаследованного от BaseException
# оператор raise позволяет генерировать различные исключения
############################################################
class LimitException(Exception):
    """Превышение лимита"""


error = LimitException('превышение лимита нагрузки')
raise error


# команда raise error сгенерирует исключение типа LimitException
# при выполнении команды raise error на экран будет выведено сообщение "превышение лимита нагрузки"
#########################################################
class LimitException(Exception):
    """Превышение лимита"""


class ServerLimitException(LimitException):
    """Превышение нагрузки на сервер"""


try:
    raise ServerLimitException('превышение серверной нагрузки')
except LimitException:
    print("LimitException")
except ServerLimitException:
    print("ServerLimitException")


# при выполнении этой программы на экране будет отображена строка "LimitException"
# программа ни при каких типах исключений не перейдет во второй блок except
# после выполнения оператора raise программа перейдет в первый блок except
############################################################
# Подвиг 4. Объявите класс-исключение с именем StringException, унаследованным от базового класса Exception. После
# этого объявите еще два класса-исключения:NegativeLengthString - ошибка, если длина отрицательная;
# ExceedLengthString - ошибка, если длина превышает заданное значение;унаследованные от базового класса StringException.
# Затем, в блоке try (см. программу) пропишите команду генерации исключения для перехода в блок обработки исключения
# ExceedLengthString.
class StringException(Exception): ...


class NegativeLengthString(StringException): ...


class ExceedLengthString(StringException): ...


try:
    raise ExceedLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")


########################################################
# Подвиг 5. Объявите в программе класс-исключение с именем PrimaryKeyError, унаследованным от базового класса Exception.
# Объекты класса PrimaryKeyError должны создаваться командами:e1 = PrimaryKeyError()
# Первичный ключ должен быть целым неотрицательным числом
# e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
# e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
# В первом варианте команды должно формироваться сообщение об ошибке "Первичный ключ должен быть целым неотрицательным
# числом". При втором варианте:"Значение первичного ключа id = <id> недопустимо"И при третьем:
# "Значение первичного ключа pk = <pk> недопустимо"Эти сообщения должны формироваться при отображении объектов
# класса PrimaryKeyError, например:print(e2) # Значение первичного ключа id = abc недопустимо
# Затем, сгенерируйте это исключение с аргументом id = -10.5, обработайте его и отобразите на экране объект исключения.
class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if 'id' not in kwargs and 'pk' not in kwargs:
            self._message = "Первичный ключ должен быть целым неотрицательным числом"
        else:
            key, value = tuple(kwargs.items())[0]
            self._message = f'Значение первичного ключа {key} = {value} недопустимо'

    def __str__(self):
        return self._message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)


############################################################
class PrimaryKeyError(Exception):
    def __init__(self, text):
        self._message = text

    def __str__(self):
        return self._message


class Item:
    def __init__(self, *args, **kwargs):
        if kwargs:
            if not self.check(*kwargs.values()):
                # raise PrimaryKeyError(
                #     f"Значение первичного ключа {self.key(*kwargs.keys())} = {self.val(*kwargs.values())} недопустимо")
                raise PrimaryKeyError(
                    f"Значение первичного ключа {tuple(kwargs.keys())[0]} = {list(kwargs.values())[0]} недопустимо")
            self.__dict__.update(kwargs)
        else:
            if not self.check(args[0]):
                raise PrimaryKeyError("Первичный ключ должен быть целым неотрицательным числом")
            self.id = args[0]

    def check(self, value):
        return type(value) == int and value > 0

    # def val(self, value):
    #     return value
    #
    # def key(self, value):
    #     return value


try:
    e = Item(id=-10.5)
except PrimaryKeyError as e:
    print(e)


########################################################
class PrimaryKeyError(Exception):
    def __init__(self, items=None):
        # print(items)  # dict_items([('id', -10.5)])
        # print(tuple(items)[0][0])  # id
        if items:
            k, v = tuple(items)[0]  # ('id', -10.5)
            self._message = f"Значение первичного ключа {k} = {v} недопустимо"
            # self._message = f"Значение первичного ключа {tuple(items)[0][0]} = {tuple(items)[0][1]} недопустимо"
        else:
            self._message = f"Первичный ключ должен быть целым неотрицательным числом"

    def __str__(self):
        return self._message


class Item:
    def __init__(self, *args, **kwargs):
        if kwargs:
            if not self.check(*kwargs.values()):
                raise PrimaryKeyError(kwargs.items())
            self.__dict__.update(kwargs)
        else:
            if not self.check(args[0]):
                raise PrimaryKeyError()
            self.volume = args[0]

    def check(self, value):
        return type(value) == int and value > 0


try:
    e = Item(id=-10.5)
except PrimaryKeyError as e:
    print(e)


############################################################
class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        super().__init__(self.get_message(kwargs))

    def get_message(self, kwargs):
        if not kwargs:
            return 'Первичный ключ должен быть целым неотрицательным числом'
        if len(kwargs) == 1:
            return 'Значение первичного ключа {} = {} недопустимо'.format(*next(iter(kwargs.items())))


# Получается, что get_massage срабатывает вместо __str__?
#
########################################################
# Подвиг 6. Объявите класс DateString для представления дат, объекты которого создаются командой:
# date = DateString(date_string)где date_string - строка с датой в формате:"DD.MM.YYYY"
# здесь DD - день (целое число от 1 до 31); MM - месяц (целое число от 1 до 12); YYYY - год (целое число от 1 до 3000).
# Например:date = DateString("26.05.2022")лиdate = DateString("26.5.2022") # незначащий ноль может отсутствовать
# Если указанная дата в строке записана неверно (не по формату), то генерировать исключение с помощью собственного
# класса:DateError - класс-исключения, унаследованный от класса Exception.В самом классе DateString переопределить
# магический метод __str__() для формирования строки даты в формате:"DD.MM.YYYY"(здесь должны фигурировать незначащие
# нули, например, для аргумента "26.5.2022" должна формироваться строка "26.05.2022").
# Далее, в программе выполняется считывание строки из входного потока командой:date_string = input()
# Ваша задача создать объект класса DateString с аргументом date_string и вывести объект на экран командой:
# print(date) # date - объект класса DateStringЕсли же произошло исключение, то вывести сообщение (без кавычек):
# "Неверный формат даты"
class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):
        try:
            day, month, year = map(int, date_string.split('.'))
            if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3000:
                self.day = day
                self.month = month
                self.year = year
            else:
                raise DateError
        except (ValueError, DateError):
            raise DateError("Неверный формат даты")

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"


try:
    date_string = input()
    date = DateString(date_string)
    print(date)
except DateError:
    print("Неверный формат даты")


############################################################
class DateString:
    def __init__(self, date_string):
        self.date_string = self.check(date_string)

    def check(self, date_string):
        d, m, y = map(int, date_string.split('.'))
        if not (1 <= d <= 31 and 1 <= m <= 12 and 1 <= y <= 3000):
            raise DateError("Неверный формат даты")
        # d, m, y = map(str, date_string.split('.'))
        d, m, y = ['0' + str(i) if len(str(i)) == 1 else str(i) for i in [d, m, y]]
        return '.'.join([d, m, y])

    def __str__(self):
        return self.date_string


########################################################
import datetime as dt


class DateError(Exception):
    pass


class DateString:
    def __init__(self, date):
        try:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y')
        except ValueError:
            raise DateError

    def __str__(self):
        return self.date.strftime('%d.%m.%Y')


############################################################
from datetime import datetime as dt


class DateString:
    PATTERN = r'%d.%m.%Y'

    class DateError(Exception):
        pass

    def __init__(self, string):
        try:
            self.date_string = dt.strptime(string, self.PATTERN)
        except ValueError:
            raise self.DateError

    def __str__(self):
        return self.date_string.strftime(self.PATTERN)


date_string = input()

try:
    print(DateString(date_string))
except DateString.DateError:
    print("Неверный формат даты")


########################################################
class DateString:
    def __init__(self, date_string):
        day, month, year = date_string.split('.')
        if any(((not 0 < int(day) < 32), (not 0 < int(month) < 13), (not 0 < int(year) < 3000))):
            raise DateError
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return f'{self._day:>02}.{self._month:>02}.{self._year:>04}'


############################################################
class DateError(Exception): ...


class DateString:
    def __init__(self, date_string):
        try:
            self.date = __import__("datetime").datetime.strptime(date_string, '%d.%m.%Y')
        except ValueError:
            raise DateError

    def __str__(self):
        return self.date.strftime('%d.%m.%Y')


date_string = input()
try:
    print(DateString(date_string))
except DateError:
    print('Неверный формат даты')


########################################################
# Значимый подвиг 7. Вам поручается разработать класс TupleData, элементами которого могут являются только объекты
# классов: CellInteger, CellFloat и CellString.Вначале в программе нужно объявить класс CellInteger, CellFloat и
# CellString, объекты которых создаются командами:cell_1 = CellInteger(min_value, max_value)
# cell_2 = CellFloat(min_value, max_value)cell_3 = CellString(min_length, max_length)
# где min_value, max_value - минимальное и максимальное допустимое значение в ячейке;
# min_length, max_length - минимальная и максимальная допустимая длина строки в ячейке.
# В каждом объекте этих классов должны формироваться локальные атрибуты с именами _min_value,
# _max_value или _min_length, _max_length и соответствующими значениями.Запись и считывание текущего значения в
# ячейке должно выполняться через объект-свойство (property) с именем:value - для записи и считывания значения в
# ячейке (изначально возвращает значение None).Если в момент записи новое значение не соответствует диапазону
# [min_value; max_value] или [min_length; max_length], то генерируется исключения командами:
# raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
# raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
# raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
# Все три класса исключений должны быть унаследованы от одного общего класса:CellException
# Далее, объявите класс TupleData, объекты которого создаются командой:ld = TupleData(cell_1, ..., cell_N)
# где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).
# Обращение к отдельной ячейке должно выполняться с помощью оператора:value = ld[index] # считывание значения из
# ячейке с индексом indexld[index] = value # запись нового значения в ячейку с индексом index
# Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом. Если значение index выходит за
# диапазон [0; число ячеек-1], то генерировать исключение IndexError.Также с объектами класса TupleData должны
# выполняться следующие функции и операторы:res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
# for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
# print(d)
class CellException(Exception): ...


class CellIntegerException(CellException): ...


class CellFloatException(CellException): ...


class CellStringException(CellException): ...


class CellInteger:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        # self.value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value=None):
        if value and not (self.min_value <= value <= self.max_value):
            raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
        self.min__value = value


class CellFloat:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value and not (self.min_value <= value <= self.max_value):
            raise CellFloatException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
        self.min__value = value


class CellString:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value and not (self.min_value <= len(value) <= self.max_value):
            raise CellStringException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
        self.min__value = value


class TupleData:
    def __init__(self, *args):
        self.data = list(args)

    def _check(self, index):
        if not (0 <= index <= len(self.data)):
            raise IndexError
        return True

    def __getitem__(self, key):
        if self._check(key):
            return self.data[key]

    def __setitem__(self, key, value):
        if self._check(key):
            self.data[key] = value

    def __len__(self):
        return len(self.data)

    def __call__(self):
        res = [val.value for val in self.data]
        return res


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")


############################################################
class Cell:
    def __init__(self, _min_value, _max_value):
        self._min_value = _min_value
        self._max_value = _max_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value=None):
        if value:
            if type(value) == int and not (self._min_value <= value <= self._max_value):
                raise CellIntegerException('значение выходит за допустимый диапазон')
            elif isinstance(value, float) and not (self._min_value <= value <= self._max_value):
                raise CellFloatException('значение выходит за допустимый диапазон')
            elif isinstance(value, str) and not (self._min_value <= len(value) <= self._max_value):
                raise CellStringException('значение выходит за допустимый диапазон')
        self.__value = value


class CellInteger(Cell): ...


class CellFloat(Cell): ...


class CellString(Cell): ...


########################################################
class Cell:
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, '_' + k, v)
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = self._check_value(value)

    def _check_value(self, value):
        raise NotImplementedError('method _check_value should be implemented in subclass')


class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _check_value(self, value):
        if type(value) == int and not (self._min_value <= value <= self._max_value):
            raise CellIntegerException('значение выходит за допустимый диапазон')
        return value


class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _check_value(self, value):
        if type(value) == float and not (self._min_value <= value <= self._max_value):
            raise CellFloatException('значение выходит за допустимый диапазон')
        return value


class CellString(Cell):
    def __init__(self, min_length, max_length):
        super().__init__(min_length=min_length, max_length=max_length)

    def _check_value(self, value):
        if type(value) == str and not (self._min_length <= len(value) <= self._max_length):
            raise CellStringException('значение выходит за допустимый диапазон')
        return value


class TupleData:
    def __init__(self, *args):
        [self._is_cell(x) for x in args]
        self.data = tuple(args)

    @staticmethod
    def _is_cell(value):
        if not isinstance(value, Cell):
            raise TypeError('Not a cell')

    def _check(self, index):
        if not (0 <= index <= len(self.data)):
            raise IndexError
        return True

    def __getitem__(self, key):
        if self._check(key):
            return self.data[key].value

    def __setitem__(self, key, value):
        if self._check(key):
            self.data[key].value = value

    def __len__(self):
        return len(self.data)

    # def __call__(self):
    #     res = [val.value for val in self.data]
    #     return res
    def __iter__(self):
        for v in self.data:
            yield v.value


############################################################
class CellException(Exception):
    msg = 'значение выходит за допустимый диапазон'


class CellIntegerException(CellException): ...


class CellFloatException(CellException): ...


class CellStringException(CellException):
    msg = 'длина строки выходит за допустимый диапазон'


class Types:
    value_type = str
    exception = CellStringException

    def __init__(self, *args):
        self.__data = None
        self._min_value, self._max_value = args[:2]
        if self.value_type == str:
            self._min_length, self._max_length = args[:2]

    @property
    def value(self):
        return self.__data

    @value.setter
    def value(self, value):
        val = value
        if self.value_type == str:
            val = len(str(value))
        if isinstance(value, self.value_type) and self._min_value <= val <= self._max_value:
            self.__data = value
        else:
            raise self.exception(self.exception.msg)

    def __str__(self):
        return str(self.__data)


class CellInteger(Types):
    value_type = int
    exception = CellIntegerException


class CellFloat(CellInteger):
    value_type = float
    exception = CellFloatException


class CellString(Types): ...


class TupleData(list):
    def __init__(self, *args):
        super().__init__(args)


########################################################
# _______________5.6 Менеджер контекста_______________________
class FileContext:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        print(('opening file'))
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(('stopping file'))
        self.file.close()


with FileContext('pass.txt', 'r') as file:
    print(file.read())

print('Finally ending')


############################################################
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print("Error: File not found")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with FileManager("test.txt", "r") as f:
    if f:
        print(f.read())


# В этом прим.__enter__() открывает файл и возвращает объект файла. Если файл не может быть открыт, он возвращает None
# __exit__() закрывает файл. Если при работе с файлом возникли ошибки, exc_type, exc_value и traceback содержат
# информацию об ошибке.В этом примере контекстный менеджер открывает файл "test.txt" для чтения и закрывает его после
# окончания работы. Если файл не найден, выводится сообщение об ошибке. Если файл успешно открыт, он выводится на экран
########################################################
class Counter:
    def __enter__(self):
        self.a = 7
        self.b = 0
        return lambda: self.b - self.a

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.b = 10  # при закрытии переименование self.b на 0


with Counter() as c:
    print(c())  # -7
print(c())  # 3


############################################################
class Counter:
    def __enter__(self):
        self.a = 7
        self.b = 0
        print('step 1')
        return lambda: 'step 3'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('step 5')
        self.b = 10


with Counter() as c:
    print('step 2')
    print(c())  # step 3
    print('step 4')


# step 1
# step 2
# step 3
# step 4
# step 5

########################################################
class CustomContextManager:

    def __enter__(self):
        print("1. Заходим в менеджер контекста")
        return lambda: '2. Возвращаем что-то из контекста, если нужно'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("3. Что-то совершаем перед выходом и покидаем менеджер контекста")


with CustomContextManager() as ccm:
    print(ccm())


# 1. Заходим в менеджер контекста
# 2. Возвращаем что-то из контекста, если нужно
# 3. Что-то совершаем перед выходом и покидаем менеджер контекста
############################################################
class DefenedVector:
    def __init__(self, v):
        self.v = v

    def __enter__(self):
        self.temp = self.v[:]  # делаем копию вектора v;
        # создает копию списка v (который хранится в self.v) и присваивает ее переменной self.temp
        return self.temp

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            self.v[:] = self.temp  # Срез self.v[:] создает копию списка self.temp и
            # присваивает его элементы в список self.v
        return False  # без неё тоже работает и исключение не подавляется , return можно вовсе опустить,
        # тогда метод exit возвратит None, а оно интерпретируется как False. Так что, часто его не пишут.


v1 = [1, 2, 3, 4, 5]
v2 = [1, 2, 3, 4]
try:
    with DefenedVector(v1) as dv:
        for i, v in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Error")
print(v1)  # В результате, при выходе из менеджера, мы получим измененный вектор v1. Если же было какое-либо исключение,
# то запись новых данных выполняться не будет и у нас останется прежний вектор v1.
print(dv)
# Error
# [1, 2, 3, 4, 5] # v1 не изменился т.к. разные длины v1 v2
# [2, 4, 6, 8, 5]
# В данном коде, return False используется для того, чтобы не подавить исключение, вызванное в блоке with. Если в блоке
# with возникает исключение, то блок __exit__ будет вызван со значениями exc_type, exc_value и exc_traceback, указывая
# на исключение, которое произошло. Если __exit__ возвращает True, то исключение подавляется, и программа продолжает
# выполнение сразу после блока with. Если __exit__ возвращает False или не возвращает ничего, то исключение не
# подавляется и передается дальше для обработки.В данном случае, return False гарантирует, что исключение не будет
# подавлено, и программа будет продолжать выполнение после блока with. Это позволяет выполнить инструкцию
# print("Error") в случае возникновения исключения в блоке with.

# Про self.__v[:] = self.__temp. [:] здесь – это не копия, а срез. То есть мы заменяем данные
# с 0 элемента по -1, аналогом можно было написать [0:999] – все значения меняются на self.__temp. Таким образом
# сохраняется id, а элементы уже новые Зачем? Без среза программа не работает как надо – не изменяет данные в менеджере.
# Я не знаю точно, почему так. Но id у двух переменных self.__v разные. А если посмотреть через дебаг, то вот изменение:
# передаём v1, а на выходе изменённый список в это переменную не передаётся! А если срез использовать, то тогда и
# список изменённый передаётся, и id одинаковый. Так что, скорее всего, нужно сохранять исходную ссылку на переменную
# в методе __exit__ Кстати, а если убрать срез присвоении self.__temp (делаем копию вектора v), то всё прекрасно
# работает. Можно вообще срезы везде убрать и всё заработает...

# self.v[:] в данном контексте используется для создания копии списка v в методе __enter__ класса DefenedVector.
# Когда мы выполняем self.temp = self.v[:], мы создаем новый список temp, который содержит те же элементы, что и
# self.v, но это будет отдельный список в памяти. Если бы мы просто присвоили self.temp = self.v, то self.temp и
# self.v были бы двумя переменными, ссылающимися на один и тот же список. Таким образом, при изменении self.temp,
# также изменялись бы и self.v, что мы хотим избежать. Использование синтаксиса [:] для создания копии списка называется
# срез списков. Срез создает новый список, содержащий элементы из исходного списка, и позволяет избежать проблемы
# совместного использования ссылок на один и тот же список.В данном случае, self.v[:] создает копию списка v
# (который хранится в self.v) и присваивает ее переменной self.temp. Таким образом, self.temp будет ссылаться на
# новый список с теми же элементами, что и self.v, но это будут два отдельных списка в памяти.

# Срез self.v[:] создает копию списка self.temp и присваивает его элементы в список self.v. Таким образом, если
# self.temp изменяется после этого, оригинальный список self.v остается неизменным. Когда мы просто выполняем
# self.v = self.temp, новая ссылка self.v будет указывать на тот же объект-список, что и self.temp. Если мы после
# этого изменим элементы в self.temp, то изменения отразятся и на self.v, так как они ссылаются на один и тот же список
# в памяти. Итак, использование среза self.v[:] в данном случае является безопасной практикой, чтобы гарантировать,
# что мы создаем копию списка и избегаем неожиданного изменения в оригинальном списке self.v.
########################################################
v1 = [1, 2, 3, 4, 5]
v2 = [1, 2, 3, 4, 5]
try:
    with DefenedVector(v1) as dv:
        for i, v in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Error")
print(v1)
print(dv)
# [2, 4, 6, 8, 10] # v1 изменился
# [2, 4, 6, 8, 10]
############################################################
try:
    with open("myfile.txt") as fin:
        with open("out.txt", "w") as fout:
            for line in fin:
                fout.write(line)
except Exception as e:
    print(e)


# Сначала завершается (отрабатывает) вложенный менеджер, а затем, внешний (первый)
########################################################
# Подвиг 3. Объявите класс PrimaryKey, который должен работать совместно с менеджером контекста следующим образом:
# with PrimaryKey() as pk:
# raise ValueError
# где pk - ссылка на объект класса PrimaryKey. Класс PrimaryKey должен в момент входа в менеджер контекста выводить
# на экран сообщение "вход", а при завершении работы менеджера контекста выводить тип возникшего исключения.
# Класс PrimaryKey следует реализовать так, чтобы менеджер контекста сам обрабатывал возникшее исключение.
class PrimaryKey:
    def __enter__(self):
        print("вход")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(exc_type)
        return True  # обработка, значит, отловить исключение и что-то сделать. при возникновении исключения, оно было
        # перехвачено менеджером и далее уже не распространялось


# метод __exit__ возвращает True, чтобы указать, что исключение было обработано.
# Метод exit у нас возвращает значение False, что означает обработку исключения (если оно произошло) вышестоящим блоком.
# Обычно именно так и делают, чтобы не скрывать возможные ошибки и в обработчике верхнего уровня реагировать должным
# образом на ошибочные ситуации. Кстати, оператор return можно вовсе опустить, тогда метод exit возвратит None, а оно
# интерпретируется как False. Так что, часто его не пишут.
# Давайте для примера возвратим значение True и смотрите, при возникновении исключения, оно было перехвачено менеджером
# и далее уже не распространялось. Снова вернем False, запустим и теперь видим это исключение снова.

with PrimaryKey() as pk:
    raise ValueError


############################################################
class PrimaryKey:
    def __enter__(self):
        print('вход')

    def __exit__(self, *args):
        print(args[0])
        return True


########################################################
class PrimaryKey:

    def __init__(self):
        self.__enter = 'вход'
        self.__exit = 'выход'

    def __enter__(self):
        print(self.__enter)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(self.__exit)

        print(exc_type)
        return True


############################################################
# Подвиг 4. Вам поручено разработать класс DatabaseConnection для управления подключением к базе данных. Объекты этого
# класса создаются командой:conn = DatabaseConnection()В самом классе необходимо объявить метод:
# def connect(self, login, password): ...для подключения к БД. В данной реализации этот метод должен устанавливать
# локальный атрибут _fl_connection_open в значение True:_fl_connection_open = True
# и генерировать исключение с помощью собственного класса ConnectionError унаследованного от базового класса Exception.
# Также в классе DatabaseConnection должен быть метод:def close(self): ...для закрытия соединения. В этом методе
# нужно атрибут _fl_connection_open установить в значение False.Метод close() необходимо вызывать всякий раз после
# завершения работы с БД, вне зависимости от того, произошли какие-либо исключения или нет.Этот функционал
# (автоматическое закрытие соединения с БД) предполагается реализовывать посредством менеджера контекста с
# использованием класса DatabaseConnection следующим образом:with DatabaseConnection() as conn:# операторы менеджера
# контекста Пропишите дополнительно в классе DatabaseConnection необходимые магические методы для такого его
# использования совместно с оператором with.
class ConnectionError(Exception): ...


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = None

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError()

    def close(self):
        self._fl_connection_open = False

    # для работы с менеджером контекста
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()


#  with DatabaseConnection() as conn: # вызов __enter__,который ссылается на conn,__enter__ возвращает текущий obj self
#     # операторы менеджера контекста

c = DatabaseConnection()

try:
    c.connect('aaa', 'bbb')
except ConnectionError:
    assert c._fl_connection_open
else:
    assert False, "не сгенерировалось исключение ConnectionError"


########################################################
# Подвиг 5. Объявите класс Box (ящик), объекты которого создаются командой:box = Box(name, max_weight)
# где name - название ящика (строка); max_weight - максимальный суммарный вес вещей в ящике (любое положительное число).
# В каждом объекте этого класса должны формироваться локальные атрибуты:_name - ссылка на параметр name;
# _max_weight - ссылка на параметр max_weight;_things - список из вещей, хранящиеся в ящике (изначально пустой список).
# В классе Box объявите метод:def add_thing(self, obj)для добавления новой вещи в ящик, где obj - кортеж из двух
# значений:(название_вещи, вес_вещи)Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится
# больше величины _max_weight, то генерировать исключение командой:raise ValueError('превышен суммарный вес вещей')
# Затем, объявите еще один класс BoxDefender, который должен работать совместно с менеджером контекста следующим
# образом (эти строчки в программе не писать):box = Box("сундук", 1000)box.add_thing(("спички", 46.6))
# box.add_thing(("рубашка", 134))
# with BoxDefender(box) as b:
# b.add_thing(("зонт", 346.6))
# b.add_thing(("шина", 500))  ...
# Здесь b - это ссылка на объект класса Box. Если при добавлении вещей возникает исключение ValueError, то объект box
# должен оставаться без изменений (с теми вещами, что были до вызова менеджера контекста). Иначе, все добавленные вещи
# остаются в объекте box.
class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = list()

    def add_thing(self, obj):
        if sum(map(lambda x: x[1], self._things)) + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)


class BoxDefender:
    def __init__(self, box):
        self._box = box
        self.thing = box._things[:]
        # self.thing = copy.deepcopy(box._things)
        # self.thing = box.things.copy()

    def __enter__(self):
        return self._box  # чтобы работать в менеджере контекста с классом Box()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            self._box._things = self.thing  # если исключение возникло присваиваем копию до вызова менеджера контекста


box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))
    ...
############################################################
class PrinterError(Exception):
    """Класс общих ошибок принтера"""


class PrinterConnectionError(PrinterError):
    """Ошибка соединения с принтером"""


class PrinterPageError(PrinterError):
    """Ошибка отсутствия бумаги в принтере"""


try:
    raise PrinterConnectionError('соединение с принтером отсутствует')
except (PrinterConnectionError, PrinterPageError) as e:
    print(e)
except PrinterError as e:
    print(e)
    #при возникновении исключений PrinterConnectionError или PrinterPageError выполнение программы перейдет в блок
    # except с этими двумя классами
    #при выполнении программы на экране будет отображена строка "соединение с принтером отсутствует"
########################################################
