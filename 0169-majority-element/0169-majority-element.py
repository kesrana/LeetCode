from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_map = defaultdict(int)
        for i in range(len(nums)):
            num_map[nums[i]] += 1
        
        threshold = len(nums) // 2

        for key, value in num_map.items():
            if value > threshold:
                return key
        
        

        
            



            