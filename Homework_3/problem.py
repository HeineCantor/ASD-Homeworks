# -------------------ATTENZIONE---------------------------
# 
# La descrizione dettagliata dell'algortimo e 
# dell'analisi di complessità si trovano nel PDF.
# 
# --------------------------------------------------------

# Sentinella
POSITIVE_INFINITY = 9e10

# Funzione Minimum Distance From Sum (Knapasack modificato) - θ(n*totalSum) [pseudopolinomiale]
def minimumDistanceFromSum(array, n, cumulativeSum, totalSum, dp):
    if(n == 0):
        return abs(totalSum - 2*cumulativeSum)
    
    if(dp[n-1][cumulativeSum] != -1):
        return dp[n-1][cumulativeSum]

    minimumIncludingElement = minimumDistanceFromSum(array, n-1, cumulativeSum+array[n-1], totalSum, dp)
    minimumExcludingElement = minimumDistanceFromSum(array, n-1, cumulativeSum, totalSum, dp)

    dp[n-1][cumulativeSum] = min(minimumExcludingElement, minimumIncludingElement)

    return dp[n-1][cumulativeSum]

# Chiamante della funzione ricorsiva
def findMinimumDistanceFromSum(array):
    arraySum = sum(array)
    arrayLength = len(array)

    dp = [
        [-1 for _ in range(arraySum)]
        for _ in range(arrayLength)
    ]

    minimumSum = minimumDistanceFromSum(array, arrayLength, 0, arraySum, dp)

    return minimumSum

# Costruttore di test case da file
def readTestFile(testPath):
    testFile = open(testPath)

    numTests = int(testFile.readline())

    testList = []

    for i in range(numTests):
        testFile.readline() # useless line for values number
        testList.append([int(x) for x in testFile.readline().strip().split(' ')])

    return testList

# Main
if __name__ == "__main__":
    testList = readTestFile("test.txt")

    for test in testList:
        print(findMinimumDistanceFromSum(test))