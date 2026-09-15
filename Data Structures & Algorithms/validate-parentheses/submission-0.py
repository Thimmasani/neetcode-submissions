class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'[':']','(':')', '{':'}'}

        stack = []

        for i in s:
            if i in lookup: stack.append(i)
            elif not stack: return False
            else:
                if i==lookup[stack[-1]]: stack.pop()
                else : return False
        
        return False if stack else True