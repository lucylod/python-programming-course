class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    # Dummy-Knoten vor den Head setzen
    dummy = ListNode(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    # fast n Schritte nach vorne bewegen
    for _ in range(n):
        fast = fast.next

    # beide Zeiger gemeinsam bewegen
    while fast.next is not None:
        fast = fast.next        #node1.next=node2
        slow = slow.next        #node2=Listnode(2)
                                #node1=ListNode(1,node2)

    # n-ten Knoten von hinten entfernen
    slow.next = slow.next.next

    return dummy.next

def list_to_linked(lst):
    dummy = ListNode(0)
    cur = dummy

    for x in lst:
        cur.next = ListNode(x)
        cur = cur.next

    return dummy.next

def linked_to_list(head):
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

eingabe = input("Gib Zahlen komma-separiert ein (z.B. 1,2,3,4,5): ").strip()
nums = [] if eingabe == "" else [int(x.strip()) for x in eingabe.split(",")]
n = int(input("Gib n ein (n-ter Knoten vom Ende wird gelöscht): "))

head = list_to_linked(nums)
new_head = removeNthFromEnd(head, n)

print("Ergebnis:", linked_to_list(new_head))

    
