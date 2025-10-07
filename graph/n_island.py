from collections import deque


def numIslands(grid):
  
  num_row = len(grid)
  num_col = len(grid[0])
  
  visited = [["0" for _ in range(num_row+1)] for _ in range(num_col+1)]

  def bfs(row , col):
    nonlocal visited , num_row , num_col
    arr = deque()
    arr.append((row,col))

    while(arr):
      curr_row , curr_col = arr.popleft()
      directions = [[-1, 0] , [1 , 0] , [0 , -1] , [0 , 1]]
      
      for dr in directions:
        drow , dcol = dr
        new_row , new_col = curr_row + drow , curr_col + dcol

        if(
          (new_row >= 0 and new_row < num_row)
          and (new_col >= 0 and new_col < num_col)
          and (grid[new_row][new_col] == "1")
          and (visited[new_row][new_col] != "1")
        ):
          
          arr.append((new_row , new_col))
          visited[new_row][new_col] = "1"
      

  count = 0
  for i in range(num_row):
    for j in range(num_col):
      if(visited[i][j] != "1" and grid[i][j] == "1"):
        visited[i][j] = "1"
        count += 1
        bfs(i , j)

  return count
      

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

print(numIslands(grid))
