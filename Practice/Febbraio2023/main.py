def optimizeDeC(pivots, i, j, dp):
    filteredPivots = [p for p in pivots if i < p < j]
    if(not any(filteredPivots)):
       return 0

    if(dp[i][j] != -1):
        return dp[i][j]

    minimumCost = (j-i) + optimizeDeC(pivots, i, filteredPivots[0], dp) + optimizeDeC(pivots, filteredPivots[0], j, dp)

    for k in range(1, len(filteredPivots)):
        minimumCost = min(
            minimumCost,
            (j-i) + optimizeDeC(pivots, i, filteredPivots[k], dp) + optimizeDeC(pivots, filteredPivots[k], j, dp)
        )

    dp[i][j] = minimumCost
    return dp[i][j]

def getSolution(pivots, elementCount):
    dp = [
        [-1 for _ in range(elementCount+1)]
        for _ in range(elementCount+1)
    ]

    return optimizeDeC(pivots, 0, elementCount, dp)

print(getSolution([2, 20, 25], 30))
print(getSolution([4, 5, 7, 8], 10))
print(getSolution([25, 50, 75], 100))