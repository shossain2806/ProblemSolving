from os import sep
from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        def reversWord(s: List[str]):
            left = 0
            right = len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
        wordlist = s.split()
        output_list = []
        for word in wordlist:
            word_list = list(word)
            reversWord(word_list)
            output_list.append(''.join(word_list))
        return " ".join(output_list)
sol = Solution()
print(sol.reverseWords("God Ding"))