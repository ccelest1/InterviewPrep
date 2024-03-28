"""
The lowest common ancestor is the lowest node in the tree that has both n1 and n2 as descendants, where n1 and n2 are the nodes for which we wish to find the LCA. Hence, the LCA of a binary tree with nodes n1 and n2 is the shared ancestor of n1 and n2 that is located farthest from the root.

    1
   /  \
  2     3
 / \   / \
4  5  6   7

Path from root to 5 = { 1, 2, 5 }
Path from root to 6 = { 1, 3, 6 }

We start checking from 0 index. As both of the value matches( pathA[0] = pathB[0] ), we move to the next index.
pathA[1] not equals to pathB[1], there’s a mismatch so we consider the previous value.
Therefore the LCA of (5,6) = 1

input: list[int] that represent the hiearchy relative to a particular root/node
output: LCA, int that is the value of the LCA of Binary Tree
BST
Assume that lists are not always going to be same length, lists are going to have values

Node class, Tree class, find LCA function
node: value, parent, left, right
Tree [ contain nodes ]
LCA -> takes in two values, then we have to find where that value occurs in tree -> understand each individual paths from root or traverse and find node where they diverge/share
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Tree:
    def __init__(self, root):
        self.root = root


# implement traversal method


def find_path(node, target, path=[]):
    if not node:
        return None
    path.append(node.value)
    if node.value == target:
        return path
    if not node.right or not node.left:
        # traverse path that we have not explored yet
        return None

    left_path = find_path(
        node.left, target, path + [node.value]
    )  # return target in path
    # eleminate left if node not found on that path
    # then only traverse right
    right_path = find_path(node.right, target, path + [node.value])
    # vice versa
    if left_path is not None and right_path is not None:
        raise ("val not unique")
    if left_path is not None:
        return left_path
    elif right_path is not None:
        return left_path
    return None


def findLCA(node, value1, value2):
    ancestors1 = find_path(node, value1)
    ancestors2 = find_path(node, value2)
    common = set(ancestors1).intersection(set(ancestors2))
    for i in range(len(ancestors1), 0, -1):
        if ancestors1[i] in common:
            return ancestors1[i]
    return None


# traverse twice, compare paths, return latest common element
# invoke find_path with both values
"""

"""


def findLCA(Tree, value1, value2):

    while current:
        if value == current.value:
            return current
        else:
            if current.left:
                current = current.left
    while current:
        if value == current.value:
            return current
        else:
            if current.right:
                current = current.left
    """
  root node = current
  while(current):
    nodes.append(current)
    if current.left:
     current = curren.left
  """


"======================="


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findAncestors(node, value, ancestors=[]):
    if node is None:
        return None
    if node.value == value:
        return ancestors
    if node.left is None and node.right is None:
        return None
    left = findAncestors(node.left, value, ancestors + [node.value])
    right = findAncestors(node.right, value, ancestors + [node.value])
    if left is not None and right is not None:
        raise ("Error: node value is not unique")
    if left is not None:
        return left
    return right


def findLestCommonAncestor(node, value1, value2):
    ancestors1 = findAncestors(node, value1)
    ancestors2 = findAncestors(node, value2)
    common = set(ancestors1).intersection(set(ancestors2))
    for ancestor in reversed(ancestors1):
        if ancestor in common:
            return ancestor
    return None


n4 = Node(12)
n1 = Node(10, n3)
n2 = Node(5)
n3 = Node(7, n2)
n5 = Node(15, n4)
n6 = Node(11, n1, n5)

findLestCommonAncestor(n6, 5, 7)
