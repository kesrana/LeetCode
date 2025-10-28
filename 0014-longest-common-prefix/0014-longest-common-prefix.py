class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #sort the list by alphabetical order so we only need to care about the first and last components of the list
        sorted_strs = sorted(strs)
        #defining variable for first and last element
        first = sorted_strs[0]
        last = sorted_strs[-1]
        result = ""
        for i in range(len(min(first, last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        return result
                
            
            