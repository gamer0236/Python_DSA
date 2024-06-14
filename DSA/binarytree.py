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

        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = Binarytreenode(child)

    def inorder_traversal(self):
        element = []

        if self.left:
            element += self.left.inorder_traversal()

        element.append(self.data)

        if self.right:
            element += self.right.inorder_traversal()

        return element
    
    def search(self,val):
        if val == self.data:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False








    
def build_tree(element):
    root = Binarytreenode(element[0])

    for i in range(1,len(element)):
        root.add_child(element[i])

    return root

elements = [17,4,1,20,9,23,18,34]

tree = build_tree(elements)
print(tree.inorder_traversal())
print(tree.search(3))

        