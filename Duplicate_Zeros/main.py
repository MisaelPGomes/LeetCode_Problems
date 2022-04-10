"""Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything."""

class Solution(object):
    def duplicateZeros(self, arr):
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                del arr[(len(arr) - 1)]
                i += 2
            else:
                i += 1




arr = [0,4,1,0,0,8,0,0,3]

solution = Solution()
solution.duplicateZeros(arr)