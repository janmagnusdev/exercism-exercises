class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    head = None
    
    def __init__(self):
        pass

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr
            curr = curr.succeeding

    def __getitem__(self, i):
        for index, element in enumerate(self):
            if index == i:
                return element
        return None
    
    def __len__(self):
        i = 0
        for _node in self:
            i = i +  1
        return i
    
    def push(self, element):
        to_add = Node(element)
        if len(self) == 0:
            self.head = to_add
            return

        last_node = self[len(self) - 1]
        last_node.succeeding = to_add
        to_add.previous = last_node


    def pop(self):
        match len(self):
            case 0:
                raise IndexError("List is empty")
            case 1:
                old_head = self.head
                self.head = None
                return old_head.value
            case _:
                last_node = self[len(self) - 1]
                last_node.previous.succeeding = None
                return last_node.value


    def shift(self):
        if len(self) == 0:
            raise IndexError("List is empty")

        old_head = self.head
        self.head = old_head.succeeding
        return old_head.value

    def unshift(self, to_add):
        new_node = Node(to_add)
        if len(self) > 0:
            old_head = self.head
            new_node.succeeding = old_head
            old_head.previous = new_node
        self.head = new_node

    def delete(self, to_delete):
        if len(self) == 0:
            raise ValueError("Value not found")

        for node in self:
            if node.value == to_delete:
                # if node is the first in chain, head must be updated respectively
                if node.previous is None:
                    self.head = node.succeeding
                else:
                    node.previous.succeeding = node.succeeding
                if node.succeeding is not None:
                    node.succeeding.previous = node.previous
                return
        else: 
            raise ValueError("Value not found")
