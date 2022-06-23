class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length_mat = len(mat)
        sum = 0
        
        for i in range(length_mat):
            sum += mat[i][i]
            mat[i][i] = 0
            
        for i in reversed(range(length_mat)):
            sum += mat[length_mat - i - 1][i]
            
        return sum
        