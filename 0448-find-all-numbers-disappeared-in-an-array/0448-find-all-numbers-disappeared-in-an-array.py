class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #define result list
        result = []
        numSet = set(nums)

        #define n
        n = len(nums)

        #iterate numbers to n and compare with nums if they are in nums
        for i in range(1, n+1):
            if i not in numSet:
                result.append(i)
        return result

        