class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        result = 0
        s = 0
        p = 1
        for i in range(len(nums)):
            p *= nums[i]
            while p >= k:
                p /= nums[s]
                s += 1
            result += i - s + 1
        return result
