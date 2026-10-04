class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # erster Knoten
        s = l1.val + l2.val
        added = ListNode(s % 10)
        carry_over = s // 10
        current_node = added

        # weiterlaufen (solange noch irgendwo etwas übrig ist oder carry existiert)
        l1 = l1.next
        l2 = l2.next

        while l1 is not None or l2 is not None or carry_over != 0:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0

            s = v1 + v2 + carry_over
            current_node.next = ListNode(s % 10)
            carry_over = s // 10
            current_node = current_node.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return added
    
ListNode(2,Listnode(4,Listnode(3))) 

