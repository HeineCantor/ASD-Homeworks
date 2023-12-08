TRIANGLE = [[2],[3,4],[6,5,7],[4,1,8,3]]
TRIANGLE = [[-1],[-2,-3]]
TRIANGLE = [[-1],[2,3],[1,-1,-3]]

def minimumTotal(triangle):
    lastRow = triangle[0]

    for i in range(1, len(triangle)):
        currentRow = [-1]*(i+1)
        currentRow[0] = triangle[i][0] + lastRow[0]
        for j in range(1,len(currentRow)-1):
            currentRow[j] = triangle[i][j] + min(lastRow[j], lastRow[j-1])
        currentRow[-1] = triangle[i][-1] + lastRow[-1]

        lastRow = currentRow
    
    return min(lastRow)

if __name__ == "__main__":
    print(minimumTotal(TRIANGLE))