'''
 Реализовать базовый класс Employee (сотрудник).
определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus};
в классе Position реализовать методы получения полного имени сотрудника get_full_name()
и дохода с учётом премии get_total_income() (wage + bonus);
проверить работу примера на реальных данных: создать экземпляры классов Employee, Position, вывести на экран имя сотрудника,
 его должность и вознаграждение сотрудника, используя методы класса Position.
 '''
class Employee:


    def __init__(self, name='', surname=''):
        self.name = name
        self.surname = surname





class Position:

    def __init__(self, employee, position='', wage=0, bonus=0):
        self.employee = employee
        self.position = position
        self._income = {'wage':wage, 'bonus':bonus}


    def get_full_name(self, employee):
        print('Имя: {} Фамилия: {}'.format(self.employee.name, self.employee.surname))


    def get_total_income(self):
        print('Полная заработная плата:{}'.format(self._income['wage'] + self._income['bonus']))



employee = Employee('Иван', 'Иванович')
employee1 = Position(employee, 'Директор', 50000, 23000)
employee1.get_full_name(employee)
print('Должность:{}'.format(employee1.position))
employee1.get_total_income()



