class ListNode(object):
    def __init__(self,x):
        self.val= x
        self.next=None

class Solution:
    def add_two_no(self,l1,l2,c=0):
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)


        if(l1.next!=None or l2.next!= None or c!=0):
            if (l1.next == None):
                l1.next = ListNode(0)
            if (l2.next == None):
                l2.next = ListNode(0)
            ret.next = self.add_two_no(l1.next, l2.next, c)
        return ret



l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
result=Solution().add_two_no(l1,l2)
while result:
    print(f"{result.val}",end=' ')
    result=result.next

