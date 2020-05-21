"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Linked_List()
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        """Adds a value to the end of a Queue"""
        # return self.storage.append(value)
        self.storage.add_value(value)
        

    def dequeue(self):
        """Removes a value from the beginning of a Queue"""
        """
        if len(self.storage) > 0:
            self.first = self.storage[0]
            self.storage.remove(self.storage[0])
            return self.first
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
        if self.head:
            node = self.head
            if self.head.next_val:
                self.head = self.head.next_val
                self.head.prev_val = None
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

"""
When using a Linked List the next and previous values need to be changed when
adding a new element, whereas, when using an array, the is index automatically
updated whenever a new value is added or removed from a list. When adding to an
array, the append() method can be used to add a value to the end. And the
remove() method can automatically remove a specified value. The [0] index can
be used to automatically ge the value at the beginning, making it easy to
remove it. In a Linked List, a value is assigned to a head and when that is
removed, the next value will have no previous value and that will be the new
head. When adding a new head, the new node has to be added to the previous
value of the current head, in order to add it to the beginning.
"""
