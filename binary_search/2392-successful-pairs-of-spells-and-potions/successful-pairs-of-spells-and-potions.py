class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n=len(potions)
        
        def count(p):
            left=0
            right=n-1
            ans=n
            
            while left<=right:
                mid=(left+right)//2
                
                if potions[mid]*p>=success:
                    ans=mid
                    right=mid - 1
                else:
                    left=mid+1
            
            return n-ans
        
        result=[]
        
        for s in spells:
            result.append(count(s))
        
        return result
