class Solution:
    def minFlips(self,a,b,c):
        flips=0

        while a or b or c:
            abit=a&1
            bbit=b&1
            cbit=c&1

            if cbit==0:
                if abit==1:
                    flips+=1
                if bbit==1:
                    flips+=1

            else:
                if abit==0 and bbit==0:
                    flips+=1

            a>>=1
            b>>=1
            c>>=1

        return flips
