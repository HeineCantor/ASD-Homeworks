POSITIVE_INFINITY = 9e10

def minimumDistanceFromSum(array, n, cumulativeSum, totalSum, dp):
    if(n == 0):
        return abs(totalSum - 2*cumulativeSum)
    
    if(dp[n-1][cumulativeSum] != -1):
        return dp[n-1][cumulativeSum]

    minimumIncludingElement = minimumDistanceFromSum(array, n-1, cumulativeSum+array[n-1], totalSum, dp)
    minimumExcludingElement = minimumDistanceFromSum(array, n-1, cumulativeSum, totalSum, dp)

    dp[n-1][cumulativeSum] = min(minimumExcludingElement, minimumIncludingElement)

    return dp[n-1][cumulativeSum]

def findMinimumDistanceFromSum(array):
    arraySum = sum(array)
    arrayLength = len(array)

    dp = [
        [-1 for _ in range(arraySum+1)]
        for _ in range(arrayLength + 1)
    ]

    minimumSum = minimumDistanceFromSum(array, arrayLength, 0, arraySum, dp)

    return minimumSum

def readTestFile(testPath):
    testFile = open(testPath)

    numTests = int(testFile.readline())

    testList = []

    for i in range(numTests):
        testFile.readline() # useless line for values number
        testList.append([int(x) for x in testFile.readline().strip().split(' ')])

    return testList


if __name__ == "__main__":
    testList = readTestFile("test.txt")

    for test in testList:
        print(findMinimumDistanceFromSum(test))