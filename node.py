class Node:

    def __init__(self, value, left, right):
        assert(isinstance(left, Node) or left is None)
        assert(isinstance(right, Node) or right is None)

        self.value = value
        self.left = left
        self.right = right
    
    def get_value(self):
        return self.value

    def get_left(self):
        return left

    def get_right(self):
        return right
    
    def __str__(self):
        return "value: {}, left: {}, right: {}".format(self.value, self.left.get_value(), self.right.get_value())

