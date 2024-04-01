import collections
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if grid == None:
            return 0
        islandArea = 0
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        maxIslandArea = 0
        def dfs(row,column):
            q = collections.deque()
            q.append((row,column))
            visited.add((row,column))
            islandArea = 1
            while q:
                r,c = q.pop()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in direction:
                    row = r+dr
                    col = c+dc
                    if(
                        row in range(rows) and 
                        col in range(columns) and 
                        grid[row][col]!=0 and 
                        (row,col) not in visited
                    ):  
                        islandArea +=1
                        visited.add((row,col))
                        q.append((row,col))
            return islandArea
        
        for row in range(rows):
            for column in range(columns):
                if (row, columns) not in visited and grid[row][column]==1:
                    islandArea = dfs(row,column)
                    if islandArea > maxIslandArea:
                        maxIslandArea = islandArea
    
        return maxIslandArea 
        

if __name__ == '__main__':
    # grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid = [[0,0,0,0,0,0,0,0]]
    solution = Solution()
    print(solution.maxAreaOfIsland(grid))