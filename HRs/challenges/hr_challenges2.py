# 02.08.24
"""
find merge point of 2 lists
[list 1] a -> b -> c
                \
                 x -> z -> NUll
                /
[list 2] e -> f -> g

with constraints that head1, head2 !== null
head1 !== head2
"""


def SLLN(self, val, link=None):
    self.val = val
    self.link = link


from typing import Optional


# find node that two lists merge at
"""
[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q

Both lists merge at node x given references to two heads of 1st and 2nd list

SinglyLinkedListNode pointer head1: a reference to the head of the first list
SinglyLinkedListNode pointer head2: a reference to the head of the second list
"""
"""
[list1] 1 -> 2
              \
                3
               /
[list2]       1
"""


class Solution:
    def findMergeNode(head1: Optional[SLLN], head2: Optional[SLLN]) -> int:
        curr1, curr2 = head1, head2
        mergedNode = False
        while curr1 and curr2:
            while not mergedNode:
                if curr1.next is not None:
                    curr1 = curr1.next
                if curr2.next is not None:
                    curr2 = curr2.next
                if curr1 == curr2:
                    mergedNode = True
                    return curr1.data
                # if curr1.next.data == curr2.next.data:
                #     mergedNode = True
                #     return curr2.next.data

    # correct solution
    def findMergeNode2(head1, head2):
        curr1, curr2 = head1, head2
        while curr1 != curr2:
            if curr1.next is None:
                curr1 = head2
            else:
                curr1 = curr1.next
            if curr2.next is None:
                curr2 = head1
            else:
                curr2 = curr2.next
        return curr2.data


# 02.20.24
"""
Brackets involves any of these possible characters and matching pairs: ()[]{}
Matching pair of brackets is not balanced if set of brackets enclosed are not matched

Sequence of brackets are balanced if these conditions are true:
- contains no unmatched brackets
- subset of brackets enclosed in confines of matched brackets pair are also a matched pair of brackets

given n string of brackets -> determine if each seq of brackets is balanced, if string is balanced return YES, else return NO

Strategy:
Determine if we are in a close, open bracket match
if we are then determine if closing brackets have open, close and so on
if we aren't then we can return false at that specified moment
"""


def isBalanced(s: str) -> str:
    # allows us to decipher a provided string and given bracket arrangement
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []

    # iterate through original string
    for char in s:
        # append only opening brackets
        if char in pairs:
            stack.append(char)
        else:
            # we know we have encountered a closing bracket
            # if stack is empty, then we know the string is not balanced
            if not stack:
                return "NO"
            # else we ant to pop what we have last in stack and ask if we look in the dict keys, is that char not equal to value in dict then we can return 'NO'
            popped = stack.pop()
            if pairs[popped] != char:
                return "NO"
    # if stack is empty we can return YES as we have encountered a balanced stack or empty string which is auto balanced, any other situation is going to be unbalanced thus NO
    if not stack:
        return "YES"
    return "NO"


test1 = isBalanced("{[()]}")
print(test1 == "YES")
test2 = isBalanced("{[(])}")
print(test2 == "NO")
test3 = isBalanced("{{[[(())]]}}")
print(test3 == "YES")


# 2.28.24 - insert node at LinkedList Head
def SinglyLinkedListNode(self, data=None):
    self.data = data
    self.next = None


def insertNodeAtHead(llist: SinglyLinkedListNode, data: int) -> SinglyLinkedListNode:
    if not llist:
        return SinglyLinkedListNode(data)
    if llist:
        new_node = SinglyLinkedListNode(data)
        new_node.next = llist
    return new_node
