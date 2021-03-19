"""
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

('Иван', '9А')
('Анастасия', '7В')
...

Количество генерируемых кортежей должно быть равно длине списка tutors. Если в списке klasses меньше элементов,
 чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
"""


from random import choice

def tut_in_kls(num):
    tutors = [
            'Иван', 'Анастасия', 'Петр', 'Сергей',
            'Дмитрий', 'Борис', 'Елена', 'Андрей'
    ]
    klasses = [
            '9А', '7В', '9Б', '9В', '8Б', '10А'
    ]

    tut=tuple((tutors.pop (tutors.index (choice ( tutors))),klasses.pop( klasses.index( choice( klasses)))))

    for a in range(len(tutors)+1):
        if a==num:
            break
        yield tut
        if len(klasses)!=0:
            tut=tuple((tutors.pop (tutors.index (choice(tutors))),klasses.pop(klasses.index (choice (klasses)))))
        else:
            tut = (tutors.pop (tutors.index(choice(tutors))), 'None')

a=tut_in_kls(8)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))



