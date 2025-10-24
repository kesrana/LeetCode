class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0

        for account in accounts:
            wealth = sum(account)
            if wealth > maxwealth:
                maxwealth = wealth
        return maxwealth

        