RIG=5
COL=5

mat=[
    ["t", "z", "x", "c", "d"],
    ["a", "h", "n", "o", "x"],
    ["h", "w", "e", "l", "o"],
    ["o", "r", "n", "l", "n"],
    ["a", "b", "r", "i", "n"]
    ]

path=[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]

def printMat(mat):
    for i in range(RIG):
        for j in range(COL):
            print(mat[i][j],end=" ")
        print("")
    print("")


def printSolution(path):
    for i in range(RIG):
        for j in range(COL):
            if path[i][j]==1:
                print("("+str(i)+","+str(j)+")")
    print("")



def isValid(k,string):
    if k==len(string):
        return True
    else:
        return False


def findFirst(mat,k):
    coordinates=[]

    for i in range(COL):
        for j in range(RIG):
            if mat[i][j]==string[k-1]:
                coordinates.append(i)
                coordinates.append(j)
                return coordinates


def buildCandidates(mat,string,k,x,y):
    coordinates=[]

    if(k-1==0):
        coordinates=findFirst(mat,k)
        return coordinates

    x_temp=x
    y_temp=y

    #su
    if(y-1>=0):
        if(mat[y-1][x]==string[k-1]):
            coordinates.append(y-1)
            coordinates.append(x)


    x=x_temp
    y=y_temp

    #sx
    if(x-1>=0):
        if(mat[y][x-1]==string[k-1]):
            coordinates.append(y)
            coordinates.append(x-1)
        
    x=x_temp
    y=y_temp

    #dx
    if(x+1<COL):
        if(mat[y][x+1]==string[k-1]):
            coordinates.append(y)
            coordinates.append(x+1)

   
    x=x_temp
    y=y_temp

    #giù
    if(y+1<RIG):
        if(mat[y+1][x]==string[k-1]):
            coordinates.append(y+1)
            coordinates.append(x)

        
    x=x_temp
    y=y_temp

    # up-sx diagonal
    if(x-1>=0 and y-1>=0):       
        if(mat[y-1][x-1]==string[k-1]):
            coordinates.append(y-1)
            coordinates.append(x-1)

    x=x_temp
    y=y_temp

    #up-dx diagonal
    if(x+1<COL and y-1>=0):
        if(mat[y-1][x+1]==string[k-1]):
            coordinates.append(y-1)
            coordinates.append(x+1)

    x=x_temp
    y=y_temp

    #down-sx diagonal
    if(x-1>=0 and y+1<RIG):
        if(mat[y+1][x-1]==string[k-1]):
            coordinates.append(y+1)
            coordinates.append(x-1)

    x=x_temp
    y=y_temp

    #down-dx diagonal
    if(x+1>=0 and y+1<RIG):
        if(mat[y+1][x+1]==string[k-1]):
            coordinates.append(y+1)
            coordinates.append(x+1)

    return coordinates         



def backtrack(mat,path,k,string,x,y):
    candidates=[]

    if(isValid(k,string)):
        printMat(path)
        return
    else:
        k+=1
        candidates=buildCandidates(mat,string,k,x,y)

        for i in range(len(candidates)-1):
            if(i%2==0):
                y=candidates[i]
                x=candidates[i+1]
            else:
                i+=1
                y=candidates[i]
                x=candidates[i+1]
            path[y][x]=k
            printMat(path)
            backtrack(mat,path,k,string,x,y)
            path[y][x]=0
            printMat(path)        


if __name__=="__main__":
    
    string="hello"
    x=y=0
    backtrack(mat,path,0,string,x,y)
