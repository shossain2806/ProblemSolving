from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row validity
        for row in board:
            item_count = 0
            unique_items = set()
            for item in row:
                if item != ".":
                    unique_items.add(item)
                    item_count += 1
                    
            if item_count != len(unique_items):
                return False
            
        # check column validity
        for row in range(len(board)):
            item_count = 0
            unique_items = set()
            for col in range(len(board)):
                if board[col][row] != ".":
                    unique_items.add(board[col][row])
                    item_count += 1
        
            if item_count != len(unique_items):
                return False
        
        # checi sub-boxes
        for box_count in range(len(board)):
            r = int(box_count / 3)
            c = box_count % 3
            item_count = 0
            unique_items = set()
            for row in range(r * 3, (r * 3) + 3):
                for col in range( c * 3, (c * 3) + 3):
                    if board[row][col] != ".":
                        unique_items.add(board[row][col])
                        item_count += 1
        
            if item_count != len(unique_items):
                return False
        
        return True
    
sudo = [
[".",".","4",".",".",".","6","3","."],
[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],
[".",".",".","5","6",".",".",".","."],
["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],
[".",".",".","5",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]
]
sol = Solution()
sol.isValidSudoku(sudo)