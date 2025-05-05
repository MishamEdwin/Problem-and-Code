grid=[[1,1,0,0,1],
      [1,1,0,1,0],
      [0,0,1,0,0],
      [0,0,0,1,0]]

rows=len(grid)
cols=len(grid[0])

count=0

#recursive dfs function
def dfs(grid,i,j):
    # checking the bounds and cells
    if(i<0 or i>rows-1 or j<0 or j>cols-1 or grid[i][j]==0): # this condition is for the recursive direction calls
        return
    grid[i][j]=0

    #recursive dfs calls
    dfs(grid,i-1,j) # up
    dfs(grid,i+1,j) # down
    dfs(grid,i,j-1) # left
    dfs(grid,i,j+1)# right


#traversing the grid
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1: # if the island is found
            count+=1        # increase the count
            dfs(grid,i,j)   # then do the dfs on that current cell

print(count)