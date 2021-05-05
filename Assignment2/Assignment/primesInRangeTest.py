import unittest
import Assignment.primesInRange as primesInRange
from _overlapped import NULL

class PrimeInRangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

# Sample happy path test
    def test100_100_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 2
        highBound = 10
        expectedResult = [2, 3, 5, 7]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
    def test200_200_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 34
        highBound = 35
        expectedResult = []
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
    def test300_300_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 11
        highBound = 11
        expectedResult = [11]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
    def test400_400_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 11
        highBound = 17
        expectedResult = [11, 13, 17]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
    def test500_500_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 950
        highBound = 1000
        expectedResult = [953,967,971,977,983,991,997]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    #Sample Sad Path Test
    def test600_600_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 3.4
        highBound = 7.1
        expectedResult = [7]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    def test700_700_ShouldDeterminePrimesInNominalRange(self):
        lowBound = None
        highBound = None
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)    
    def test800_800_ShouldDeterminePrimesInNominalRange(self):
        lowBound = -17
        highBound = 10
        expectedResult = [2, 3, 5, 7]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)    
    