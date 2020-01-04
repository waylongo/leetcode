from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                l = r = mid
                while l > 0 and nums[l - 1] == nums[mid]:
                    l -= 1
                while r < len(nums) - 1 and nums[r + 1] == nums[mid]:
                    r += 1
                return [l, r]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]


if __name__ == "__main__":
    nums = [1]
    print(nums)
    sol = Solution()
    res = sol.searchRange(nums, 1)
    print(res)
