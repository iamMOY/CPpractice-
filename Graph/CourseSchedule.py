class Solution:
    def courseSchedule(numCourse: int, prerequisites: list[int]) ->bool:
        courseList = {i: [] for i in range(numCourse)}
        
        for i,j in prerequisites:
            courseList[i].append(j)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if courseList[course] == []:
                return True
            
            for pre in courseList[course]:
                if not dfs(pre): return False
                visited.add(pre)
                return True 
        return True