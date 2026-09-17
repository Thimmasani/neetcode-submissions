class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = set()

        def spread(i,j):
            if (grid[i][j]=="0") or ((i,j) in visited) : return
            else:
                visited.add((i,j))
                if (i+1)<m :
                    spread(i+1,j)
                if (i-1)>=0:
                    spread(i-1,j)
                if (j+1)<n :
                    spread(i,j+1)
                if (j-1)>=0:
                    spread(i,j-1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]!="0") and ((i,j) not in visited) :
                    count+=1
                    spread(i,j)
                
        return count


                

        