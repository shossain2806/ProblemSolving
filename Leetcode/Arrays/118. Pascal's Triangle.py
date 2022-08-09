from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1, 1]]
        prev_generated = self.generate(numRows - 1)
        last = prev_generated[-1]
        index_count = numRows - 2
        gen = []
        for index in range(index_count):
            gen.append(last[index] + last[index + 1])
        gen.insert(0,1)
        gen.append(1)
        prev_generated.append(gen)
        return prev_generated
    
    
print(Solution().generate(5))