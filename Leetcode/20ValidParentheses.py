# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
                continue
            if len(stack) == 0:
                return False
            if i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
            elif i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)
            elif i == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(i)
        return True if len(stack) == 0 else False
        
