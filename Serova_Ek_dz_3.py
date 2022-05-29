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