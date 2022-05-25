# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = "" #reverse l1=[2,4,3] to a=342
        while l1:
            if a == "":
                a = l1.val
                l1 = l1.next
            else:
                a = "{}{}".format(l1.val, a)
                l1 = l1.next
        b = "" #reverse l2=[5,6,4] to b=465
        while l2:
            if b == "":
                b = l2.val
                l2 = l2.next
            else:
                b = "{}{}".format(l2.val, b)
                l2 = l2.next
        c = str(int(a)+int(b)) #c=807
        d = c[::-1] #d=708
        
		#trasfer d to ListNode
        self.head = ListNode(d[0])
        r = self.head
        p = self.head
        for i in d[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r