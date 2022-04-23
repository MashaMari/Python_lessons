first = input('К, Н, или Б: ')
second = input('К, Н, или Б: ')

if first == second:
    print('Ничья!')
    exit()

if first == 'К' and second == 'Н':
    print('Первый выиграл')
    exit()
if first == 'К' and second == 'Б':
    print('Второй выиграл')
    exit()
if first == 'Н' and second == 'К':
    print('Второй выиграл')
    exit()
if first == 'Н' and second == 'Б':
    print('Первый выиграл')
    exit()
if first == 'Б' and second == 'К':
    print('Первый выиграл')
    exit()
if first == 'Б' and second == 'Н':
    print('Второй выиграл')
    exit()                   

print('Программа закончила выполняться')
