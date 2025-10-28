'''
we need a roman to int transformer
use hashmap
check values after the current to see whether to add or subtract current roman in string
CODE:

hashmap[roman] = int
for i in range(len(string) - 1):
    if hashmap[roman] < the next roman in the string
        subtract from result
    else:
        add to result

add the last char in the string
'''
class Solution:         
    def romanToInt(self, s: str) -> int:
        #use hashmap for fast look ups from roman to int
        roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #now we iterate through the string to calculate the total int
        result = 0
        for i in range(len(s) - 1):
            #if greater than the next, add
            if roman_to_int[s[i]] > roman_to_int[s[i+1]]:
                result += roman_to_int[s[i]]
            #if less than the next, minus
            elif roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                result -= roman_to_int[s[i]]
            #if equal we add
            else:
                result += roman_to_int[s[i]]
        
        result += roman_to_int[s[-1]]

        return result



     

