staircase = {1: 1, 2: 2, 3: 3}


def numPaths(n):
    if n in staircase.keys():
        return staircase[n]
    else:
        staircase[n] = (staircase[n - 1] + staircase[n - 2] + staircase[n - 3])
        return staircase[n]
