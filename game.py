import random

class Array:

    def __init__(self, _array, _extraArray=None):
        self.myArray = _array
        self.yuk = self.myArray.__len__()
        self.gen = self.myArray[0].__len__()
        self.extraArray = _extraArray
        self.printCheck = True

    @staticmethod
    def randomArray():
        gen = random.randrange(20, 25)
        yuk = random.randrange(10, 15)
        array = [[0] * gen for i in range(yuk)]
        for i in range(yuk):
            for j in range(gen):
                array[i][j] = random.randrange(0, 2) == 1
                array[i][j] = random.randrange(0, 2) == 0 
        return Array(array)


    def printArray(self):
        print("Yukseklik =", self.yuk, "Ve  Genislik =", self.gen)
        for i in range(self.yuk):
            for j in range(self.gen):
                x = self.myArray[i][j]
                def one(): 
                    print("*|", end='')
                def zero():
                    print(" |", end='')
                {
                1:  one,
                0: zero,
                }.get(x)()                    
            print()
        print("\n--------------------------------------------")
    pass

    def countKomsu(self,eksenX,eksenY):
        toplam = 0
        
        if eksenX == 0 and eksenY == 0:
            toplam += self.myArray[eksenY + 1][eksenX]
            toplam += self.myArray[eksenY + 1][eksenX + 1]
            toplam += self.myArray[eksenY][eksenX + 1]
        
        elif eksenX == self.gen-1 and eksenY == self.yuk-1:
            toplam += self.myArray[eksenY - 1][eksenX]
            toplam += self.myArray[eksenY - 1][eksenX - 1]
            toplam += self.myArray[eksenY][eksenX - 1]
        
        elif eksenX == 0 and eksenY == self.yuk - 1:
            toplam += self.myArray[eksenY][eksenX + 1]
            toplam += self.myArray[eksenY - 1][eksenX + 1]
            toplam += self.myArray[eksenY - 1][eksenX]
        
        elif eksenX == self.gen-1 and eksenY == 0:
            toplam += self.myArray[eksenY][eksenX - 1]
            toplam += self.myArray[eksenY + 1][eksenX - 1]
            toplam += self.myArray[eksenY + 1][eksenX]
        
        elif eksenY == 0 and eksenX != 0 and eksenX != self.gen - 1:
            toplam += self.myArray[eksenY + 1][eksenX]
            toplam += self.myArray[eksenY + 1][eksenX + 1]
            toplam += self.myArray[eksenY + 1][eksenX - 1]
            toplam += self.myArray[eksenY][eksenX - 1]
            toplam += self.myArray[eksenY][eksenX + 1]
        
        elif eksenY == self.yuk - 1 and eksenX != 0 and eksenX != self.gen - 1:
            toplam += self.myArray[eksenY - 1][eksenX]
            toplam += self.myArray[eksenY - 1][eksenX + 1]
            toplam += self.myArray[eksenY - 1][eksenX - 1]
            toplam += self.myArray[eksenY][eksenX + 1]
            toplam += self.myArray[eksenY][eksenX - 1]
        
        elif eksenX == 0 and eksenY != 0 and eksenY != self.yuk - 1:
            toplam += self.myArray[eksenY][eksenX + 1]
            toplam += self.myArray[eksenY + 1][eksenX + 1]
            toplam += self.myArray[eksenY - 1][eksenX + 1]
            toplam += self.myArray[eksenY + 1][eksenX]
            toplam += self.myArray[eksenY - 1][eksenX]
        
        elif eksenX == self.gen-1 and eksenY != 0 and eksenY != self.yuk - 1:
            toplam += self.myArray[eksenY][eksenX -1]
            toplam += self.myArray[eksenY + 1][eksenX - 1]
            toplam += self.myArray[eksenY - 1][eksenX - 1]
            toplam += self.myArray[eksenY + 1][eksenX]
            toplam += self.myArray[eksenY - 1][eksenX]
        
        else:
            toplam += self.myArray[eksenY][eksenX - 1]
            toplam += self.myArray[eksenY][eksenX + 1]
            toplam += self.myArray[eksenY + 1][eksenX + 1]
            toplam += self.myArray[eksenY + 1][eksenX - 1]
            toplam += self.myArray[eksenY - 1][eksenX + 1]
            toplam += self.myArray[eksenY - 1][eksenX - 1]
            toplam += self.myArray[eksenY + 1][eksenX]
            toplam += self.myArray[eksenY - 1][eksenX]
        return toplam

    def arrayCheck(self):
        for i in range(self.yuk):
            for j in range(self.gen):
                return True
        return False

    def nextArray(self):
        eksenY = 0
        eksenX = 0
        new_array = []
        for eksenY in range(self.yuk):
            eksenX = 0
            changeArray = []
            for eksenX in range(self.gen):
                if self.countKomsu(eksenX,eksenY) > 3:
                    changeArray.append(0)
                elif self.countKomsu(eksenX,eksenY) < 2:
                    changeArray.append(0)
                elif self.myArray[eksenY][eksenX] == 0 and self.countKomsu(eksenX,eksenY) == 3:
                    changeArray.append(1)
                else:
                    changeArray.append(self.myArray[eksenY][eksenX])
                eksenX += 1
            new_array.append(changeArray)
            eksenY += 1
        self.myArray = new_array

if __name__ == '__main__':
    hello = Array.randomArray()
    hello.printArray()
    while hello.arrayCheck():
        hello.nextArray()
        hello.printArray()