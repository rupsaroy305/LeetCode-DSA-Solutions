class Solution:
    def searchMatrix(self,matrix,target):
        m=len(matrix)
        n=len(matrix[0])
        l,r=0,m*n-1

        while l<=r:
            mid=(l+r)//2
            x=matrix[mid//n][mid%n]

            if x==target:
                return True
            elif x<target:
                l=mid+1
            else:
                r=mid-1

        return False