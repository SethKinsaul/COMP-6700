"""
    Created on April 29, 2021
    @author: Seth Kinsaul
    Test cases for the Status operation 
"""
import unittest
import Tiles2048.status as status

class statusTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.
    #Happy Path
    def test_status_HappyPathTest010(self):
        expectedResult = {'status': 'lose'}
        userParms = {'grid': "2424242424242424", 'direction': 'left', 'score': '0', 'integrity': '7E1D09C768AE3CB4CB7B6C2C88A18BC2D532140018E4E29EE8B1E80D7DDD061D', 'status': 'ok'}
        actualResult = status._status(userParms)
        self.assertEqual(expectedResult, actualResult)
        
    def test_status_HappyPathTest020(self):
        expectedResult = {'status': 'ok'}
        userParms = {'grid': "0020022200002222", 'direction': 'left', 'score': '0', 'integrity': '7E1D09C768AE3CB4CB7B6C2C88A18BC2D532140018E4E29EE8B1E80D7DDD061D', 'status': 'ok'}
        actualResult = status._status(userParms)
        self.assertEqual(expectedResult, actualResult)
        
    def test_status_HappyPathTest030(self):
        expectedResult = {'status': 'win'}
        userParms = {'grid': "2048000000000000000", 'direction': 'left', 'score': '0', 'integrity': '7E1D09C768AE3CB4CB7B6C2C88A18BC2D532140018E4E29EE8B1E80D7DDD061D', 'status': 'ok'}
        actualResult = status._status(userParms)
        self.assertEqual(expectedResult, actualResult)
        