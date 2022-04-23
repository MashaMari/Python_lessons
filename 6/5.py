true_pass = '12345'
password = input()
while password != true_pass:
    print('False password!')
    password = input('Введите пароль: ')
print('True password!')    