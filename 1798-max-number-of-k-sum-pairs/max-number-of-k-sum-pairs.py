class Solution:
    def maxOperations(self, nums, k):
        freq = {}
        ops = 0
        
        for num in nums:
            complement = k - num
            
            if freq.get(complement, 0) > 0:
                ops += 1
                freq[complement] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1
        
        return ops