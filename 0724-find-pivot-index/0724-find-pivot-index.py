class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sumLeft = sum(nums[:i])
            sumRight = sum(nums[i+1:])
            if sumLeft == sumRight:
                return i
        return -1
        