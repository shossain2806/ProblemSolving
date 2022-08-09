class Solution:
    def dominantIndex(self, nums) -> int:
        
        # find largest
        prev_largest = 0 if nums[0] < nums[1] else 1
        curr_largest = 1 if prev_largest == 0 else 0
        length = len(nums)
        for index in range(2, length):
            if nums[index] > nums[curr_largest]:
                prev_largest = curr_largest
                curr_largest = index
            elif nums[index] > nums[prev_largest]:
                prev_largest = index
                
        if nums[curr_largest] >= nums[prev_largest] * 2:
            return curr_largest
        return -1
    
Solution().dominantIndex([0,0,1,2])