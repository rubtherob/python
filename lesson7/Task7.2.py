'''
* (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами,
его можно создать в любом текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации,
 библиотеки использовать нельзя.


'''

import os


def create_structure(path):
    if os.path.isdir(os.path.join(path, 'myproject'))==True:
        print('Папка уже существует')
    else:
        if os.path.isfile(os.path.join(path, 'config.yaml'))==True:
            os.mkdir(os.path.join(path, 'myproject'))

            # settings
            os.mkdir(os.path.join(path, 'myproject', 'settings'))
            f = open(os.path.join(path, 'myproject','settings', "__init__.py"), 'tw', encoding='utf-8')
            f.close()
            f = open(os.path.join(path, 'myproject', 'settings', "dev.py"), 'tw', encoding='utf-8')
            f.close()
            f = open(os.path.join(path, 'myproject', 'settings', "prod.py"), 'tw', encoding='utf-8')
            f.close()


           #mainapp
            os.mkdir(os.path.join(path, 'myproject', 'mainapp'))
            f = open(os.path.join(path, 'myproject', 'mainapp', "__init__.py"), 'tw', encoding='utf-8')
            f.close()
            f = open(os.path.join(path, 'myproject', 'mainapp', "models.py"), 'tw', encoding='utf-8')
            f.close()
            f = open(os.path.join(path, 'myproject', 'mainapp', "views.py"), 'tw', encoding='utf-8')
            f.close()
            os.mkdir(os.path.join(path, 'myproject', 'mainapp','templates'))
            os.mkdir(os.path.join(path, 'myproject', 'mainapp', 'templates','mainapp'))
            f = open(os.path.join(path, 'myproject', 'mainapp', 'templates','mainapp','base.html'), 'tw', encoding='utf-8')
            f.close()
            f = open(os.path.join(path, 'myproject', 'mainapp', 'templates','mainapp','index.html'), 'tw', encoding='utf-8')
            f.close()



            #authapp
            os.mkdir(os.path.join(path, 'myproject','authapp'))
            f = open(os.path.join(path, 'myproject', 'authapp', "__init__.py"), 'tw', encoding='utf-8')
            f.close()
            f = open(os.path.join(path, 'myproject', 'authapp', "models.py"), 'tw', encoding='utf-8')
            f.close()
            f = open(os.path.join(path, 'myproject', 'authapp', "views.py"), 'tw', encoding='utf-8')
            f.close()
            os.mkdir(os.path.join(path, 'myproject', 'authapp', 'templates'))
            os.mkdir(os.path.join(path, 'myproject', 'authapp', 'templates', 'authapp'))
            f = open(os.path.join(path, 'myproject', 'authapp', 'templates', 'authapp', 'base.html'), 'tw',
                     encoding='utf-8')
            f.close()
            f = open(os.path.join(path, 'myproject', 'authapp', 'templates', 'authapp', 'index.html'), 'tw',
                     encoding='utf-8')
            f.close()

create_structure('D:\Deskop\courses\python\Test')