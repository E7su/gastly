class Solution:
    def merge(self, nums1, m, nums2, n):
        index = len(nums1) - 1
        m -= 1
        n -= 1
        while (n >= 0):
            if (m < 0 or nums1[m] < nums2[n]):
                nums1[index] = nums2[n]
                n -= 1
            else:
                nums1[index] = nums1[m]
                m -= 1
            index -= 1
