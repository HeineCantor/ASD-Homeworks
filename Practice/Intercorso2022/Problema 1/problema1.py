def countOccurences(sequence, start, end, valueToCheck):
    if(start == end):
        return int(sequence[start] == valueToCheck)

    mid = (start + end) // 2

    c1 = countOccurences(sequence, start, mid, valueToCheck)
    c2 = countOccurences(sequence, mid + 1, end, valueToCheck)

    return c1 + c2

def readTestFile(testFilePath):
    file = open(testFilePath, "r")
    testNumber = int(file.readline())
    testsList = []
    for i in range(testNumber):
        line = file.readline()
        testsList.append([int(x) for x in line.split(' ')])

    return (testNumber, testsList)

if __name__ == "__main__":
    testNumber, testList = readTestFile(testFilePath="./test_file.txt")
    for test in testList:
        valueToCount = test[0]
        valueListToCheck = test[1:]
        numberOfOccurences = countOccurences(valueListToCheck, 0, len(valueListToCheck) - 1, valueToCount)
        #print(f"Number of occurences of {valueToCount} is: {numberOfOccurences}")
        print(numberOfOccurences)