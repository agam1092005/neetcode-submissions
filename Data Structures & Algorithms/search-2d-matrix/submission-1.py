class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = -1
        for i in matrix:
            print(i)
            if target >= i[0] and target <= i[-1]:
                idx = matrix.index(i)
                break
            else:
                continue
        
        if idx == -1:
            return False
        else:
            arr = matrix[idx]
            L, R = 0, len(arr)-1

            while L <= R:
                mid = L + (R-L)//2

                if target > arr[mid]:
                    L = mid+1
                elif target < arr[mid]:
                    R = mid-1
                else:
                    return True
        return False
        
