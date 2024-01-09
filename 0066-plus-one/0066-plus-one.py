class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        result = []

        for i in range(len(digits) - 1, -1, -1):
            cs = digits[i] + c
            result.insert(0, cs % 10)
            c = cs // 10

        if c:
            result.insert(0, c)

        return result