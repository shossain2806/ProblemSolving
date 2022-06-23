# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        rtype = True
        for char in s:
        
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                continue
                
            if len(stack) == 0:
                rtype = False
                break
                
            current = stack.pop()

            if current == '(' and char == ')':
                continue
            elif current == '{' and char == '}':
                continue
            elif current == '[' and char == ']':
                continue
            else:
                rtype = False
                break
        rtype = rtype and (len(stack) == 0)
        return rtype


sol = Solution()

print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
