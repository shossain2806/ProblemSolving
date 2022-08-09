class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        c = '0'
        len_a = len(a) - 1
        len_b = len(b) - 1
        res = ''
        while len_a >= 0 or len_b >= 0:
            val_a = a[len_a] if len_a >= 0 else '0'
            val_b = b[len_b] if len_b >= 0 else '0'
            sum = '0'
            if val_a == '0' and val_b == '0':
                sum = '0' if c == '0' else '1'
                c = '0'
            elif (val_a == '0' and val_b == '1') or (val_a == '1' and val_b == '0'):
                if c == '0':
                    sum = '1'
                else:
                    sum = '0'
                    c = '1'
            else:
                if c == '0':
                    sum = '0'
                    c = '1'
                else:
                    sum = '1'
                    c = '1'
            res = sum + res
            len_a -= 1
            len_b -= 1
            
        if c == '1':
            res = c + res
        return res
                
            
                
                