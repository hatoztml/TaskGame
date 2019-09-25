import random

class Array:

    def __init__(self,yuk,gen):
        self.yuk = yuk
        self.gen = gen
        self.myArray = []
    
    def randomArray(self):
        gen = 0
        yuk = 0
        while yuk < self.yuk:
            gen = 0
            temp_array = []
            while gen < self.gen:
                temp_array.append(random.randrange(0,2))
                gen += 1
            self.myArray.append(temp_array)
            yuk += 1

    def printArray(self):
        print("Yukseklik =", self.yuk, "Ve  Genislik =", self.gen)
        for i in range(self.yuk):
            for j in range(self.gen):
                if self.myArray[i][j]:
                    print("1|", end='')
                else:
                    print(" |", end='')
            print()
        print("--------------------------------------------")
    
if __name__ == '__main__':
    gen = random.randrange(25, 30)
    yuk = random.randrange(10, 15)
    hello = Array(yuk,gen)
    hello.randomArray()
    hello.printArray()