# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for n in range (9):
            numSet = set()
            numList = list()
            for i in range(9):
                if board[n][i].isdigit():
                    numSet.add(board[n][i])
                    numList.append(board[n][i])
            if len(numSet) != len(numList):
                return False
                       
        #check columns
        for n in range (9):
            numSet = set()
            numList = list()
            for i in range(9):
                if board[i][n].isdigit():
                    numSet.add(board[i][n])
                    numList.append(board[i][n])
            if len(numSet) != len(numList):
                return False
            
        #check grids
        for n in range (9):
            #construct grid
            div = int(n / 3)
            mod = int(n % 3)
            posX = div * 3
            posY = mod * 3
            numSet = set()
            numList = list()
            for i in range(posX, posX + 3):
                for j in range(posY, posY + 3):
                    if board[i][j].isdigit():
                        numSet.add(board[i][j])
                        numList.append(board[i][j])
                        
            if len(numSet) != len(numList):
                return False
        return True