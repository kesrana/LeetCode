class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        #initialize result variable
        result = 0

        #iterate through the hours list and see who meets the target
        for i in range(len(hours)):
            #if meets target
            if hours[i] >= target:
                result += 1
        
        return result
        