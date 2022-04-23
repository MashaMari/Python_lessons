import random
random_number = random.randint(2, 10)

def is_simple(n):
    if n % random_number == 0:
        print('no')
    else:
        print('yes')
is_simple(38)            