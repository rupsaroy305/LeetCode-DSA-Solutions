import bisect
class MedianFinder:
    def __init__(self):
        self.nums=[]
    def addNum(self,num):
        bisect.insort(self.nums,num)
    def findMedian(self):
        n=len(self.nums)
        if n%2:
            return self.nums[n//2]
        return (self.nums[n//2-1]+self.nums[n//2])/2