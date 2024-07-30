# This problem was asked by Amazon.
# Given an integer N, construct all possible binary search trees with N nodes.

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None
        pass

def generate_trees(start, end):
    if(start > end):
        return [None]
    
    all_trees = []
    for i in range(start, end + 1):
        left_trees = generate_trees(start, i - 1)
        right_trees = generate_trees(i +1, end)
        for l in left_trees:
            for r in right_trees:
                current_tree = Node(i)
                current_tree.left = l
                current_tree.right = r
                all_trees.append(current_tree)
    return all_trees

def tree_as_json(tree):
    if(tree == None):
        return None
    return {"value": tree.val, "left" : tree_as_json(tree.left), "right": tree_as_json(tree.right)}

def solve(n):
    # Binary search tree is a tree with left node value < current node value < right node value.
    # So the idea is root node value will run from 1 to N, and use a recursive approach to generate left tree and right tree.
    trees = generate_trees(1, n)
    return trees

if __name__ == '__main__':
    trees = solve(3)
    for tree in trees:
        print(tree_as_json(tree))