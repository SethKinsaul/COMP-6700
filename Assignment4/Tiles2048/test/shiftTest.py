"""
    Created on March 8, 2021
    @author: Seth Kinsaul
    Test cases for the shift operation 
"""
import unittest
import Tiles2048.shift as shift

class ShiftTest(unittest.TestCase):
    # Tests fail due to randomness of a 2 or 4 being placed after the grid shifts
    def test_shift_HappyPathTest010(self):
        userParms = {'grid': "2020000000000000", 'direction': 'left', 'score': '0', 'integrity': '7E1D09C768AE3CB4CB7B6C2C88A18BC2D532140018E4E29EE8B1E80D7DDD061D', 'status': 'ok'}
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, {'grid': '4000000000400000', 'score': '4', 'integrity': '7E1D09C768AE3CB4CB7B6C2C88A18BC2D532140018E4E29EE8B1E80D7DDD061D', 'status': 'ok'})
        
    def test_shift_HappyPathTest020(self):
        userParms = {'grid': "2020000000000220", 'direction': 'right', 'score': '0', 'integrity': '7E1D09C768AE3CB4CB7B6C2C88A18BC2D532140018E4E29EE8B1E80D7DDD061D', 'status': 'ok'}
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, {'grid': '000400040000004', 'score': '8', 'integrity': '7D0686C3B2F8B3F16A6D69EAA5C823082911CD085350464315E1803F7685B0F7', 'status': 'ok'})
    
    def test_shift_HappyPathTest030(self):
        userParms = {'grid': "2000200000000000", 'direction': 'up', 'score': '0', 'integrity': '7E1D09C768AE3CB4CB7B6C2C88A18BC2D532140018E4E29EE8B1E80D7DDD061D', 'status': 'ok'}
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, {'grid': '4002000000000000', 'score': '4', 'integrity': 'C2ED4A1A9B64008EB47823DC129E0D48D925FE9DC077346B965B1A421A8C25BA', 'status': 'ok'})
        
    def test_shift_HappyPathTest040(self):
        userParms = {'grid': "2000200000000000", 'direction': 'down', 'score': '0', 'integrity': '7E1D09C768AE3CB4CB7B6C2C88A18BC2D532140018E4E29EE8B1E80D7DDD061D', 'status': 'ok'}
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, {'grid': '4000000000002000', 'score': '4', 'integrity': '05C479D1ADF03E682F4557395CC863F164EE63B0AE4B6E3C4AAD16CAC2524088', 'status': 'ok'})
        
            