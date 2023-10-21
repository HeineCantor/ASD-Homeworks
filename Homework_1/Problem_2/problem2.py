def commonPrefix(string1, string2):
    prefix = ""

    minLength = min(len(string1), len(string2))

    i = 0

    while i < minLength and string1[i] == string2[i]:
        prefix += string1[i]
        i += 1

    return prefix

def findPrefix(array, start, end):
    if start == end:
        return array[start]
    
    if(end > start):
        middle = (start + end) // 2

        s1 = findPrefix(array, start, middle)
        s2 = findPrefix(array, middle+1, end)
        return commonPrefix(s1, s2)

    return ""

def readTestFile(testPath):
    testFile = open(testPath)
    testList = []

    numberOfTests = int(testFile.readline())

    tempList = []

    for line in testFile:
        if line.strip() == "0":
            testList.append(tempList)
            tempList = []
        else:
            tempList.append(line.strip())

    return testList

if __name__ == "__main__":
    testList = readTestFile("./testfile.txt")
    
    for test in testList:
        lcp = findPrefix(test, 0, len(test) - 1)
        print(lcp)