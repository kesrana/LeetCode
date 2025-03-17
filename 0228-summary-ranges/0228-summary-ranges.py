class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i] == nums[i+1] -1:
                i += 1
            
            if start != nums[i]:
                result.append(str(start) + "->" + str(nums[i]))
            
            else:
                result.append(str(nums[i]))
            
            i+= 1

        return result
            



        