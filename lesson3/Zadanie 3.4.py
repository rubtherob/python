"""* (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
        строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
         а значения — словари, реализованные по схеме
        предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:

"""






def thesaurus_adv(*args):
    List_name= args
    result_list= {}
    for name in List_name:
        if (name.split()[1][0]) in result_list:
            if result_list[name.split()[1][0]].get(name[0]) != None:
                result_list[name.split()[1][0]][name[0]].append(name)

            else:
                result_list[name.split()[1][0]][name[0]]=[name]
        else:
            result_list[name.split()[1][0]]= {name[0]:[name]}

    return result_list






print(thesaurus_adv('Олег Сванов','Георгий Королёв', 'Инокентий Иванов', 'Гавриил Купцов', 'Ахмед Синичкин', 'Арина Ивлеева','Армен Григорян','Алина Илистовая'))