def get_day_of_week(d, m, y):
    m = m - 2
    if m <= 0:
        m += 12
    c = y // 100
    y = y % 100
    day_of_week = (d + ((13 * m - 1) // 5 ) + y + (y //4 + c // 4 - 2*c + 777)) % 7
    return day_of_week
    print(day_of_week)
