import unittest
import sys
sys.path.append("../src/")
from central_tendancy import mean


class TestMean(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean(1,2,3), 2, "Should be 2")
        self.assertEqual(round(mean(0.1,0.2,0.3),2), 0.2, "Should be 0.2")
        self.assertEqual(round(mean(10202,3945,56654),2), 23600.33, "Should approximately equal 23600.33")

    def test_mean_list(self):
        self.assertEqual(mean([1,2,3,4,5,6,7,8,9,10]), 5.5, "Should be 5.5")
        self.assertEqual(round(mean([0.1,0.2,0.3]),2), 0.2, "Should be 0.2")

    def test_mean_tuple(self):
        self.assertEqual(round(mean((0.1,0.2,0.3)),2), 0.2, "Should be 0.2")

if __name__ == "__main__":
    unittest.main()
