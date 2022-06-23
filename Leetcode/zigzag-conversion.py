# https://leetcode.com/problems/zigzag-conversion/

class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigZag = []

        for step in range(0, numRows):
            zigZag.append([])

        currentRow = 0
        increasing = True

        while len(s) != 0:
            char = s[0]
            s = s[1:]
            zigZag[currentRow].append(char)

            if increasing:
                if currentRow < numRows - 1:
                    currentRow += 1
                else:
                    increasing = False
                    currentRow = max(0, numRows - 2)
            else:
                if currentRow > 0:
                    currentRow -= 1
                else:
                    increasing = True
                    currentRow = min(1, numRows - 1)
        
        output = ""
        for index in range (0, numRows):
            list = zigZag[index]
            for char in list:
                 output += char
            
        return output

sol = Solution()

print(sol.convert(s="PAYPALISHIRING", numRows = 3))
print(sol.convert(s="PAYPALISHIRING", numRows = 4))
print(sol.convert(s="ABC", numRows = 1))