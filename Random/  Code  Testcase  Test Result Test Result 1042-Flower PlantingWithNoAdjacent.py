# solution 1: greedy approach faster faster solution
from collections import defaultdict
class Solution:
    # def gardenNoAdj(self,n: int, path: list[list[int]]) -> list:
    #     flowers = [1,2,3,4]
    #     garden = defaultdict(list)
    #     for i,j in path:
    #         garden[i-1].append(j-1)
    #         garden[j-1].append(i-1)

    #     result = [0]*n

    #     for i in range(n):
    #         used_flowers  = set(result[node] for node in garden[i])

    #         for flower in flowers:
    #             if flower not in used_flowers:
    #                 result[i] = flower
    #                 break
    #     return result


# solution 2: Using Recursion 
    def gardenNoAdj(self,n: int, path: list[list[int]]) -> list:
        flowers = [1,2,3,4]
        garden = defaultdict(list)
        for i,j in path:
            garden[i-1].append(j-1)
            garden[j-1].append(i-1)

        result = [-1]*n
        def plant(node):
            if node == n: # we have completed all the plants
                return result
            for flower in flowers:
                if isSafe(node, flower):
                    result[node] = flower # Assign
                    if plant(node+1): # recurssion -> checking for the next node
                        return result
                result[node] = -1 # BackTrack

        def isSafe(node,flower):
            for neighbour in garden[node]:
                if result[neighbour] == flower:
                    return False
            return True
        
        return plant(0)         


if __name__ == '__main__':
    solution = Solution()
    # path = [[1,2],[2,3],[3,1]]
    # n = 3

    # path = [[1,2],[3,4]]
    # n = 4

    path = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    n=4
    print(f"{solution.gardenNoAdj(n,path)}")
