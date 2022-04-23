import random
random_number = random.randint(0, 100)
while True:
    user_number = int(input('Введите любое число от 0 до 100: '))
    if user_number > random_number:
        print('Заданное число меньше')
    elif user_number < random_number:
        print('Заданное число больше')
    else:
        print('Вы угадали') 
        exit()   