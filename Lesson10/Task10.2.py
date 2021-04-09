'''
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Создать абстрактный класс Clothes (одежда). Сделать в этом классе свойство cloth_size
(используя декоратор @property) - размер ткани, необходимый для производства одежды.
Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:

для пальто: (size/6.5 + 0.5)
для костюма: (2*height + 0.3)
Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
Распечатать список одежды: размер требуемой ткани, тип и параметр.
Рассчитать и вывести на экран общий объем ткани, необходимый для пошива всей одежды из этого списка, используя свойство
 cloth_size. Например:

30.3 - Suit (height: 15)
20 - Coat (size: 3)
13.5 - Coat (size: 2)
4.3 - Suit (seze: 2)
...
Итого: 250.3
'''
class Clothes:


    def __init__(self, list):
        self.list_clothes=list



    @property
    def cloth_size(self):
        self.list_clothes.get_size()

    def get_size(self):
        result = 0
        for i in self:
            result += i.get_size()
        return result


    def __getitem__(self, indx):
        return self.list_clothes[indx]





class Suit:


    def __init__(self, height):
        self.height=height


    def get_size(self):

        return (2*self.height + 0.3)



class Coat:


    def __init__(self, size):
        self.size = size

    def get_size(self):
       return (self.size // 6.5 + 0.5)


import random

def create_random():
    return random.randrange(0,2)


clothes = Clothes([])


for i in range (10):
    if create_random() == 0:

        clothes.list_clothes.append(Suit(random.randrange(150, 200)))
        print(clothes.list_clothes[i].get_size(), '- Suit', '(height :{})'.format(clothes.list_clothes[i].height))  #30.3 - Suit (height: 15)
    else:
        clothes.list_clothes.append(Coat(random.randrange(28, 40)))
        print(clothes.list_clothes[i].get_size(), '- Coat', '(size :{})'.format(clothes.list_clothes[i].size))

print('Итого:', clothes.get_size())