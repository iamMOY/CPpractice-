# suboptimal solution but works :)

class Solution:
    def TopKFrequent(self,nums: list[int], k: int) -> list[int]:
        frequency_count = {}
        for num in nums:
            frequency_count[num] = frequency_count.get(num,0)+1
        sorted_frequency = sorted(frequency_count.items(), key = lambda x: x[1], reverse= True)
        return [x[0] for x in sorted_frequency[:k]]
    
    def OptimalSolution(self,nums: list[int], k: int) -> list[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = count.get(num,0)+1
        
        for num, freq in count.items():
            frequency[freq].append(num)
        res = []
        for i in range(len(frequency)-1, 0,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res
    

if __name__ == '__main__':
    solution = Solution()
    ans = solution.TopKFrequent(nums = [1,2,3,3,3,4,4,4,5,5,5],k=2)
    ans2= solution.OptimalSolution(nums = [1,2,3,3,3,4,4,4,5,5,5],k=2)
    print(ans)
    print(ans2)
