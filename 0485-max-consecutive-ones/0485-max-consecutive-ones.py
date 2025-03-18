class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentLength = 0
        maxLength = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                currentLength += 1
            else:
                maxLength = max(maxLength, currentLength)
                currentLength = 0
        return max(maxLength, currentLength)


        