class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqMap = Counter(nums)
        result = sorted(freqMap, key=freqMap.get, reverse=True)
        return result[:k]
        
        