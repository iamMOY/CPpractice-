# suboptimal solution but works :)

class Solution:
    def TopKFrequent(self,nums: list[int], k: int) -> list[int]:
        frequency_count = {}
        for num in nums:
            frequency_count[num] = frequency_count.get(num,0)+1
        sorted_frequency = sorted(frequency_count.items(), key = lambda x: x[1], reverse= True)
        return [x[0] for x in sorted_frequency[:k]]
    

if __name__ == '__main__':
    solution = Solution()
    ans = solution.TopKFrequent(nums = [1,1,1,3,3,3,3,4,4,4,4,4,4,4,4],k=2)
