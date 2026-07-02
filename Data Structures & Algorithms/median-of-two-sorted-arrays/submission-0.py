class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2
        merged.sort()

        n = len(merged)
        if n % 2 == 0:
            return (merged[(n // 2) - 1] + merged[n // 2]) / 2.0
        else:
            return merged[n // 2]