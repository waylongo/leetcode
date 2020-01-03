from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            if nums[low] == val:
                nums[low], nums[high], high = nums[high], nums[low], high-1
            else:
                low += 1
        print(nums)
        return low

if __name__ == "__main__":
    nums = [3,2,2,3,2]
    print(nums)
    sol = Solution()
    res = sol.removeElement(nums, 3)
    print(res)