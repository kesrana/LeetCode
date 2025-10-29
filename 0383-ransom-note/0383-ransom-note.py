from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)

        for key, value in ransom_freq.items():
            if ransom_freq[key] > magazine_freq[key]:
                return False
        return True