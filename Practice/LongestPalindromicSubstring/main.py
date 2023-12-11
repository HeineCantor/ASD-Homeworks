TEST = "babadaradanitopinonavevanonipoti"

def findLongestPalindrome(s, i, j, dp):
        if(i == j or i > j):
            dp[i][j] = (i, j)
            return (i, j)
        
        if(dp[i][j] != -1):
            return dp[i][j]

        internalPalindrome = findLongestPalindrome(s, i+1, j-1, dp)

        if(s[i] == s[j] and internalPalindrome == (i+1, j-1)):
            dp[i][j] = (i, j)
            return (i, j)

        leftPalindrome = findLongestPalindrome(s, i, j-1, dp)
        rightPalindrome = findLongestPalindrome(s, i+1, j, dp)

        if(leftPalindrome[1] - leftPalindrome[0] >= rightPalindrome[1] - rightPalindrome[0]):
            dp[i][j] = leftPalindrome
            return leftPalindrome
        else:
            dp[i][j] = rightPalindrome
            return rightPalindrome
        
def longestPalindrome(s):
    dp = [
        [-1 for _ in range(len(s))]
        for _ in range(len(s))
    ]

    palindromeRange = findLongestPalindrome(s, 0, len(s)-1, dp)

    return s[palindromeRange[0]:palindromeRange[1]+1]

if __name__ == "__main__":
     print(longestPalindrome(TEST))