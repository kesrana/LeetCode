class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slowPointer = 0
        for fast in range(len(nums)):
            if nums[slowPointer] == 0 and nums[fast] != 0:
                nums[slowPointer], nums[fast] = nums[fast], nums[slowPointer]

            if nums[slowPointer] != 0:
                slowPointer += 1
        