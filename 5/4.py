first = int(input('Введите цену первого товара: '))
second = int(input('Введите цену второго товара: '))
if first > second:
    scidka = second // 2
    sum = first + scidka
    print('Сумма к оплате:',sum)
else:
    skidka = first // 2
    print('Сумма к оплате:',sum, second + skidka)
