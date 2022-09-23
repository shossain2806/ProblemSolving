class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
#         nums = list(map(lambda x: x * x, nums))
#         nums.sort()
#         return nums

        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        
        for index in range(n - 1, -1 , -1):
            if abs(nums[left]) < abs(nums[right]):
                result[index] = nums[right] ** 2
                right -= 1
            else:
                result[index] = nums[left] ** 2
                left += 1
        return result