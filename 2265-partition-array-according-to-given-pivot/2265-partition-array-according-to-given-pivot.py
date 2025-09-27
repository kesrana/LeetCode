'''
[9,12,5,10,14,3,10]
[3,5,9,10,10,12,14], pivot = 10
  
'''

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #define three lists and concatenate them together at the end
        lessThan = []
        equal = []
        greaterThan = []

        for num in nums:
            if num < pivot:
                lessThan.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greaterThan.append(num)
        return lessThan + equal + greaterThan


        
        


        