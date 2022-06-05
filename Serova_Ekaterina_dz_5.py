#Task#1

def gen_range(stop_value, start_value=0, step=1):
    current = start_value
    while current < stop_value:
        yield current
        current += step

n = int(input('Введите значение n: '))

obj_gen = gen_range(n, 1, 2)

for i in obj_gen:
    print(i)

#Task#2

def gen_range(stop_value, start_value=0, step=1):
    gen_current = []
    current = start_value
    while current < stop_value:
        gen_current.append(current)
        current += step
    return gen_current

n = int(input('Введите значение n: '))

obj_gen = gen_range(n, 1, 2)

for i in obj_gen:
    print(i)

#task 3

def gen_new_list(tutor, klass):
    i = 0
    while i < len(tutor) and i < len(klass):
        yield tutor[i], klass[i]
        i += 1
    while i < len(tutor):
        yield tutor[i], None
        i += 1

tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей',
'Дмитрий', 'Борис', 'Елена','Олег', 'Станислав'
]
klasses = [
'9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for i in gen_new_list(tutors,klasses):
    print(i)

# task 4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [j for i, j in zip(src, src[1:]) if j > i]

print(result)

# task 5

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

for number in numbers:
    if numbers.count(number) == 1:
       result.append(number)

print(result)
