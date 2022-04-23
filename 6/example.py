number = 1000
i = 0
while number != 10000:
    left = number // 100
    right = number % 100
    left = left // 10 + left % 10 * 10
    if left == right:
        i = i + 1
    number = number + 1
print(i)        
