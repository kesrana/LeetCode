class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrMap = Counter(arr)
        seen = set()
        for value in arrMap.values():
            if value in seen:
                return False
            seen.add(value)
            continue
        return True
