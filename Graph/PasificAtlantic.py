
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, columns = len(heights), len(heights[0])
        pac, alt = set(), set()
        flow = []
        def dfs(r,c,visit, prevHeight):
            if(
                (r,c) in visit or
                r<0 or c<0 or r == rows or c == columns or
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                r_new, c_new = r+ dr, c+dc
                dfs(r_new,c_new,visit,heights[r][c])
        # From  top row and botton row
        for c in range(columns):
            dfs(0,c,pac, heights[0][c])
            dfs(rows-1, c, alt,heights[rows-1][c])

        # for left columns to right-most column
        for r in range(rows):
            dfs(r,0,pac, heights[r][0])
            dfs(r,columns-1, alt,heights[r][columns-1])

        for r in range(rows):
            for c in range(columns):
                if (r,c) in alt and (r,c) in pac:
                    flow.append([r,c])

        return flow