class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        
        for i in tokens:
            if i in op:
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                if i == '+':
                    ans = pop2+pop1
                elif i == '-':
                    ans = pop2-pop1
                elif i == '*':
                    ans = pop2*pop1
                else:
                    ans = float(pop2/pop1)
                
                stack.append(int(ans))
            else:
                stack.append(int(i))

        return stack[0]