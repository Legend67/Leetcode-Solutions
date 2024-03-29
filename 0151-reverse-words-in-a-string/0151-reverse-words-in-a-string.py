class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        w = s.split()
        w.reverse()
        return ' '.join(w)
        