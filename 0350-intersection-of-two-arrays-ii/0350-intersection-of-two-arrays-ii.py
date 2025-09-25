class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        #sort the two lists and use two pointer method
        nums1.sort()
        nums2.sort()

        #initialize two pointer method one pointer for each list
        ptr1 = 0
        ptr2 = 0

        #iterate through both lists and stop if one of the ptrs go to the end of the list
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            #if numbers are equal add to result
            if nums1[ptr1] == nums2[ptr2]:
                result.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1
        return result

