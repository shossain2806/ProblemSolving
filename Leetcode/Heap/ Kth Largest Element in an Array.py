from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def max_heapify(heap_size, index):
            left = index * 2 + 1
            right = index * 2 + 2
            largest = index
            
            if left < heap_size and nums[left] > nums[largest]:
                largest = left
                
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
                
            if index != largest:
                nums[index], nums[largest] = nums[largest], nums[index]
                max_heapify(heap_size, largest)
                
        
        for index in range(len(nums) // 2 - 1, -1, -1):
            max_heapify(len(nums), index)

        for index in range(len(nums) - 1, 0, -1):
            nums[index], nums[0] = nums[0], nums[index]
            max_heapify(index, 0)
            if k == len(nums) - 1 - index + 1:
                break
        return nums[-k]
        
sol = Solution()
# print(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
# print(sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
# print(sol.findKthLargest([1], 1))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 1)) #output: 5, expected 6