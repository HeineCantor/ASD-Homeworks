def isPrime(number):
    for i in range(2, number):
        if(number % i == 0):
            return False
        
    return True

def getPrimes(p, s):
    primeList = []

    for i in range(p+1, s+1):
        if(isPrime(i)):
            primeList.append(i)

    return primeList

def isSolutionValid(s, n, p, k, path):
    if(k != n):
        return False

    tmpSum = 0

    for element in path:
        tmpSum += element

    return s == tmpSum

def buildCandidates(s, n, p, k, path, primeList):
    if(len(path) > 0):
        candidates = [x for x in primeList if x > max(path)]
    else:
        candidates = primeList

    return candidates

def findPrimesSum(s, n, p, k, path, primeList):
    if(isSolutionValid(s, n, p, k, path)):
        print(path)
    elif k < n:
        k+=1
        candidates = buildCandidates(s, n, p, k, path, primeList)
        for candidate in candidates:
            path.append(candidate)
            findPrimesSum(s, n, p, k, path, primeList)
            path.pop()

if __name__ == "__main__":
    s = 63
    n = 3
    p = 5

    s = 23
    n = 3
    p = 2

    s = 17
    n = 1
    p = 5

    primesPath = []
    primeList = getPrimes(p, s)
    findPrimesSum(s, n, p, 0, primesPath, primeList)