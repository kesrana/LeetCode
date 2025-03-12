class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i**2)
        sorted_ans = sorted(ans)
        return sorted_ans
            