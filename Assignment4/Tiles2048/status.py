def _status(userParms):
    status = "lose"
    grid = userParms['grid']
    VALID_NUMS = ('0', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024')
    a = numConcat2(grid[0], grid[1], grid[2], grid[3])
    for i, x in enumerate(grid):
        if grid[i] == "0":
            status = "ok"
        if a == "2048":
            status = "win"
            break
    result = {'status': status}
    return result

def numConcat(str1, str2):
    str1 += str2
    return str1

def numConcat2(str1, str2, str3, str4):
    str1 += str2 + str3 + str4
    return str1