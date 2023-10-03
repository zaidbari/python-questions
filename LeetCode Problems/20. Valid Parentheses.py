'''
20. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Question Link: https://leetcode.com/problems/valid-parentheses/
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        
        for i in s:
            if i in '[{(':
                top+=1
                stack.append(i)
            elif stack:
                element = stack.pop()
                if element=='[' and i!=']':
                    return False
                if element=='{' and i!='}':
                    return False
                if element=='(' and i!=')':
                    return False
            else:
                return False
                    
        if not stack:
            return True