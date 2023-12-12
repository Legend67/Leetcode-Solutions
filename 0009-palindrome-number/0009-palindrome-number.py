class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        o, r = x, 0

        while o != 0:
            digit = o % 10
            r = r * 10 + digit
            o //= 10

        return r == x