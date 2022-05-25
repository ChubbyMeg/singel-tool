# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def linklist_to_str(self,linklst):
        str = ""
        while linklst:
            if str == "":
                str = linklst.val
                linklst = linklst.next
            else:
                str = "{}{}".format(linklst.val, str)
                linklst = linklst.next
        return str
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode = [2,4,3]
        :type l2: ListNode = [5,6,4]
        :rtype: ListNode
        """
        a = self.linklist_to_str(l1) #a=342
        b = self.linklist_to_str(l2) #b=465
        c = str(int(a)+int(b)) #c=807
        d = c[::-1] #d=708
        
        self.head = ListNode(d[0])
        r = self.head
        p = self.head
        for i in d[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r
