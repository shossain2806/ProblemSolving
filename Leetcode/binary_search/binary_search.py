class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_index = 0
        upper_index = len(nums) - 1
        while lower_index <= upper_index:
            mid = int((upper_index + lower_index) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                upper_index = mid - 1
            else:
                lower_index = mid + 1
        return -1