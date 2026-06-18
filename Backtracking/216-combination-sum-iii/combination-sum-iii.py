class Solution:
    def combinationSum3(self, k, n):
        res = []

        def functions_rupsa(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return

            for i in range(start, 10):
                if total + i > n:
                    continue

                path.append(i)
                functions_rupsa(i + 1, path, total + i)
                path.pop()

        functions_rupsa(1, [], 0)
        return res
        