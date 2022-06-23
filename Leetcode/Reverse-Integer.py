# https://leetcode.com/problems/reverse-integer/

from math import fabs
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:

        neg = x < 0
        if neg:
            x *= -1
        digits = len(str(x))
        multipier = digits - 1
        res = 0
        while x != 0:
            mod = x % 10
            x = int (x / 10)
            res += mod * (10 ** multipier)
            multipier -= 1
        if neg:
            res *= -1

        if (res <= 2 ** 31 - 1 and res >= -2**31) == False:
            return 0
        return res


sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))
print(sol.reverse(0))