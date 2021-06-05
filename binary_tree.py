"""
problem: https://www.urionlinejudge.com.br/judge/pt/problems/view/1194

Given the prefix and infix traversals, return the postfix.

solution reference: https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
"""
from dataclasses import dataclass

@dataclass
class Node:
    value: str
    left: 'Node' = None
    right: 'Node' = None


def build_tree(prefix, infix, start, end):
    """
    Generates the binary tree from prefix and infix traversal recursivelly

    Arguments:
    prefix: list - the prefix traversal
    infix: list - the infix traversal
    start: int
    end: int

    Outpus:
    node: Node - A node from the binary tree
    """
    if start > end:
        return

    node = Node(value=prefix[build_tree.pre_idx ])
    build_tree.pre_idx += 1

    # if its a leaf, return the node
    if start == end:
        return node

    value_idx = infix.index(node.value)

    node.left = build_tree(prefix, infix, start, value_idx-1)
    node.right = build_tree(prefix, infix, value_idx+1, end)

    return node


def get_postfix(node, postfix_list=[]):
    """
    Returns a postfix traversal given a root node

    Arguments:
    node: Node - The root node of a binary tree
    postfix_list: list

    Outputs:
    postfix_list: list with the postfix sequence
    """
    if not node:
        return

    # left child
    get_postfix(node.left, postfix_list)

    # right child
    get_postfix(node.right, postfix_list)

    postfix_list.append(node.value)

    return postfix_list

def main():
    prefix = 'A B C D E F'.split()
    infix = 'C B A E D F'.split()

    build_tree.pre_idx = 0

    root = build_tree(prefix, infix, start=0, end=len(infix)-1)

    postfix = get_postfix(root, postfix_list=[])

    print(f"The postfix traversal is: {postfix}")

if __name__ == "__main__":
    main()
