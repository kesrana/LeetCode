class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #initialize hashset and turn it into a list
        nums = sorted(list(set(nums)))
        nums_reverse = reversed(nums)
        result = float('inf')
        iterate = 0

        #use a for loop to find the third maximum number
        for i, num in enumerate(nums_reverse):
            if num < result:
                result = num
                iterate += 1
            if iterate >= 3 or i == len(nums) - 1:
                if len(nums) == 2:
                    return max(nums)
                return result
            
            
            




        