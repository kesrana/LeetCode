'''
takes in [1,8,9]
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #start from the last element in the list
        for i in range(len(digits)-1,-1,-1):
            #if the element in less than 9 we just add and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            #if its 9 or greater, turn it into 0 and continue the for loop
            digits[i] = 0
        #if every element was 9 or greater then we have to just concatenate a 1 in the first element
        return [1] + digits
            
            
        
        