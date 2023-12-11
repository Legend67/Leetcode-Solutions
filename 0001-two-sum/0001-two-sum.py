class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}

        i = 0
        while i < len(nums):
            n = nums[i]
            if n in dicts:
                return dicts[n], i
            else:
                dicts[target - n] = i
            i += 1
        return None