def get_imt(weight, height):
    height = height / 100
    imt = weight / (height * height)
    return imt

def interpritate_imt(imt):
    if imt <= 16:
        return 'Deficit'   
    elif imt <= 23:
        return 'Normal'
    else:
        return 'Excess'       

def ask_info():
    weight = int(input('Input your weight: '))
    height = int(input('Input your height: '))    
    imt = get_imt(weight, height)
    print(interpritate_imt(imt))

FLAG = input('Do you want to know about your imt? (Y/N): ')
while FLAG == 'Y':
    ask_info()
    FLAG = input('Do you want to know about your imt? (Y/N): ')
    if FLAG == 'N':
        exit()
ask_info()    