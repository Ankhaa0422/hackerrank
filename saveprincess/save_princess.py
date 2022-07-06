#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    mBairlal = list(khailt(n,grid,'m'))
    pBairlal = list(khailt(n,grid,'p'))
    shalguur = True
    while (shalguur):
        if pBairlal[0] < mBairlal[0]:
            mBairlal[0] -= 1
            print("UP")
        elif pBairlal[0] > pBairlal[0]:
            mBairlal[0] += 1
            print("DOWN")
        elif pBairlal[1] < mBairlal[1]:
            mBairlal[1] -= 1
            print("LEFT")
        elif pBairlal[1] > mBairlal[1]:
            mBairlal[1] += 1
            print("RIGHT")
        else: 
            shalguur = False

def khailt(n,grid,utga):
    for mur in range(n):
        for bagana in range(n):
            if grid[mur][bagana] == utga:
                return(mur,bagana)
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)