class Solution:
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        mp={}
        for c in s:
            mp[c]=mp.get(c,0)+1
        for c in t:
            if c not in mp:
                return False
            mp[c]-=1
            if mp[c]<0:
                return False
        return True