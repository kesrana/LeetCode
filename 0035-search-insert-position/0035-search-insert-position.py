class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = first + (last - first) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
                
        return first
        