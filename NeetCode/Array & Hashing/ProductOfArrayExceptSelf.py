class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if 0 in nums:
            print('Zero')
        return nums


if __name__ == '__main__':
	solution = Solution() 
	solution.productExceptSelf(nums=[1,0])
