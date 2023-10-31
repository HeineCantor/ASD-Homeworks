chessboard = []

def generateChessboard(N):
    chessboard.clear()
    for i in range(N):
        row = [False for x in range(N)]
        chessboard.append(row)


def displayChessboard(chessboard):
    print("--------------------")
    for row in chessboard:
        print("|", end="")
        for cell in row:
            if(cell == True):
                print("X", end="")
            else:
                print("O", end="")
            print("|", end="")
        print("")

    print("--------------------")

def isSolutionValid(chessboard, k, n):
    if k < n:
        return False
    
    for row in chessboard:
        if not any(row):
            return False

    return True

def buildCandidates(chessboard, k, n, candidatesList):
    tempCandidates = [True for x in range(n)]

    for i in range(k-1):
        for j in range(n):
            if(chessboard[i][j]):
                tempCandidates[j] = False
                rightDiagonal = j+(k-1-i)
                leftDiagonal = j-(k-1-i)
                if(rightDiagonal < n):
                    tempCandidates[rightDiagonal] = False
                if(leftDiagonal >= 0):
                    tempCandidates[leftDiagonal] = False
                break

    candidatesList.extend(tempCandidates)

def tooManyQueensBacktrack(chessboard, k, n):
    candidatesForNextRow = []

    solutionsCount = 0

    if(isSolutionValid(chessboard, k, n)):
        displayChessboard(chessboard)
        solutionsCount += 1
    elif k < n:
        k = k + 1
        buildCandidates(chessboard, k, n, candidatesForNextRow)
        for i in range(len(candidatesForNextRow)):
            chessboard[k-1][i] = candidatesForNextRow[i]
            solutionsCount += tooManyQueensBacktrack(chessboard, k, n)
            chessboard[k-1][i] = False        

    return solutionsCount

def readTestFile(testPath):
    testFile = open(testPath)
    testList = []

    numberOfTests = int(testFile.readline())

    for line in testFile:
        testList.append(int(line))

    return testList

if __name__ == "__main__":
    testList = readTestFile("./test.txt")

    for test in testList:
        print(f"TESTING FOR {test} QUEENS.")
        generateChessboard(test)

        howManySolutions = tooManyQueensBacktrack(chessboard, 0, test)

        print(f"Solutions found: {howManySolutions}")
        print("=====================================")


    