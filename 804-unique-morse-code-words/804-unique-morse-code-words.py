class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodeMapArray = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        indexOfCharInArrayCorrection = -97
        
        collection = set()
        
        for word in words:
            concatWord = ''
            for char in word:
                concatWord += morseCodeMapArray[ord(char)+indexOfCharInArrayCorrection]
            
            collection.add(concatWord)
            
        return len(collection)