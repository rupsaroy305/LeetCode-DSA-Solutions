from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)
        
        radiant = deque()
        dire = deque()
        
        # store indices
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            
            # smaller index wins this round
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        
        return "Radiant" if radiant else "Dire"
