# Задача 2*: Написать функцию, которая будет принимать три аргумента(дата, месяц, год) и возвращать день недели переданной даты


date = int(input('Input date: '))
month = (input('Input month: '))
year = int(input('Input year (XXI century): '))

if month == 'январь' or month == 'октябрь':
    cod_m = 1
elif month == 'май':
    cod_m = 2  
elif month == 'август':
    cod_m = 3  
elif month == 'февраль' or month == 'март' or month == 'ноябрь':   
    cod_m = 4  
elif month == 'июнь':
    cod_m = 5  
elif month == 'декабрь' or month == 'сентябрь':
    cod_m = 6  
elif month == 'апрель' or month == 'июль':
    cod_m = 0
                
year = year - 2000
cod_y = (6 + year + int(year / 4)) % 7
date_week = (cod_m + cod_y + date) % 7   

if date_week == 2:
    print('Понедельник')
elif date_week == 3:
    print('Вторник')
elif date_week == 4:
    print('Среда')
elif date_week == 5:
    print('Четверг')
elif date_week == 6:
    print('Пятница')
elif date_week == 0:
    print('Суббота')
elif date_week == 1:
    print('Воскресенье')

                  
                             