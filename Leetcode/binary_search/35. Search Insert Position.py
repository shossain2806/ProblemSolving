class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # empty
        if len(nums) == 0:
            return 0
        # target less than first element
        if nums[0] > target:
            return 0
        # target greater than last element
        if nums[-1] < target:
            return len(nums)
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if left > right:
            return left
        else:
            return right