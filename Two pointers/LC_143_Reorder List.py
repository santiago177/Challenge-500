from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printList(n):
            cur = n
            while cur:
                print(cur.val)
                cur = cur.next
        """
        Do not return anything, modify head in-place instead.
        """
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        mid = s
        node = mid.next
        prev = mid.next = None
        while node:
            t = node.next
            node.next = prev
            prev = node
            node = t

        p1, p2 = head, prev
        while p2:
            t1 = p1.next
            t2 = p2.next
            p1.next = p2
            p2.next = t1
            p1 = t1
            p2 = t2
        printList(head)
        return head




test = Solution()
nodes = [ListNode() for i in range(4)]
nodes[0].next = nodes[1]
nodes[0].val = 1
nodes[1].next = nodes[2]
nodes[1].val = 2
nodes[2].next = nodes[3]
nodes[2].val = 3
nodes[3].val = 4

print(test.reorderList(nodes[0]))
