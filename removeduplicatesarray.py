#Creates two pointers, one that tracks the num of unique values and 
#another one that tracks current element in array to compare uniqueness 


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[l] = nums[i]
                l += 1

        return l
