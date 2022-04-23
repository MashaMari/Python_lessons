def get_status(points):
    if points >= 85:
        return ('Winner')
    elif points >= 60:
        return ('Prizer')
    else:
        return ('Participant')
        
n = int(input('Type number of participant: '))
for i in range(n):
    points = int(input(f'Points of participant №{i+1}:'))
    print(get_status(points))
#print(get_status(92))                