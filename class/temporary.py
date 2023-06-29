class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.free_cells = 9
        self.size = 3
        self.pole = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.winner = None
        self.diagonals = [[self.pole[i][i] for i in range(self.size)], [self.pole[i - 1][i] for i in range(self.size)]]
        for diag in self.diagonals:
            for cell in diag:
                cell.priority += 2

    def __getitem__(self, coords):
        self._valid_coords(coords)
        return self.pole[coords[0]][coords[1]].value

    def __setitem__(self, coords, value):
        self._valid_coords(coords)
        if value in (1, 2):  # if value in (0, 1, 2):
            return self.pole[coords[0]][coords[1]].value
        self.__bool__()

    def __bool__(self):
        for row in self.pole:
            if not any(row) and len(set(row)) == 1:
                self.winner = row[0].value
                return False

        for row in zip(self.pole):
            if not any(row) and len(set(row)) == 1:
                self.winner = row[0].value
                return False

        for diag in self.diagonals:
            if not any(diag) and len(set(diag)) == 1:
                self.winner = diag[0].value
                return False

        if self.free_cells == 0:
            self.winner = 0
            return False

        return True

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
        if not (type(y) == type(x) == int and 0 <= x < 3 and 0 <= y < 3):
            raise IndexError('некорректно указанные индексы')

    def init(self):
        self.__init__()

    def human_go(self):
        while True:
            print('Введите координаты свободной клетки через пробел:')
            coords = input()
            if len(coords) != 2:
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

            if self.pole[x][y]:
                self.pole[x][y].value = self.HUMAN_X
                self.free_cells -= 1
                self._compute_priority(y, x)
                break
            else:
                print('Выбранная клетка занята.')
                continue

    def computer_go(self):
        free_cells = [(y, x) for y, row in enumerate(self.pole) for x, cell in enumerate(row) if cell]
        y, x = max(free_cells, key=lambda c: self.pole[c[0]][c[1]].priority)
        if y == x:
            for cell in (self.pole[0][1], self.pole[1][0], self.pole[2][1]):
                cell.priority += 2
        self.free_cells -= 1
        self.pole[x][y].value = self.COMPUTER_O

    def _compute_priority(self, y, x):
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
        for row in self.pole:
            for cell in row:
                print(cell, end=' ')
            print()
        print('_____________________')


class Cell:
    def __init__(self):
        self.value = 0
        self.priority = 2

    def __bool__(self):
        return not self.value

    def __str__(self):
        if self.value == 1:
            return 'X'
        if self.value == 2:
            return '0'
        return '-'

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
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
