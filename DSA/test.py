class Binarytreenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,child):
        if child == self.data:
            return 

        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = Binarytreenode(child)
                # return self.left

        if child > self.data:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = Binarytreenode(child)
                # return self.right


    def inorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
            
    def find_max(self):
        
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def serach(self,val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.serach(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.serach(val)
            else:
                return False

def build_tree(element):
    root = Binarytreenode(element[0])

    for i in range(1,len(element)):
        root.add_child(element[i])

    return root


numbers = [17,45,3,8,79,523,12]
tree= build_tree(numbers)
print(tree.inorder_traversal())
print(tree.find_max())
print(tree.serach(17))