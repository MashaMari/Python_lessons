number = int(input("Введите числоменьше 1000: "))

hundred = number // 100
decimal = (number % 100) // 10
units = number % 10
if hundred == 0:
    if decimal == 0:
        print(units)
    else:
        print(decimal)
else:
    print(hundred)            
