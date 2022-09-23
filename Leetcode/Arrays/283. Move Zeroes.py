class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use two pointers
        # swap to last
        count_zeros = 0
        non_zeros = []
        for num in nums:
            if num == 0:
                count_zeros += 1
            else:
                non_zeros.append(num)
        
        non_zeros.extend([0] * count_zeros)
        
        for index in range(nums):
            nums[index] = non_zeros[index]
                

nums=[0,-82274,0,-81492,-44192,-80403,-23777,0,10834,78248,-68572,0,0,0,0,0,14865,-49786,-69494,0,0,-73053,-88816,93679,-41000,0,0,91318,0,-43735,0,0,0,0,-83989,-15927,0,0,-69203,83129,-88065,45677,20017,-76098,-7459,0,-28499]
sol = Solution()
sol.moveZeroes(nums=nums)
