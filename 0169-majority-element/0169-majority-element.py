class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        result = max(freqMap, key = freqMap.get)
        return result
        
            



            