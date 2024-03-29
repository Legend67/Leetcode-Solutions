class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = []
    
        for i in nums:
            x = abs(i) - 1
            if nums[x] < 0:
                d.append(abs(i))
            else:
                nums[x] *= -1
        return d
