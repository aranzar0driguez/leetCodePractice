class Solution(object):
    def longestCommonPrefix(self, strs):

        output = ""

        #keeps track of every letter in the first word 
        for i in range(len(strs[0])):

            #Need to iterate through the words in the strs array 
            for s in strs:
                #compares different words but same char
                if i == len(s) or s[i] != strs[0][i]:
                    return output

            output += strs[0][i]
        return output

            
        """
        :type strs: List[str]
        :rtype: str
        """
        