# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
# Example 5:
#
# Input: s = "([)]"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class solution:
    def isvalid(self, s:str) -> bool:
        stack = []
        print(f"Please enter the string of the parentheses: {s}")
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == '[':
                stack.append('[')
            elif s[i] == '{':
                stack.append('{')
            elif s[i] == ')':
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
            elif s[i] == ']':
                if len(stack) ==0:
                    return False
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            elif s[i] == '}':
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False        
        

obj = solution()
finalresult = obj.isvalid("()[]{}")
print(finalresult)

    
        