from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #define hashmap 
        num_map = defaultdict(int)
        #store frequency of elements
        for i in range(len(nums)):
            num_map[nums[i]] += 1
        
        #find the most frequent element
        for key, value in num_map.items():
            if value > len(nums) // 2:
                return key
        return 0
        