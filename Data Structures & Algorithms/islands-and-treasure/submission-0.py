class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,columns = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==0:
                    queue.append((r,c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            (r,c) = queue.popleft()
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if (nr>-1 and nr<rows and nc>-1 and nc<columns and grid[nr][nc]==2147483647):
                    grid[nr][nc] = 1+grid[r][c]
                    queue.append((nr,nc))
