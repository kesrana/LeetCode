class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numSet1 = set(nums1)
        numSet2 = set(nums2)

        diff1 = list(numSet1 - numSet2)
        diff2 = list(numSet2 - numSet1)

        return [diff1, diff2]
