class Solution(object):
    def getConcatenation(self, nums):

        arrayLength = len(nums)

        for i in range(0, arrayLength):
            nums.append(nums[i])

        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        