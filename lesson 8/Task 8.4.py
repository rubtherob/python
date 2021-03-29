'''
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать
входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


 a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5


'''


def val_checker(lambda_func):


    def val_checkers(func):

        def val_checkerss(*args):
            for arg in args:
                print(arg)
            if lambda_func(arg) is not True:
                raise ValueError('Число меньше 0')
            func(arg)
        return val_checkerss
    return val_checkers

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

calc_cube(5)
