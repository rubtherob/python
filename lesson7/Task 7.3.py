'''Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание,
 что html-файлы расположены в родительских папках (они играют роль пространств имён);
  предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
'''
import os
import shutil

def change_templates(path):
    if os.path.isdir(os.path.join(path,'myproject'))!=True:
        print('Нет нужной директории')
    else:
        os.mkdir(os.path.join(path, 'myproject', 'templates'))
        shutil.copytree(os.path.join(path, 'myproject', 'mainapp', 'templates','mainapp'),
                             os.path.join(path, 'myproject', 'templates','mainapp'))
        shutil.copytree(os.path.join(path, 'myproject', 'authapp', 'templates','authapp')
                                ,os.path.join(path, 'myproject', 'templates','authapp'))




change_templates('D:\Deskop\courses\python\Test')