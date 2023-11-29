def lis(array):
    dp=[]
    dp=[[0,0,0]]
    max=0

    for i in range(len(array)):
        
        if array[i]>array[i-1]:
            dp.append([0,dp[0][1],1])
            
            for j in range(1,len(dp)):
                dp[j][0]=array[i]
                dp[j][1]+=array[i]
                dp[j][2]+=1


        else:
            dp[0][0]=array[i]
            dp[0][1]=array[i]
            dp[0][2]=1

    for k in range(len(dp)):
        if dp[k][2] > max:
            max=dp[k][2]
    return max



array=[10,9,2,5,3,7,101,18]
print(lis(array))
