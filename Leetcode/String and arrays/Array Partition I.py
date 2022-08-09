class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        len_nums = len(nums)
        nums.sort()
        sum = 0
        for index in range(0, len_nums - 1, 2):
            sum += min(nums[index], nums[index + 1])
            
        return sum