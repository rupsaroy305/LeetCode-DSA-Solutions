class Solution:
    def uniqueOccurrences(self, arr):
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        counts = list(freq.values())
        
        return len(counts) == len(set(counts))