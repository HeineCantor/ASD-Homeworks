def findMaximalRectangle(matrix, topLeft, bottomRight, dp):
    if (topLeft == bottomRight):
        return matrix[bottomRight[1]][bottomRight[0]]

    if(topLeft[0]>bottomRight[0] or topLeft[1]>bottomRight[1]):
        return 0

    topSubrect = findMaximalRectangle(matrix, topLeft, (bottomRight[0], bottomRight[1]-1), dp)
    leftSubrect = findMaximalRectangle(matrix, topLeft, (bottomRight[0]-1, bottomRight[1]), dp)

    topSubrectIsMaximal = topSubrect == (bottomRight[0]-topLeft[0]+1)*(bottomRight[1]-topLeft[1])
    leftSubrectIsMaximal = leftSubrect == (bottomRight[0]-topLeft[0])*(bottomRight[1]-topLeft[1]+1)

    if(matrix[bottomRight[1]][bottomRight[0]] == 1 and
        topSubrectIsMaximal and leftSubrectIsMaximal): # this is a rectangle
        return (bottomRight[0]-topLeft[0]+1)*(bottomRight[1]-topLeft[1]+1)

    rightSubrect = findMaximalRectangle(matrix, (topLeft[0]+1, topLeft[1]), bottomRight, dp)
    bottomSubrect = findMaximalRectangle(matrix, (topLeft[0], topLeft[1]+1), bottomRight, dp)

    dp[topLeft][bottomRight] = max(topSubrect, leftSubrect, rightSubrect, bottomSubrect)
    return dp[topLeft][bottomRight]

def maximalRectangle(matrix):
    width = len(matrix[0])
    height = len(matrix)

    allPossibleCoords = {}

    for i in range(width):
        for j in range(height):
            allPossibleCoords[(i, j)] = -1

    dp = {
        key:allPossibleCoords for key in allPossibleCoords
    }

    matrix = [
        [int(cell) for cell in row] for row in matrix
    ]

    return findMaximalRectangle(matrix, (0, 0), (width-1, height-1), dp)


if __name__ == "__main__":
    TEST = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(maximalRectangle(TEST))