dp={}

def coinChange(coins,value,i):
    
    if i>=len(coins):
        dp[(i,value)] = float('inf')
        return float('inf')
    
    if value<0:
        dp[(i,value)] = float('inf')
        return float('inf')
    
    if value==0:
        dp[(i,value)] = 0
        return dp[(i,value)]
    
    if (i,value) in dp:
        return dp[(i,value)]

    a = 1 + coinChange(coins,value-coins[i],i)
    b = coinChange(coins,value,i+1)
    dp[(i,value)] = min(a,b)
    return min(a,b)


coins=[1,2]
amount=6
print(coinChange(coins,amount,0))


coins=[1,2,3,4,5,6,7,8,9,13,45,85,134,6,67]
amount=50
print(coinChange(coins,amount,0))
