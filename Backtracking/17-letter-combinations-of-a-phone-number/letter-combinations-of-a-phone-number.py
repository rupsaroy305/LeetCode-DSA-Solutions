class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = []
        
        def functions_rupsa(i, path):
            if i == len(digits):
                res.append(path)
                return

            for ch in phone[digits[i]]:
                functions_rupsa(i + 1, path + ch)

        functions_rupsa(0, "")
        return res