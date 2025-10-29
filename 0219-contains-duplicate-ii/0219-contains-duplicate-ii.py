from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #create hashmap to store the number and then the index for value
        num_map = defaultdict(int)

        for i in range(len(nums)):
            #if its already in the dict
            if nums[i] in num_map and abs(i - num_map[nums[i]]) <= k:
                return True
            #else store in dict
            num_map[nums[i]] = i
        
        return False

