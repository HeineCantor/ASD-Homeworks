# def findMaxCoins(nums, i, j , dp):
#     if i+1==j:
#         return 0

#     maxBurstCost = 0
#     for k in range(i+2, j):
#         maxBurstCost = max(
#             maxBurstCost,
#             findMaxCoins(nums, i, k, dp) + findMaxCoins(nums, k, j, dp) + nums[i]*nums[k]*nums[j]
#         )

#     return maxBurstCost

def maxCoins(nums) -> int:
    nums = [1] + nums + [1]
    n = len(nums)

    dp = [
        [-1 for _ in range(len(nums))]
        for _ in range(len(nums))
    ]
    
    for i in range(1, n-1):


print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))