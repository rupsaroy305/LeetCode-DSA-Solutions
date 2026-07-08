class Solution:
    def reverseWords(self,s):
        words=s.split()
        ans=[]
        for i in range(len(words)-1,-1,-1):
            ans.append(words[i])
        return " ".join(ans)

        