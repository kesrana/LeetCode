class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        def self_dividing(num: int) -> bool:
            for digit in str(num):
                if digit == "0" or num % int(digit) != 0:
                    return False
            return True
        
        for num in range(left, right + 1):
            if self_dividing(num):
                result.append(num)
        return result
