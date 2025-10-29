class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #iterate through possible substrings. Max is len(s) //2 as if substring > half of OG string, its not a substring
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                substring = s[:i]
                #if substring can form OG string
                if substring * (len(s)//i) == s:
                    return True
        return False


                
            
            
        