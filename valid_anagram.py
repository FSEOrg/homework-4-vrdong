class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.getKey(s) == self.getKey(t):
            return True
        return False
    
    def getKey(self, s: str):
        key = [0] * 26
        for c in s:
            key[ord(c)- ord('a')] += 1
        return key       
