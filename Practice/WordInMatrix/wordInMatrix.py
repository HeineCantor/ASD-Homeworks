testMatrix = [
    ['t', 'z', 'x', 'c', 'd'],
    ['a', 'h', 'n', 'o', 'x'],
    ['h', 'w', 'e', 'l', 'o'],
    ['o', 'r', 'n', 'l', 'n'],
    ['a', 'b', 'r', 'i', 'n'],
]

testMatrix2 = [
    ["r", "t", "r"],
    ["o", "a", "r"]
]

def printPath(path):
    for step in path:
        print(f"{step[0]+1} {step[1]+1}")

    print("===")

def isAValidSolution(matrix, path, k, targetWord):
    if(k == 0):
        return False

    xCoord = path[k-1][0]
    yCoord = path[k-1][1]

    if(k == len(targetWord) and matrix[yCoord][xCoord] == targetWord[-1]):
        return True
    
    return False

def buildCandidates(matrix, path, k, targetWord):
    candidates = []

    if(k == 1):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == targetWord[0]):
                    candidates.append((i, j))
    else:
        xCoord = path[k-2][0]
        yCoord = path[k-2][1]

        nextCharacter = targetWord[k-1]

        if(xCoord > 0):
            if(matrix[yCoord][xCoord-1] == nextCharacter):
                candidates.append((xCoord-1, yCoord))
            if(yCoord > 0 and matrix[yCoord-1][xCoord-1] == nextCharacter):
                candidates.append((xCoord-1, yCoord-1))
            if(yCoord < len(matrix)-1 and matrix[yCoord+1][xCoord-1] == nextCharacter):
                candidates.append((xCoord-1, yCoord+1))

        if(xCoord < len(matrix[0])-1):
            if(matrix[yCoord][xCoord+1] == nextCharacter):
                candidates.append((xCoord+1, yCoord))
            if(yCoord > 0 and matrix[yCoord-1][xCoord+1] == nextCharacter):
                candidates.append((xCoord+1, yCoord-1))
            if(yCoord < len(matrix)-1 and matrix[yCoord+1][xCoord+1] == nextCharacter):
                candidates.append((xCoord+1, yCoord+1))

        if(yCoord > 0):
            if(matrix[yCoord-1][xCoord] == nextCharacter):
                candidates.append((xCoord, yCoord-1))
            
        if(yCoord < len(matrix)-1):
            if(matrix[yCoord+1][xCoord] == nextCharacter):
                candidates.append((xCoord, yCoord+1))

    return candidates

def wordBacktrack(matrix, path, k, targetWord):
    if(isAValidSolution(matrix, path, k, targetWord)):
        printPath(path)
    elif k<len(targetWord):
        k+=1
        candidates = buildCandidates(matrix, path, k, targetWord)
        for candidate in candidates:
            path.append(candidate)
            wordBacktrack(matrix, path, k, targetWord)
            path.pop()

if __name__ == "__main__":
    wordToSearch = "hello"
    path = []
    wordBacktrack(testMatrix, path, 0, wordToSearch)

    path = []
    wordToSearch="ora"
    wordBacktrack(testMatrix2, path, 0, wordToSearch)