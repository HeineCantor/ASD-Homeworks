testLabyrinth=[
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

def printLabyrinth(labyrinthMatrix):
    for row in labyrinthMatrix:
        for cell in row:
            if cell:
                print("1 ", end="")
            else:
                print("0 ", end="")
        print("")

def printSolution(solutionPath, labyrinthMatrix):
    print("LABYRINTH SOLUTION:")
    labyrinthSize = len(labyrinthMatrix)

    for i in range(labyrinthSize):
        for j in range(labyrinthSize):
            if (j, i) in solutionPath:
                print("1 ", end="")
            else:
                print("0 ", end="")
        print("")

def isSolutionValid(path, labyrinth, k, exit):
    return path[k] == exit

def buildCandidates(path, labyrinth, k, exit):
    xCoordinate = path[k-1][0]
    yCoordinate = path[k-1][1]
    
    candidates = []

    if(xCoordinate+1 < len(labyrinth)):
        if(labyrinth[yCoordinate][xCoordinate+1] == 1):
            candidates.append((xCoordinate+1, yCoordinate))
    if(yCoordinate+1 < len(labyrinth)):
        if(labyrinth[yCoordinate+1][xCoordinate] == 1):
            candidates.append((xCoordinate, yCoordinate+1))

    return candidates

def labyrinthBacktrack(path, labyrinth, k, exit):
    cadidatesForNextMove = []

    if(isSolutionValid(path, labyrinth, k, exit)):
        printSolution(path, labyrinth)
    else:
        k += 1
        candidatesForNextMove = buildCandidates(path, labyrinth, k, exit)
        for candidate in candidatesForNextMove:
            path.append(candidate)
            labyrinthBacktrack(path, labyrinth, k, exit)
            path.pop()


if __name__ == "__main__":
    print("Labyrinth to solve:")
    printLabyrinth(testLabyrinth)

    labyrinthSize = len(testLabyrinth)
    path = [(0, 0)]

    labyrinthBacktrack(path, testLabyrinth, 0, (labyrinthSize - 1, labyrinthSize - 1))
