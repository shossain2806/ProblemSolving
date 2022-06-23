class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 1
        right = int ( x / 2) 
        
        while left <= right:
            mid = int((right + left ) / 2)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                left = mid + 1
            else:
                right = mid - 1
        return -1