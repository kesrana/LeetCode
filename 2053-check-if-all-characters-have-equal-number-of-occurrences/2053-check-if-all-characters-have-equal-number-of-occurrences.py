class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        sMap = Counter(s)
        result = set(sMap.values())
        if len(result) == 1:
            return True
        else:
            return False
                      

