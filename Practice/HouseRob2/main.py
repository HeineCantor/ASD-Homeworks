def findMaximalRob(nums, dp, n, i=0):
    if i > n:
        return 0

    if(dp[i] != -1):
        return dp[i]

    takeHouse = findMaximalRob(nums, dp, n, i+2) + nums[i]
    notTakeHouse = findMaximalRob(nums, dp, n, i+1)

    dp[i] = max(takeHouse, notTakeHouse)
    return dp[i]

def rob(nums) -> int:
    dp = [-1 for _ in range(len(nums))]
    maximalRob1 = findMaximalRob(nums, dp, len(nums)-2, 0)

    dp = [-1 for _ in range(len(nums))]
    maximalRob2 = findMaximalRob(nums, dp, len(nums)-2, 1)
    print(maximalRob1)
    print(maximalRob2)
    return max(maximalRob1, maximalRob2)

print(rob([1, 2, 3]))