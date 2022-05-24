
#задание 4
list_employee = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй',
              'директор аэлита']

for employee in list_employee:
    correct_name = employee.split()[-1].capitalize()
    print('Привет, {}!'.format(correct_name))