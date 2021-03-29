'''
Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
 email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
 email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
 имеет ли смысл в данном случае использовать функцию re.compile()?


'''


import re



def email_parse(email_address):
    email=re.search(R'\w+@\w+\.\w+',email_address,re.IGNORECASE)
    if email:
        email=re.split('@',email_address)
        print (email)
    else:
        raise ValueError('Не правильно введён адрес',email_address)



email_parse('r213124@mail.ru')