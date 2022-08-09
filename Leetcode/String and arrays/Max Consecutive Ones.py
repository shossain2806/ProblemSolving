class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maximum = 0
        for num in nums:
            if num == 0:
                maximum = max(maximum, current)
                current = 0
            else:
                current += 1
                
        return max(maximum, current)