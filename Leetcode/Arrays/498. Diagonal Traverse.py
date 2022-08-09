from typing import List

class Solution:
    def isValid(self,x,y,m,n):
        return x >=0 and x < m and y >=0 and y < n
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        x = 0
        y = 0
        is_up_trending = True
        output = []
        while True:
            if self.isValid(x,y,m,n) == False:
                break
            output.append(mat[x][y])
            if is_up_trending == True:
                next_x = x - 1
                next_y = y + 1
                if self.isValid(next_x, next_y, m, n):
                    x = next_x
                    y = next_y
                else:
                    is_up_trending = False
                    if self.isValid(x, y + 1, m, n):
                        y = y + 1
                    else:
                        x = x + 1
            else:
                next_x = x + 1
                next_y = y - 1
                if self.isValid(next_x, next_y, m, n):
                    x = next_x
                    y = next_y
                else:
                    is_up_trending = True
                    if self.isValid(x + 1, y, m, n):
                        x = x + 1
                    else:
                        y = y + 1
                    
        return output
    
    
Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])