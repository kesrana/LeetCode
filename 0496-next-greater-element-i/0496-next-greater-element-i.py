from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums2_map = defaultdict(int)

        for i in range(len(nums2)):
            nums2_map[nums2[i]] = i
        
        for i in range(len(nums1)):
            idx = nums2_map[nums1[i]]
            found = False
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    result.append(nums2[j])
                    found = True
                    break
            if not found:
                result.append(-1)
        return result



        




        