import random

class Array:

    def __init__(self, _array, _extraArray=None):
        self.myArray = _array
        self.yuk = self.myArray.__len__()
        self.gen = self.myArray[0].__len__()
        self.extraArray = _extraArray


    @staticmethod
    def randomArray():
        width = random.randrange(25, 30)
        height = random.randrange(10, 15)
        array = [[0] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                if random.randrange(0, 2) == 1:
                    array[i][j] = 1
                else:
                    array[i][j] = 0
        return Array(array)

    def printArray(self):
        print("Yukseklik =", self.yuk, "Ve  Genislik =", self.gen)
        for i in range(self.yuk):
            for j in range(self.gen):
                if self.myArray[i][j]:
                    print("1|", end='')
                else:
                    print(" |", end='')
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
    

if __name__ == '__main__':
    hello = Array.randomArray()
    hello.printArray()