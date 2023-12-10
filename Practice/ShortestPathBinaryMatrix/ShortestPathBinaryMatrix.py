
def spm(grid):
    N = len(grid)
    q=[(0,0,1)]  # r, c, lenght
    visit=set()
    visit.add((0,0))
    direct=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

    while q:
        r, c, lenght = q.pop()
    
        if grid[r][c]==1: return -1
        
        if r==N-1 and c ==N-1:
            return lenght

        for x,y in direct:

            if (r+x,c+y) in visit:
                continue
            if min(r+x,c+y)<0 or max(r+x,c+y)>=N:
                continue

            else:
                visit.add((r+x,c+y))
                if grid[r+x][c+y] != 1:
                    q.append((r+x,c+y,lenght+1))
    return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]
print(spm(grid))

grid = [[0,1],[1,0]]
print(spm(grid))

grid = [[1,0,0],[1,1,0],[1,1,0]]
print(spm(grid))

grid = [[1,0,0],[1,1,1],[1,1,0]]
print(spm(grid))
