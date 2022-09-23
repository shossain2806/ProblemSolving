from traceback import print_tb
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        base = ""
        for _ in range(n):
            base += "()"
        results.append(base)
        if n == 1:
            return results
        sorted_p = ''.join(sorted(base))
        results.append(sorted_p)
        if n == 2:
            return results

        for n in range(len(base)):
            if base[n] == ')':
                first_part = base[0:n]
                second_part = base[n + 1:len(base)]
                res = first_part + second_part + base[n]
                results.append(res)
            
        return results
    
print(Solution().generateParenthesis(3))