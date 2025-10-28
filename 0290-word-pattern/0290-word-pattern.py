class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #split the strings in s
        s = s.split()
        #compare the lists at the end to see if the pattern matches
        pattern_list = []
        s_list = []
        #hashmap transforming char into int and storing number pattern
        pattern_map = {}
        s_map = {}
        i = 0
        j = 0

        for char in pattern:
            if char not in pattern_map:
                pattern_map[char] = i
                i += 1
            pattern_list.append(pattern_map[char])
        
        for char in s:
            if char not in s_map:
                s_map[char] = j
                j += 1
            s_list.append(s_map[char])
        
        return pattern_list == s_list
         
        