"""
    Created on April 1, 2021
    @author: Seth Kinsaul
    Shift operation to move the grid in four different directions and combine numbers of the same numerical value. 
    row major order for operation
"""
import random
import hashlib

DIRECTION = ('up', 'down', 'left', 'right')
VALID_NUMS = ('0', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024')

def _shift(userOperation):
    _check_missing(userOperation)
    grid = userOperation['grid']
    direction = userOperation['direction']
    oldScore = userOperation["score"]
    status = "ok"
    
    dupGrid = []
    for i, x in enumerate(grid):
        print(dupGrid)
        if grid[i] == "0":
            dupGrid.append(int(grid[i]))
        elif grid[i] != "0" and i+3 < len(grid):
            c = numConcat(grid[i], grid[i+1])
            if c in VALID_NUMS:
                dupGrid.append(int(c))
            d = numConcat(c, grid[i+2])
            if d in VALID_NUMS:
                dupGrid.append(int(d))
            e = numConcat(d, grid[i+3])
            if e in VALID_NUMS:
                dupGrid.append(int(d))
            if grid[i] in VALID_NUMS:
                dupGrid.append(int(grid[i]))
        else:
            dupGrid.append(int(x))
    print(dupGrid)

    if direction == "left":
        newGrid = [dupGrid[i:i+4] for i in range(0, len(dupGrid), 4)]
        nextGrid = [list(filter(None, i))+([0]*i.count(0)) for i in newGrid]
        lastGrid = [i for b in nextGrid for i in b]
        (finalGrid, oldScore) = merge(lastGrid,oldScore)
        
        shiftedGrid = addTwoOrFour(finalGrid)
        
        status = getStatus(shiftedGrid)
        shiftedGrid = toString(shiftedGrid)
        integrity = _determineHash(shiftedGrid)
        
        userOperation['score'] = oldScore
        userOperation['grid'] = shiftedGrid
        
        result = {'grid': shiftedGrid, 'score': str(oldScore), 
              'integrity': integrity.upper(), 'status': status}
        return result
    
    elif direction == "right":
        newGrid = [dupGrid[i:i+4] for i in range(0, len(dupGrid), 4)]
        nextGrid = [list(filter(None, i))+([0]*i.count(0)) for i in newGrid]
        lastGrid = [i for b in nextGrid for i in b]
        (finalGrid, oldScore) = merge(lastGrid,oldScore)
        
        rowOne = finalGrid[0:4]
        rowOne = pushNonZerosToEnd(rowOne, len(rowOne))
        rowTwo = finalGrid[4:8]
        rowTwo = pushNonZerosToEnd(rowTwo, len(rowTwo))
        rowThree = finalGrid[8:12]
        rowThree = pushNonZerosToEnd(rowThree, len(rowThree))
        rowFour = finalGrid[12:16]
        rowFour = pushNonZerosToEnd(rowFour, len(rowFour))
        shiftedGrid = rowOne + rowTwo + rowThree + rowFour
        
        shiftedGrid = addTwoOrFour(shiftedGrid)
        status = getStatus(shiftedGrid)
        shiftedGrid = toString(shiftedGrid)
        integrity = _determineHash(shiftedGrid)
        
        userOperation['grid'] = shiftedGrid
        result = {'grid': shiftedGrid, 'score': str(oldScore), 
              'integrity': integrity.upper(), 'status': status}
        return result
    
    elif direction == "up": #52
        colOne = [dupGrid[0], dupGrid[4], dupGrid[8], dupGrid[12]]
        colTwo = [dupGrid[1], dupGrid[5], dupGrid[9], dupGrid[13]]
        colThree = [dupGrid[2], dupGrid[6], dupGrid[10], dupGrid[14]]
        colFour = [dupGrid[3], dupGrid[7], dupGrid[11], dupGrid[15]]
        cols = [colOne, colTwo, colThree, colFour]
        
        nextGrid = [list(filter(None, i))+([0]*i.count(0)) for i in cols]
        lastGrid = [i for b in nextGrid for i in b]
        (finalGrid, oldScore) = merge(lastGrid,oldScore)
        shiftedGrid = [finalGrid[0], finalGrid[4],finalGrid[8],finalGrid[12],finalGrid[1],finalGrid[5],
                       finalGrid[9],finalGrid[13],finalGrid[2],finalGrid[6],finalGrid[10],finalGrid[14],
                       finalGrid[3],finalGrid[7],finalGrid[11],finalGrid[15]]
        
        shiftedGrid = addTwoOrFour(shiftedGrid)
        status = getStatus(shiftedGrid)
        shiftedGrid = toString(shiftedGrid)
        integrity = _determineHash(shiftedGrid)
        
        userOperation['grid'] = shiftedGrid
        userOperation['score'] = oldScore
        userOperation['integrity'] = integrity
        
        result = {'grid': shiftedGrid, 'score': str(oldScore), 
              'integrity': integrity.upper(), 'status': status}
        return result
    
    elif direction == "down":
        colOne = [dupGrid[0], dupGrid[4], dupGrid[8], dupGrid[12]]
        colTwo = [dupGrid[1], dupGrid[5], dupGrid[9], dupGrid[13]]
        colThree = [dupGrid[2], dupGrid[6], dupGrid[10], dupGrid[14]]
        colFour = [dupGrid[3], dupGrid[7], dupGrid[11], dupGrid[15]]
        cols = [colOne, colTwo, colThree, colFour]
        
        nextGrid = [list(filter(None, i))+([0]*i.count(0)) for i in cols]
        lastGrid = [i for b in nextGrid for i in b]
        (finalGrid, oldScore) = merge(lastGrid,oldScore)
        
        rowOne = [finalGrid[0], finalGrid[1], finalGrid[2], finalGrid[3]]
        rowOne = pushNonZerosToEnd(rowOne, len(rowOne))
        rowTwo = [finalGrid[4],finalGrid[5],finalGrid[6],finalGrid[7]]
        rowTwo = pushNonZerosToEnd(rowTwo, len(rowTwo))
        rowThree = [finalGrid[8], finalGrid[9], finalGrid[10], finalGrid[11]]
        rowThree = pushNonZerosToEnd(rowThree, len(rowThree))
        rowFour = [finalGrid[12], finalGrid[13], finalGrid[14], finalGrid[15]]
        rowFour = pushNonZerosToEnd(rowFour, len(rowFour))
        rows = [rowOne, rowTwo, rowThree, rowFour]
        lGrid = [i for b in rows for i in b]
        
        shiftedGrid = [lGrid[0], lGrid[4],lGrid[8],lGrid[12],lGrid[1],lGrid[5],
                       lGrid[9],lGrid[13],lGrid[2],lGrid[6],lGrid[10],lGrid[14],
                       lGrid[3],lGrid[7],lGrid[11],lGrid[15]]
        
        shiftedGrid = addTwoOrFour(shiftedGrid)
        status = getStatus(shiftedGrid)
        shiftedGrid = toString(shiftedGrid)
        integrity = _determineHash(shiftedGrid)
        
        userOperation['grid'] = shiftedGrid
        userOperation['score'] = oldScore
        userOperation['integrity'] = integrity
        
        result = {'grid': shiftedGrid, 'score': str(oldScore), 
              'integrity': integrity.upper(), 'status': status}
        return result
    
    else: #down
        colOne = [dupGrid[0], dupGrid[4], dupGrid[8], dupGrid[12]]
        colTwo = [dupGrid[1], dupGrid[5], dupGrid[9], dupGrid[13]]
        colThree = [dupGrid[2], dupGrid[6], dupGrid[10], dupGrid[14]]
        colFour = [dupGrid[3], dupGrid[7], dupGrid[11], dupGrid[15]]
        cols = [colOne, colTwo, colThree, colFour]
        nextGrid = [list(filter(None, i))+([0]*i.count(0)) for i in cols]
        lastGrid = [i for b in nextGrid for i in b]
        (finalGrid, oldScore) = merge(lastGrid,oldScore)
        
        rowOne = [finalGrid[0], finalGrid[1], finalGrid[2], finalGrid[3]]
        rowOne = pushNonZerosToEnd(rowOne, len(rowOne))
        rowTwo = [finalGrid[4],finalGrid[5],finalGrid[6],finalGrid[7]]
        rowTwo = pushNonZerosToEnd(rowTwo, len(rowTwo))
        rowThree = [finalGrid[8], finalGrid[9], finalGrid[10], finalGrid[11]]
        rowThree = pushNonZerosToEnd(rowThree, len(rowThree))
        rowFour = [finalGrid[12], finalGrid[13], finalGrid[14], finalGrid[15]]
        rowFour = pushNonZerosToEnd(rowFour, len(rowFour))
        rows = [rowOne, rowTwo, rowThree, rowFour]
        lGrid = [i for b in rows for i in b]
        
        shiftedGrid = [lGrid[0], lGrid[4],lGrid[8],lGrid[12],lGrid[1],lGrid[5],
                       lGrid[9],lGrid[13],lGrid[2],lGrid[6],lGrid[10],lGrid[14],
                       lGrid[3],lGrid[7],lGrid[11],lGrid[15]]

        shiftedGrid = addTwoOrFour(shiftedGrid)
        status = getStatus(shiftedGrid)
        shiftedGrid = toString(shiftedGrid)
        integrity = _determineHash(shiftedGrid)
        
        userOperation['grid'] = shiftedGrid
        userOperation['score'] = oldScore
        userOperation['integrity'] = integrity
        
        result = {'grid': shiftedGrid, 'score': str(oldScore), 
              'integrity': integrity.upper(), 'status': status}
        return result
    
# Combine tiles shifted in the same direction that have a equal numerical value
def merge(grid,oldScore): #106
    oldScore = int(oldScore)
    for i in range(len(grid)):
        if i != 15 and grid[i] != 0 and i % 4 != 3 and grid[i] == grid[i+1]:
                grid[i] = int(grid[i]) * 2
                grid[i+1] = 0
                oldScore += int(grid[i])
    return grid, oldScore
       
# Adds a two or four of equal probability to an empty tile on the shifted grid
def addTwoOrFour(shiftedGrid):
    twoOrFour = random.randint(0,99)
    indexes = []
    for x in range(16):
        if shiftedGrid[x] == 0:
            indexes.append(x)
    zeros = len(indexes)
    ran = random.randint(0,zeros)
    if twoOrFour >= 0 and twoOrFour <= 49:
        y = indexes[ran]
        shiftedGrid[y] = 2
    else:
        y = indexes[ran]
        shiftedGrid[y] = 4 
    return shiftedGrid
# Convert List to string
def toString(grid):
    gridString = ""
    for x in grid:
        gridString += str(x)
    return gridString
 
def _determineHash(gridString):
    myHash = hashlib.sha256() # Create hash object
    myHash.update(gridString.encode()) # Encode data and update
    myHashDigest = myHash.hexdigest()  # Put the encoded data in hexadecimal format
    return myHashDigest

def getStatus(grid):
    status = "lose"
    for x in grid:
        if x == 0:
            status = "ok"
        if x == 2048:
            status = "win"
            break
    return status

def numConcat(str1, str2):
    str1 += str2
    return str1

def pushZerosToEnd(grid, n):
    count = 0
    for i in range(n):
        if grid[i] != 0:
            grid[count] = grid[i]
            count += 1
    while count < n:
        grid[count] = 0
        count += 1
    return grid 

def pushNonZerosToEnd(grid, n):
    count = 0
    x = 0
    dupArr = []
    for i in range(n):
        if grid[i] == 0:
            grid[count] = 0
            count += 1
        else:
            dupArr.append(grid[i])
    while count < n:
        grid[count] = dupArr[x]
        count += 1
        x += 1
    return grid    

def _check_missing(userParms):
    if "grid" not in userParms:
        return "error: missing grid"
    if "score" not in userParms:
        return "error: missing score";
    if "direction" not in userParms:
        return "error: missing direction";
    if "integrity" not in userParms:
        return "error: missing integrity";
    