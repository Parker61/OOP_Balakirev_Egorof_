# Испытание магией_____крестики-нолики_____

# Техническое задание Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом.
# Объекты этого класса будут создаваться командой:game = TicTacToe()В каждом объекте этого класса должен быть
# публичный атрибут:pole - двумерный кортеж, размером 3x3.Каждый элемент кортежа pole является объектом класса Cell:
# cell = Cell()В объектах этого класса должно автоматически формироваться локальное свойство:value - текущее значение
# в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.Также с объектами класса Cell должна выполняться
# функция:bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.
# К каждой клетке игрового поля должен быть доступ через операторы:res = game[i, j] # получение значения из клетки с
# индексами i, jgame[i, j] = value # запись нового значения в клетку с индексами i, jЕсли индексы указаны неверно
# (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение командой:
# raise IndexError('некорректно указанные индексы')Чтобы в программе не оперировать величинами: 0 - свободная
# клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны быть три публичных атрибута (атрибуты класса):
# FREE_CELL = 0      # свободная клеткаHUMAN_X = 1        # крестик (игрок - человек)COMPUTER_O = 2     # нолик (игрок
# - компьютер)В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):
# init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
# show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
# human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
# computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).
# Также в классе TicTacToe должны быть следующие объекты-свойства (property):
# is_human_win - возвращает True, если победил человек, иначе - False;
# is_computer_win - возвращает True, если победил компьютер, иначе - False;
# is_draw - возвращает True, если ничья, иначе - False.Наконец, с объектами класса TicTacToe должна выполняться функция:
# bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в
# противном случае.Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе
########################################################################
from random import choice, randint, randrange


class Cell:
    def __init__(self):
        self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return not self.value
        # return self.value == 0  # True, если клетка свободна (value = 0)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.size = 3
        self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))
        self.lst_human = []
        self.lst_computer = []
        # self.is_human, self.is_computer, self._is_draw = False, False, False
        self.init()

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL
        self.lst_human = []
        self.lst_computer = []
        self.is_human, self.is_computer, self._is_draw = False, False, False
        # self.lst_human = []
        # self.lst_computer = []
        # self.is_computer_win
        # self.is_draw

    def show(self):
        for row in self.pole:
            print()
            for cell in row:
                print(cell.value, end=' ')
        print()

    def human_go(self):
        # key_row = int(input("Enter index: "))
        # key_col = int(input("Enter index: "))
        # key = key_row, key_col,
        key = tuple(map(int, input('Enter index: ').split()))
        while self.__getitem__(key) != self.FREE_CELL:  # while key != 0
            print("Error, Enter index yet")
            key = tuple(map(int, input('Enter index: ').split()))
        self.__setitem__(key, self.HUMAN_X)

    def computer_go(self):
        key_row = randrange(len(self.pole))
        key_col = randrange(len(self.pole))
        key = key = key_row, key_col,
        # key = choice(choice(self.pole)).value
        # while key == self.FREE_CELL:
        while self.__getitem__(key) != self.FREE_CELL:  # FREE_CELL = 0 - свободная клетка
            key_row = randrange(len(self.pole))
            key_col = randrange(len(self.pole))
            key = key = key_row, key_col,
            # key = choice(choice(self.pole)).value
            # if self.FREE_CELL else choice(choice(self.pole)
        self.__setitem__(key, self.COMPUTER_O)

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = index
        if not 0 <= r < self.size or c not in range(self.size):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        self.pole[r][c].value = value
        # self.is_human_win
        # self.is_computer_win
        # self.is_draw

    @property
    def is_human_win(self):
        v = 0
        for i in range(len(self.pole)):  # сумма по строкам
            # v = 0
            for j in range(len(self.pole)):
                if self.pole[i][j].value == self.HUMAN_X:
                    v += 1
            # return True if v == 3 else False
            self.lst_human.append(v)
        v = 0
        for i in range(len(self.pole)):  # сумма по столбцам
            x = -1
            # v = 0
            for j in range(len(self.pole)):
                if self.pole[i][x + 1].value == self.HUMAN_X:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_human.append(v)
        v = 0
        for i in range(1):  # сумма по диагонали с (0,0) по (2,2)
            # v = 0
            x = 0
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.HUMAN_X:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_human.append(v)
        v = 0
        for i in range(1):  # сумма по диагонали с (0,2) по (2,0)
            # v = 0
            x = 2
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.HUMAN_X:
                    v += 1
                x -= 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        if 3 in self.lst_human:
            self.is_human = True
            return self.is_human
        elif len(self.lst_human) == 0:
            self.is_human = False
            return self.is_human
        else:
            self.is_human = False
            return self.is_human

    @property
    def is_computer_win(self):
        v = 0
        for i in range(len(self.pole)):  # сумма по строкам
            # v = 0
            for j in range(len(self.pole)):
                if self.pole[i][j].value == self.COMPUTER_O:
                    v += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        v = 0
        for i in range(len(self.pole)):  # сумма по столбцам
            x = -1
            # v = 0
            for j in range(len(self.pole)):
                if self.pole[i][x + 1].value == self.COMPUTER_O:
                    v += 1
                x += 1
            # return True if v == 3 else False
        self.lst_computer.append(v)
        v = 0
        for i in range(1):  # сумма по диагонали с (0,0) по (2,2)
            # v = 0
            x = 0
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.COMPUTER_O:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)
        v = 0
        for i in range(1):  # сумма по диагонали с (0,2) по (2,0)
            # v = 0
            x = 2
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.COMPUTER_O:
                    v += 1
                x -= 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        if 3 in self.lst_computer:
            # print(self.lst_computer)
            self.is_computer = True
            return self.is_computer  # победа
        elif len(self.lst_computer) == 0:
            self.is_computer = False
            return self.is_computer
        else:
            self.is_computer = False
            return self.is_computer

    @property
    def is_draw(self):  # возвращает True, если ничья,  - иначе - False.
        if not self.__bool__() and not self.is_human_win and not self.is_computer_win:
            self._is_draw = True
            return self._is_draw  # ничья
        else:
            self._is_draw = False
            return self._is_draw

    def __bool__(self):
        # возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.
        if not self.is_human_win and self.is_computer_win == False and any(
                cell.value == self.FREE_CELL for row in self.pole for cell in row):
            return True  # игра не окончена
        else:
            return False


#
#######################################################################
from random import choice, randint, randrange


class Cell:
    def __init__(self):
        self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return self.value == 0  # True, если клетка свободна (value = 0)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.size = 3
        self.win = 0  # 0 - игра , 1 - победа человека, 2 - победа компьютера, 3 - ничья
        self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))

    def init(self):
        for i in range(self.size):
            for j in range(self.size):
                self.pole[i][j].value = 0
        self.win = 0  # 0 - игра

    def show(self):
        for row in self.pole:
            print(*map(lambda x: x.value, row))
        print('________________________________________________________________')

    def human_go(self):
        # if not self.__bool__():
        if not self:
            return
        while True:
            i, j = map(int, input('Enter index: ').split())
            if not (0 <= i < self.size) or not (0 <= j < self.size):
                continue
            # self.pole[y][x].value можно заменить на просто self[y, x], для этого и  __setitem__ создавали)
            if self[i, j] == self.FREE_CELL:  # отправляет в getitem
                self[i, j] = self.HUMAN_X  # отправляет в setitem
                break

    def computer_go(self):
        if not self:
            return
        while True:
            i = randint(0, self.size - 1)
            j = randint(0, self.size - 1)
            if self[i, j] != self.FREE_CELL:
                continue
            self[i, j] = self.COMPUTER_O
            break

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = index
        if not 0 <= r < self.size or c not in range(self.size):
            raise IndexError('некорректно указанные индексы')

    def __update_win_status(self):
        for row in self.pole:
            if all(i.value == self.HUMAN_X for i in row):  # проверка на выигрыш по строкам человека
                self.win = 1
                return
            if all(i.value == self.COMPUTER_O for i in row):
                self.win = 2
                return
        for i in range(self.size):  # проверка на выигрыш по столбцам человека
            if all(col.value == self.HUMAN_X for col in (row[i] for row in self.pole)):
                self.win = 1
                return
            if all(col.value == self.COMPUTER_O for col in (row[i] for row in self.pole)):
                self.win = 2
                return
        # проверка на выигрыш по диагоналям человека
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self.size)) \
                or all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(self.size)):
            self.win = 1
            return
        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self.size)) \
                or all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(self.size)):
            self.win = 2
            return
        # проверка на ничью
        if all(col.value != self.FREE_CELL for row in self.pole for col in row):
            self.win = 3
            return

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        self.pole[r][c].value = value
        self.__update_win_status()  # пересчёт статуса победителя

    @property
    def is_human_win(self):
        return self.win == 1

    @property
    def is_computer_win(self):
        return self.win == 2

    @property
    def is_draw(self):  # возвращает True, если ничья,  - иначе - False.
        return self.win == 3

    def __bool__(self):
        return self.win == 0 and self.win not in (1, 2, 3)


########################################################################
class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        '''Инициализация'''
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.free_cells = 9
        self.winner = None
        self.diagonals = [[self.pole[i][i] for i in range(3)], [self.pole[-i - 1][i] for i in range(-3, 0)]]
        # Список self.diagonals содержит все возможные диагонали на игровом поле, включая главную диагональ и все
        # побочные диагонали. Для каждой диагонали список элементов заполняется по порядку, начиная с верхнего левого
        # угла игрового поля и заканчивая нижним правым углом.
        for diag in self.diagonals:
            for cell in diag:
                cell._priority += 2

    def __getitem__(self, coords):
        '''Геттер значения клетки по координатам'''
        if self._valid_coords(*coords):
            return self.pole[coords[0]][coords[1]].value
        raise IndexError('некорректно указанные индексы')

    def __setitem__(self, coords, value):
        '''Сеттер значения клетки по координатам'''
        if not self._valid_coords(*coords):
            raise IndexError('некорректно указанные индексы')
        if value in (0, 1, 2):
            self.pole[coords[0]][coords[1]].value = value
        self.__bool__()

    def __bool__(self):
        '''Проверка окончена игра или нет'''
        for row in self.pole:  # перебор по строкам
            if not any(row) and len(set(row)) == 1:
                # any(row) xотя бы один элемент в последовательности True,т е. хотя бы один self.value = 0,т.к return
                # not self.value
                # not any(row) вернет False обращаясь к def __bool__(self):/ return not self.value когда self.value = 0,
                # если все элементы row являются ложными. это означает, что если все элементы
                # в ряду пустые (отсутствуют), то возвращается False, а если в ряду есть хотя бы один непустой элемент
                # и все элементы имеют одинаковое значение, то возвращается True. len(set(row)) возвращает количество
                # уникальных значений в строке. Если это значение равно 1, то все элементы в этой строке имеют одно и
                # то же значение, и выражение вернет True. len(set(row)) == 1 проверяет, что длина множества уникальных
                # элементов в списке row равна 1, то есть все элементы списка равны между собой. Если оба условия
                # истинны, то значит в данной строке все ячейки пустые и равны между собой, что соответствует ситуации
                # "ничья" в игре. Таким образом, если все клетки в первом столбце равны нулю, а в других столбцах есть
                # свободные клетки, то игра продолжится, и не будет закончена как ничья до тех пор, пока не будут
                # заполнены все клетки на игровом поле.
                self.winner = row[0].value  # определяется победитель
                return False  # был найден победитель, игра заканчивается и дальнейшие проверки уже не нужны.
        for col in zip(*self.pole):  # транспорнирование матрицы, перебор по столбцам
            # col будет содержать все элементы из одного столбца игрового поля.
            if not any(col) and len(set(col)) == 1:
                self.winner = col[0].value
                return False
        for diag in self.diagonals:
            # Каждый элемент списка diag представляет собой объект Cell
            if not any(diag) and len(set(diag)) == 1:
                self.winner = diag[0].value
                return False
        if self.free_cells == 0:
            self.winner = 0
            return False
        return True  # продолжение игры

    @property
    def is_human_win(self):
        return self.winner == self.HUMAN_X

    @property
    def is_computer_win(self):
        return self.winner == self.COMPUTER_O

    @property
    def is_draw(self):
        return self.winner == 0

    @classmethod
    def _valid_coords(cls, y, x):
        '''Проверка координат'''
        return type(y) == type(x) == int and 0 <= y < 3 and 0 <= x < 3

    def init(self):
        self.__init__()

    def human_go(self):
        '''Ход человека'''
        while True:
            print('Введите координаты свободной клетки через пробел:')
            coords = input()
            if len(coords.split()) != 2:
                print('Было введено неверное количество координат.')
                continue
            try:
                y, x = map(int, coords.split())
                if not self._valid_coords(y, x):
                    print('Введённые координаты вне диапазона поля.')
                    continue
            except ValueError:
                print('Введённые данные не являются координатами.')
                continue
            # if self.pole[y][x].value not in [1, 2]:
            if self.pole[y][x]:  # обращение к клетке а она обращается к __bool__(self): return not self.value  ->
                # self.value = 0 -> not False -> True
                # проверять, существует ли объект Cell для ячейки поля (y, x), но не будет проверять её значение.
                self.pole[y][x].value = self.HUMAN_X
                self.free_cells -= 1
                self._compute_priority(y, x)
                break
            else:
                print('Выбранная клетка занята.')
                continue

    def computer_go(self):
        '''Ход компьютера'''
        # собирает все клетки которые не заняты, if cell проверка не занята ли клетка через __bool__
        free_cells = [(y, x) for y, row in enumerate(self.pole) for x, cell in enumerate(row) if cell]
        y, x = max(free_cells, key=lambda c: self.pole[c[0]][c[1]]._priority)
        # координаты свободной ячейки с максимальным значением приоритета.
        if y == x == 1:  # Реакция на среднюю клетку
            for cell in (self.pole[0][1], self.pole[1][0], self.pole[1][2], self.pole[2][1]):
                cell._priority += 2
        self.free_cells -= 1
        self.pole[y][x].value = self.COMPUTER_O

    def _compute_priority(self, y, x):
        '''Просчёт хода компьютера'''
        # Реакция на ход противника
        # Метод self._compute_priority(y, x) используется для пересчёта приоритетов доступных ходов для игрока. Он
        # вызывается после того, как игрок сделал очередной ход в свободную ячейку поля.Для каждой свободной ячейки
        # поля метод вычисляет её приоритет, основываясь на том, сколько потенциальных выигрышных комбинаций может быть
        # построено, если игрок сделает ход в эту ячейку. Чем больше потенциальных выигрышных комбинаций можно
        # построить, тем выше приоритет у этой ячейки.Пересчёт приоритетов доступных ходов позволяет игроку выбирать
        # более "выгодные" ходы на каждом шаге игры и повышать свои шансы на победу.Кроме того, метод
        # self._compute_priority(y, x) также запускается один раз в начале игры, чтобы вычислить начальные приоритеты
        # для всех ячеек поля.
        for cell in self.pole[y]:
            cell._priority -= 1
        for cell in list(zip(*self.pole))[x]:
            cell._priority -= 1
        if y == x:
            for cell in self.diagonals[0]:
                cell._priority -= 1
        if y + x == 2:
            for cell in self.diagonals[1]:
                cell._priority -= 1
        # Корректировка опасности
        for row in self.pole + [list(lst) for lst in zip(*self.pole)] + self.diagonals:
            counter = [0, 0, 0]
            for cell in row:
                counter[cell.value] += 1
            if counter[1] == 2:
                for cell in row:
                    cell._priority = 5
            if counter[2] == 2:
                for cell in row:
                    cell._priority = 6

    def show(self):
        '''Отрисовка поля'''
        for row in self.pole:
            for cell in row:
                print(cell, end=' ')
            print()
        print('* ' * 10)


class Cell:
    def __init__(self):  # содержит значение клетки и приоритет.
        self.value = 0
        self._priority = 2
        # используется для определения приоритета клетки при выполнении каких-либо операций.

    def __bool__(self):
        return not self.value

    def __str__(self):
        if self.value == 1:
            return 'X'
        if self.value == 2:
            return '0'
        return '-'

    # __eq__ при проверке того, занята ли определенная клетка на игровом поле или нет
    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        # Хеш-код нужен, чтобы быстро и эффективно сравнивать объекты между собой быстро сравнить их между собой и
        # выполнить необходимые действия (например, проверить, занята ли определенная клетка на игровом поле или нет).
        return hash(self.value)


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()
    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
    step_game += 1

print("Stop____________________________________")
game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
    # elif game.is_draw:
else:
    print("Ничья.")

########################################################################
from random import choice


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self._n = 3
        self.init()

    @property
    def is_human_win(self):
        return self.__is_human_win

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @property
    def is_draw(self):
        return self.__is_draw

    def init(self):
        self.__is_human_win, self.__is_computer_win, self.__is_draw = False, False, False
        self.pole = tuple(tuple(Cell() for j in range(self._n)) for i in range(self._n))
        self.total_lst = []

    def show(self):
        for i in range(self._n):
            for j in range(self._n):
                if self.pole[i][j].value == self.FREE_CELL: print(f'{i}_{j}', end=' ')
                if self.pole[i][j].value == self.HUMAN_X: print('_x_', end=' ')
                if self.pole[i][j].value == self.COMPUTER_O: print('_0_', end=' ')
            print()
            print()

    def human_go(self):
        key = tuple(map(int, input('Ваш ход- ').split()))
        self.__setitem__(key, self.HUMAN_X)

    def computer_go(self):
        key = choice(self.total_lst)
        self.__setitem__(key, self.COMPUTER_O)

    def __bool__(self):
        '''возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае'''
        return not any((self.is_human_win, self.is_computer_win, self.is_draw))

    def check_win(self):
        '''Проверка таблицы поля на выйгрыш или ничью'''
        self.total_lst = [(i, j) for j in range(self._n) for i in range(self._n) if
                          self.pole[i][j].value == self.FREE_CELL]
        humax = tuple(True if self.pole[i][i].value == self.HUMAN_X else False for i in range(self._n) if
                      self.pole[i][i].value != self.FREE_CELL)
        if len(humax) == 3:
            if self.check_vs(humax): return False

        humax = tuple(True if self.pole[i][self._n - 1 - i].value == self.HUMAN_X else False for i in range(self._n) if
                      self.pole[i][self._n - 1 - i].value != self.FREE_CELL)
        if len(humax) == 3:
            if self.check_vs(humax): return False
        for i in range(self._n):
            humax = tuple(True if value == self.HUMAN_X else False for value in self[i, :] if value != self.FREE_CELL)
            if len(humax) == 3:
                if self.check_vs(humax): return False
        for j in range(self._n):
            humax = tuple(True if value == self.HUMAN_X else False for value in self[:, j] if value != self.FREE_CELL)
            if len(humax) == 3:
                if self.check_vs(humax): return False
        if len(self.total_lst) == 0:
            self.__is_human_win, self.__is_computer_win, self.__is_draw = False, False, True
            return False
        return True

    def check_vs(self, humax):
        '''вспомогательная функция для check_win'''
        if all(humax):
            self.__is_human_win, self.__is_computer_win, self.__is_draw = True, False, False
            return True
        if sum(humax) == 0:
            self.__is_human_win, self.__is_computer_win, self.__is_draw = False, True, False
            return True
        return False

    def check_index(self, indx):
        if not isinstance(indx, (slice, tuple)) or not all(0 <= n <= 2 for n in indx if type(n) == int):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.check_index(item)
        if type(item[1]) == slice:
            return tuple(n.value for n in self.pole[item[0]][item[1]])
        if type(item[0]) == slice:
            lst = [self.pole[i][item[1]] for i in range(3)][item[0]]
            return tuple(n.value for n in lst)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.check_index(key)
        cell = self.pole[key[0]][key[1]]
        if not cell:
            raise ValueError('клетка уже занята')
        if self:
            cell.value = value
            self.check_win()


class Cell:
    def __init__(self, value=0):
        self.value = value  # value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

    def __bool__(self):  # возвращает True, если клетка свободна (value = 0) и False - в противном случае.
        return not self.value


#######################################################################
from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not bool(self.value)

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.value == other.value
        return self.value == other

    def __str__(self):
        self.str = {0: u'\u2b1c', 1: u'\u274c', 2: u'\u2b55'}
        return self.str[self.value]


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    @staticmethod
    def check_index(indexes):
        for index in indexes:
            if type(index) != int or index not in range(0, 3):
                raise IndexError('Некорректно указаны индексы')

    def __getitem__(self, item):
        self.check_index(item)
        i, j = item
        return self.pole[i][j].value

    def __setitem__(self, item, val):
        self.check_index(item)
        i, j = item
        self.pole[i][j].value = val
        self.check_win()

    def __init__(self):
        self.pole = [[Cell() for i in range(3)] for j in range(3)]
        self._is_human_win = False
        self._is_computer_win = False
        self._is_draw = False

    def init(self):
        self.__init__()

    def show(self):
        for row in self.pole:
            for col in row:
                print(col, end=' ')
            print()
        print()

    def human_go(self):
        while True:
            i, j = map(int, input("Введите 2 числа через пробел ").split())
            if not self[i, j]:
                item = i, j
                self.__setitem__(item, self.HUMAN_X)
                break

    def computer_go(self):
        while True:
            i = randint(0, 2)
            j = randint(0, 2)
            if not self[i, j]:
                self.__setitem__((i, j), self.COMPUTER_O)
                break

    @property
    def is_human_win(self):
        self.check_win()
        return self._is_human_win

    @is_human_win.setter
    def is_human_win(self, val):
        self._is_human_win = val

    @property
    def is_computer_win(self):
        self.check_win()
        return self._is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, val):
        self._is_computer_win = val

    @property
    def is_draw(self):
        self.check_win()
        return self._is_draw

    @is_draw.setter
    def is_draw(self, val):
        self._is_draw = val

    def __bool__(self):
        for i in self.pole:
            for j in i:
                if j.value == 0 and not self.check_win():
                    return True
        return False

    def check_win(self):
        d = {1: "self.is_human_win=True", 2: "self.is_computer_win=True", 0: "self.is_draw=True"}
        for i in range(3):
            # Функция exec() поддерживает динамическое выполнение кода Python и принимает большие блоки кода
            if self[i, 0] == self[i, 1] == self[i, 2] and self[i, 0] != 0:
                exec(d[self[i, 0]])
                return
        for i in range(3):
            if self[0, i] == self[1, i] == self[2, i] and self[0, i] != 0:
                exec(d[self[0, i]])
                return
        if self[0, 0] == self[1, 1] == self[2, 2] and self[0, 0] != 0:
            exec(d[self[0, 0]])
            return
        elif self[0, 2] == self[1, 1] == self[2, 0] and self[0, 2] != 0:
            exec(d[self[0, 2]])
            return
        for i in self.pole:
            if 0 in i:
                return
        exec(d[0])


########################################################################
from random import randint


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self, space='_', human='X', computer='O'):
        self.d = {self.FREE_CELL: space,
                  self.HUMAN_X: human,
                  self.COMPUTER_O: computer}

    def find_strike(self, who):  # 1 - human, 2 - computer
        rows = any(all(self[row, i].value == who for i in [0, 1, 2]) for row in [0, 1, 2])
        cols = any(all(self[i, col].value == who for i in [0, 1, 2]) for col in [0, 1, 2])
        diag1 = all(self[i, i].value == who for i in [0, 1, 2])
        diag2 = all(self[2 - i, i].value == who for i in [0, 1, 2])

        return any([rows, cols, diag1, diag2])

    @property
    def is_human_win(self):
        return self.find_strike(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.find_strike(self.COMPUTER_O)

    @property
    def is_nobody_win(self):
        return not (self.is_human_win or self.is_computer_win)

    @property
    def any_free_space(self):
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                if self[i, j].is_free:
                    return True
        return False

    @property
    def is_draw(self):
        return not self.any_free_space and self.is_nobody_win

    def __bool__(self):
        return self.any_free_space and self.is_nobody_win

    def human_go(self):  # c защитой от дурака и различными комментариями
        message = 'Пожалуйста введите координаты: '
        while True:
            try:
                x, y = map(int, input(message).split())
                self[x, y] = self.HUMAN_X
                break
            except Warning:
                print('Клетка уже занята!')
            except ValueError:
                print('Координаты - два целых числа!')
            except IndexError:
                print('Клетки с данными координатами не существует!')
            message = 'Повторите попытку: '

    def computer_go(self):  # ИИ в разработке. пока рандом
        x = randint(0, 2)
        y = randint(0, 2)
        while not self[x, y].is_free:
            x = randint(0, 2)
            y = randint(0, 2)
        self[x, y] = self.COMPUTER_O

    def show(self):  # console
        for row in self.pole:
            print(' '.join(self.d[row[col].value] for col in [0, 1, 2]))

    def __getitem__(self, key):
        return self.pole[key[0]][key[1]]

    def __setitem__(self, item, value):
        cell = self.pole[item[0]][item[1]]
        if cell:
            cell.value = value
        else:
            raise Warning('клетка уже занята')

    def clear(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def init(self):
        self.clear()
        self.step_game = 0

    def start_console_game(self):
        self.init()

        while self:
            if self.step_game % 2 == 0:
                self.human_go()
            else:
                print('Ход компьютера: ')
                self.computer_go()
            self.show()
            self.step_game += 1

        if self.is_human_win:
            print("Поздравляем! Вы победили!")
        elif self.is_computer_win:
            print("Все получится, со временем")
        else:
            print("Ничья.")


class Cell:
    def __init__(self):
        self.value = 0

    @property
    def is_free(self):
        return not self.value

    def __bool__(self):
        return self.is_free


#########################################################################
import random as rnd


class Discriptor:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    is_human_win = Discriptor()
    is_draw = Discriptor()
    is_computer_win = Discriptor()

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False
        self.FREE_CELL = 9

    def __getitem__(self, key):
        i, j = self.check(key)
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i, j = self.check(key)
        self.pole[i][j].value = value
        self.who_won()

    def __bool__(self):
        return not any([self.is_human_win, self.is_computer_win, self.is_draw])

    def init(self):
        self.__init__()

    def check(self, key):
        if not all(map(lambda x: isinstance(x, int) and x in (0, 1, 2), key)):
            raise IndexError('некорректно указанные индексы')
        return key

    def show(self):
        marks = {0: ' ', 1: 'X', 2: 'O'}
        for i, row in enumerate(self.pole):
            print(' | '.join(marks[elem.value] for elem in row))
            print(('-' * 12) * bool(i - 2))

    def human_go(self):
        answer = list(map(int, input('Введите клетку: номер строки, номер столбца: ').split()))
        self[answer] = self.HUMAN_X  # in __setitem__
        self.FREE_CELL -= 1

    def computer_go(self):
        while True:
            i = rnd.randint(0, 2)
            j = rnd.randint(0, 2)
            if self.pole[i][j]:
                self[(i, j)] = self.COMPUTER_O
                self.FREE_CELL -= 1
                break

    def who_won(self):
        if self.FREE_CELL == self.__class__.FREE_CELL:
            self.is_draw = True
            return
        for row in [*self.pole, *zip(*self.pole)]:
            check = set(map(lambda x: x.value, row))
            if not self.func(check):
                break
        check_main = set()
        check_off = set()
        for i in range(3):
            check_main.add(self.pole[i][i].value)
            check_off.add(self.pole[i][2 - i].value)
        self.func(check_main)
        self.func(check_off)

    def func(self, check):
        if check == {1}:
            self.is_human_win = True
        elif check == {2}:
            self.is_computer_win = True
        else:
            return True


class Cell:

    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not bool(self.value)


########################################################################
# моё решение переработанное
from random import randint, randrange


class Cell:
    def __init__(self):
        self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

    def __bool__(self):
        return not self.value
        # return self.value == 0  # True, если клетка свободна (value = 0)

    def __str__(self):
        self.str = {0: u'\u2b1c', 1: u'\u274c', 2: u'\u2b55'}
        return self.str[self.value]
        # return f'{self.value}'  # return str(self.value)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.size = 3
        self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))
        self.CELLS = 9
        self.init()

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL  # self.__class__.FREE_CELL
        self.is_human, self.is_computer, self.__is_draw = False, False, False

    def show(self):
        for row in self.pole:
            for i in row:
                if i.value == self.FREE_CELL:
                    print("⬜", end=' ')
                else:
                    if i.value == self.HUMAN_X:
                        print('❌', end=' ')
                    else:
                        print('⭕', end=' ')
            print()
            # print(*['⬜' if i.value == self.FREE_CELL else '❌' if i.value == self.HUMAN_X else '⭕' for i in row])
        print()

    def human_go(self):
        while True:
            try:
                key = tuple(map(int, input('Enter index: ').split()))
                # if self.__check_index(key):
                #     continue
                # if self.__check_range(key):
                #     continue
                if self.__getitem__(key) != self.FREE_CELL:
                    # if self[key] != self.FREE_CELL: # in __getitem__
                    print("Error, Enter index yet")
                    continue
                # self.__setitem__(key, self.HUMAN_X)
                self[key] = self.HUMAN_X  # in __setitem__
                self.CELLS -= 1
                break
            except ValueError:
                print('Введённые данные не являются координатами.')
            except IndexError:
                print('некорректно указанные индексы')

    def computer_go(self):
        while True:
            key = (randrange(len(self.pole)), randint(0, len(self.pole) - 1))
            if self.__getitem__(key) != self.FREE_CELL:
                continue
            self.__setitem__(key, self.COMPUTER_O)
            self.CELLS -= 1
            break

    # def computer_go(self):
    #     free_cells = [i for row in self.pole for i in row if i.value == self.FREE_CELL]
    #     choice(free_cells).value = self.COMPUTER_O

    def __getitem__(self, item):
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        r, c = key
        self.pole[r][c].value = value
        self.__check_won_()  # проверка на победителя

    def __check_won_(self):
        if self.CELLS == self.__class__.FREE_CELL:
            self.__is_draw = True
            return
        for row in [*self.pole]:  # по строкам
            check = set(map(lambda x: x.value, row))
            if not self.__check_func(check):
                break
        for row in [*zip(*self.pole)]:  # по столбцам
            check = set(map(lambda x: x.value, row))
            if self.__check_func(check):
                return
        check_main_diag = set()
        check_second_diag = set()
        for i in range(self.size):
            check_main_diag.add(self.pole[i][i].value)  # проверка главной диагонали
            check_second_diag.add(self.pole[i][2 - i].value)  # проверка обратной диагонали
        self.__check_func(check_main_diag)
        self.__check_func(check_second_diag)

    def __check_func(self, check):
        if check == {1}:
            self.is_human = True
        elif check == {2}:
            self.is_computer = True
        else:
            return False

    @property
    def is_human_win(self):
        return self.is_human

    @property
    def is_computer_win(self):
        return self.is_computer

    @property
    def is_draw(self):  # возвращает True, если ничья,  - иначе - False.
        return self.__is_draw

    def __bool__(self):  # True, если игра не окончена (никто не победил и есть свободные клетки
        return not any([self.is_computer_win, self.is_human_win, self.is_draw])  # return False if game over


########################################################################
from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    def init(self):
        self.__init__()

    def __getitem__(self, item):
        x, o = self.__validate_indx(item)
        return self.pole[x][o].value

    def __setitem__(self, key, value):
        x, o = self.__validate_indx(key)
        hum_comp = self.human_go if value == self.HUMAN_X else self.computer_go
        if self.pole[x][o]:
            self.pole[x][o].value = value
        else:
            print('Клетка уже занята')
            hum_comp()

    def human_go(self):
        x, y = map(int, input('Введи два числа через пробел: ').split())
        self[x, y] = self.HUMAN_X

    def computer_go(self):
        x, y = randint(0, 2), randint(0, 2)
        self[x, y] = self.COMPUTER_O

    def __get_winner(self, flag):
        check = [[flag == x[i].value for i in range(3)] for x in self.pole]

        if flag in (self.HUMAN_X, self.COMPUTER_O):
            return any(
                (
                    any([all(i) for i in check]),
                    any([all([i[x] for i in check]) for x in range(3)]),
                    all([check[i][i] for i in range(3)]),
                    all([check[i][-i - 1] for i in range(3)]),
                ),
            )
        return all([flag == x for i in check for x in i])

    @property
    def is_human_win(self):
        return self.__get_winner(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.__get_winner(self.COMPUTER_O)

    @property
    def is_draw(self):
        return self.__get_winner(self.FREE_CELL)

    def __bool__(self):
        return not any((self.is_human_win, self.is_computer_win, self.is_draw))

    def show(self):
        for i in self.pole:
            print(*['⬜' if bool(x) else '❌' if x.value == 1 else '⭕' for x in i])
        print()

    @staticmethod
    def __validate_indx(item):
        if not all(type(x) is int and 0 <= x < 3 or type(x) is slice for x in item):
            raise IndexError('некорректно указанные индексы')
        return item[0], item[1]


########################################################################
from random import choice


class Cell:
    def __init__(self, value=0):
        self.value = value

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.init()

    def init(self):
        self.pole = tuple(tuple(Cell(self.FREE_CELL) for _ in '>>>') for _ in '>>>')

    def __freecells(self):
        return [(r, c) for r in range(3) for c in range(3) if self.pole[r][c].value == self.FREE_CELL]

    def __checked(self, key):
        if not (0 <= key[0] < 3 and 0 <= key[1] < 3):
            raise IndexError('некорректно указанные индексы')
        return key

    def __getitem__(self, key):
        r, c = self.__checked(key)
        return self.pole[r][c].value

    def __setitem__(self, key, v):
        r, c = self.__checked(key)
        self.pole[r][c].value = v

    def show(self):
        print(*(' '.join('+XO'[j.value] for j in i) for i in self.pole), sep='\n')

    def human_go(self):
        while True:
            try:
                y, x = map(int, input('Ваш ход y, x: ').split(', '))
                if 1 <= y <= 3 and 1 <= x <= 3:
                    if self.pole[y - 1][x - 1].value != self.FREE_CELL:
                        print('Эта клетка уже занята')
                        continue
                    self.pole[y - 1][x - 1].value = self.HUMAN_X
                    break
            except:
                pass
            print('Ведите 2 числа от 1 до 3 через запятую, например: 1, 2')

    def computer_go(self):
        r, c = choice(self.__freecells())
        self.pole[r][c].value = self.COMPUTER_O

    def __checkwin(self, p):
        if any(all(self.pole[i][j].value == p for j in range(3)) or \
               all(self.pole[j][i].value == p for j in range(3)) for i in range(3)):
            return True
        return any(all(self.pole[i][j].value == p for i, j in k) for k in \
                   (((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))))

    @property
    def is_human_win(self):
        return self.__checkwin(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.__checkwin(self.COMPUTER_O)

    @property
    def is_draw(self):
        return not self.__freecells() and not self.is_human_win() and not self.is_computer_win()

    def __bool__(self):
        return bool(self.__freecells())

    ################################
    #ещё  моё решение
    from random import randint, randrange, choice

    class Cell:
        def __init__(self):
            self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

        def __bool__(self):
            return not self.value

        def __str__(self):
            self.str = {0: u'\u2b1c', 1: u'\u274c', 2: u'\u2b55'}
            return self.str[self.value]

    class TicTacToe:
        FREE_CELL = 0  # свободная клетка
        HUMAN_X = 1  # крестик (игрок - человек)
        COMPUTER_O = 2  # нолик (игрок - компьютер)

        def __init__(self):
            self.size = 3
            self.pole = tuple(tuple(Cell() for _ in range(self.size)) for _ in range(self.size))
            self.init()

        def init(self):
            for row in self.pole:
                for cell in row:
                    cell.value = self.FREE_CELL

        def show(self):
            for row in self.pole:
                for i in row:
                    if i.value == self.FREE_CELL:
                        print("⬜", end=' ')
                    else:
                        if i.value == self.HUMAN_X:
                            print('❌', end=' ')
                        else:
                            print('⭕', end=' ')
                print()
                # print(*['⬜' if i.value == self.FREE_CELL else '❌' if i.value == self.HUMAN_X else '⭕' for i in row])
            print()

        def human_go(self):
            while True:
                try:
                    key = tuple(map(int, input('Enter index: ').split()))
                    if self.__getitem__(key) != self.FREE_CELL:
                        print("Error, Enter index yet")
                        continue
                    self[key] = self.HUMAN_X  # in __setitem__
                    break
                except ValueError:
                    print('Введённые данные не являются координатами.')
                except IndexError:
                    print('некорректно указанные индексы')

        def computer_go(self):
            free_cells = [i for row in self.pole for i in row if i.value == self.FREE_CELL]
            choice(free_cells).value = self.COMPUTER_O

        def __getitem__(self, item):
            r, c = item
            return self.pole[r][c].value

        def __setitem__(self, key, value):
            r, c = key
            self.pole[r][c].value = value

        def __check_func(self, who):  # 1 - human, 2 - computer
            rows = any(all(self[row, i] == who for i in [0, 1, 2]) for row in [0, 1, 2])
            cols = any(all(self[i, col] == who for i in [0, 1, 2]) for col in [0, 1, 2])
            diag1 = all(self[i, i] == who for i in [0, 1, 2])
            diag2 = all(self[2 - i, i] == who for i in [0, 1, 2])
            return any([rows, cols, diag1, diag2])

        @property
        def is_human_win(self):
            return self.__check_func(self.HUMAN_X)

        @property
        def is_computer_win(self):
            return self.__check_func(self.COMPUTER_O)

        @property
        def is_nobody_win(self):
            return not (self.is_human_win or self.is_computer_win)

        @property
        def any_free_space(self):
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if not self[i, j]:  # call __getitem__ and after call to __bool__ from class Cell()
                        # self.pole[i][j].value
                        return True  # есть ещё свободные клетки self[i, j] = self.value = 0
            return False

        @property
        def is_draw(self):
            return not self.any_free_space and self.is_nobody_win

        def __bool__(self):
            return self.any_free_space and self.is_nobody_win