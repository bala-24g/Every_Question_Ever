class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class SuccessorPredecessor:
    def __init__(self):
        self.successor = None
        self.predecessor = None

    def successor_predecessor(self, root, val):
        if root:
            if root.data == val:
                if root.left:
                    temp = root.left
                    while temp.right:
                        temp = temp.right
                    self.predecessor = temp.data
                if root.right:
                    temp = root.right
                    while temp.left:
                        temp = temp.left
                    self.successor = temp.data
            elif root.data > val:
                self.successor = root.data
                self.successor_predecessor(root.left, val)
            elif root.data < val:
                self.predecessor = root.data
                self.successor_predecessor(root.right, val)
#if root:
# if root.data==val,Go to left and go as far right as possible, that will be predecessor.
#if root.data==val,Go to right and as left as possible, that will be successor
#elif root.data>val: successor is root.data and call the function for root.left
#elif root.data<val: predecessor is root.data and call function for root.right

