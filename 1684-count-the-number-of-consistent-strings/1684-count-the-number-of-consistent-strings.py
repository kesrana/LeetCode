class Solution(object):
    def countConsistentStrings(self, allowed, words):
        result = 0
        for word in words:
            consistent = True
            for char in word:
                if char not in allowed:
                    consistent = False
                    break
            if consistent:
                result += 1
        return result
                



        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        