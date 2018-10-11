"""

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dic = {
            '2': 'abc', '3': 'def', '4': 'ghi', 
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz',
        }
        if not digits: return []
        self.rt = []
        self.traversal(digits, 0, len(digits), '')
        return self.rt
    
    def traversal(self, digits, i, length, res):
        
        if i == length:
            self.rt.append(res)
            return 
        
        nums = self.dic[digits[i]]
        for k in range(len(nums)):
            self.traversal(digits, i+1, length, res+nums[k])
        