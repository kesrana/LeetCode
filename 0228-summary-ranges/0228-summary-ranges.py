class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            #if not consecutive
            if nums[i] != nums[i-1] + 1:
                #if start was the prev element corner case
                if start == nums[i-1]:
                    result.append(str(start))
                #else store the range
                else:
                    result.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        
        #we have to account for the end element in case there is no break.
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result

                    



