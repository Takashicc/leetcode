# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List


class Solution:
    # First solution
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            if num in lookup:
                return True
            lookup[num] = 1
        return False


def main():
    assert Solution().containsDuplicate([1, 2, 3, 1]) is True
    assert Solution().containsDuplicate([1, 2, 3, 4]) is False
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


if __name__ == '__main__':
    main()
