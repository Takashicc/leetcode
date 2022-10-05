# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]

from typing import List


class Solution:
    # First solution
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         num1 = nums[i]
    #         remaining = target - num1
    #         for j in range(i + 1, len(nums)):
    #             num2 = nums[j]
    #             if remaining == num2:
    #                 return [i, j]

    # Second solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in lookup:
                return [lookup[remaining], i]
            else:
                lookup[num] = i


def main():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]


if __name__ == '__main__':
    main()
