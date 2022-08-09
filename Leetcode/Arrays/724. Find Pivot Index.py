class Solution:
    def pivotIndex(self, nums) -> int:

        length = len(nums)
        left_sum = 0
        right_sum = 0
        pivot = 0
        indexes = range(pivot + 1, length)
        for index in indexes:
            right_sum += nums[index]
            
        while pivot < length:
            if left_sum == right_sum:
                return pivot
            else: 
                left_sum += nums[pivot]
                pivot += 1
                right_sum -= 0 if pivot == length else nums[pivot]
           
            
        return -1
    
print(Solution().pivotIndex([1,2,3]))