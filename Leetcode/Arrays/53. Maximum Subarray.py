from typing import List
import math
# look for dp with kadane's
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubArray(nums, left, right) -> int:
            
            # base case if array is empty
            if left > right:
                return -math.inf
            
            curr = left_best_sum = right_best_sum = 0
            
            # get mid
            mid = (left + right) // 2
            
            # calc left max
            for index in range(mid-1, left - 1, -1):
                curr += nums[index]
                left_best_sum = max(left_best_sum, curr)
                
            # reset curr
            curr = 0
            
            for index in range(mid + 1, right + 1):
                curr += nums[index]
                right_best_sum = max(right_best_sum, curr)
                
            sum = left_best_sum + nums[mid] + right_best_sum
            
            left_sum = findBestSubArray(nums, left, mid - 1)
            right_sum = findBestSubArray(nums, mid+1, right)
            
            return max(sum, left_sum, right_sum)
        
        return findBestSubArray(nums, 0, len(nums) - 1)
            
            
            