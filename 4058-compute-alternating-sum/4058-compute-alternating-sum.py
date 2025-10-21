class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result = 0
        #iterate through nums
        for i in range(len(nums)):
            #if even
            if i % 2 == 0:
                result += nums[i]
            #if odd
            else:
                result -= nums[i]
        return result
                    