class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

        # setdefault вернёт пустой список, если ключа нет, а если есть, то его значение,
        # Метод dict.setdefault() вернет значение словаря dict, соответствующее ключу key.
        # Если указанный ключ key отсутствует, вставит его в словарь dict со значением default и вернет значение
        # default. Если значение по умолчанию default не установлено и ключ отсутствует, метод вставит ключ в словарь
        # со значением None, при этом никакое значение не возвращается.

        # ч/з key == pk :
        # self.dict_db.setdefault(record.pk, []).append(record)
        # print(self.dict_db.items())
        # dict_items([(1, [<__main__.Record object at 0x0000022469570250>]), (2, [<__main__.Re....

        # for item in self.dict_db.items():  # item: [<__main__.Record object at 0x000001C4133B0650>]
        #     for value in item[1]:  # value: <__main__.Record object at 0x000001C4133B0710>

    def read(self, pk):
        for row in self.dict_db.values():
            for i in row:  # row:  [<__main__.Record object at 0x00000156F4C60B10>]
                if i.pk == pk:  # i 7
                    return i  # <__main__.Record object at 0x000001FE18000610>

    # obj = [i for item in self.dict_db.values() for i in item if i.pk == pk]
    # return obj[0]

    # r = (x for row in self.dict_db.values() for x in row)
    # obj = tuple(filter(lambda x: x.pk == pk, r))
    # return obj[0] if len(obj) > 0 else None


class Record:
    record_count = 0

    def __init__(self, fio, descr, old):
        self.descr = descr
        self.old = old
        self.fio = fio
        self.pk = self.__count()

    @classmethod
    def __count(cls):
        cls.record_count += 1
        return cls.record_count

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    # hash(()) -> выч-ся на основе кортежа

    def __eq__(self, other):
        return hash(self) == hash(other)


# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33']

db = DataBase('bdDatabase')
for l in lst_in:
    args = list(map(str.strip, l.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"
