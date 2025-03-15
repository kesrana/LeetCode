class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array
        answer = [1] * len(nums)
        
        # Left pass: Calculate product of all elements to the left of each index
        product = 1
        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]
        
        # Right pass: Calculate product of all elements to the right of each index
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]
        
        return answer