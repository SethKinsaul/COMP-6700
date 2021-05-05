"""
    Created on March 8, 2021
    @author: Seth Kinsaul
    Create operation to build the initial state of a 2048 grid 
"""
import random
import hashlib

def _create(userOperation):
    # Variables
    grid = [0]*16
    score = 0
    status = "ok"
    # Generate the grid with two 2's randomly placed
    generatedGrid = _generateGrid(grid)
    integrity = _determineHash(generatedGrid)
    result = {'grid': generatedGrid, 'score': score, 
              'integrity': integrity.upper(), 'status': status}
    return result

def _determineHash(gridString):
    myHash = hashlib.sha256() # Create hash object
    myHash.update(gridString.encode()) # Encode data and update
    myHashDigest = myHash.hexdigest()  # Put the encoded data in hexadecimal format
    
    return myHashDigest
    
def _generateGrid(grid):
    gridString = ""
    
    random.seed();    
    r = random.randint(0,15)
    r2 = random.randint(0,15)
    if r == r2:
        _generateGrid(grid)
    elif r != r2:
        grid[r] = 2
        grid[r2] = 2
    for x in grid:
        gridString += str(x)
        
    return gridString    

