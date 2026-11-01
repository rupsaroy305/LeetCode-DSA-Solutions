class Solution:
    def rangeBitwiseAnd(self, left, right):
        t=0
        while left!=right:
            left>>=1
            right>>=1
            t+=1

        return left<<t