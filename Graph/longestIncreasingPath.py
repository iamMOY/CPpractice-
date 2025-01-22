def longestIncreasingPath(matrix: list[list[int]]) -> int:
    if matrix == None:
        return 0
    
    rows , columns = len(matrix), len(matrix[0])
    dp = [[-1]* columns for _ in range(rows)]
    
    def dfs(r,c):
        if dp[r][c] != -1:
            return dp[r][c]
        
        max_length = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_r, new_c = r + dr, c+dc
            if(
                 new_r in range(rows) and
                 new_c in range(columns) and
                 matrix[new_r][new_c]> matrix[r][c]
            ):
                max_length = max(max_length, 1 + dfs(new_r,new_c))
        dp[r][c] = max_length
        return max_length
    
    longest_path = 0
    for r in range(rows):
        for c in range(columns):
                longest_path = max(longest_path, dfs(r,c))
    
    return longest_path

if __name__ == "__main__":
    # matrix = [[9,9,4],
    #           [6,6,8],
    #           [2,1,1]] # 4; [1, 2, 6, 9]
    
    # matrix = [[3,4,5],[3,2,6],[2,2,1]] # 4 [3,4,5,6]
    matrix = [[1]]
    answer  = longestIncreasingPath(matrix)
    print(answer)