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
            result = x**num
            return result
        return wrapper
    return decorator

@digits_dec(2) # по умолчанию берет степень НОЛЬ измените на @digits_dec(2)
def a(x):
    return x

print(a(11))


from functools import wraps

# В decorator_without_param передается ссылка на декорируемую функцию.
def decorator_without_param(*args, **kwargs):
    # args = (<function function at 0x00000220D56EB670>,)
    # kwargs = {}
    func, *other_args = args
    # Что бы не изненять свойства декорированной функции (from functools import wraps)
    @wraps(func)
    # В wrapper передаются аргументы декорируемой функции.
    def wrapper(*args, **kwargs):
        # args = ('string1', 'string2')
        # kwargs = {'str3': 'string3', 'str4': 'string4'}
        print('Декоратор что то делает перед вызовом декорированной функции.')
        result = func(*args, **kwargs)
        print(f'Декоратор распечатал результат декорируемой функции --> {result}')
        print('Декоратор что то делает после вызова декорированной функции.')
        return result
    return wrapper


@decorator_without_param
def function(string1, string2, str3, str4):
    """Documentation of function."""
    return string1, string2, str3, str4


function('string1', 'string2', str3='string3', str4='string4')
print('\n'*3)
# Декоратор что то делает перед вызовом декорированной функции.
# Декоратор распечатал результат декорируемой функции --> ('string1', 'string2', 'string3', 'string4')
# Декоратор что то делает после вызова декорированной функции.


# В decorator_with_param передаются параметры класса декоратора.
def decorator_with_param(*args, **kwargs):
    # args = ('param1', 'param2')
    # kwargs = {'parameter3': 'param3', 'parameter4': 'param4'}
    param1, param2, *other_args = args
    param3, param4, *other_kwargs = kwargs.values()
    # В get_func передается ссылка на декорируемую функцию.
    def get_func(*args, **kwargs):
        # args = (<function function at 0x000001C95974B790>,)
        # kwargs = {}
        func, *other_args = args
        # Что бы не изненять свойства декорированной функции (from functools import wraps)
        @wraps(func)
        # В wrapper передаются аргументы декорируемой функции.
        def wrapper(*args, **kwargs):
            # args = ('string1', 'string2')
            # kwargs =  {'str3': 'string3', 'str4': 'string4'}
            print('Декоратор что то делает перед вызовом декорированной функции.')
            result = func(*args, **kwargs)
            print(f'Декоратор распечатал результат декорируемой функции --> {result}')
            print(f'Декоратор распечатал свои параметры --> {param1, param2, param3, param4}')
            print('Декоратор что то делает после вызова декорированной функции.')
        return wrapper
    return get_func


@decorator_with_param('param1', 'param2', parameter3='param3', parameter4='param4')
def function(string1, string2, str3, str4):
    """Documentation of function."""
    return string1, string2, str3, str4


function('string1', 'string2', str3='string3', str4='string4')
print('\n'*3)
# Декоратор что то делает перед вызовом декорированной функции.
# Декоратор распечатал результат декорируемой функции --> ('string1', 'string2', 'string3', 'string4')
# Декоратор распечатал свои параметры --> ('param1', 'param2', 'param3', 'param4')
# Декоратор что то делает после вызова декорированной функции.


class DecoratorWithoutParams:
    # В __init__ передается ссылка на декорируемую функцию.
    def __init__(self, *args, **kwargs):
        # args = (<function function at ...>,),
        # kwargs = {}
        self.func, *self.other = args

    # В __call__ передаются аргументы декорируемой функции.
    def __call__(self, *args, **kwargs):
        # args = ('string1', 'string2'),
        # kwargs =  {'str3': 'string3', 'str4': 'string4'}
        print('Декоратор что то делает перед вызовом декорированной функции.')
        result = self.func(*args, **kwargs)
        print(f'Декоратор распечатал результат декорируемой функции --> {result}')
        print('Декоратор что то делает после вызова декорированной функции.')
        # Что бы не изненять свойства декорированной функции
        self.__class__.__name__ = self.func.__name__
        self.__class__.__doc__ = self.func.__doc__
        return result


@DecoratorWithoutParams
def function(string1, string2, str3, str4):
    """Documentation of function."""
    return string1, string2, str3, str4


function('string1', 'string2', str3='string3', str4='string4')
print('\n'*3)
# Декоратор что то делает перед вызовом декорированной функции.
# Декоратор распечатал результат декорируемой функции --> ('string1', 'string2', 'string3', 'string4')
# Декоратор что то делает после вызова декорированной функции.


class DecoratorWithParams:
    # В __init__ передаются параметры класса декоратора.
    def __init__(self, *args, **kwargs):
        # args = ('param1', 'param2'),
        # kwargs = {'parameter3': 'param3', 'parameter4': 'param4'}
        self.param1, self.param2, *self.other_args = args
        self.param3, self.param4, *self.other_kwargs = kwargs.values()

    # В __call__ передается ссылка на декорируемую функцию.
    def __call__(self, *args, **kwargs):
        # args = (<function function at 0x000001E19DC7A940>,),
        # kwargs = {}
        self.func, *self.other = args
        # Что бы не изненять свойства декорированной функции (from functools import wraps)
        @wraps(self.func)
        # В wrapper передаются аргументы декорируемой функции.
        def wrapper(*args, **kwargs):
            # args = ('string1', 'string2'),
            # kwargs = {'str3': 'string3', 'str4': 'string4'}
            print('Декоратор что то делает перед вызовом декорированной функции.')
            result = self.func(*args, **kwargs)
            print(f'Декоратор распечатал результат декорируемой функции --> {result}')
            print(f'Декоратор распечатал свои параметры --> {self.param1, self.param2, self.param3, self.param4}')
            print('Декоратор что то делает после вызова декорированной функции.')
            return result
        return wrapper


@DecoratorWithParams('param1', 'param2', parameter3='param3', parameter4='param4')
def function(string1, string2, str3, str4):
    """Documentation of function."""
    return string1, string2, str3, str4


function('string1', 'string2', str3='string3', str4='string4')
print('\n'*3)
# Декоратор что то делает перед вызовом декорированной функции.
# Декоратор распечатал результат декорируемой функции --> ('string1', 'string2', 'string3', 'string4')
# Декоратор распечатал свои параметры --> ('param1', 'param2', 'param3', 'param4')
# Декоратор что то делает после вызова декорированной функции.


# Подвиг 9 (на повторение). Необходимо объявить функцию-декоратор class_log для класса, которая бы создавала логирование
# вызовов методов класса. Например следующие строчки программы:vector_log = []  @class_log(vector_log)
# декорируют класс Vector и в список vector_log добавляются имена методов, которые были вызваны при использовании этого
# класса. В частности, после выполнения команд:v = Vector(1, 2, 3)v[0] = 10в списке vector_log должны быть два метода:
# ['__init__', '__setitem__']Ваша задача реализовать декоратор с именем class_log.

# Напоминание. Ранее вы уже создавали функцию-декоратор для класса следующим образом:
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         setattr(cls, k, integer_params_decorated(v))
#     return cls
# Здесь у нас на вход принимается ссылка на класс, потому что мы декорируем класс. В нашем случае, это будет ссылка на
# класс Vector. Далее, имея эту ссылку, мы можем пройтись по коллекции __dict__ этого класса (cls.__dict__),
# __dict__ - это словарь, который хранит имя атрибута (к) класса и его значение (v). Т.к. методы - это тоже атрибуты
# класса, только в виде функций, то в значениях (v) хранится ссылка на функцию, т.е. на этот метод. И далее, методом
# callable() мы проверяем, что если это действительно функция, мы его имя и значение помещаем в переменную methods.
# Т.е. фильтруем коллекцию __dict__ и в methods оставляем только функции (методы). После этого мы перебираем эту
# отфильтрованную коллекцию methods, и с помощью setattr как бы ещё раз создаём в нашем классе эти методы с названием k,
# но только теперь мы их декорируем декоратором integer_params_decorated(v) (здесь v - это ссылка на функцию (метод)).
# И вот уже в этом декораторе мы прописываем логику, что при вызове этот метод нужно добавить в список логов. При этом
# обратите внимание, методы просто становятся декорированные. Это не значит, что как только вы его декорировали, он
# сразу улетает в список логов. Декоратор срабатывает только при вызове функции, в нашем случае методов. Т.е. пока
# методы не вызываются, у нас класс просто превращается в такой вид:
# class Vector:
#     @integer_params_decorated()
#     def __init__(self):
#         pass
# А вот срабатывать этот декоратор будет только при вызове функции (метода). И соответственно, логика, прописанная в
# этом декораторе, будет выполняться только при вызове метода

# здесь 2 декоратора - 1 декоратор класса, 2 декоратор функции, только декоратор функции используем не через синтаксис
# @decorator а обычным вызовом class.method = decorator(class.method). В декораторе класса у нас есть такой код :
# for k, v in cls.__dict__.items():
#       if callable(v):
#           setattr(cls, k, decorator(v))
# return cls Здесь мы берем все аттрибуты класса (именно класса, а не экземпляра класса) из словаря __dict__
# перебираем их и проверяем если аттрибут является вызываем (т.е. методом) callable(v) если аттрибут является методом
# то мы переназначаем на его имя k  декорированный декоратором функции decorator(v) метод v . Мы бы могли сделать
# аналогичный функционал без декоратора класса если бы каждый метод класса обернули декоратором @decorator(vector_log).
# Правда для этого надо немного изменить декоратор для того что бы он мог принимать аргумент.vector_log = []
vector_log = []


def class_log(lst):
    def dec_class(cls):  # class Vector
        method = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in method.items():  # в methods помещаются все вызываемые методы из класса cls (__init__, __setitem__)
            setattr(cls, k, dec_method(v, lst))  # v = dec_method(v, lst)

        return cls

    return dec_class


def dec_method(func_method, lst):
    def wrapper(*args, **kwargs):
        lst.append(func_method.__name__)
        return func_method(*args, **kwargs)

    return wrapper


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)


#######################################################################
def class_log(lst):
    def dec_class(cls):
        for name, method in cls.__dict__.items():
            if callable(method):
                setattr(cls, name, dec_method(method, lst))

            def dec_method(func_method, lst):
                def wrapper(*args, **kwargs):
                    lst.append(func_method.__name__)
                    return func_method(*args, **kwargs)

                return wrapper

        return cls

    return dec_class


################################################################################################################################
def class_log(lst):
    def dec_class(cls):
        for name, method in cls.__dict__.items():
            if callable(method):
                setattr(cls, name, dec_method(method, lst))
        return cls

    return dec_class


def dec_method(func_method, lst):
    def wrapper(*args, **kwargs):
        lst.append(func_method.__name__)
        return func_method(*args, **kwargs)

    return wrapper


################################################################
#  class_decorators
class class_log:
    def __init__(self, lst):
        self.storage = lst

    def __call__(self, cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, self.decorated(v))
        return cls

    def decorated(self, func):
        def wrapper(*args):
            self.storage.append(func.__name__)
            return func(*args)

        return wrapper


################################################################
def class_log(log_descriptor):
    def decorator(method):
        def wrapper(*args, **kwargs):
            log_descriptor.append(method.__name__)
            return method(*args, **kwargs)

        return wrapper

    def class_decorator(cls):
        for k, v in cls.__dict__.items():
            if callable(v):
                setattr(cls, k, decorator(v))
        return cls

    return class_decorator


################################################################
# Сделал декоратор класса, который декорирует все методы, которые могут быть вызваны...
def class_log(vector_log):
    def decor(cls):
        methods = {name: method for name, method in cls.__dict__.items() if callable(method)}

        def counter(method):

            def wrapper(self, *args):
                if method.__name__ not in vector_log:
                    vector_log.append(method.__name__)
                return method(self, *args)

            return wrapper

        for method_name in methods:
            setattr(cls, method_name, counter(methods[method_name]))

        return cls

    return decor


################################################################
# Здесь мы модифицировали наш старый декоратор таким образом, чтобы он выполнял декорируемую функцию iters раз, а затем
# выводил среднее время выполнения. Однако чтобы добиться этого, пришлось воспользоваться природой функций в Python.
# Функция benchmark() на первый взгляд может показаться декоратором, но на самом деле таковым не является. Это обычная
# функция, которая принимает аргумент iters, а затем возвращает декоратор. В свою очередь, он декорирует функцию
# fetch_webpage(). Поэтому мы использовали не выражение @benchmark, а @benchmark(iters=10) — это означает, что тут
# вызывается функция benchmark() (функция со скобками после неё обозначает вызов функции), после чего она возвращает
# сам декоратор.Да, это может быть действительно сложно уместить в голове, поэтому держите правило:
# Декоратор принимает функцию в качестве аргумента и возвращает функцию.В нашем примере benchmark() не удовлетворяет
# этому условию, так как она не принимает функцию в качестве аргумента. В то время как функция actual_decorator(),
# которая возвращается benchmark(), является декоратором.


def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)


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
# Подвиг 9 (на повторение). Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса
# StringDigit должны создаваться командой:sd = StringDigit(string)где string - строка из цифр (например,
# "12455752345950"). Если в строке string окажется хотя бы один не цифровой символ, то генерировать исключение
# командой:raise ValueError("в строке должны быть только цифры")Также в классе StringDigit нужно переопределить
# оператор + (конкатенации строк) так, чтобы операции:sd = sd + "123"sd = "123" + sdсоздавали новые объекты класса
# StringDigit (а не класса str). Если же при соединении строк появляется не цифровой символ, то генерировать
# исключение:raise ValueError("в строке должны быть только цифры")

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

########################################################################
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

########################################################################
# _____4.1 Наследование в объектно-ориентированном программировании________________________
# Подвиг 4. Наследование часто используют, чтобы вынести общий код дочерних классов в базовый класс. Сделаем такой
# пример. Объявите в программе базовый класс Animal (животное), объекты которого можно создать командой:
# an = Animal(name, old)где name - название животного (строка); old - возраст животного (целое число). Такие же
# локальные атрибуты (name и old) должны создаваться в объектах класса.Далее, объявите дочерний класс
# (от базового Animal) с именем Cat (кошки), объекты которого создаются командой:cat = Cat(name, old, color, weight)
# где name, old - те же самые параметры, что и в базовом классе; color - цвет кошки (строка); weight - вес кошки
# (любое положительное число).В объектах класса Cat должны автоматически формироваться локальные атрибуты: name,
# old, color, weight. Формирование атрибутов name, old должен выполнять инициализатор базового класса.
# По аналогии объявите еще один дочерний класс Dog (собака), объекты которого создаются командой:
# dog = Dog(name, old, breed, size)здесь name, old - те же самые параметры, что и в базовом классе;
# breed - порода собаки (строка); size - кортеж в формате (height, length) высота и длина - числа.
# В объектах класса Dog по аналогии должны формироваться локальные атрибуты: name, old, breed, size.
# За формирование атрибутов name, old отвечает инициализатор базового класса. Наконец, в классах Cat и Dog
# объявите метод:get_info() - для получения информации о животном.Этот метод должен возвращать строку в формате:
# "name: old, <остальные параметры через запятую>"

from typing import Any


class Animal:

    def __init__(self, name, old):

        self.name = name
        self.old = old

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'name' and self.check_string(__value):
            raise AttributeError('name should be a atring')

        if __name == 'old' and type(__value) is not int:
            raise AttributeError('old should be an int')

        super().__setattr__(__name, __value)

    @classmethod
    def check_string(self, value):
        if type(value) is not str:
            raise ValueError('value should be a string')

    @classmethod
    def check_positive_value(self, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError('value should be positive int or float')

    @classmethod
    def check_tuple(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise ValueError('value should be a tuple with two items')
        h, l = value
        if type(h) not in (int, float) or type(l) not in (int, float):
            raise ValueError('values in tuple should be in (int, float)')

    @staticmethod
    def dec(func):
        def wrapper(self):
            res = f'{self.name}: {self.old}, '
            cur = func(self)
            return res + cur

        return wrapper


class Cat(Animal):

    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.check_string(color)
        self.color = color
        self.check_positive_value(weight)
        self.weight = weight

    @Animal.dec
    def get_info(self):
        return f'{self.color}, {self.weight}'


class Dog(Animal):

    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.check_string(breed)
        self.breed = breed
        self.check_tuple(size)
        self.size = size

    @Animal.dec
    def get_info(self):
        return f'{self.breed}, {self.size}'


c = Cat('кот', 4, 'black', 2.25)
print(c.get_info())

########################################################################
# Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, ..., xN)где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).
# С объектами этого класса должны выполняться команды:v1 = Vector(1, 2, 3)v2 = Vector(3, 4, 5)
# v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:raise TypeError('размерности векторов
# не совпадают')В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих
# координат вектора.На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:
# v = VectorInt(1, 2, 3, 4)v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты
# должны быть целыми числами')При операциях сложения и вычитания с объектом класса VectorInt:v = v1 + v2  # v1 -
# объект класса VectorIntv = v1 - v2  # v1 - объект класса VectorIntдолжен формироваться объект v как объект класса
# Vector, если хотя бы одна координата является вещественной. Иначе, v должен быть объектом класса VectorInt.
class Vector:

    def __init__(self, *args):
        self.coords = list(args)

    def get_coords(self):
        return tuple(self.coords)

    def validate(func):
        def wrapper(instance, other, *args):
            if len(instance) != len(other):
                raise TypeErro('размерности векторов не совпадают')
            elif type(instance) == VectorInt:  # случай, когда второй параметр принадлежит к типу VectorInt
                instance, other = other, instance  # для первого парам. (если он VectorInt) замена не требуется,
                return func(instance, other)  # т.к. type(self) = Vector в методах add и sub
            else:
                return func(instance, other)

        return wrapper

    def __len__(self):
        return len(self.coords)

    @validate
    def __add__(self, other):
        return type(self)(*map(sum, zip(self.coords, other.coords)))

    @validate
    def __sub__(self, other):
        return type(self)(*map(lambda x, y: x - y, self.coords, other.coords))  # type(self) будет оцениваться
        # как Vector или VectorInt Цель использования type(self) состоит в обработке случая, когда второй параметр
        # (other) принадлежит классу VectorInt. В этом случае декоратор меняет местами позиции instance и other перед
        # вызовом фактического метода оператора. Это позволяет правильно выполнять сложение или вычитание, независимо
        # от того, является ли экземпляр типом VectorInt или другого класса.


class VectorInt(Vector):

    def __init__(self, *args):
        if list(map(int, list(args))) == list(args):
            super().__init__()
            self.coords = list(args)
        else:
            raise ValueError('координаты должны быть целыми числами')

########################################################################
