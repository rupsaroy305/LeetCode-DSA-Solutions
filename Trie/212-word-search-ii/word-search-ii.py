class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['$'] = word
        m, n = len(board), len(board[0])
        ans = []
        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node:
                return
            node = node[ch]
            if '$' in node:
                ans.append(node.pop('$'))
            board[i][j] = '#'
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, node)
            board[i][j] = ch
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        return ans