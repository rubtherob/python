"""
    Дан список:
    ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

    Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
    ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

    Сформировать из обработанного списка строку:
    в "05" часов "17" минут температура воздуха была "+05" градусов

    Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?

    Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
    *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.

"""





Given_list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
a=0
joining=' '
while a < len(Given_list):
    if Given_list[a].isdigit() or Given_list[a][1:].isdigit():
        if len(Given_list[a])== 1:
            Given_list[a] = '0' + str(Given_list[a])
        elif (len(Given_list[a])== 2 and Given_list[a][0].isdigit()== False):
            Given_list[a] = str(Given_list[a][0]) + '0' + str(Given_list[a][1:])
        Given_list.insert(a, '"')
        Given_list.insert(a+2, '"')
        a+= 2
    else:
        a+= 1

print(Given_list)
print(joining.join(Given_list))