"""
    Created on March 8, 2021
    @author: Seth Kinsaul
    Test cases for the info operation
"""
import unittest
import Tiles2048.info as info


class InfoTest(unittest.TestCase):
    #Happy Paths
    def test100_010_ShouldReturnMyUserName(self):
        expectedResult = {'user': 'smk0036'}
        userParms = {'op': 'info'}
        actualResult = info._info(userParms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_020_ShouldReturnMyUserName(self):
        expectedResult = {'user': 'smk0036'}
        userParms = {'op': 'info'}
        actualResult = info._info(userParms)
        self.assertEqual(expectedResult, actualResult)
    #Sad Path    
    def test200_010_ShouldReturnMyUserName(self):
        expectedResult = {'user': 'smk0031'}
        userParms = {'op': 'info'}
        actualResult = info._info(userParms)
        self.assertNotEqual(expectedResult, actualResult)