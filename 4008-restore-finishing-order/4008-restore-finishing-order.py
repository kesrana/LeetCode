from collections import defaultdict
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        #initialize the hashmap to store the friend and what place they finished
        friendsMap = defaultdict(int)

        for i in range(len(order)):
            if order[i] in friends:
                friendsMap[order[i]] = i
        
        #sort the hashmap by the second index of the tuple that being outputed which is the value (not key)
        friendsMap_sorted = sorted(friendsMap.items(), key=lambda x: x[1])

        result = [key for key, value in friendsMap_sorted]
        return result
        
        


        



        

        