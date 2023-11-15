DIM=4

def printMaze(maze):
    for i in range(N):
        for j in range(N):
            print(maze[i][j],end=" ")
        print("")
    print("")


def backtracking(maze,path,i,j):

    #out of bounds check
    if( i>=DIM and j>=DIM ):
        return
    
    #if solution make last move and print
    if( i==DIM-1 and j==DIM-1):
        path[i][j]=1
        print("SOLUTION FOUND")
        printMaze(path)
        path[i][j]=0
        return
    
    #make first move
    path[i][j]=1
    #printMaze(path)
    #make move --> right
    if(j+1<DIM and maze[i][j+1]==1):
        backtracking(maze,path,i,j+1)

    #make move --> go down
    if(i+1<DIM and maze[i+1][j]==1):
        backtracking(maze,path,i+1,j)


    path[i][j]=0
    #printMaze(path)


if __name__=="__main__":

    N=4
    i=j=0

    maze=[
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1]]

    path=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

    ps=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

    backtracking(maze,path,i,j)
