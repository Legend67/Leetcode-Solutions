class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = [0] * 26  
    
        for i in s:
            c[ord(i) - ord('a')] += 1  
    
        for i in t:
            c[ord(i) - ord('a')] -= 1  
    
        return all(val == 0 for val in c)
        