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
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, " \
                                                                                      "is_computer_win, is_draw. Возможно не пересчитывается " \
                                                                                      "статус игры в момент присвоения новых значения по" \
                                                                                      "индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

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
