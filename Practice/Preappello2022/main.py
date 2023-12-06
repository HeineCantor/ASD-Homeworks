testProblem = [[8,5,3,2], [3,4,7,6]]
associationList = []

dp = []
counter = 0

def findMaxLinks(sourceList, destinationList):
    for i in range(len(associationList)):
        tmpList = []
        for j in range(len(sourceList)):
            tmpList.append(-1)
        dp.append(tmpList)

    print(dp)

if __name__ == "__main__":
    sourceList = testProblem[0]
    destinationList = testProblem[1]

    for pair in zip(testProblem[0], testProblem[1]):
        associationList.append(pair)

    sourceList.sort()
    destinationList.sort()

    findMaxLinks(sourceList, destinationList)