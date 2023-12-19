def findMinimumJumps(nums, n, dp):
    if(n == 0):
        return 0

    minimum = 1e4+1

    for i in range(n):
        if(n - i <= nums[i]):
            tmpMinimum = 1 + findMinimumJumps(nums, i, dp)
            minimum = min(minimum, tmpMinimum)

    return minimum

def jump(nums):
    dp = [None for _ in range(len(nums))]

    return findMinimumJumps(nums, len(nums)-1, dp)


if __name__ == "__main__":
    print(jump([2, 3, 0, 1, 4]))