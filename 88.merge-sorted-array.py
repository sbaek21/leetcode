#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index = m+n-1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[index] = nums1[m-1]
                index -= 1
                m -= 1
            elif nums1[m-1] < nums2[n-1]:
                nums1[index] = nums2[n-1]
                index -= 1
                n -= 1

        if m == 0:
            if n > 0:
                for i in range(n-1, -1, -1):
                    nums1[i] = nums2[i]

# @lc code=end

