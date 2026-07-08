class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif i == 'D':
                stack.append(2 * int(stack[-1]))
            else:
                stack.append(int(i))
        
        return sum(stack)
