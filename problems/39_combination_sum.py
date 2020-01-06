from typing import List

#backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, path, res)
        return res

    def dfs(self, candidates, target, idx, path, res):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in range(idx, len(candidates)):
            if candidates[i] > target: break
            self.dfs(candidates, target - candidates[i], i, path+[candidates[i]], res)



if __name__ == "__main__":
    nums = [2,3,6,7]
    print(nums)
    sol = Solution()
    res = sol.combinationSum(nums, 7)
    print(res)