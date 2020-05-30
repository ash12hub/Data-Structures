"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if self.right is not None and target > self.value:
            return self.right.contains(target)
        elif self.left is not None and target < self.value:
            return self.left.contains(target)
        else:
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
        
        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        
        print(node.value)

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        next_level = True
        nodes = []
        left = None
        right = None
        current_node = node
        print(current_node.value)
        while next_level:
            next_level = False
            if current_node.right:
                nodes.append(current_node.right)
                right = current_node.right.value
                next_level = True
            if current_node.left:
                nodes.append(current_node.left)
                left = current_node.left.value
                next_level = True
            if right:
                print(right)
            if left:
                print(left)
            
            current_node = nodes[0]
            del nodes[0]
            right = None
            left = None
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversals
    def dft_print(self, node):
        nodes = [node]
        while len(nodes) > 0:
            current_node = nodes[-1]
            del nodes[-1]

            if current_node.left:
                nodes.append(current_node.left)

            if current_node.right:
                nodes.append(current_node.right)

            print(current_node.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            self.pre_order_dft(node.left)

        if node.right:
            self.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)

        if node.right:
            self.post_order_dft(node.right)

        print(node.value)
