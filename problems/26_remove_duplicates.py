from typing import List


# hash table
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict = {}
        idx = 0
        for i in nums:
            if i not in dict:
                dict[i] = i
                nums[idx] = i
                idx += 1
        print(nums)
        return len(dict)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            nums[idx] = nums[i]
            idx += 1
        return idx

# two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ii, jj = 1, 1
        while jj < len(nums):
            if nums[ii-1] != nums[jj]:
                nums[ii] = nums[jj]
                ii += 1
            jj += 1
        return ii

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(nums)
    sol = Solution()
    res = sol.removeDuplicates(nums)
    print(res)
