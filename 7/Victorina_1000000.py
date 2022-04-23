import time
question = 'what the symbol of next year?'
right_answer = 'tiger'

#Настройки
tries = 3
time_for_answer = 7

for i in range(tries):
    print(question)
    start = time.time()
    user_answer = input()
    end = time.time()
    if user_answer == right_answer:
        if end - start < time_for_answer:
            print('You are win!!!!', 'You spend ', end-start, 'seconds')
        else:
            print('You need to answer faster')    
        exit()

print('You are lose')    