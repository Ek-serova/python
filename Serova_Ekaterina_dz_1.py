### 1. Реализовать вывод информации о промежутке времени в зависимости от
# его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#Примеры:
#duration = 53
#53 сек
#duration = 153
#2 мин 33 сек
#duration = 4153
#1 час 9 мин 13 сек
#duration = 400153
#4 дн 15 час 9 мин 13 сек

user_time = int(input('Введите время в секундах: '))

one_minute = 60
one_hour = 3600
one_day = 86400

if user_time < one_minute:
    print('{} сек'.format(user_time))
if one_minute <= user_time < one_hour:
    minute=user_time//one_minute
    second=user_time%one_minute
    print('{} мин {} сек'.format(minute,second))
if one_hour <= user_time < one_day:
    hour=user_time//one_hour
    user_time=user_time%one_hour
    minute = user_time // one_minute
    second = user_time % one_minute
    print('{} час {} мин {} сек'.format(hour, minute, second))
if one_day <= user_time:
    day=user_time//one_day
    user_time = user_time % one_day
    hour=user_time//one_hour
    user_time = user_time % one_hour
    minute = user_time // one_minute
    second = user_time % one_minute
    print('{} дн {} час {} мин {} сек'.format(day, hour, minute, second))

#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
#* Решить задачу под пунктом b, не создавая новый список.



list_cubes = [x**3 for x in range(1000) if  x%2 != 0 ]
my_sum_list =[]

for n in range(len(list_cubes)):
    number_in_str = str(list_cubes[n])
    list_sum=list(number_in_str) #разбиение числа на отдельные
    #print(list_sum_number_in_str)
    for i in range(len(list_sum)):
        list_sum[i]=int(list_sum[i])
    #print (list_sum)
    sum_numbers = sum(list_sum) # сумма чисел
    #print(sum_numbers)
    if sum_numbers%7==0:
        my_sum_list.append(list_cubes[n])
print (sum(my_sum_list))

list_cubes = [x**3+17 for x in range(1000) if  x%2 != 0 ]
my_sum_list =[]

for n in range(len(list_cubes)):
    number_in_str = str(list_cubes[n])
    list_sum=list(number_in_str) #разбиение числа на отдельные
    #print(list_sum_number_in_str)
    for i in range(len(list_sum)):
        list_sum[i]=int(list_sum[i])
    #print (list_sum)
    sum_numbers = sum(list_sum) # сумма чисел
    #print(sum_numbers)
    if sum_numbers%7==0:
        my_sum_list.append(list_cubes[n])
print (sum(my_sum_list))

#Склонение слова
#Реализовать склонение слова «процент» во фразе «N процентов».
#Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
#1 процент
#2 процента
#3 процента
#4 процента
#5 процентов
#6 процентов..


for i in range(1,101):
    str_percent=str(i)
    if str_percent[-1]=='1':
        print('{} процент'.format(str_percent))
    elif str_percent[-1]=='2' or str_percent[-1]=='3' or str_percent[-1]=='4':
        print('{} процента'.format(str_percent))
    else:
        print('{} процентов'.format(str_percent))








