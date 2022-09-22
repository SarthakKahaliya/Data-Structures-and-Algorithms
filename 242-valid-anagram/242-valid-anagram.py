class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashCountS = dict()
        hashCountT = dict()
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in hashCountS:
                hashCountS[s[i]] = 0
            
            hashCountS[s[i]] += 1
            
            
            if t[i] not in hashCountT:
                hashCountT[t[i]] = 0
            
            hashCountT[t[i]] += 1
            
                
        for key in hashCountS.keys():
            if key not in hashCountS or key not in hashCountT:
                return False
            if hashCountS[key] != hashCountT[key]:
                return False
            
        return True
            