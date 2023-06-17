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

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL
        self.lst_human = []
        self.lst_computer = []
        self.is_human_win
        self.is_computer_win
        self.is_draw

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
        self.is_human_win
        self.is_computer_win
        self.is_draw

    @property
    def is_human_win(self):
        for i in range(len(self.pole)):  # сумма по строкам
            v = 0
            for j in range(len(self.pole)):
                if self.pole[i][j].value == self.HUMAN_X:
                    v += 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        for i in range(len(self.pole)):  # сумма по столбцам
            x = -1
            v = 0
            for j in range(len(self.pole)):
                if self.pole[i][x + 1].value == self.HUMAN_X:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        for i in range(1):  # сумма по диагонали с (0,0) по (2,2)
            v = 0
            x = 0
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.HUMAN_X:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        for i in range(1):  # сумма по диагонали с (0,2) по (2,0)
            v = 0
            x = 2
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.HUMAN_X:
                    v += 1
                x -= 1
            # return True if v == 3 else False
            self.lst_human.append(v)

        if 3 in self.lst_human:
            # print(self.lst_human)
            return True
        elif len(self.lst_human) == 0:
            return False
        else:
            return False

    @property
    def is_computer_win(self):
        for i in range(len(self.pole)):  # сумма по строкам
            v = 0
            for j in range(len(self.pole)):
                if self.pole[i][j].value == self.COMPUTER_O:
                    v += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        for i in range(len(self.pole)):  # сумма по столбцам
            x = -1
            v = 0
            for j in range(len(self.pole)):
                if self.pole[i][x + 1].value == self.COMPUTER_O:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        for i in range(1):  # сумма по диагонали с (0,0) по (2,2)
            v = 0
            x = 0
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.COMPUTER_O:
                    v += 1
                x += 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        for i in range(1):  # сумма по диагонали с (0,2) по (2,0)
            v = 0
            x = 2
            for j in range(len(self.pole)):
                if self.pole[j][x].value == self.COMPUTER_O:
                    v += 1
                x -= 1
            # return True if v == 3 else False
            self.lst_computer.append(v)

        if 3 in self.lst_computer:
            # print(self.lst_computer)
            return True  # победа
        elif len(self.lst_computer) == 0:
            return False
        else:
            return False

    @property
    def is_draw(self):  # возвращает True, если ничья,  - иначе - False.
        if not self.__bool__() and not self.is_human_win and not self.is_computer_win:
            return True  # ничья
        else:
            return False

    def __bool__(self):
        # возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.
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

print("Stop________________")
game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
elif game.is_draw:
    # else:
    print("Ничья.")

# не писать):
# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
# #     step_game += 1
# #
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")
# Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было
#     бы сыграть в "Крестики-нолики" между человеком и компьютером.
#     P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.
