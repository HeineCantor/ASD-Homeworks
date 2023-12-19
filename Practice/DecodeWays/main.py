TEST = "12"
TEST = "226"
TEST = "1201234"
TEST = "10"

def findNumDecodings(s, n, i, dp):
    if i==n:
        if(s[i] != '0'):
            return 1
        return 0

    if i==n-1:
        if(s[i] != '0'):
            if int(s[i:]) <= int("26"):
                if(s[i+1] != '0'):
                    return 2
                return 1
            if(s[i+1] != '0'):
                return 1
        return 0
    
    if(dp[i] != -1):
        return dp[i]

    decodeWays = 0

    if(s[i] != '0'):
        decodeWays += findNumDecodings(s, n, i+1, dp)
        if(int(s[i:i+2]) <= int("26")):
            decodeWays += findNumDecodings(s, n, i+2, dp)

    dp[i] = decodeWays
    return dp[i]

def numDecodings(s):
    dp = [-1]*len(s)

    return findNumDecodings(s, len(s)-1, 0, dp)

if __name__ == "__main__":
    print(numDecodings(TEST))