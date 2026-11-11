from decimal import Decimal, getcontext
class Solution:
    def myPow(self, x, n):
        getcontext().prec=50
        x=Decimal(str(x))
        if n<0:
            x=1/x
            n=-n
        result=Decimal(1)
        while n>0:
            if n%2==1:
                result*=x
            x*=x
            n//=2
        return float(result)