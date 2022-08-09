from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        len_grid = len(grid)
        res = 0
        for row_i in range(len_grid):
            row_data = grid[row_i]
            for row_j in range(len_grid):
                count = 0
                for row_k in range(len_grid):
                    if row_data[row_k] != grid[row_k][row_j]:
                        break
                    count +=1
                if count == len_grid:
                    res += 1
        return res
                
                
    def equalPairs2(self, grid: List[List[int]]) -> int:
        len_grid = len(grid)
        res = 0
        row_arr = []
        col_arr = []
        for row_i in range(len_grid):
            row_data = grid[row_i]
            row_arr.append(",".join(map(str, row_data)))
            col_data = ''
            for col_i in range(len_grid):
                if col_i == 0:
                    col_data += str(grid[col_i][row_i])
                else:
                    col_data += ',' + str(grid[col_i][row_i])
            col_arr.append(col_data)
        
        for item in row_arr:
            for item2 in col_arr:
                if item == item2:
                    res += 1
        return res
    
Solution().equalPairs2([[11,1], [1,11]])