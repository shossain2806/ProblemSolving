
class Solution:
    def longestConsecutive(self, nums) -> int:
        lookup = {}
        longest_length = 0
        nums.sort()
        
        for num in nums:
            if  lookup.get(num, 0) > 0:
                continue
            lookup[num] = lookup.get(num - 1, 0) + 1
            max_value = lookup[num]
            next_num = num + 1
            while lookup.get(next_num, 0) > 0:
                lookup[next_num] = lookup[next_num - 1] + 1
                max_value = lookup.get(next_num, max_value)
                next_num = next_num + 1
               
            longest_length = max(longest_length, max_value)
        
        return longest_length




print(Solution().longestConsecutive(nums=[-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]))