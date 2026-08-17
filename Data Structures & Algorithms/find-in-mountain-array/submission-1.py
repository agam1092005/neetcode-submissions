class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        L, R = 1, n-2
        
        while L <= R:
            mid = L + (R-L)//2
            left, middle, right = mountainArr.get(mid-1), mountainArr.get(mid), mountainArr.get(mid+1)
            
            if left < middle < right:
                L = mid+1
            elif left > middle > right:
                R = mid-1
            else:
                break

        peak = mid

        L, R = 0, peak-1
        while L <= R:
            mid = L + (R-L)//2
            if target > mountainArr.get(mid):
                L = mid+1
            elif target < mountainArr.get(mid):
                R = mid-1
            else:
                return mid


        L, R = peak, n-1
        while L <= R:
            mid = L + (R-L)//2
            if target < mountainArr.get(mid):
                L = mid+1
            elif target > mountainArr.get(mid):
                R = mid-1
            else:
                return mid
        
        return -1

        