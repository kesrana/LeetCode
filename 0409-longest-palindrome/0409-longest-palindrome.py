class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqMap = Counter(s)
        result = 0
        has_odd_frequency = False

        for freq in freqMap.values():
            if freq % 2 == 0:
                result += freq

            else:
                result += freq - 1
                has_odd_frequency = True

        if has_odd_frequency == True:
            return result + 1

        return result

                
        