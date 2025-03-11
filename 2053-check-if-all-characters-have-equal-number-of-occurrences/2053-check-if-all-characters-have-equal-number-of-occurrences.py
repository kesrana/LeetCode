class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        sMap = Counter(s)
        result = set(sMap.values())
        if len(result) == 1:
            return True
        else:
            return False

'''
first test case: "abcabc" check functionality 
assertequal(input, expected results)

2nd test case: "aaaaaaa" return true

3rd test case: aaabbbbb return false

4th test case: ""

5th test case: numbers function wouldnt run takes string
'''
                      

