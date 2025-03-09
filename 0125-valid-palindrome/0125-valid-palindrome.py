class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char.lower()        
        reversed_string = ''.join(reversed(new_s))
        return new_s == reversed_string

