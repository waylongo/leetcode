from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        print(candidates)
        self.dfs(candidates, target, 0, path, res)
        return res

    def dfs(self, candidates, target, idx, path, res):
        # print(target)
        if target < 0:
            return
        elif target == 0:
            res.append(path)
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            if i > idx and candidates[i] == candidates[i - 1]: continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)

if __name__ == "__main__":
    nums = [10,1,2,7,6,1,5]
    print(nums)
    sol = Solution()
    res = sol.combinationSum2(nums, 8)
    print(res)