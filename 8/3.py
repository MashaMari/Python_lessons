def solve(a, b, c):
    D = b * b - 4 * a * c
    if D < 0:
        print('Корней нет')
    elif D == 0:
        x = (-b - D ** 0.5) / (2 * a)
        print('Один корень: ')
        print(x)
    else:
        x1 = (-b - D ** 0.5) / (2 * a)
        x2 = (-b + D ** 0.5) / (2 * a) 
        print('Два корня: ')
        print(x1)
        print(x2)
solve(3, 7, -10)        