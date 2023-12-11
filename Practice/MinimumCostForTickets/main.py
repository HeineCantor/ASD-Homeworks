from math import ceil

def findMinCostTickets(days, costs, n, dp):
    if n==0:
        return 0

    minimum = 10e3+1

    for i in range(n):
        difference = days[n] - days[i]
        if(difference <= 30):
            costToDayi = findMinCostTickets(days, costs, i, dp)
            minimum = min(
                minimum,
                costToDayi + difference*costs[0],
                costToDayi + ceil(difference/7)*costs[1],
                costToDayi + ceil(difference/30)*costs[2]
            )

    dp[n] = minimum
    return minimum

def mincostTickets(days, costs):
    dp = [-1 for _ in range(len(days))]

    mincost = findMinCostTickets(days, costs, len(days)-1, dp)
    print(dp)
    return mincost
    
if __name__ == "__main__":
    days = [1,4,6,7,8,20]
    costs = [2, 7, 15]

    print(mincostTickets(days, costs))