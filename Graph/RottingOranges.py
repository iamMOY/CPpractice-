import collections
# 1: Fresh, 2: Rotten, 0: None
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Approach 1: calculating time each orange takes to rot; thereby maintaining a grid of time
        """
        visited = set()
        q = collections.deque()
        rows, columns = len(grid), len(grid[0])
        rotten_times = [[-1]*columns for _ in range(rows)]
        fresh_count = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    rotten_times[r][c] = 0
                    q.append((r,c))
                elif grid[r][c]== 1:
                    fresh_count+=1

        if fresh_count == 0:
            return -1
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                r_new, c_new = r+dr, c+dc
                if(
                    r_new in range(rows) and
                    c_new in range(columns) and
                    (r_new, c_new) not in visited and 
                    grid[r_new][c_new] == 1
                ):
                    grid[r_new][c_new] = 2
                    rotten_times[r_new][c_new] = rotten_times[r][c]+1
                    fresh_count-=1
                    q.append((r_new,c_new))
                    visited.add((r_new,c_new))

        return max(max(row) for row in rotten_times) if fresh_count == 0 else -1
    
# # approach 2: No need to maintain any grid for rotten_time 
    
#     def orangesRotting2(self, grid: list[list[int]]) -> int:
#         time = 0
#         rows, columns = len(grid), len(grid[0])
#         q = collections.deque()
#         fresh = 0

#         for r in range(rows):
#             for c in range(columns):
#                 if grid[r][c] == 2:
#                     q.append((r,c))
#                 elif grid[r][c]==1:
#                     fresh+=1
        
#         if fresh == 0:
#             return 0
        
#         directions = [[1,0],[-1,0],[0,1],[0,-1]]
#         while q and fresh>0:
#             for i in range(len(q)):
#                 r,c = q.popleft()
#                 for dr, dc in directions:
#                     r_new = r + dr
#                     c_new = c+ dc
#                     if(
#                         r_new < 0 or r_new == rows or
#                         c_new <0 or c_new == columns or
#                         grid[r_new][c_new] != 1
#                     ):
#                         continue
#                     grid[r_new][c_new] = 2
#                     q.append((r_new,c_new))
#                     fresh-=1

#             time+=1
        
#         return time if fresh == 0 else -1

if __name__ == "__main__":
    solution = Solution()
    # grid = [[2,1,1],[1,1,0],[0,1,1]]
    grid = 
    grid = 
    minutes = solution.orangesRotting(grid)
    print(minutes)