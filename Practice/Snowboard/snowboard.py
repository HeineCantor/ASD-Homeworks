snowboardArea = [
    [ 1,  2,  3,  4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]

feldbergTest = [
    [56, 14, 51, 58, 88],
    [26, 94, 24, 39, 41],
    [24, 16, 8, 51, 51],
    [76, 72, 77, 43, 10],
    [38, 50, 59, 84, 81],
    [5, 23, 37, 71, 77],
    [96, 10, 93, 53, 82],
    [94, 15, 96, 69, 9],
    [74, 0, 62, 38, 96],
    [37, 54, 55, 82, 38]
]

def isAValidSolution(snowboard, path, k):
    if k == 0:
        return False

    lastCell = path[k-1]
    
    xCoordinate = lastCell[0]
    yCoordinate = lastCell[1]

    lastCellValue = snowboard[yCoordinate][xCoordinate]

    # if around you there are only greater values
    neighborCells = []
    if(xCoordinate > 0):
        neighborCells.append(snowboard[yCoordinate][xCoordinate-1])
    if(xCoordinate < len(snowboard[0])-1):
        neighborCells.append(snowboard[yCoordinate][xCoordinate + 1])
    if(yCoordinate > 0):
        neighborCells.append(snowboard[yCoordinate - 1][xCoordinate])
    if(yCoordinate < len(snowboard[0])-1):
        neighborCells.append(snowboard[yCoordinate+1][xCoordinate])
    
    if(all(x >= lastCellValue for x in neighborCells)):
        return True

    return False

def buildCandidates(snowboard, path, k):
    candidates = []

    if(k-1 == 0):
        for i in range(len(snowboard)):
            for j in range(len(snowboard[0])):
                candidates.append((j, i))
    else:
        lastCell = path[k-2]
        
        xCoordinate = lastCell[0]
        yCoordinate = lastCell[1]

        lastCellValue = snowboard[yCoordinate][xCoordinate]

        if(xCoordinate > 0 and snowboard[yCoordinate][xCoordinate-1] < lastCellValue):
            candidates.append((xCoordinate-1, yCoordinate))
        if(xCoordinate < len(snowboard[0])-1 and snowboard[yCoordinate][xCoordinate + 1] < lastCellValue):
            candidates.append((xCoordinate+1, yCoordinate))
        if(yCoordinate > 0 and snowboard[yCoordinate - 1][xCoordinate] < lastCellValue):
            candidates.append((xCoordinate, yCoordinate-1))
        if(yCoordinate < len(snowboard[0])-1 and snowboard[yCoordinate+1][xCoordinate] < lastCellValue):
            candidates.append((xCoordinate, yCoordinate+1))

    return candidates

def snowboardBacktrack(snowboard, path, k):
    longestPathLength = 0

    if isAValidSolution(snowboard, path, k):
        #print(path)
        return len(path)
    else:
        k+=1
        candidates = buildCandidates(snowboard, path, k)
        for candidate in candidates:
            path.append(candidate)
            longestPathLength = max(snowboardBacktrack(snowboard, path, k), longestPathLength)
            path.pop()

    return longestPathLength

if __name__ == "__main__":
    path = []
    lengthOfLongestPath = snowboardBacktrack(feldbergTest, path, 0)
    print(f"Longest snowboard path length: {lengthOfLongestPath}")