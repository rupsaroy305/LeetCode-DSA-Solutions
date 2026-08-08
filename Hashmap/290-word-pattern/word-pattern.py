class Solution:
    def wordPattern(self,pattern,s):
        words=s.split()
        if len(pattern)!=len(words):
            return False
        mp1={}
        mp2={}
        for i in range(len(pattern)):
            a=pattern[i]
            b=words[i]
            if a in mp1 and mp1[a]!=b:
                return False
            if b in mp2 and mp2[b]!=a:
                return False
            mp1[a]=b
            mp2[b]=a
        return True