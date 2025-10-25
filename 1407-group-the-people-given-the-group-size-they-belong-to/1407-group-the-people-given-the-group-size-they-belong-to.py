from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #initialize the result list
        result = []
        #store list in hash map to have quick loop ups for what group they shoul be in
        groupsizes_map = defaultdict(list)

        #iterate thorough the groupsizes and store the values in the hashmap
        for i in range(len(groupSizes)):
            groupsizes_map[groupSizes[i]].append(i)

        #define result and store the values of the dict in there
        result = []
        
        for key, value in groupsizes_map.items():
            for i in range(0, len(value), key):
                result.append(value[i:i+key])
        return result
            
        

            
            


        
        
        
        