# -------------------ATTENZIONE---------------------------
# 
# La descrizione dettagliata dell'algortimo e 
# dell'analisi di complessità si trovano nel PDF.
# 
# --------------------------------------------------------

# Funzione Merge modificata - θ(n)
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

# Funzione Merge Sort modificata - θ(n log(n))
def inversionCount(array, start, end):
    inversions = 0

    if start < end:
        middle = (start + end) // 2

        inversions += inversionCount(array, start, middle)
        inversions += inversionCount(array, middle+1, end)
        inversions += mergeAndCount(array, start, middle, end)

    return inversions

# Funzione di lettura da file dei casi di test
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

# Main
if __name__ == "__main__":
    testList = readTestFile("./test.txt")
    
    for test in testList:
        inversions = inversionCount(test, 0, len(test) - 1)
        #print(f"Number of inversions for {test}: {inversions}")
        print(inversions)
