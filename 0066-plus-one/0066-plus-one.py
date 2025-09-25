class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ""
        ans = []
        for i in digits:
            digit += str(i)
        
        digit_int = int(digit) + 1
        digit = str(digit_int)
        for i in range(len(digit)):
            ans.append(int(digit[i]))
        return ans
        
        