class Solution:
    def suggestedProducts(self,products,searchWord):
        products.sort()

        ans=[]
        prefix=""

        for ch in searchWord:
            prefix+=ch
            temp=[]

            for p in products:
                if p.startswith(prefix):
                    temp.append(p)

                if len(temp)==3:
                    break

            ans.append(temp)

        return ans
        