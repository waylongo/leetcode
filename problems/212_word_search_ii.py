from typing import List
# TLE

class Solution:
    def findWords(self, A: List[List[str]], words: List[str]) -> List[str]:
        res = []

        for word in words:
            if self.exist(A, word):
                res.append(word)
        return res

    def exist(self, A: List[List[str]], word: str) -> bool:

        for i in range(len(A)):
            for j in range(len(A[0])):
                if self.dfs(A, i, j, word, 0):
                    return True
        return False

    def dfs(self, A, i, j, word, index):
        if i < 0 or i > len(A) - 1 or j < 0 or j > len(A[0]) - 1:
            return False

        if A[i][j] != word[index]:
            return False

        if index == len(word) - 1:
            return True

        tmp = A[i][j]
        A[i][j] = "#"
        res = self.dfs(A, i - 1, j, word, index + 1) or \
              self.dfs(A, i + 1, j, word, index + 1) or \
              self.dfs(A, i, j - 1, word, index + 1) or \
              self.dfs(A, i, j + 1, word, index + 1)
        A[i][j] = tmp
        return res

if __name__ == "__main__":
    board = \
    [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    sol = Solution()
    res = sol.findWords(board, words)
    print(res)