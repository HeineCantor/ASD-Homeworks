# s is sum    p is prime
def numPrim(s,p):
    primeList=[]
    found =False
  
    for p in range(p+1,s+1):
        #found reset
        found=False

        for i in range(2,s):
            #pruning
            if found==True:
                break
            #se entro qui non è primo
            if(p%i==0 and i != p ):
                found=True
        #se found è rimasto false --> allora è num primo
        if(found==False):
            primeList.append(p)      
    #print(primeList)
    return primeList

def isValid(s,n,sum,k):
    if( sum==s and k==n ):
        return True

def buildCandidates(s,p,k,sol):
    candidates=[]
    if(k-1==0):
        candidates=numPrim(s,p)
    else:
        candidates=numPrim(s,sol[k-2])
    return candidates



def backtrack(s,p,n,sum,numOfVal,k,sol):
    candidates=[]

    if(isValid(s,n,sum,k)):
        print("Soluzione trovata")
        print(sol)

    elif(k<n):
        k+=1
        candidates= buildCandidates(s,p,k,sol)
        for candidate in candidates:
            sol.append(candidate)
            #for i in range(len(sol)):
            sum+=sol[k-1]
            backtrack(s,p,n,sum,numOfVal,k,sol)
            sum-=sol[k-1]
            sol.pop()


if __name__=="__main__":

    n=2
    p=1
    s=7
    sum=numOfVal=k=0
    sol=[]
    #print(numPrim(17,1))
    backtrack(s,p,n,sum,numOfVal,k,sol)
