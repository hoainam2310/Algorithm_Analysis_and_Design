import unittest
import fractional_knapsack as fk

class unitTesting(unittest.TestCase):

    def test_1(self):
        result = fk.FractionalKnapSack.getMaxValue([10,40,20,30], [60,40,100,120], 50)
        self.assertEqual(result, 240)
    def test_2(self):
        result = fk.FractionalKnapSack.getMaxValue([2,3,5,7,1,4,1], [10,5,15,7,6,18,3], 15)
        self.assertEqual(result, 55.333333333333336)
    def test_3(self):
        result = fk.FractionalKnapSack.getMaxValue([18,15,10], [25,24,15], 20)
        self.assertEqual(result, 31.5)
    def test_4(self):
        result = fk.FractionalKnapSack.getMaxValue([5,10,20,30,40], [30,20,90,100,90], 60)
        self.assertEqual(result, 231.25)
    def test_5(self):
        result = fk.FractionalKnapSack.getMaxValue([20,40,10,20,30], [10,25,15,10,10], 25)
        self.assertEqual(result, 24.375)
    def test_6(self):
        result = fk.FractionalKnapSack.getMaxValue([5,20,10], [50,140,60], 30)
        self.assertEqual(result, 220)
    def test_7(self):
        result = fk.FractionalKnapSack.getMaxValue([3,2,1,4,5], [25,20,15,30,50], 6)
        self.assertEqual(result, 65)
    def test_8(self):
        result = fk.FractionalKnapSack.getMaxValue([2,1,3,2], [12,10,20,15], 5)
        self.assertEqual(result, 38.33333333333333)
    def test_9(self):
        result = fk.FractionalKnapSack.getMaxValue([4,2,1,10,2], [12,2,1,4,1], 15)
        self.assertEqual(result, 18.4)
    def test_10(self):
        result = fk.FractionalKnapSack.getMaxValue([3,9,10,3,6,7], [2,9,3,4,1,0], 4)
        self.assertEqual(result, 5)
    def test_11(self):
        result = fk.FractionalKnapSack.getMaxValue([12,16,5,8,2], [3,4,10,5,1], 6)
        self.assertEqual(result, 10.625)

if __name__ == '__main__':
    unittest.main()


