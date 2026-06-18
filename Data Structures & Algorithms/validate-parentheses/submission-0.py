class Solution:
    def isValid(self, s: str) -> bool:
        D = {')': '(', '}': '{', ']': '['}

        stack = []
        for i in range(len(s)):
            if s[i] in D:
                if stack and stack[-1] == D[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return not stack
