class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        leftptr = 0
        rightptr = len(s) - 1

        while leftptr < rightptr:
            if not self.is_vowel(slist[leftptr]):
                leftptr += 1
                continue
            if not self.is_vowel(slist[rightptr]):
                rightptr -= 1
                continue
            slist[leftptr], slist[rightptr] = slist[rightptr], slist[leftptr]

            leftptr += 1
            rightptr -= 1
        return "".join(slist)


    def is_vowel(self, char: str) -> bool:
        return char in "AEIOUaeiou"