class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        for val in s:
            
            if val in hashMap:
                hashMap[val] += 1
            else:
                hashMap[val] = 1
        
        for key, val in hashMap.items():
            if val == 1:
                for i in range(len(s)):
                    if s[i] == key:
                        return i
                    
                    
        return -1
            