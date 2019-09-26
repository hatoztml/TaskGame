import unittest
import random
from game import Array

class TestSum(unittest.TestCase):

    def testArrayCheckContinue(self):
        self.assertEqual(Array.arrayCheck(Array.randomArray()), True)
    
    def testArrayPrint(self):
        self.assertEqual(Array.printArray(Array.randomArray()), None)

    def testCountKomsu(self):
        value = Array.countKomsu(Array.randomArray(),1,2)
        value2 = value
        self.assertEqual(value, value2)

if __name__ == '__main__':
    unittest.main()