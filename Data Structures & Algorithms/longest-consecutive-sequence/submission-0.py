class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        cmax = 1
        c = 1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i] - 1:
                c += 1
                cmax = max(c, cmax)
            else:
                c = 1

        return cmax