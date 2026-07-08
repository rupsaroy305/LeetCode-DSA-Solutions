class Solution:
    def romanToInt(self,s):
        value={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans=0
        i=0
        while i<len(s):
            if i+1<len(s) and value[s[i]]<value[s[i+1]]:
                ans+=value[s[i+1]]-value[s[i]]
                i+=2
            else:
                ans+=value[s[i]]
                i+=1
        return ans