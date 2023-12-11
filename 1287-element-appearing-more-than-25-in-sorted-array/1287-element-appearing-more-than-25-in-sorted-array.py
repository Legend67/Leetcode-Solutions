class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = defaultdict(int)

        for i in arr:
            c[i] += 1
        t = len(arr) / 4

        for k, v in c.items():
            if v > t:
                return k

        return -1