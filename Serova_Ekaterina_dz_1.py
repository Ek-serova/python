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
