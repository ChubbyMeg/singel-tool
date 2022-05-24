class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #1.目前prefix比現在的字串長
        #2.目前prefix比現在的字串短
        #3.目前prefix跟現在的字串一模一樣
        common_prefix = strs[0]
        if common_prefix == "":
            return ""
        for i in range(1,len(strs)):
            if len(common_prefix) <= len(strs[i]):
                max_len = len(common_prefix)
            else:
                max_len = len(strs[i])
            j = 0
            for j in range(0,max_len):
                if common_prefix[j] != strs[i][j]:
                    j -= 1
                    break
            print("curren prefix={}".format(common_prefix))
            print("j={}".format(j))
            common_prefix = strs[i][:j+1]
            print("new prefix={}".format(common_prefix))
            if common_prefix == "":
                break
        return common_prefix
