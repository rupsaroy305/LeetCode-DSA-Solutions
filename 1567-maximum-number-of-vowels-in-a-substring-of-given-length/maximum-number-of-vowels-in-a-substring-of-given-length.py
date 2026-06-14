class Solution:
    def maxVowels(self, s, k):
        vowels = set("aeiou")
        
        window_count = 0
        
        # first window
        for i in range(k):
            if s[i] in vowels:
                window_count += 1
        
        max_count = window_count
        
        # slide window
        for i in range(k, len(s)):
            if s[i] in vowels:
                window_count += 1
            if s[i - k] in vowels:
                window_count -= 1
            
            if window_count > max_count:
                max_count = window_count
        
        return max_count