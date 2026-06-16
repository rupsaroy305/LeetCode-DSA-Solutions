class Solution:
    def findKthLargest(self,nums,k):
        count={}
        
        for num in nums:
            if num not in count:
                count[num]=0
                
            count[num]+=1
        
        current=0
        
        for num in range(10000,-10001,-1):
            if num in count:
                current+=count[num]
                if current>=k:
                    return num