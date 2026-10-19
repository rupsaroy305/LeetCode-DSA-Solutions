from collections import deque
class Solution:
    def minMutation(self,startGene,endGene,bank):
        bank=set(bank)
        q=deque([(startGene,0)])
        seen={startGene}
        genes='ACGT'
        while q:
            gene,steps=q.popleft()
            if gene==endGene:
                return steps
            for i in range(8):
                for c in genes:
                    newGene=gene[:i]+c+gene[i+1:]
                    if newGene in bank and newGene not in seen:
                        seen.add(newGene)
                        q.append((newGene,steps+1))
        return -1