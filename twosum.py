class Solution(object):
    def twoSum(self, nums, target):

        map = {}

        for i in range(len(nums)):
            map[nums[i]] = i

        for n in range(len(nums)):
            y = target - nums[n]
            if y in map and n!= map[y]:
                return [map[y], n]
                            
        """
        This solution utilizes hashmaps to store the index values at which specific values from 
        the nums array are stored. 

        It then iterates through the nums array and attempts to find a value in the hashmap that
        can be added (to the current number in the iteration) to reach the target.

        Lastly, it doubles check to ensure that the current index value is not the same as the 
        one found in the index. 
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        