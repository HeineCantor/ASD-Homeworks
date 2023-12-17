TEST = [3, 5, 18]
TEST = [3, 5, 55]



def findMaximumBurgers(maxTime, minBurger, maxBurger):
    maxSteps = (maxTime // minBurger)+1

    dp = [
        [-1 for _ in range(maxTime+1)]
        for _ in range(maxSteps+1)
    ]

    for i in range(maxSteps+1):
        dp[i][0] = 0

    for j in range(maxTime+1):
        dp[0][j] = 0

    for i in range(1, maxSteps+1):
        for j in range(1, maxTime+1):
            if minBurger <= j:
                dp[i][j] = max(dp[i-1][j-minBurger]+minBurger, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

            if maxBurger <= j:
                dp[i][j] = max(dp[i-1][j-maxBurger]+maxBurger, dp[i-1][j], dp[i][j])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp)
    return dp[-1][-1]

if __name__ == "__main__":
    print(findMaximumBurgers(TEST[2], TEST[0], TEST[1]))