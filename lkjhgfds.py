from random import randint


# здесь объявляйте классы
class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) is not bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if (type(value) is not int) or (value not in range(9)):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) is not bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        if True == self.is_open:
            return False
        return True


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance==None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for i in range(M + 1)] for i in range(N + 1)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        mines = self.total_mines
        while mines != 0:
            a = randint(1, self.M-1)
            b = randint(1, self.N-1)
            if self.__pole_cells[b][a].is_mine == False:
                self.__pole_cells[b][a].is_mine = True
                mines -= 1

                self.__pole_cells[b + 1][a + 1].number += 1
                self.__pole_cells[b + 1][a].number += 1
                self.__pole_cells[b + 1][a - 1].number += 1
                self.__pole_cells[b][a - 1].number += 1
                self.__pole_cells[b][a + 1].number += 1
                self.__pole_cells[b - 1][a + 1].number += 1
                self.__pole_cells[b - 1][a - 1].number += 1
                self.__pole_cells[b - 1][a].number += 1
            else:
                continue

    def open_cell(self, i, j):
        if i + 1 > self.N or j + 1 > self.M:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

        self.__pole_cells[i + 1][j + 1].is_open = True

    def show_pole(self, open = False):
        if open == False:
            for i in range(len(self.__pole_cells)):
                for j in range(len(self.__pole_cells[i])):
                    if self.__pole_cells[i][j].is_open is True:
                        print('#', end = ' ')
                    elif self.__pole_cells[i][j].is_mine is True:
                        print('*', end=' ')
                    else:
                        print(self.__pole_cells[i][j].number, end=' ')
                print()
        else:
            for i in range(len(self.__pole_cells)):
                for j in range(len(self.__pole_cells[i])):
                    if self.__pole_cells[i][j].is_mine is True:
                        print('*', end=' ')
                    else:
                        print(self.__pole_cells[i][j].number, end=' ')
                print()

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"

p.show_pole()