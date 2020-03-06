# 133. Single Number
#
# Given a non-empty array of integers, every element appears twice
# except for one.  Find that single one.
#
# Note: Your algorithm should have a linear runtime complexity.  Could
# you implement it without using extra memory?  [No, not that I can
# figure out.]


def multiscan(nums):
    # Idea is to repeatedly check if the number at index 0 has a twin.
    # If not, win!  If so, fill in with numbers from end,
    n_nums = len(nums)
    while n_nums > 0:
        n1 = nums[0]
        found_duplicate = False
        for idx2 in range(1, n_nums):
            if n1 == nums[idx2]:
                # Found duplicate
                found_duplicate = True
                # Replace duplicate with end
                nums[idx2] = nums[n_nums - 1]
                # Replace initial with end
                nums[0] = nums[n_nums - 2]
                n_nums -= 2
                break
        if not found_duplicate:
            return n1


def sortscan(nums):
    nums = sorted(nums)
    n1 = nums[0]
    idx = 1
    while idx < len(nums):
        n2 = nums[idx]
        if n1 == n2:
            n1 = nums[idx + 1]
            idx += 2
        else:
            return n1
    return n1


class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for n, count in counts.items():
            if count == 1:
                return n

    def singleNumber_2(self, nums: List[int]) -> int:
        for idx1, n1 in enumerate(nums):
            for idx2, n2 in enumerate(nums):
                if idx1 == idx2:
                    continue
                if n1 == n2:
                    break
            if idx2 + 1 == len(nums) and (n1 != n2 or (idx1, n1) == (idx2, n2)):
                return n1

    def singleNumber_3(self, nums: List[int]) -> int:
        return multiscan(nums)

    def singleNumber_4(self, nums: List[int]) -> int:
        return sortscan(nums)

    singleNumber = singleNumber_4
