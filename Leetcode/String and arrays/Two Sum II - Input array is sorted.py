from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list = []
        lower = 0 
        upper = len(numbers) - 1
        while lower <= upper:
            if numbers[lower] + numbers[upper] == target:
                list.append(lower + 1)
                list.append(upper + 1)
                break
           
            if numbers[lower] + numbers[upper] > target:
                upper = upper - 1
            else:
                lower = lower + 1
          
        return list
        
        
        
sol = Solution()

print(sol.twoSum(numbers=[2,7,11,15,17], target=9))
print(sol.twoSum(numbers=[2,7,11,15,17], target=22))
print(sol.twoSum(numbers=[2,7,11,15,17], target=9))
print(sol.twoSum(numbers=[2,3,4], target=6))
print(sol.twoSum(numbers=[-1,0], target=-1))