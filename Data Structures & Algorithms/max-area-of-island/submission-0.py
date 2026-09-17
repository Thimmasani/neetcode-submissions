class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        def spread(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1+ spread(i+1,j) + spread(i-1,j)+spread(i,j+1)+spread(i,j-1)

        max_area=0
        for i in range(m):
            for j in range(n):
                max_area = max(max_area,spread(i,j))
                
        return max_area




        