class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashCount = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in hashCount:
                hashCount[s[i]] = 0
    
            hashCount[s[i]] += 1
            
            
            if t[i] not in hashCount:
                hashCount[t[i]] = 0
            
            hashCount[t[i]] -= 1
            
                
        for val in hashCount.values():
            if val != 0:
                return False
            
        return True
            