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
        self.init()

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL
        self.lst_human = []
        self.lst_computer = []
        self.is_human, self.is_computer, self._is_draw = False, False, False

    def show(self):
        for row in self.pole:
            print()
            for cell in row:
                print(cell.value, end=' ')
        print()

    def human_go(self):
        while True:
            try:
                key = tuple(map(int, input('Enter index: ').split()))
                if self.__check_index(key):
                    continue
                if self.__check_range(key):
                    continue
                if self.__getitem__(key) != self.FREE_CELL:
                    print("Error, Enter index yet")
                    continue
                self.__setitem__(key, self.HUMAN_X)
                break
            except ValueError:
                print('Введённые данные не являются координатами.')
                continue

    def computer_go(self):
        while True:
            try:
                key_row = randrange(len(self.pole))
                key_col = randrange(len(self.pole))
                key = key_row, key_col,
                if self.__getitem__(key) != self.FREE_CELL:
                    continue
                self.__setitem__(key, self.COMPUTER_O)
                break
            except ValueError:
                print('Введённые данные не являются координатами.')
                continue

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            # raise IndexError('некорректно указанные индексы')
            print('некорректно указанные индексы')
            return True
        # return False

    def __check_range(self, index):
        r, c = index
        if not 0 <= r < self.size or c not in range(self.size):
            # raise IndexError('некорректно указанные индексы')
            print('некорректно указанные диапазоны')
            return True
        # return False

    def __getitem__(self, item):
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        r, c = key
        self.pole[r][c].value = value

    @property
    def is_human_win(self):
        v = 0
        for i in range(len(self.pole)):  # сумма по строкам
            for j in range(len(self.pole)):
                if self.pole[i][j].value == self.HUMAN_X:
                    v += 1
            #return True if v == 3 else False
            self.lst_human.append(v)
        v = 0
        for i in range(len(self.pole)):  # сумма по столбцам
            x = -1
            for j in range(len(self.pole)):
                if self.pole[i][x + 1].value == self.HUMAN_X:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_human.append(v)
        v = 0
        for i in range(1):  # сумма по диагонали с (0,0) по (2,2)
            x = 0
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.HUMAN_X:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_human.append(v)
        v = 0
        for i in range(1):  # сумма по диагонали с (0,2) по (2,0)
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
            for j in range(len(self.pole)):
                if self.pole[i][j].value == self.COMPUTER_O:
                    v += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        v = 0
        for i in range(len(self.pole)):  # сумма по столбцам
            x = -1
            for j in range(len(self.pole)):
                if self.pole[i][x + 1].value == self.COMPUTER_O:
                    v += 1
                x += 1
            # return True if v == 3 else False
        self.lst_computer.append(v)
        v = 0
        for i in range(1):  # сумма по диагонали с (0,0) по (2,2)
            x = 0
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.COMPUTER_O:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)
        v = 0
        for i in range(1):  # сумма по диагонали с (0,2) по (2,0)
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
        if not self.is_human_win and self.is_computer_win == False and any(
                cell.value == self.FREE_CELL for row in self.pole for cell in row):
            return True  # игра не окончена
        else:
            return False


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

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe,
                                                                                 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[
           0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[
    1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

# game.init()
# game[0, 0] = TicTacToe.COMPUTER_O
# game[1, 0] = TicTacToe.COMPUTER_O
# game[2, 0] = TicTacToe.COMPUTER_O
# assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
