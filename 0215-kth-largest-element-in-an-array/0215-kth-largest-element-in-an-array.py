[6,5,4,3,2,1]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        return nums[k-1]
        