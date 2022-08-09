from typing import List

class Solution:
    def isValid(self, x, y, m, n):
        return x >= 0 and x < m and y >= 0 and y < n
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = 0
        modes = 4 #0 ,1,2,3
        mode = 0
        
        visit = [ [0] * n for _ in range(m)]
        output = []
        count = 0
        while count < m * n:
            
            if self.isValid(x, y, m, n) and visit[x][y] == 0:
                visit[x][y] = 1  
                output.append(matrix[x][y])
                count += 1
                
            if mode == 0: # right
                next_x = x
                next_y = y + 1
                if self.isValid(next_x, next_y, m, n) and visit[next_x][next_y] == 0:
                    x = next_x
                    y = next_y
                else:
                    mode = (mode + 1) % modes
                
                    
            elif mode == 1: # down
                next_x = x + 1
                next_y = y
                if self.isValid(next_x, next_y,m, n) and visit[next_x][next_y] == 0:
                    x = next_x
                    y = next_y
                else:
                    mode = (mode + 1) % modes
                    
                
            elif mode == 2: # left
                next_x = x
                next_y = y - 1
                if self.isValid(next_x, next_y, m, n) and visit[next_x][next_y] == 0:
                    x = next_x
                    y = next_y
                else:
                    mode = (mode + 1) % modes
            
            elif mode == 3: # up

                next_x = x - 1
                next_y = y
                if self.isValid(next_x, next_y, m, n) and visit[next_x][next_y] == 0:
                    x = next_x
                    y = next_y
                else:
                    mode = (mode + 1) % modes
                    
        return output
        
        
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))