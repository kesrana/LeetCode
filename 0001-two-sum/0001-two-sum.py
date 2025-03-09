class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unordered_map = {}
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]
            if comp in unordered_map:
                return [unordered_map[comp], i]
            unordered_map[nums[i]] = i 

        