"""35. Search Insert Position Leet Code
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #nums = [1, 3, 5, 6]
        length = len(nums)
        half = int(length/2)
        inferior_lim = 0
        superior_lim = length
        if target >= nums[half]:
            inferior_lim = half
            if target in nums:
                for position in range(inferior_lim, superior_lim):
                    num = nums[position]
                    if num == target:
                        return position
            else:
                for position in range(inferior_lim, superior_lim):
                    num = nums[position]
                    if num < target < nums[superior_lim - 1]:
                        superior_lim -=1
                    elif target > nums[superior_lim - 1]:
                        return superior_lim
                    else:
                        return position


        else:
            superior_lim = half
            if target in nums:
                for position in range(inferior_lim, superior_lim):
                    num = nums[position]
                    if num == target:
                        return position
            else:

                count = 0
                for num in nums[:superior_lim]:
                    if num < target:
                        count +=1


                return count











        #else:
        #    superior_lim = half
        #    for position in range(inferior_lim, superior_lim):
        #        num = nums[position]
        #        if num == target:
        #            print(position)





test = Solution()
print(test.searchInsert([1, 3, 5], 4))