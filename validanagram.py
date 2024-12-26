"""
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.
"""

class Solution(object):
    def isAnagram(self, s, t):
        
        s_dict = {}
        t_dict = {}

        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        return s_dict == t_dict   
        

        """
        For this solution, you could also do from Collections import Counter 
        and then use the Counter(array) function to return back a dictionary!
        
        :type s: str
        :type t: str
        :rtype: bool
        """
        