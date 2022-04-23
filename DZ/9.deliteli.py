# Задача 1: Написать функцию, которая будет печатать все делители передаваемого в функцию аргумента и возвращать их количество

# q=0
# a = 25
# for i in range(1, a+1):
#     if a%i==0:
#         print(i)
#         q+=1
#     i+=1
# print(q)

def print_dels(num):
    q = 0
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
            q += 1
    return q
      
print_dels(10)

    