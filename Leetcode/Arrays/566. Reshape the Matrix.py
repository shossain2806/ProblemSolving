class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        new_mat = [[] for _ in range(r)]
        in_row = 0
        in_col = 0
        
        for row in range(len(mat)):
            for columm in range(len(mat[row])):
                new_mat[in_row].append(mat[row][columm])
                in_col += 1
                if in_col == c:
                    in_col = 0
                    in_row += 1
                    
        return new_mat