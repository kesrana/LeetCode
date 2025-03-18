class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                if num1[i] == num2[j]:
                    result.append(num1[i])
        return result

        