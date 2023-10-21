def mergeAndCount(array, start, mid, end):
    leftList = []
    rightList = []

    for i in range(mid - start + 1):
        leftList.append(array[start + i])
    for j in range(end - mid):
        rightList.append(array[mid + 1 + j])

    i = j = 0

    inversions = 0
    counted = False

    for k in range(start, end+1):
        if i < len(leftList) and j < len(rightList):
            if not counted and rightList[j] < leftList[i]:
                inversions += len(leftList) - i
                counted = True
            if leftList[i] <= rightList[j]:
                array[k] = leftList[i]
                i += 1
            else:
                array[k] = rightList[j]
                j += 1
                counted = False
        else:
            if i < len(leftList):
                array[k] = leftList[i]
                i += 1
            else:
                array[k] = rightList[j]
                j += 1

    return inversions

def inversionCount(array, start, end):
    inversions = 0

    if start < end:
        middle = (start + end) // 2

        inversions += inversionCount(array, start, middle)
        inversions += inversionCount(array, middle+1, end)
        inversions += mergeAndCount(array, start, middle, end)

    return inversions

def readTestFile(testPath):
    testFile = open(testPath)
    testsList = []

    readTestStart = True
    testLineCounter = 0
    tempTestList = []

    for line in testFile:
        if readTestStart:
            readTestStart = False
            testLineCounter = int(line)
        else:
            tempTestList.append(int(line))
            testLineCounter -= 1
            if testLineCounter == 0:
                readTestStart = True
                testsList.append(tempTestList)
                tempTestList = []

    return testsList

if __name__ == "__main__":
    testList = readTestFile("./problem1_testcase_1.txt")
    
    for test in testList:
        inversions = inversionCount(test, 0, len(test) - 1)
        #print(f"Number of inversions for {test}: {inversions}")
        print(inversions)
