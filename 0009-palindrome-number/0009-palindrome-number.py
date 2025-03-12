class Solution:
    def isPalindrome(self, x: int) -> bool:
        to_str = str(x)
        reverse_str = "".join(reversed(to_str))
        return to_str == reverse_str