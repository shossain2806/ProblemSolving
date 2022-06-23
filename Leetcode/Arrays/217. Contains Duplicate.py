from cgitb import lookup
from pickle import FALSE, TRUE
from sys import flags
from typing import List

class Solution:
    def alternateContainsDuplicate(self, nums: List[int]) -> bool:
        # sort 
        length = len(nums)
        if length == 0:
            return FALSE
        nums.sort()
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                return True
        return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dictionary 
        lookup = { }
        for entry in nums:
            flag = lookup.get(entry, False)
            if flag == True:
                return True
            lookup[entry] = True
        return False

sol = Solution()
print(sol.containsDuplicate(nums=[1,2,3,1]))
print(sol.containsDuplicate(nums=[1,2,3,4]))
print(sol.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))
