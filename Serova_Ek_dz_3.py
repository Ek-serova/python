#Задание 1-2

def num_translate():
    number={
        'one' : 'один',
        'two' : 'два',
        'three' : 'три',
        'four' : 'четыре',
        'five' : 'пять',
        'six' : 'шесть',
        'seven' : 'семь',
        'eight' : 'восемь',
        'nine' : 'девять',
        'ten' : 'десять'
    }
    number_en = input('Напишите число: ')
    if number.get(number_en.lower()) != None:
        number_rus = number[number_en.lower()]
        if number_en[0].isupper() == True:
            print(number_rus.capitalize())
        else:
            print(number_rus)
    else:
        print ('None')

num_translate()

#задание 3-4

def thesaurus_adv(*args):
    result={}
    for name_en in args:
        name,surname = name_en.split(" ")
        if result.get(surname[0]) == None:
            result.setdefault(surname[0], {})
            result.setdefault(surname[0],thesaurus(name,surname,result[surname[0]]))
        else:
            result[surname[0]] = thesaurus(name,surname,result[surname[0]])

    print(result)

def thesaurus(name_em,surname_em,result_thesaurus={}):
    if result_thesaurus.get(name_em[0]) == None:
        result_thesaurus.setdefault(name_em[0], [])
        result_thesaurus[name_em[0]].append(f'{name_em} {surname_em}')
    else:
        result_thesaurus[name_em[0]].append(f'{name_em} {surname_em}')
    return result_thesaurus

thesaurus_adv("Иван Иванов", "Инна Серова", "Егор Андреев", "Полина Алексеева", "Петр Алексеев", "Андрей Александров")

#задание 5

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_joket(n,flag=True):
    """функция выдает слчайную шутку"""
    for i in range(n):
        joke =f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        print (joke)
        list = []
        if flag == True:
            list_2 = joke.split()
            for noun in nouns:
                for fun in list_2:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs:
                for fun in list_2:
                    if adverb == fun:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for fun in list_2:
                    if adjective == fun:
                        adjectives.remove(adjective)

get_joket(2,flag=True)