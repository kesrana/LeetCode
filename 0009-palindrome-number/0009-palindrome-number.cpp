class Solution {
public:
    bool isPalindrome(int x) {
        string sX = to_string(x);
        string reverse(sX.rbegin(), sX.rend());
        return sX == reverse;
    }
};