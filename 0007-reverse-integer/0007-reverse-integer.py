class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = -1
            x = abs(x)
        else:
            s = 1
    
        r = int(str(x)[::-1]) * s
    
        if r < -2**31 or r > 2**31 - 1:
            return 0
        else:
            return r
