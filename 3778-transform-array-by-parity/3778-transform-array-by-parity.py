class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        #iterate through nums and create answer list
        result = []
        for i, num in enumerate(nums):
            if num % 2 == 0:
                result.append(0)
            else:
                result.append(1)
        return sorted(result)

        