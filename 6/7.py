import random
random_number = random.randint(0, 10)
user_number = int(input('Введите любое число от 0 до 10: '))
while user_number != random_number:
    if random_number > user_number:
        print('Загаданное число больше')
        user_number = int(input('Введите любое число от 0 до 10: '))
    elif random_number < user_number:    
        print('Загаданное число меньше')
        user_number = int(input('Введите любое число от 0 до 10: '))
else:        
    print('Вы угадали!')
       