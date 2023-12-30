class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        lw = s.rfind(' ')
        if lw == -1:
            return len(s)
        else:
            return len(s[lw + 1:])