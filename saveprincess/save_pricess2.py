#

def nextMove(n,r,c,grid):
    gege = olyo(n,grid)
    mur = gege[0]
    bagana = gege[1]
    if mur < int(r):
        return('UP')
    elif mur > int(r):
        return('DOWN')
    elif bagana > int(c):
        return('RIGHT')
    elif bagana < int(c):
        return('LEFT')
    
def olyo(n,grid):
    for r in range(n):
        for c in range(n):
            if(grid[r][c] == 'p'):
                return (r,c)
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))