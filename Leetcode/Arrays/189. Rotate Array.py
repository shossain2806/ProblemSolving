from typing import List
# first reverse whole part
# then reverse first part
# then reverse end part


class Solution:
    def reverse(self, nums: List[int], start_index: int, end_index: int) -> None:
        
        while start_index < end_index:
            nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
            start_index += 1
            end_index -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        self.reverse(nums=nums,start_index=0, end_index=n-1)
        self.reverse(nums=nums,start_index=0,end_index=k-1)
        self.reverse(nums=nums,start_index=k,end_index=n-1)
        
    
 
nums = [1,2,3,4,5]
sol = Solution()
sol.rotate(nums=nums, k=2)
print(nums)