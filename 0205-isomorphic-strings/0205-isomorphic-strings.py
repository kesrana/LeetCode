'''
paper
p:0, a:1, e:2, r: 3
[0, 1, 0, 2, 3]
'''

from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        s_pattern = []
        t_pattern = []
        i, j = 0, 0

        for char in s:
            if char not in s_map:
                s_map[char] = i
                i+=1
            s_pattern.append(s_map[char])
        for char in t:
            if char not in t_map:
                t_map[char] = j
                j+=1
            t_pattern.append(t_map[char])
        return s_pattern == t_pattern




