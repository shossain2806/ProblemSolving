# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        start_index = 0
        end_index = length - 1
        palindrome = s[0]

        while(start_index < end_index):
            lower_bound = start_index 
            upper_bound = end_index
            current_palindrome = ""
            if upper_bound - lower_bound < len(palindrome):
                break
            while (lower_bound < upper_bound):
                start = lower_bound
                end = upper_bound
                if end - start < len(palindrome):
                    break
                is_palindrome = True
                while(start < end):
                    if s[start] == s[end]:
                        start += 1
                        end -= 1
                    else:
                        is_palindrome = False
                        break
                
                if is_palindrome:
                    current_palindrome = s[lower_bound: upper_bound + 1]
                    if len(current_palindrome) > len(palindrome):
                        palindrome = current_palindrome
            
                upper_bound -= 1
            start_index += 1
        return palindrome

    def printMat(self, dp):
        length = len(dp)
        for index in range(0, length):
            print(dp[index])

    def longV2(self, text: str) -> str:
        textLen = len(text)
        start = 0
        maxLen = 1
        # initiaze dp
        dp = [[0 for x in range(textLen)] for y
                          in range(textLen)]

        # length 1       
        for index in range(0, textLen):
            dp[index][index] = 1

        # length 2
        for index in range(0, textLen - 1):
            if text[index] == text[index + 1]:
                dp[index][index + 1] = 1
                start = index
                maxLen = 2

        self.printMat(dp)
        return ""

        # length 3 or more

sol = Solution()
# print(sol.longestPalindrome("babad"))
# print(sol.longestPalindrome("bb"))
# print(sol.longestPalindrome("aba"))
# print(sol.longestPalindrome("cbbd"))
# print(sol.longestPalindrome("a"))
# print(sol.longestPalindrome("ac"))
# print(sol.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(sol.longV2("geek"))