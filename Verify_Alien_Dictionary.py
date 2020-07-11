class Solution:
    def letterFind(self,letter):
    # order is fixed with 26 letters
        # for indx in range(len(order)):
        #     if letter == order[indx]:
        #         return indx
        return self.letterMap[letter]
    
    
    def compareString(self,str1,str2):
        L = min(len(str1),len(str2))
        for i in range(L):
            if self.letterFind(str1[i]) > self.letterFind(str2[i]):
                return False
            elif self.letterFind(str1[i]) < self.letterFind(str2[i]):
                return True
        if len(str1) > len(str2):
            return False
        else:
            return True
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        self.letterMap = {}
        for i in range(len(order)):
            self.letterMap[order[i]] = i        
        
        for j in range(len(words)-1):
            indx1 = j
            indx2 = j+1
            if not self.compareString(words[indx1],words[indx2]):
                return False
        return True
