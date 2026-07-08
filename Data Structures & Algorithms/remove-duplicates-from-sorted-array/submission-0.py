class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        L = sorted(set(nums))
        nums[:len(L)] = L
        return len(L)