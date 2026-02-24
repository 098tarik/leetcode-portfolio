"""
Given a binary tree, 
we say a node is aligned if its value is equal to its depth 
(distance from root). 
A descendant chain is a sequence of nodes where each node
 is the parent of the next node. 
 Return the length of the longest descendant chain of aligned nodes.
The chain does not need to start at the root.


Example:
                7
               / \
              1   3
             / \   \
            2   8   2
           / \     / \
          4   3   3   3

Output: 3
The aligned nodes are the circled ones:
Depth
  0             7
               / \
  1          (1)   3
             / \   \
  2        (2)  8  (2)
           / \     / \
  3       4  (3) (3) (3)

The longest descendant chain of aligned nodes is 1 -> 2 -> 3 on the left
subtree.
"""

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def align_tree(root):
    result = [0]  # mutable container so nested function can update it

    def visit(node, depth, streak):
        if not node:
            return

        if node.val == depth:
            streak += 1
        else:
            streak = 0

        result[0] = max(result[0], streak)

        visit(node.left, depth + 1, streak)
        visit(node.right, depth + 1, streak)

    visit(root, 0, 0)
    return result[0]

def run_tests():
  tests = [
      # Test 1: from the book
      (Node(7, Node(1, Node(2, Node(4), Node(3)),
                    Node(8)), Node(3, Node(2, Node(3)))), 3),
      # Test 2
      (Node(0,
            Node(1,
                 Node(2,
                      Node(3),
                      None),
                 Node(4)),
            Node(5)), 4),

      # Test 3: Empty tree
      (None, 0),

      # Test 4: Single node aligned at root
      (Node(0), 1),

      # Test 5: Single node not aligned
      (Node(1), 0),

      # Test 6: Multiple valid chains, should return longest
      (Node(0,
            Node(1,
                 Node(2,
                      Node(4),
                      None),
                 Node(2,
                      Node(3),
                      None))), 4),

      # Test 7: No aligned nodes
      (Node(5,
            Node(4,
                 Node(3),
                 Node(3)),
            Node(2)), 0),

      # Test 8
      (Node(0,
            Node(1),
            Node(1)), 2),
  ]

  for i, (root, want) in enumerate(tests, 1):
    got = align_tree(root)
    assert got == want, f"\nTest {i} failed! Got: {got}, Want: {want}"

run_tests()