class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lstr = ['(', '[', '{']
        rstr = [')', ']', '}']
        if s[0] in rstr:
            return False #first char can't be right str
        lst = []
        for i in range(len(s)):
            if s[i] in lstr:
                lst.insert(0, s[i]) #FILO
            else:
                if s[i] in rstr and len(lst) == 0:
                    return False #first char can't be right str
                if s[i] == ')' and lst[0] == '(':
                    lst.pop(0) #remove first left str
                elif s[i] == ']' and lst[0] == '[':
                    lst.pop(0)
                elif s[i] == '}' and lst[0] == '{':
                    lst.pop(0)
                else:
                    return False
        if len(lst) != 0:
            return False
        else:
            return True