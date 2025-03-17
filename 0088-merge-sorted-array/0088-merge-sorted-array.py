'''
nums1= [1,2,3,0,0,0], size = m, length of list = m + n
nums2 = [2,5,6], size = n
result: nums1 = [1,2,2,3,5,6]
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m,len(nums1)):
            nums1[i] = nums2[i-m]
        
        nums1.sort()
        return nums1


        

        """
        Do not return anything, modify nums1 in-place instead.
        """
        