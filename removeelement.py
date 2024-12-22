"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements 
may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

#scenario ONE
nums1 = [3,2,2,3]
val1 = 3


#scenario two 
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2

n = len(nums1)
pointer = 0

while pointer < n:
    if nums1[pointer] == val1:
        nums1[pointer] = nums1[n - 1]
        n -= 1

    else:
        pointer += 1     


k = n
print(k)
print(nums1)
