# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tem=l1
        s=""
        while tem:
            s=s+str(tem.val)
            tem=tem.next
        s1=""
        tem=l2
        while tem:
            s1=s1+str(tem.val)
            tem=tem.next
        su=str(int(s[::-1])+int(s1[::-1]))
        a=su[::-1]
        print(a)
        ans=ListNode(0)
        tem=ans
        for i in range(len(a)):
            tem.next=ListNode(int(a[i]))
            tem=tem.next
        return ans.next
    
        