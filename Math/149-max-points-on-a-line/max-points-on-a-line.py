class Solution:
    def maxPoints(self, points):
        n=len(points)
        if n<=2:
            return n
        answer= 0
        for i in range(n):
            slopes={}
            same=0
            max_count=0
            for j in range(i+1,n):
                dx=points[j][0]-points[i][0]
                dy=points[j][1]-points[i][1]
                if dx==0:
                    slope="vertical"
                elif dy==0:
                    slope="horizontal"
                else:
                    gcd=self.gcd(abs(dx), abs(dy))
                    dx=dx//gcd
                    dy=dy//gcd
                    if dx<0:
                        dx=-dx
                        dy=-dy
                    slope=(dy, dx)
                slopes[slope]=slopes.get(slope,0)+1
                max_count=max(max_count,slopes[slope])
            answer=max(answer,max_count+1)
        return answer
    def gcd(self,a,b):
        while b:
            a, b= b,a%b
        return a