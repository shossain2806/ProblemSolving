import imp
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       
        arr_len = len(nums)
        max_int = 1000000
        min_len = max_int
        main = 0
        secondary = 0
        current_sum = 0
        
        while True:
            if main == arr_len and (secondary == main or current_sum < target):
                break
            
            if current_sum >= target:
                min_len = min(min_len, main - secondary)
                current_sum -= nums[secondary]
                secondary += 1
                
            elif current_sum < target:
                current_sum += nums[main]
                main += 1

        return 0 if min_len == max_int else min_len
    
sol = Solution()
print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(sol.minSubArrayLen(target = 4, nums = [1,4,4]))
print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))
print(sol.minSubArrayLen(target=11, nums=[1, 2, 3, 4 , 5]))
print(sol.minSubArrayLen(target=7, nums=[2,3,1,2,4,3]))

