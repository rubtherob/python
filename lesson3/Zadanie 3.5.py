''' Реализовать функцию get_jokes(),
        возвращающую n шуток, сформированных из трех слов, взятых из трёх списков (по одному слову из каждого списка):
'''

from random import choice

def get_jokes(amount=2,flag='yes'):
    """Функция возвращающая n шуток, сформированных из трех слов.

        Keyword arguments:
        amount -- Кол-во шуток которые будут сгенерированны в результате, по стандарту 2
        flag -- Флаг разрешающий или запрещающий повторы слов в шутках "Yes"-Разрешает повторы,"No"-запрещает

        """
    Result=[]
    Joke=''
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if flag=='yes':
        for a in range (amount):
            Joke += str(choice ( nouns))+ ' '
            Joke += str(choice ( adverbs))+ ' '
            Joke += str(choice ( adjectives))
            Result.append( Joke)
            Joke= ''
    else:
        for a in range (amount):
            print((int(nouns.index(choice(nouns)))))
            Joke += str(nouns.pop(int(nouns.index(choice(nouns)))))+' '
            Joke += str(adverbs.pop(int(adverbs.index(choice(adverbs)))))+' '
            Joke += str(adjectives.pop(int(adjectives.index(choice(adjectives)))))
            Result.append(Joke)
            Joke=''
    return Result

print(get_jokes(3 ,'no'))