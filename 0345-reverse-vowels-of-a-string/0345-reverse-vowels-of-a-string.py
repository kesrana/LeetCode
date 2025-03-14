class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        leftptr = 0
        rightptr = len(slist) - 1

        while leftptr < rightptr:
            if self.is_vowel(slist[leftptr]) and self.is_vowel(slist[rightptr]):
                temp = slist[leftptr]
                slist[leftptr] = slist[rightptr]
                slist[rightptr] = temp
                leftptr += 1
                rightptr -= 1
            elif self.is_vowel(slist[leftptr]) and not self.is_vowel(slist[rightptr]):
                rightptr -= 1
            elif not self.is_vowel(slist[leftptr]) and self.is_vowel(slist[rightptr]):
                leftptr += 1
            else:
                rightptr -= 1
                leftptr += 1

        ans = "".join(slist)
        return ans

    def is_vowel(self, char: str) -> bool:
        return True if char in "aeiouAEIOU" else False