class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = strs[0]
        for i in range(1,len(strs)):
            if common_prefix == "":
                break
            j = 0
            isBreak = 0
            for j in range(len(common_prefix)):
                if (j > len(strs[i])-1):
                    isBreak = 1
                    break
                if common_prefix[j] != strs[i][j]:
                    isBreak = 1
                    break
            print "i={},j={}".format(i,j)
            print "strs[i][:j+1]={}".format(strs[i][:j+1])
            print "strs[i][:j]={}".format(strs[i][:j])
            if isBreak == 1:
                common_prefix = strs[i][:j]
            else:
                common_prefix = strs[i][:j+1]
            if common_prefix == "":
                break
        return common_prefix