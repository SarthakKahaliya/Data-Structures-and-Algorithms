class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for val in s:
            if val == '(':
                stack.append(')')
            elif val == '{':
                stack.append('}')
            elif val == '[':
                stack.append(']')
            elif val in ')}]':
                if not stack:
                    return False
                elif val == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True