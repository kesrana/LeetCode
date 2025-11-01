class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        j = 0

        sorted_g = sorted(g)
        sorted_s = sorted(s)

        while i < len(sorted_g) and j < len(sorted_s):
            if sorted_g[i] <= sorted_s[j]:
                sorted_s[j] -= sorted_g[i]
                i += 1
            j += 1
        
        return i
            



        