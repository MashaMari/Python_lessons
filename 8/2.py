# def min(a,b):
#     if a> b:
#         print(b)
#     else:
#         print(a)
# min(5,6)     

number = int(input(''))
number2 = int(input(''))
def my(a,b):
    if a > b:
        print(number, 'больше' ,number2)
    elif a < b:
        print(number2, 'меньше' ,number)
    else:
        print('Они равны')  
my(number, number2)              