# class dog:
#     def _init_(self):
#         self.name = input('name: ')

# a = dog() 
# print(a.name)   

from unicodedata import name


class cat:
    def __init__(self):
        self.name = name

    def meow(self):
        print(self.name, 'say meow') 

    def _add_(self, other):
        print(self.name, 'attacks', other.name)       

b = cat('Vasya')
c = cat('Barsik')
b + c
c + b
# b.meow()
# c.meow()
# print(b.name)

int()