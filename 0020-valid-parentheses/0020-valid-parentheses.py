class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty list to represent the stack
        if len(s) % 2 != 0:
            return False
        else:
            mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False
        return not stack