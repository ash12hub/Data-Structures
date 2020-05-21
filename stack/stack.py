"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = Linked_List()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        """Push value to the end of the Stack"""

        # self.storage.append(value)
        self.storage.add_value(value)

    def pop(self):
        """Pop value from the end of the Stack"""
        """
        if len(self.storage) > 0:
            value = self.storage[-1]
            self.storage.remove(self.storage[-1])
            return value
        else:
            return None
        """
        return self.storage.remove_value()

class Linked_List:
    def __init__(self, node=None):
        self.length = 1 if node else 0
        self.head=node
        self.tail=node
    
    def __len__(self):
        return self.length

    def add_value(self, value):
        new_node = List_Node(value, None, None)
        self.length += 1

        if self.tail:
            self.tail.next_val = new_node
            new_node.prev_val = self.tail
        else:
            self.head = new_node
        self.tail = new_node

    def remove_value(self):
        if self.tail:
            node = self.tail
            if self.tail.prev_val:
                self.tail = self.tail.prev_val
                self.tail.next_val = None
            else:
                self.head = None
                self.tail = None
            self.length -= 1
            return node.value
        else:
            return None
        

class List_Node:
    def __init__(self, value, next_val=None, prev_val=None):
        self.value = value
        self.next_val = next_val
        self.prev_val = prev_val
