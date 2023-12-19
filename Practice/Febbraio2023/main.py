def optimizeDeC(pivots, i, j, dp):
    filteredPivots = [p for p in pivots if i < p < j]

    if not any(filteredPivots):
        return 0

    if(dp[i][j] != -1):
        return dp[i][j]

    minimumCost = float("inf")

    for pivot in filteredPivots:
        minimumCost = min(
            minimumCost,
            (j-i) + optimizeDeC(pivots, i, pivot, dp) + optimizeDeC(pivots, pivot, j, dp)
        )

    dp[i][j] = minimumCost
    return dp[i][j]

def optimizedDeC_BottomUp():
    pass

def getSolution(pivots, elementCount):
    dp = [
        [-1 for _ in range(elementCount+1)]
        for _ in range(elementCount+1)
    ]

    return optimizeDeC(pivots, 0, elementCount, dp)

print(getSolution([2, 20, 25], 30))
print(getSolution([4, 5, 7, 8], 10))
print(getSolution([25, 50, 75], 100))