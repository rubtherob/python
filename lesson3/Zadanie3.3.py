"""Написать функцию thesaurus(), принимающую в качестве аргументов
        имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имен,
        а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:

"""


def thesaurus(*args):
    List_name=args
    result_list={}
    for name in List_name:
        if (name[0]) in result_list:
            result_list[name[0]].append(name)
        else:
            result_list[name[0]]= [name]

    return result_list






print(thesaurus('Инокентий', 'Гавриил', 'Ахмед', 'Арина'))