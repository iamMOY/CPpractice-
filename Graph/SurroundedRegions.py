import collections
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m = len(board)
        n = len(board[0])
        
        def dfs(i,j):
            if (i<0 or j<0 or 
                i == m or j == n or
                board[i][j] != "O"):
                return    
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            board[i][j] = "T"
            for dr, dc in directions:
                i_new = i+dr
                j_new = j+dc
                dfs(i_new,j_new)
        
        # Capture Unsurrounded Regions (O -> T)
        for i in range(m):
            for j in range(n):
                if (i in [0,m-1] or j in [0,n-1]
                    and board[i][j]=="O"):
                    dfs(i,j)


        # Capture Surrounded Regions (O -> X)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j]="X"
        for row in board:
            print(*row, sep = "\t")
        
        # Uncapture unsurouned regions (T -> O)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j]="O"

if __name__ == "__main__":
    solution = Solution()
    board = [["O","O","X"],["O","O","O"],["O","O","O"]]
    # print(board)
    for row in board:
        print(*row, sep="\t")
    print()
    solution.solve(board)
    for row in board:
        print(*row, sep="\t")