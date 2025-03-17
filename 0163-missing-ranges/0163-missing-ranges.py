class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []

        if nums and nums[0] > lower:
            result.append([lower, nums[0]-1])

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                result.append([nums[i-1] + 1, nums[i] - 1])

        if nums and nums[-1] < upper:
            result.append([nums[-1] + 1, upper])
        
        if not nums:
            result.append([lower,upper])
        return result
        