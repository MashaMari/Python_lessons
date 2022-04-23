#Напишите программу, которая с помощью цикла for будет считать количество согласных букв в ведённом пользователем предложении

#qwrtpsdfghjklzxcvbnm

##### Вариант 1: Поиск согласных букв с помощью метода find()
user_text = input('Input text: ')
letters = 0
consonants = 'QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm'
for letter in user_text:
    if consonants.find(letter) != -1:
            letters = letters + 1
            print("Позиция буквы ", letter, " - ", consonants.find(letter))
print("Количество согласных:", letters)



##### Вариант 2: Поиск согласных букв с помощью метода find() более сложным способом
# user_text = input('Input text: ')
# letters = 0
# consonants = 'QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm'
# for letter in user_text:
#     for cons in consonants:
#         if consonants.find(letter) != -1:
#             letters = letters + 1
#             print("Позиция буквы ", letter, " - ", consonants.find(letter))
# print("Количество согласных:", letters)


##### Вариант 3: Поиск всех знаков с помощью метода find()
# user_text = input('Input text: ')
# big_letters = 0
# letters = 0
# marks = 0
# lett = 'йцукенгшщзхъфывапролджэячсмитьбюёeyuioaqwrtpsdfghjklzxcvbnm'
# big_lett = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮEYUIOAQWRTPSDFGHJKLZXCVBNM'
# punctuation = '?.,!;:'
# for letter in user_text:
#     if lett.find(letter) != -1:
#         letters = letters + 1
#     if big_lett.find(letter) != -1:
#         big_letters = big_letters + 1
#     if punctuation.find(letter) != -1:
#         marks = marks + 1        
# print("Количество строчных букв:", letters)
# print("Количество заглавных букв:", big_letters)
# print("Количество всех букв:", letters + big_letters)
# print("Количество знаков припинания:", marks)
# print("Количество всех знаков без пробелов:", letters + big_letters + marks)
       