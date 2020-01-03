from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                low, high = j + 1, len(nums) - 1
                while low < high:
                    four_sum = nums[i] + nums[j] + nums[low] + nums[high]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif four_sum < target:
                        low += 1
                    else:
                        high -= 1

        return res


if __name__ == "__main__":
    nums = [0, -1, 0, 1, -2, -5, 3, 5, 0]
    nums.sort()
    print(nums)
    sol = Solution()
    res = sol.fourSum(nums, 6)
    print(res)
