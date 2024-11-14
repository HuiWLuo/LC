# 1020. Number of Enclaves
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
            if i==-1 or j==-1 or i==n or j==m or grid[i][j]==0:
                return 
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or n-1==i or m-1==j) and grid[i][j]==1:
                    dfs(i,j)
        s=0
        for i in range(n):
            for j in range(m):
                s+=grid[i][j]
        return s


# 1905. Count Sub Islands
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(i: int, j: int) -> int: # return number of cell included
            if not (0 <= i < m and 0 <= j < n): # outside grid
                return 0
            if grid2[i][j] == -1:
                return -1
            if grid2[i][j] == 0: # water / checked
                return 0
            if grid2[i][j] == 1 and grid1[i][j] == 0: # not fully included
                grid2[i][j] = -1
                return -1

            grid2[i][j] = 0
            res = 1
            
            for ii, jj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                compare = dfs(i + ii, j + jj)
                if compare < 0:
                    grid2[i][j] = -1
                    return -1
                res += compare
            return res
        
        m, n = len(grid1), len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and dfs(i, j) > 0:
                    ans += 1

        return ans
