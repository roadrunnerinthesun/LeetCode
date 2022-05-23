# 20. Valid Parenthis

""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Declare stack
        stack = []
        # If starting parentheses is encountered, then append it to the stack
        for char in s:
            if char in ['(' , '[' , '{']:
                stack.append(char)
        # If starting parentheses is not encountered, then return False
            else:
                if not stack: 
                   return False
            # Match pair of parentheses to pop out if end parentheses is encountered
                current_char = stack.pop() 
                if current_char == '(': 
                    if char != ")": 
                        return False
                if current_char == '{': 
                    if char != "}": 
                        return False
                if current_char == '[': 
                    if char != "]": 
                        return False
        # If stack is empty
        if stack: 
            return False
        return True