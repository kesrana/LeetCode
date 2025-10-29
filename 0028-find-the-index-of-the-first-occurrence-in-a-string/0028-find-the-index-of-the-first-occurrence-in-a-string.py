'''
sadbutsad
sad


while i < length of haystack and j < length needle:
    if i == j:
        result += 1

return result == j
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #iterate through haystack
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

            