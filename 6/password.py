true_pass = '12345'
password = input('Type password: ')
kolvo_p = 0
while password != true_pass:
    print('Incorrect password.') 
    password = input('Type correct passward: ')
    kolvo_p = kolvo_p + 1
print('Correct password')
print(kolvo_p, '- number of tries')    