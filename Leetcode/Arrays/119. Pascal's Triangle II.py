class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prevRes = self.getRow(rowIndex - 1)
        res = [1]
        for index in range(len(prevRes) - 1):
            res.append(prevRes[index] + prevRes[index + 1])
            
        res.append(1)
        return res