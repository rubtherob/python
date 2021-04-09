'''
Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки
(целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
 вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
 Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
  умножение и округление до целого числа деления клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
 ячеек этих двух клеток.
Добавить к классу метод print(columns), распечатыващий на экране звездочки рядами по columns звездочек в одном ряду в
количестве равном числу ячеек клетки.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, если в клетке 12 ячеек, а запросили напечатать по 5 звездочек в ряду, то на экране должно быть:

*****
*****
**
'''
class Cell:

    def __init__(self,cells):
        self.cells=cells

    def __add__(self, other):
        new_cell=Cell(self.cells+other.cells)
        return new_cell

    def __sub__(self, other):
        check=self.cells-other.cells
        if check>=0:
            new_cell = Cell(check)
            return new_cell
        else:
            raise ValueError('Ошибка вычитания.')


    def __mul__(self,other):
        new_cell=Cell(self.cells*other.cells)
        return new_cell

    def __truediv__(self,other):
        new_cell=Cell(self.cells//other.cells)
        return (new_cell)

    def print(self,columns):
        str=self.cells//columns
        last_str=self.cells%columns
        for i in range (str):
            print('*'*columns)
        print('*'*last_str)




cell_1=Cell(3)
cell_2=Cell(10)
cell_3=Cell(7)



cell_4=cell_1+cell_2
print(cell_4.cells)

cell_5=cell_2-cell_1
print(cell_5.cells)

cell_6=cell_2*cell_3
print(cell_6.cells)

cell_7=cell_2/cell_1
print(cell_7.cells)



cell_3.print(10)
