array=[1,2,3,9,3,4,1,6,7,8,9,2,3,4,5,6,23,5,6,4,5,5,1,2,3,4,6,7,8,9,3,2,4,5,6,2,1,67,900]
totalSum = sum(array)
dp = [[-1 for _ in range(totalSum  + 1)] for _ in range(len(array) + 1)]


def minPart(array,i,firstSum,secondSum):
    
    if i==len(array):
        return abs(firstSum - secondSum)
    
    if dp[i][abs(firstSum-secondSum)] !=-1:
        return dp[i][abs(firstSum-secondSum)]

    a= minPart(array,i+1,firstSum + array[i], secondSum)
    b= minPart(array,i+1,firstSum, secondSum + array[i])

    dp[i][(abs(firstSum-secondSum))]=min(a,b)
    return dp[i][abs(firstSum-secondSum)]


if __name__=="__main__":
    print(minPart(array,0,0,0))
