class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeq = 0
        currentSeq = 1
        sorted_nums = sorted(set(nums))

        if not nums:
            return 0
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                currentSeq += 1
            else:
                longestSeq = max(longestSeq, currentSeq)
                currentSeq = 1

        return max(longestSeq, currentSeq)


        

        