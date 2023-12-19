def maxRob(nums, n, dp):
    if(n == 0):
        return nums[n]

    if(dp[n] != -1):
        return dp[n]

    maximumRob = max(maxRob(nums, n-1, dp), nums[n])

    for i in range(n-1):
        maximumRob = max(
            maximumRob,
            nums[n] + maxRob(nums, i, dp)
        )
    
    dp[n] = maximumRob
    return maximumRob

def rob(nums):
    dp = [-1 for _ in range(len(nums))]

    return maxRob(nums, len(nums)-1, dp)