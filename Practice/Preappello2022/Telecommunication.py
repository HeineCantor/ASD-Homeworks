def tel(x,y):
    xy=[]
    dp = [1]*len(x)  #di base ogni elemento vale uno, essendo l'elemento stesso una "sottosequenza" più lunga

    #costruisco le tuple delle coordinate
    for i in range(len(x)):
        xy.append((x[i],y[i]))

    #ordino le tuple
    xy.sort(key=lambda x:x[0])

    for i in range(len(x)-1,-1,-1):
        for j in range(i+1,len(x)):
            #print(xy[i],xy[j],"\n") #debug
            if xy[i][0]<=xy[j][0] and xy[i][1]<=xy[j][1]:   #verifico se entrambe le coordinate di i sono entrambe minori rispetto a quelle di j
                dp[i]=max(dp[i],1+dp[j])
    return max(dp)
            
            
x=[2,5,3,9,12,4]
y=[1,7,2,4,3,10]

x=[8,5,3,2]
y=[3,4,7,6]

print(tel(x,y))
