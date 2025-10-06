class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        #double for loop to find + or -
        for operation in operations:
            for char in operation:
                if char == "-" in operation:
                    x -= 1
                    break
                elif char == "+" in operation:
                    x += 1
                    break
        return x
                
        