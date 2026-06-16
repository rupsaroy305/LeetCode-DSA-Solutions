class SmallestInfiniteSet:

    def __init__(self):
        self.numbers=set()
        self.current=1

    def popSmallest(self):
        if self.numbers:
            smallest=min(self.numbers)
            self.numbers.remove(smallest)
            return smallest
        
        ans=self.current
        self.current+=1
        return ans

    def addBack(self,num):
        if num<self.current:
            self.numbers.add(num)