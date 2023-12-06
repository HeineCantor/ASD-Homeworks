testProblem = [[8,5,3,2], [3,4,7,6]]
testProblem = [[2,5,3,9,12,4], [1,7,2,4,3,10]]
associationList = []

counter = 0

def findMaxLinks(possibleLinks : list):
    possibleLinks.sort()

    dp = [-1]*len(possibleLinks)

    return maxLinksDP(possibleLinks, len(possibleLinks)-1, dp)

'''
Spiegazione: se si ordinano le source in ordine crescente,
si otterrà un certo ordine di destination. Quelle che si
possono prendere sono solo quelle maggiori tra loro, di
conseguenza l'algoritmo si riduce a un Longest Increasing
Subset (LIS). 

Ad esempio, se ho dei collegamenti del tipo:

(8->3), (5->4), (3->7), (2->6)
ordino per destinazioni in ordine crescente:
(2->6), (3->7), (5->4), (8->3)
ed estraggo le destinazioni:
6,7,4,3

Devo quindi trovare il LIS di questa lista, che rappresenta
il maggior numero di collegamenti che non si intersecano,
perché sono tutti con S>S' and D>D'.
'''

def maxLinksDP(possibleLinks, n, dp):
    if n == 0:
        return 1

    maximum = 0
    lastGreatestValue = -1

    for i in range(n):
        if(dp[i] != -1):
            iMaximum = dp[i]
        else: 
            iMaximum = maxLinksDP(possibleLinks, i, dp)
        
        if (iMaximum > maximum):
            maximum = iMaximum
            lastGreatestValue = possibleLinks[i][1]

    if (possibleLinks[n][1] > lastGreatestValue):
        maximum += 1

    return maximum

if __name__ == "__main__":
    sourceList = testProblem[0]
    destinationList = testProblem[1]

    for pair in zip(testProblem[0], testProblem[1]):
        associationList.append(pair)

    maximumLength = findMaxLinks(associationList)

    print(maximumLength)