#test cases

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        #corner case
        if len(s) < 3:
            return []
        
        #define result list and first variable
        result = []
        first = 0

        for i in range(1, len(s)):
            #if theres a mismatch
            if s[i] != s[i-1]:
                if i - first >= 3:
                    result.append([first, i-1])
                first = i
        #if theres no mismatch/checking for the last group
        if len(s) - first >= 3:
            result.append([first, len(s)-1])
        return result

