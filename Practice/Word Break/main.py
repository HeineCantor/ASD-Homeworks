def getWordDistance(originalWord, testWord):
    shortestLength = min(len(originalWord), len(testWord))

    difference = len(originalWord) - shortestLength

    for i in range(shortestLength):
        if(originalWord[i] != testWord[i]):
            difference += 1

    return difference

def getMinimumDistanceWord(originalWord, testWord1, testWord2):
    distance1 = getWordDistance(originalWord, testWord1)
    distance2 = getWordDistance(originalWord, testWord2)

    if distance1 < distance2:
        return testWord1
    
    return testWord2

def wordBreak(s: str, wordDict) -> bool:
    dp = [""]*(len(s)+1)

    for i in range(len(s)+1):
        minimumDistanceWord = ""
        for j in range(len(wordDict)):
            if len(wordDict[j]) <= i:
                minimumDistanceWord = getMinimumDistanceWord(s, minimumDistanceWord, dp[i-len(wordDict[j])]+wordDict[j])
        dp[i]=minimumDistanceWord

    return dp[-1]==s

if __name__ == "__main__":
    print(wordBreak("leetcode", ["leet", "code"]))
    print(wordBreak("applepenapple", ["apple", "pen"]))
    print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))