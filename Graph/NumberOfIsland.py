class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        island = 0
        visited = set()
        
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row , col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if(
                        r in range(rows) and 
                        c in range(columns) and 
                        grid[r][c] == '1' and 
                        (r,c) not in visited
                    ):
                        visited.add((r,c))
                        q.append((r,c))


        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    island +=1
        
        return island

if __name__ == '__main__':
    grid =  [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    solution = Solution()
    island = solution.numIslands(grid)