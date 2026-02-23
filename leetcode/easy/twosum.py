from typing import List


# -------------------------------------------------------------------------
# Two Sum - Brute Force  |  Time: O(n²)  |  Space: O(1)
#
# Check every possible pair of numbers using nested loops. For each element,
# scan every element that comes after it to see if the two add up to target.
# Simple but slow — as the list grows, the number of comparisons grows fast.
# -------------------------------------------------------------------------
class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# -------------------------------------------------------------------------
# Two Sum - Hashmap  |  Time: O(n)  |  Space: O(n)
#
# Trade memory for speed by building a dictionary that maps each number to
# its index. Then loop through again: for each number, calculate the
# complement (target - num) and check if it already exists in the hashmap.
# A dictionary lookup is O(1), so we cut the overall time from O(n²) to O(n).
# -------------------------------------------------------------------------
class SolutionHashmap:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []
