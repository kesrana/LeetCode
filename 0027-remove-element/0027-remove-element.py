'''
[3,2,2,3]
val=3
k=2
   v
[3,2,2,3]
 ^
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #last known position where = val
        k = 0
        #iterate through nums
        for i in range(len(nums)):
        #only if does not = value
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
