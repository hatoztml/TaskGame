import random

class Array:

    def __init__(self,yuk,gen):
        self.yuk = yuk
        self.gen = gen
        self.myArray = []
    
    
if __name__ == '__main__':
    gen = random.randrange(25, 30)
    yuk = random.randrange(10, 15)
    hello = Array(yuk,gen)