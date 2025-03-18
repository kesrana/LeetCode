class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedNum = 0
        nums.sort()
        i = 0
        for i in range(len(nums)):
            if nums[i] == expectedNum:
                expectedNum += 1    
            else:
                if i > len(nums):
                    expectedNum += 1
                    break
                return expectedNum
        return expectedNum
        

