from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans =[]
        freqMap = Counter(nums)
        for key, value in freqMap.items():
            if value > len(nums) // 3:
                ans.append(key)
        return ans



        