NEGATIVE_INFINITY = -1e10

def maxCrossSum(array, start, middle, end):
    
    tmpSum = 0

    leftCrossingSum = NEGATIVE_INFINITY
    rightCrossingSum = NEGATIVE_INFINITY

    for i in range(middle, -1, -1):
        tmpSum += array[i]
        leftCrossingSum = max(leftCrossingSum, tmpSum)

    tmpSum = 0

    for i in range(middle, end+1):
        tmpSum += array[i]
        rightCrossingSum = max(rightCrossingSum, tmpSum)

    return max(leftCrossingSum + rightCrossingSum - array[middle], leftCrossingSum, rightCrossingSum)


def maxContigousSum(array, start, end):
    if(start == end):
        return array[start]
    
    middle = (start + end) // 2

    leftSum = maxContigousSum(array, start, middle)
    rightSum = maxContigousSum(array, middle+1, end)
    crossSum = maxCrossSum(array, start, middle, end)

    return max(leftSum, rightSum, crossSum)

def readTestFile(testPath):
    testFile = open(testPath)
    testList = []

    tmpList = []

    for line in testFile:
        if(line == "END"):
            break
        tmpList = []
        for element in line.split(' '):
            tmpList.append(int(element))
        testList.append(tmpList)

    return testList

if __name__ == "__main__":
    testList = readTestFile("./test.txt")

    for test in testList:
        maximumSum = maxContigousSum(test, 0, len(test)-1)
        print(maximumSum)