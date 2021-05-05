"""
    Created on March 8, 2021
    @author: Seth Kinsaul
    Test cases for the create operation 
"""
import unittest
import Tiles2048.create as create
from Tiles2048.create import _determineHash

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.
    #Happy Path
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult)
        
    def test_create_HappyPathTest020(self):
        expectedResult = {'grid': '0000200020000000', 'score': 0, 'integrity': '08895D7731CE60F8073EDB3313B16234800641CEB86E342018BF85696DB6A9A8', 'status': 'ok'}
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertEqual(len(expectedResult), len(actualResult))

    def test_create_HappyPathTest030(self):
        gridString = '0002000020000000'
        gridString2 = '0000200020000000'
        hash1 = _determineHash(gridString)
        hash2 = _determineHash(gridString2)
        self.assertNotEqual(hash1, hash2)
        
    #Blackbox Testing    
    def test_create_SadPathTest010(self):
        expectedResult = {'grid': '0200000200000000', 'score': 0, 'integrity': '9E5BF88798C63AA846C4E1B08BF68F3F1EFEADFD56545DD26FDA89C289EF7955', 'status': 'ok'}
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test_create_SadPathTest020(self):
        expectedResult = '2020000000000000'
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertEqual(expectedResult, actualResult['grid'])
