# Испытание свойствами и методами Видео-разбор (решение смотреть только после своей попытки):
# https://youtu.be/26pwwOu_-d0    Время первого испытания. Представьте, что вы получили задание от заказчика.
# Вас просят реализовать простую имитацию локальной сети, состоящую из набора серверов, соединенных между собой
# через роутер.Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у каждого есть свой
# уникальный IP-адрес. Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов.
# Алгоритм следующий. Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3. Для этого,
# он сначала отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).

class Server:
    """для описания работы серверов в сети Соответственно в объектах класса Server должны быть локальные свойства:"""
    server__ip = 1

    def __init__(self):
        self.buffer = []  # buffer - список принятых пакетов (изначально пустой)
        self.ip = Server.server__ip  # ip - IP-адрес текущего сервера, каждый новый созданный объект = ip предыдущего + 1
        Server.server__ip += 1
        self.router = None  # привязка объекта сервера к роутеру

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
        (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer); """
        if self.router:
            self.router.buffer.append(data)
            # self.router-вызвать объект роутера и добавить в buffer в классе роутера data

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список) и очищает входной буфер;   """
        packets = self.buffer[:]
        self.buffer.clear()
        return packets

    def get_ip(self):
        """возвращает свой IP-адрес.  """
        return self.ip


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер). И одно обязательное локальное
    свойство (могут быть и другие свойства):   """

    def __init__(self):
        self.buffer = []  # список для хранения принятых от серверов пакетов (объектов класса Data).
        self.servers = {}  # список серверов подключенных к роутеру, объекты класса Server от которых принимаются пакеты
        # и отправляются пакеты из роутера другим серверам

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру  """
        self.servers[server.ip] = server  # для присоединения сервера server (объекта класса Server)
        server.router = self  # связывания роутера с сервером

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера        """
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None  # отвязка роутера от сервера

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера
                соответствующим серверам (после отправки буфер должен очищаться) """

        for d in self.buffer:  # перебрать d объекты класса Data
            if d.ip in self.servers:  # ip - IP-адрес назначения из класса Data
                self.servers[d.ip].buffer.append(d)  # обратиться по ip к соотв серверу и
                # добавили пакет d в buffer кл Server
        self.buffer.clear()


class Data:
    """для описания пакета информации объекты класса Data должны содержать, два следующих локальных свойства: """

    def __init__(self, data, ip):
        self.data = data  # data - передаваемые данные (строка)
        self.ip = ip  # ip - IP-адрес назначения.


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()


# if Router alone   ################################
class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    ip = 1

    def __init__(self):
        self.ip = self.__class__.ip
        self.__class__.ip += 1
        self.buffer = []

    def get_data(self):
        inbox_data = self.buffer[:]
        self.buffer = []
        return inbox_data

    def get_ip(self):
        return self.ip

    @staticmethod
    def send_data(data):
        router.buffer.append(data)


class Router:
    buffer = []
    linked_servers = []

    @classmethod
    def link(cls, server):
        cls.linked_servers.append(server)
        server.router = cls

    @classmethod
    def unlink(cls, server):
        cls.linked_servers.remove(server)
        server.router = None

    @classmethod
    def send_data(cls):
        temp_buffer = Router.buffer[:]
        Router.buffer.clear()
        for dt in temp_buffer:
            for ls in cls.linked_servers:
                if dt.ip == ls.ip:
                    ls.buffer.append(dt)


#####___ several Routers___ #####
class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    ip = 1

    def __init__(self):
        self.ip = Server.ip
        Server.ip += 1
        self.buffer = []
        self.router = None

    def get_data(self):
        inbox_data = self.buffer[:]
        self.buffer = []
        return inbox_data

    def get_ip(self):
        return self.ip

    def send_data(self, data):
        self.router.buffer.append(data)


class Router:
    def __init__(self):
        self.buffer = []
        self.linked_servers = []

    def link(self, server):
        self.linked_servers.append(server)
        server.router = self

    def unlink(self, server):
        self.linked_servers.remove(server)
        server.router = None

    def send_data(self):
        temp_buffer = self.buffer[:]
        for dt in temp_buffer:
            for ls in self.linked_servers:
                if dt.ip == ls.ip:
                    ls.buffer.append(dt)
                    self.buffer.remove(dt)


# учел случай, что в нем могут находиться сообщения, адресованные пока еще не подключенным серверам. Потому удалял
# из буффера только реально отправленные сообщения. Неотправленные продолжат оставаться в буффере
################################
class Server:

    def send_data(self, data):  # в классе лучше не обращаться к данным другого класса напрямую
        self.router.receive_data(data)


class Router:

    def receive_data(self, data):
        self.buffer.append(data)


################################################################
class Router:
    # В задаче полагается строго один экземпляр класса Router, поэтому применяем
    # паттерн Singleton
    __INSTANCE = None

    @classmethod
    def get_instance(cls):
        """Чтобы была возможность обращаться к экземпляру класса через имя класса,
        не обращаясь к экземпляру напрямую"""
        return cls.__INSTANCE

    def __new__(cls, *args, **kwargs):
        """Примитивный Singleton"""
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
        return cls.__INSTANCE

    def __init__(self):
        self.linked_servers = {}  # словарь подключенных серверов, доступ по IP
        self.buffer = []  # список принятых от серверов пакетов с данными

    def link(self, server):
        """Подключение сервера к роутеру"""
        self.linked_servers[server.ip] = server

    def unlink(self, server):
        """Отключение сервера от роутера"""
        del self.linked_servers[server.ip]

    def send_data(self):
        """Отправка данных по серверам"""
        for data_package in self.buffer:
            server_to_send = self.linked_servers.get(data_package.ip)  # опред сервер по ip
            server_to_send.buffer.append(data_package)  # отправка соотв серверу
        self.buffer.clear()  # в конце очищаем буфер роутера


class Server:
    """ Последний использованный ip адрес. Нулевой не используется, каждый новый
    созданный сервер имеет ip адрес на один больше предыдущего"""
    __IP = 0

    def __new__(cls, *args, **kwargs):
        """IP адрес для создаваемого экземпляра класса"""
        cls.__IP += 1
        return super().__new__(cls)

    def __init__(self):
        self.buffer = []  # список полученных от роутера данных
        self.ip = self.__IP  # ip адрес сервера

    @staticmethod
    def send_data(data):
        """Для загрузки данных на буфер роутера"""
        Router.get_instance().buffer.append(data)

    def get_data(self):
        """Чтобы получить данные из буфера сервера"""
        temp_buffer = self.buffer.copy()
        self.buffer.clear()  # очищаем буфер после извлечения данных
        return temp_buffer

    def get_ip(self):
        """Чтобы узнать ip адрес"""
        return self.ip


class Data:
    """Класс описывающий данные"""

    def __init__(self, data, ip):
        self.data = data  # Данные в виде строки
        self.ip = ip  # ip сервера получателя


########################################################################
class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    ip = 0

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        cls.ip += 1
        obj.ip = cls.ip
        obj.buffer = []
        return obj

    def get_ip(self):
        return self.ip

    def get_data(self):
        __buffer = self.buffer[:]
        self.buffer.clear()
        return __buffer

    @staticmethod
    def send_data(data: Data):
        Router.buffer.add(data)


class Router:
    buffer = set()
    list_servers = set()

    @classmethod
    def link(cls, server: Server):
        cls.list_servers.add(server)

    @classmethod
    def unlink(cls, server: Server):
        if server in cls.list_servers:
            cls.list_servers.remove(server)

    @classmethod
    def send_data(cls):
        for server in cls.list_servers:
            server.buffer.extend([data for data in cls.buffer if data.ip == server.ip])
        cls.buffer.clear()


########################################################################
class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    ip = 0

    def __init__(self):
        self.ip = Server.ip + 1
        Server.ip = self.ip
        self.buffer = []
        self.router = None

    def get_ip(self):
        return self.ip

    def get_data(self):
        copy_buffer = self.buffer[:]
        self.buffer.clear()
        return copy_buffer

    def send_data(self, data: Data):
        self.router.buffer.add(data)


class Router:
    def __init__(self):
        self.buffer = set()
        self.list_servers = set()

    def link(self, server: Server):
        self.list_servers.add(server)
        server.router = self

    def unlink(self, server: Server):
        if server in self.list_servers:
            self.list_servers.remove(server)
            server.router = None

    def send_data(self):
        for server in self.list_servers:
            server.buffer.extend([data for data in self.buffer if data.ip == server.ip])
        # for server in self.list_servers:
        #     for data in self.buffer:
        #         if data.ip == server.ip:
        #             server.buffer.append(data)
        self.buffer.clear()


########################################################################
class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    ip = 0

    def __init__(self):
        self.ip = self.set_ip()
        self.buffer = []
        self.router = None

    @classmethod
    def set_ip(cls):
        cls.ip += 1
        return cls.ip

    def get_data(self):
        inbox_data = self.buffer[:]
        self.buffer = []
        return inbox_data

    def get_ip(self):
        return self.ip

    def send_data(self, data):
        self.router.buffer.append(data)


class Router:
    def __init__(self):
        self.buffer = []
        self.linked_servers = []

    def link(self, server):
        self.linked_servers.append(server)
        server.router = self

    def unlink(self, server):
        self.linked_servers.remove(server)
        server.router = None

    def send_data(self):
        temp_buffer = self.buffer[:]
        for dt in temp_buffer:
            for ls in self.linked_servers:
                if dt.ip == ls.ip:
                    ls.buffer.append(dt)
                    self.buffer.remove(dt)


########################################################################################################################
# Данное решение частично нарушает концепцию ООП, тк разные классы знают о некоторых методах друг-друга и используют
# "чужие" методы внутри себя, что деалет код не очень гибким, т.к. они начинают зависеть от друг-друга. Я исходил из
# того, что якобы существует стандартизированный псевдо-протокол по которому работают роутеры и сервера, а значит есть
# ряд методов, который обязан у них быть. Отчасти это позволило ужать решение.НО, наиболее лучшим решением будет
# добавление доп функций, где сервер и роутер отправляют сигналы друг-другу о состоянии, но решение что делать
# принимают самостоятельно, используя свои внутринние методы, о которых другие классы ничего не должны знать.
class Router:
    def __init__(self):
        self.buffer = list()
        self.linkedServers = dict()

    def dictExceptionHandler(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except KeyError:
                print("ERROR: Can't reach a server")
                pass

        return wrapper

    def link(self, server):
        self.linkedServers.setdefault(server.get_ip(), server).set_port(self)

    @dictExceptionHandler
    def unlink(self, server):
        self.linkedServers.pop(server.get_ip()).set_port(None)

    def get_data(self, data):
        self.buffer.append(data)

    @dictExceptionHandler
    def send_data(self):
        for data in self.buffer:
            self.linkedServers[data.ip].buffer.append(data)
        self.buffer.clear()


class Server:
    NEW_IP = 0

    @classmethod
    def set_ip(cls):
        try:
            return cls.NEW_IP
        finally:
            cls.NEW_IP += 1

    def __init__(self):
        self.ip = self.set_ip()
        self.buffer = list()
        self.port = None

    def set_port(self, port):  # где port=self экземляр из класса Router
        self.port = port

    def send_data(self, data):
        self.port.get_data(data)

    def get_data(self):
        try:
            return list(self.buffer)
        finally:
            self.buffer.clear()

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
####################################################################################################################
class Router:
    def __init__(self):
        self.buffer = []
        self.__connection_lst = []

    def link(self, server):
        if server not in self.__connection_lst:
            self.__connection_lst.append(server)
            self._connect_server(server, True)
            #print(f"Подключен сервер с IP {server.get_ip()}")
        else:
            pass#print(f"Cервер с IP {server.get_ip()} уже подключен!")

    def unlink(self, server):
        if server in self.__connection_lst:
            self.__connection_lst.remove(server)
            self._connect_server(server, False)
            #print(f"Отключен сервер с IP {server.get_ip()}")
        else:
            pass#print(f"Cервера с IP {server.get_ip()} нет в списке подключных!")

    def send_data(self):
        for data in self.buffer:
            for server in self.__connection_lst:
                if data.ip == server.ip:
                    server.buffer.append(data)
        self.buffer.clear()
        #print(f"Все пакеты отправлены")

    def reception_data(self, data):
        self.buffer.append(data)


    def _connect_server(self, server, connect):
        if connect:
            server.connect_router = self
        else:
            server.connect_router = None

    def get_buf(self):
        return self.buffer


class Server:
    __count_ip = 0

    def __new__(cls, *args, **kwargs):
        cls.__count_ip += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = self.__count_ip
        self.buffer = []
        self.connect_router = None

    def send_data(self, data):
        if self.connect_router:
            self.connect_router.reception_data(data)
            #print(f"С сервера (IP:{self.get_ip()}) успешно отправлено сообщение!")
        else:
            pass#print(f"Сервер(IP:{self.get_ip()}) не подключен к роутеру. Сообщенеи не отправлено!")


    def get_data(self):
        data_lst = self.buffer[:]
        self.buffer.clear()
        return data_lst

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
################################################################################################################################################
#Не нужно создавать копии данных при очистке буффера.Реальный буффер в роутере (маршрутизаторе и т.п.) будет ограничен
# по памяти. Если представить, что у вас огромное количество данных, то может возникнуть ситуация, когда
# невозможно создать копии всех данных и, соответственно, возникнут проблемы при передаче данных.Метод pop([index])
# списков позволяет "вернуть" объект по индексу, или последний элемент в списке, если index, не указан.В общем, ниже
# можно посмотреть как я реализовал очистку буффера сервера в методе get_data и очистку буффера роутера в
# методе send_data.
from random import randrange


class Data:
    def __init__(self, data, ip) -> None:
        self.data = data
        self.ip = ip


class Server:
    __max_server = 10
    __ip_address = list(range(1, __max_server))

    def __del__(self):
        Server.__ip_address.append(self.ip)

    def __init__(self):
        self.buffer = []
        self.ip = Server.__ip_address.pop(randrange(len(Server.__ip_address)))
        self.router = None

    def send_data(self, data: Data):
        if self.router:
            self.router.get_from_server(data)

    def get_data(self):
        return [self.buffer.pop() for _ in range(len(self.buffer))]

    def get_ip(self):
        return self.ip

    def link_to_router(self, router):
        self.router = router

    def unlink_router(self):
        self.router = None

    def get_data_from_router(self, data):
        self.buffer.append(data)


class Router:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Router.__instance = None

    def __init__(self) -> None:
        self.buffer = []  # data - передаваемые данные (строка);ip - IP-адрес назначения.
        self.servers = {}  # объекта класса Server

    def link(self, server: Server):  # {ip -server назначения : объект Server(buffer, ip, router)}
        self.servers.setdefault(server.get_ip(), server)  # setdefault(server.ip, server)
        server.link_to_router(self)

    def unlink(self, server: Server):
        s_ip = server.get_ip()
        if s_ip in self.servers:
            del self.servers[s_ip]
            server.unlink_router()

    def send_data(self):
        while len(self.buffer):
            data = self.buffer.pop()
            if data.ip in self.servers:
                self.servers[data.ip].get_data_from_router(data)  # server назначения

    # def send_data(self):
    #     for data in self.buffer:
    #         if data.ip in self.servers:
    #             self.servers[data.ip].get_data_from_router(data)
    #             # self.buffer.remove(data) #почему-то так не работает
    #     self.buffer.clear()

    def get_from_server(self, data: Data):
        self.buffer.append(data)
#####################################################################################################################
class Server:
    IP = 0

    def __new__(cls, *args, **kwargs):
        cls.IP += 1
        return super().__new__(cls)

    def __init__(self):
        self.buffer = list()
        self.ip = self.IP

    def send_data(self, data):
        if isinstance(data, Data):
            if self.get_ip() in Router.linked_servers:
                Router.buffer.append(data)

    def get_data(self):
        buffer_data, self.buffer = self.buffer, list()
        return buffer_data

    def get_ip(self):
        return self.ip


class Router:
    buffer = list()
    linked_servers = dict()

    def link(self, server):
        if isinstance(server, Server):
            server_ip = server.get_ip()
            self.linked_servers[server_ip] = server

    def unlink(self, server):
        if isinstance(server, Server):
            server_ip = server.get_ip()
            if server_ip in self.linked_servers:
                del self.linked_servers[server_ip]

    def send_data(self):
        for package in self.buffer:
            destination_server_ip = package.ip
            if destination_server_ip in self.linked_servers:
                destination_server = self.linked_servers[destination_server_ip]
                destination_server.buffer.append(package)
        self.buffer = list()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
#######################################################################################################################

#####################################################################################################################

#######################################################################################################################

################################################################################################################################################

################################################################################################################################################

################################################################################################################################################

################################################################################################################################################

################################################################################################################################################

################################################################################################################################################

################################################################################################################################################

################################################################################################################################################

########################################################################
