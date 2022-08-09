from curses import halfdelay


class Solution:
    
    def check_substring(self, str1, str2):
        return str1 == str2
    
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)
        curr_index = 0
        for (index, char) in enumerate(haystack):
            if char == needle[0]:
                len_t = min(index + len_needle, len_haystack)
                if self.check_substring(haystack[index : len_t], needle) == True:
                    return index
                
        return -1
    
    
Solution().strStr('mississippi', 'issip')
