def findMaxSubarray(nums, n, dp):
    if(n == 0):
        return nums[n]

    maximum = None

    for i in range(n-1):
        iMaximum = findMaxSubarray(nums, i, dp)

        if maximum is None or iMaximum > maximum:
            maximum = iMaximum
    
    if maximum is None:
        maximum = 0

    if nums[n-1] + maximum > maximum:
        maximum += nums[n-1]

    return maximum

def maxSubArray(nums):
    dp = [-1]*len(nums)

    return findMaxSubarray(nums, len(nums)-1, dp)

if __name__ == "__main__":
    testArray = [-2,1,-3,4,-1,2,1,-5,4]
    
    print(maxSubArray(testArray))