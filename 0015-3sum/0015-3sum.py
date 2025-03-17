#sort the list into ascending order
#use three loops to find three different values that add up to 0
# im going make three values into tuple and then add it into list called result
#0, 1 ,1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sortedNum = sorted(nums)
        for i in range(len(sortedNum)):
            a = sortedNum[i]

            if a > 0:
                break
            if i > 0 and sortedNum[i-1] == sortedNum[i]:
                continue
            
            left, right = i+1, len(sortedNum) - 1
            while left < right:
                temp = a + sortedNum[left] + sortedNum[right]
                if temp < 0:
                    left += 1
                elif temp > 0:
                    right -= 1
                else:
                    result.append([a, sortedNum[left], sortedNum[right]])
                    left += 1
                    right -= 1
                    while sortedNum[left] == sortedNum[left-1] and left <right:
                        left += 1
                    while sortedNum[right] == sortedNum[right + 1] and left < right:
                        right -= 1
        return result
                    





                    
                
        

        