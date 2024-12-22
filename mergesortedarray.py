"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

nums1 = [2,2,3,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3

# last index of nums1
pointer = m + n - 1

while n > 0 and m > 0:
    if nums2[n - 1] > nums1[m - 1]:
        nums1[pointer] = nums2[n - 1]
        n -= 1
    else:
        nums1[pointer] = nums1[m - 1]
        m -= 1
    
    #shifts pointer back 
    pointer -= 1

# These are the leftovers that were NOT sorted
while n > 0:
    nums1[pointer] = nums2[n - 1]
    pointer, n = pointer - 1, n - 1


print(nums1)
