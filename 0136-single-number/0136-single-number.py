class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        for key, value in freqMap.items():
            if value == 1:
                return key
                

            