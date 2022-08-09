from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1
        carry = 1
        while length >= 0:
            sum = digits[length] + carry
            digits[length] = sum % 10
            carry = int(sum / 10)
            length -= 1
            
        if carry == 1:
            digits.insert(0, carry)
        return digits
    
    
print(Solution().plusOne([9,9]))