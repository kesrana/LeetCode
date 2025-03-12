class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freqMap = Counter(nums)
        result = max(freqMap, key = freqMap.get)
        return result
        
            



            