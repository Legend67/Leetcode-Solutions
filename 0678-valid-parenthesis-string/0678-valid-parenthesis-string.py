class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_open = []
        stack_star = []
    
        for i in range(len(s)):
            if s[i] == '(':
                stack_open.append(i)
            elif s[i] == '*':
                stack_star.append(i)
            elif s[i] == ')':
                if stack_open:
                    stack_open.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
    
        while stack_open and stack_star:
            if stack_open[-1] > stack_star[-1]:
                return False
            stack_open.pop()
            stack_star.pop()
    
        return len(stack_open) == 0
