class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lower = 0
        upper = len(nums) - 1
        
        while lower <= upper:
            mid = int((lower + upper) / 2)
            if nums[mid] == target:
                return mid
            if nums[lower] < nums[mid]:
                if nums[lower] <= target and target < nums[mid]:
                    upper = mid - 1
                else:
                    lower = mid + 1
            elif nums[lower] > nums[mid]:
                if nums[mid] < target and target <= nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid - 1
            else:
                lower = mid + 1

        return -1
    


