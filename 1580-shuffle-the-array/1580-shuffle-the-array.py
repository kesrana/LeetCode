class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if n + i >= len(nums):
                break
            result.append(nums[i])
            if n + i < len(nums):
                result.append(nums[n+i])
            else:
                break
        return result

            

        
        