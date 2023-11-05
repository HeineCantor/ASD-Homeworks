testMatrix = [
    [1, 2, 3],
    [4, 5, 6]
]

testMatrix2 = [
    [1, 2],
    [3, 4]
]

def isSolutionValid(matrix, path, k):
    if(k==0):
        return False

    if(path[k-1] == (len(matrix[0])-1, len(matrix)-1)):
        return True
    
    return False

def buildCandidates(matrix, path, k):
    candidates = []

    if(k-1 == 0):
        candidates.append((0, 0))
    else:
        xCoordinate = path[k-2][0]
        yCoordinate = path[k-2][1]

        if(yCoordinate < len(matrix)):
            candidates.append((xCoordinate, yCoordinate + 1))
        if(xCoordinate < len(matrix[0])):
            candidates.append((xCoordinate + 1, yCoordinate))
            
    return candidates

def printPathSolution(matrix, path):
    for element in path:
        print(f"{matrix[element[1]][element[0]]} ", end="")

    print("")

def allPossiblePaths(matrix, path, k):
    if(isSolutionValid(matrix, path, k)):
        printPathSolution(matrix, path)
    else:
        k+=1
        candidates = buildCandidates(matrix, path, k)
        for candidate in candidates:
            path.append(candidate)
            allPossiblePaths(matrix, path, k)
            path.pop()
    

if __name__ == "__main__":
    path = []
    allPossiblePaths(testMatrix2, path, 0)