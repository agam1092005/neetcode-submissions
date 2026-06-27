class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket_stack = []
        star_stack = []

        for idx, val in enumerate(s):
            if val == '(':
                bracket_stack.append(idx)
            elif val == '*':
                star_stack.append(idx)
            else:
                if not bracket_stack and not star_stack:
                    return False
                
                if bracket_stack:
                    bracket_stack.pop()
                else:
                    star_stack.pop()
                
        while bracket_stack and star_stack:
            if bracket_stack.pop() > star_stack.pop():
                return False
        
        return not bracket_stack