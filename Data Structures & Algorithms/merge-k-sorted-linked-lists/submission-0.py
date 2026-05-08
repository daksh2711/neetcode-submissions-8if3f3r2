# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(l1,l2):

            dummy=ListNode()
            node=dummy

            while l1 and l2:
                if l1.val<=l2.val:
                    node.next=l1
                    l1=l1.next
                else:
                    node.next=l2
                    l2=l2.next
                node=node.next
            if l1:
                node.next=l1
            else:
                node.next=l2
            return dummy.next

        res=None

        for ll in lists:
            res=mergeTwo(res,ll)
        return res