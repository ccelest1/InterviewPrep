"""
For your reference:
SinglyLinkedListNode:
    int data
    SinglyLinkedListNode next
"""


# get Node value given positions from end of list
def getNode(llist: list, positionFromTail: int) -> int:
    size, head = 0, llist
    while head:
        size += 1
        head = head.next
    getNode, counter = llist, 0
    while getNode.next and counter < size - positionFromTail - 1:
        getNode = getNode.next
        counter += 1
    return getNode.data


# delete Node
def deleteNode(llist: list, position: int):
    head = llist
    if position == 0:
        llist = llist.next

    for _ in range(position - 1):
        if head is None:
            return llist
        head = head.next

    if head.next:
        head.next = head.next.next

    return llist


# compare lists
def compare_lists(llist1, llist2):
    head1, head2 = llist1, llist2
    while head1 and head2:
        if head1.data is not head2.data:
            return 0
        head1 = head1.next
        head2 = head2.next
    if head1 is None and head2 is None:
        return 1
    return 0


# merge 2 lists in sorted order
def SinglyLinkedListNode(self, data, next=None):
    self.data = data
    self.next = next


def MergeLists(head1, head2):
    head3 = SinglyLinkedListNode(0)
    current = head3
    curr1, curr2 = head1, head2

    while curr1 is not None and curr2 is not None:
        if curr1.data < curr2.data:
            """
            temp = curr1
            """
            current.next = SinglyLinkedListNode(curr1.data)
            curr1 = curr1.next
        elif curr2.data < curr1.data:
            """
            temp = curr2
            """
            current.next = SinglyLinkedListNode(curr2.data)
            curr2 = curr2.next
        else:
            # if both nodes have same value, matching node.data
            current.next = SinglyLinkedListNode(curr1.data)
            current = current.next
            current.next = SinglyLinkedListNode(curr2.data)
            curr1 = curr1.next
            curr2 = curr2.next
        current = current.next

    if curr1 is not None:
        current.next = curr1
    elif curr2 is not None:
        current.next = curr2

    return head3.next
