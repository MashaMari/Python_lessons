friends = int(input('Введи кол-во друзей: '))
sum = 0
for i in range(friends):
    age = int(input('Введи возраст друга: '))
    sum = sum + age
print('Средний возраст: ', sum/friends)    
            
