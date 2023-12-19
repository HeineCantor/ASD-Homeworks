def findMinDistance(word1, word2, i, j, dp):
    if i == len(word1) and j == len(word2):
        return 0

    if(word1[min(i, len(word1)-1)] == word2[min(j, len(word2)-1)]):
        return findMinDistance(word1, word2, min(i+1, len(word1)), min(j+1, len(word2)), dp)

    minimum = 0

    insertion = 1e10
    deletion = 1e10
    replacement = 1e10

    if dp[i][j] != -1:
        return dp[i][j]

    if i < len(word1):
        deletion = 1 + findMinDistance(word1, word2, i+1, j, dp)
    
    if j < len(word2):
        insertion = 1 + findMinDistance(word1, word2, i, j+1, dp)

    if i < len(word1) and j < len(word2):
        replacement = 1 + findMinDistance(word1, word2, i+1, j+1, dp)

    minimum = min(insertion, deletion, replacement)

    dp[i][j] = minimum

    return minimum
    

def minDistance(word1, word2):
    dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    minimumDistance = findMinDistance(word1, word2, 0, 0, dp)
    print(dp)
    return minimumDistance

if __name__ == "__main__":
    print(minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopical"))