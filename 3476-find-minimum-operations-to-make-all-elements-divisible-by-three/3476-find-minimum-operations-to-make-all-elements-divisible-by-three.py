class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #initialize result
        result = 0
        for i in range(len(nums)):
            #check if divisible by 3
            if nums[i] % 3 == 0:
                continue
            else:
                result += 1
        return result
        