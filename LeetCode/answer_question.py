#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# LeetCode


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = {}
        for index, i in enumerate(nums):
            if target - i in hashtable:
                return [hashtable[target - i], index]
            hashtable[i] = index


# nums_list = [2, 7, 11, 15]
# targ = 9
nums_list = [-3, 4, 3, 90]
targ = 0
solution = Solution()
print(solution.twoSum(nums_list, targ))
