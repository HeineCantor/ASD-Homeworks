testLabyrinth=[
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
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

def printSolution(solutionPath):
    pass

def isSolutionValid(path, labyrinth, start, exit):
    return start == exit

def buildCandidates(path, labyrinth, start, exit):
    xCoordinate = start[0]
    yCoordinate = start[1]
    
    candidates = []

    if(xCoordinate+1 < len(labyrinth)-1):
        if(labyrinth[yCoordinate][xCoordinate+1] == 1):
            candidates.append((xCoordinate+1, yCoordinate))
    if(yCoordinate+1 < len(labyrinth)-1):
        if(labyrinth[yCoordinate+1][xCoordinate] == 1):
            candidates.append((xCoordinate, yCoordinate+1))

    return candidates

def labyrinthBacktrack(path, labyrinth, start, exit):
    cadidatesForNextMove = []

    if(isSolutionValid(labyrinth, start, exit)):
        printSolution(path)
    else:
        start += 1
        candidatesForNextMove = buildCandidates(path, labyrinth, start, exit)
        for candidate in candidatesForNextMove:
            path.append(candidate)
            labyrinthBacktrack(path, labyrinth, start, exit)


if __name__ == "__main__":
    print("Labyrinth to solve:")
    printLabyrinth(testLabyrinth)

    labyrinthSize = len(testLabyrinth)
    path = []

    labyrinthBacktrack(path, testLabyrinth, (0, 0), (labyrinthSize - 1, labyrinthSize - 1))
