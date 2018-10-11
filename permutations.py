"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.rt = []
        self._run(nums, [])
        return self.rt
    
    def _run(self, nums, lst):
        if len(nums) == 1:
            self.rt.append(lst+nums)
            return
        for i in range(len(nums)):
            self._run(nums[:i]+nums[i+1:], lst+[nums[i]])
