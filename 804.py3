class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        x=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        xx=set()
        
        for i in words:
            e=""
            for j in i:
                m=ord(j)-97
                e+=x[m]
            xx.add(e) 
        return(len(xx))
