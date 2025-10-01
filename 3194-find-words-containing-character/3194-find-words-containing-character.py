class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        #iterate through the words in the list
        for i, word in enumerate(words):
            #iterate through the characters in the word
            for char in word:
                if char == x:
                    result.append(i)
                    #break out of this inner for loop and go onto the next outer for loop
                    break
        return result



        
            
        