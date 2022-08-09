class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ''
        index = 0
        
        # filter empty
        length = len(strs)
        while True:
            count = 0
            prev = None
            for string in strs:
                if not prev:
                    if len(string) == index:
                        return longest
                    else:
                        prev = string[index]
                    count += 1
                else:
                    if index < len(string):
                        if prev != string[index]:
                            return longest
                        else:
                            count += 1
                    else:
                        return longest
            if count == length and count:
                index += 1
                longest += prev
            else:
                break
                    
        return longest